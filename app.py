st.title('나는 짱이다')
st.write('바이브코딩 재미있다!!')
st.write('중간에 놓쳤는데 김진영꺼 복붙하기 야아르으')
import streamlit as st
import time
st.title('나는 짱이다')
st.write('바이브코딩 재미있다!!')
st.write('중간에 놓쳤는데 김진영꺼 복붙하기 야아르으')
st.set_page_config(
    page_title="AI 학습 유형 분석",
    page_icon="📚",
    layout="centered",
)

# -----------------------------
# 질문 데이터
# -----------------------------

questions = [
    {
        "question": "하루 평균 공부 시간은 어느 정도인가요?",
        "answers": [
            {"text": "30분 이하", "scores": {"P": 2}},
            {"text": "30분~1시간", "scores": {"P": 1}},
            {"text": "1~2시간", "scores": {"J": 1}},
            {"text": "2~4시간", "scores": {"J": 2}},
            {
                "text": "4시간 이상",
                "scores": {
                    "J": 3,
                    "challenger": 1,
                },
            },
        ],
    },
    {
        "question": "현재 공부를 하는 가장 큰 이유는 무엇인가요?",
        "answers": [
            {
                "text": "공부 습관을 만들고 싶다",
                "scores": {"growth": 2},
            },
            {
                "text": "수행평가/숙제를 해결하고 싶다",
                "scores": {"J": 1},
            },
            {
                "text": "시험 성적을 올리고 싶다",
                "scores": {"growth": 3},
            },
            {
                "text": "상위권에 도전하고 싶다",
                "scores": {"challenger": 3},
            },
            {
                "text": "재미있고 흥미롭게 공부하고 싶다",
                "scores": {
                    "explorer": 3,
                    "P": 1,
                },
            },
        ],
    },
    {
        "question": "문제를 풀다가 막히면 보통 어떻게 하나요?",
        "answers": [
            {
                "text": "바로 포기한다",
                "scores": {"P": 1},
            },
            {
                "text": "정답만 빠르게 확인한다",
                "scores": {"P": 2},
            },
            {
                "text": "해설을 읽고 이해한다",
                "scores": {"growth": 2},
            },
            {
                "text": "다시 스스로 고민해본다",
                "scores": {
                    "J": 1,
                    "growth": 1,
                },
            },
            {
                "text": "끝까지 혼자 해결하려고 한다",
                "scores": {
                    "challenger": 2,
                    "J": 1,
                },
            },
        ],
    },
    {
        "question": "한 번에 집중 가능한 시간은 어느 정도인가요?",
        "answers": [
            {
                "text": "10분 이하",
                "scores": {"P": 2},
            },
            {
                "text": "10~20분",
                "scores": {"P": 1},
            },
            {
                "text": "20~40분",
                "scores": {"J": 1},
            },
            {
                "text": "40~60분",
                "scores": {"J": 2},
            },
            {
                "text": "1시간 이상",
                "scores": {
                    "J": 3,
                    "challenger": 1,
                },
            },
        ],
    },
    {
        "question": "어떤 방식의 공부를 가장 선호하나요?",
        "answers": [
            {
                "text": "짧고 쉬운 문제 반복",
                "scores": {"growth": 1},
            },
            {
                "text": "다양한 문제를 자유롭게 풀기",
                "scores": {
                    "explorer": 3,
                    "P": 1,
                },
            },
            {
                "text": "틀린 문제 다시 분석하기",
                "scores": {"growth": 3},
            },
            {
                "text": "어려운 문제 오래 고민하기",
                "scores": {
                    "challenger": 3,
                    "J": 1,
                },
            },
            {
                "text": "계획대로 차근차근 학습하기",
                "scores": {
                    "J": 3,
                    "growth": 1,
                },
            },
        ],
    },
]

# -----------------------------
# 유형 데이터
# -----------------------------

type_data = {
    "즉흥적인 탐험가": {
        "emoji": "⚡",
        "description": """
새로운 방식과 자유로운 학습을 선호하며,
다양한 문제를 탐색하는 과정에서 흥미를 느끼는 유형입니다.
""",
        "strength": [
            "새로운 유형 적응이 빠름",
            "창의적인 접근 가능",
            "다양한 분야 탐색 능력 우수",
        ],
        "weakness": [
            "반복 학습을 지루하게 느낄 수 있음",
            "장기 루틴 유지가 어려울 수 있음",
        ],
        "recommendations": [
            "15~20분 단위 짧은 학습",
            "랜덤 문제 풀이",
            "다양한 과목 번갈아 학습",
        ],
    },
    "즉흥적인 도전자": {
        "emoji": "⚔️",
        "description": """
빠른 성취감과 경쟁 상황에서 강한 동기를 얻는 유형입니다.
""",
        "strength": [
            "승부욕이 강함",
            "어려운 문제 도전 성향 높음",
        ],
        "weakness": [
            "쉬운 문제를 지루하게 느낄 수 있음",
            "감정 기복이 커질 수 있음",
        ],
        "recommendations": [
            "제한 시간 문제 풀이",
            "고난도 문제 도전",
            "실전형 문제 반복",
        ],
    },
    "즉흥적인 성장가": {
        "emoji": "🌱",
        "description": """
짧고 가벼운 학습을 선호하지만,
꾸준한 성장에서 성취감을 느끼는 유형입니다.
""",
        "strength": [
            "꾸준한 성장 가능",
            "반복 학습 적응력 우수",
        ],
        "weakness": [
            "큰 목표 유지가 어려울 수 있음",
            "어려운 문제 회피 가능성",
        ],
        "recommendations": [
            "하루 단위 작은 목표 설정",
            "짧은 복습 루틴 만들기",
            "매일 학습 기록 남기기",
        ],
    },
    "전략적인 탐험가": {
        "emoji": "🧭",
        "description": """
새로운 유형을 탐색하는 것을 좋아하지만,
체계적인 방식으로 학습을 확장하는 유형입니다.
""",
        "strength": [
            "분석적 사고 우수",
            "개념 연결 능력 뛰어남",
        ],
        "weakness": [
            "탐색 범위가 너무 넓어질 수 있음",
            "완벽주의 성향 가능성",
        ],
        "recommendations": [
            "개념별 구조화 학습",
            "탐색 후 요약 정리",
            "장기 학습 계획 세우기",
        ],
    },
    "전략적인 도전자": {
        "emoji": "🛡️",
        "description": """
높은 목표를 세우고 장기적인 계획 아래
꾸준히 성과를 만들어가는 유형입니다.
""",
        "strength": [
            "자기관리 능력 우수",
            "고난도 문제 해결 능력 뛰어남",
        ],
        "weakness": [
            "스스로에게 과도한 압박 가능",
            "휴식을 놓치기 쉬움",
        ],
        "recommendations": [
            "심화 문제 반복 풀이",
            "실전 문제 분석",
            "장기 목표 기반 학습",
        ],
    },
    "전략적인 성장가": {
        "emoji": "📘",
        "description": """
체계적인 분석과 반복 학습을 통해
안정적으로 실력을 향상시키는 유형입니다.
""",
        "strength": [
            "꾸준함이 매우 강함",
            "실수 분석 능력 우수",
        ],
        "weakness": [
            "새로운 방식 도전에 소극적일 수 있음",
            "안전한 방식만 고수 가능성",
        ],
        "recommendations": [
            "오답 노트 작성",
            "약점 단원 반복 학습",
            "주간 학습 계획표 활용",
        ],
    },
}

# -----------------------------
# 세션 상태 초기화
# -----------------------------

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "scores" not in st.session_state:
    st.session_state.scores = {
        "P": 0,
        "J": 0,
        "explorer": 0,
        "challenger": 0,
        "growth": 0,
    }

if "finished" not in st.session_state:
    st.session_state.finished = False

# -----------------------------
# 점수 적용 함수
# -----------------------------


def apply_scores(score_data):
    for key, value in score_data.items():
        st.session_state.scores[key] += value


# -----------------------------
# 결과 계산 함수
# -----------------------------


def calculate_result():
    scores = st.session_state.scores

    pj_type = "즉흥적인" if scores["P"] > scores["J"] else "전략적인"

    role_scores = {
        "탐험가": scores["explorer"],
        "도전자": scores["challenger"],
        "성장가": scores["growth"],
    }

    role_type = max(role_scores, key=role_scores.get)

    return f"{pj_type} {role_type}"


# -----------------------------
# 메인 UI
# -----------------------------

st.title("📚 AI 학습 유형 분석")

if not st.session_state.finished:

    current_index = st.session_state.current_index
    current_question = questions[current_index]

    progress = (current_index + 1) / len(questions)

    st.progress(progress)

    st.markdown(f"## 질문 {current_index + 1}")
    st.markdown(f"### {current_question['question']}")

    st.write("")

    for answer in current_question["answers"]:

        if st.button(
            answer["text"],
            use_container_width=True,
            key=answer["text"],
        ):
            apply_scores(answer["scores"])

            if current_index < len(questions) - 1:
                st.session_state.current_index += 1
            else:
                with st.spinner("AI가 학습 성향을 분석중입니다..."):
                    time.sleep(2)

                st.session_state.finished = True

            st.rerun()

else:

    result_type = calculate_result()

    data = type_data[result_type]

    scores = st.session_state.scores

    st.success("분석 완료!")

    st.markdown(f"# {data['emoji']} {result_type}")

    st.markdown(data["description"])

    st.divider()

    st.subheader("📊 성향 점수")

    st.write(f"즉흥형(P): {scores['P']}")
    st.write(f"전략형(J): {scores['J']}")

    st.write(f"탐험가: {scores['explorer']}")
    st.write(f"도전자: {scores['challenger']}")
    st.write(f"성장가: {scores['growth']}")

    st.divider()

    st.subheader("🔥 강점")

    for item in data["strength"]:
        st.write(f"• {item}")

    st.divider()

    st.subheader("⚠️ 주의할 점")

    for item in data["weakness"]:
        st.write(f"• {item}")

    st.divider()

    st.subheader("📚 추천 학습 전략")

    for item in data["recommendations"]:
        st.write(f"✅ {item}")

    st.divider()

    if st.button("다시 테스트하기"):
        st.session_state.current_index = 0
        st.session_state.finished = False
        st.session_state.scores = {
            "P": 0,
            "J": 0,
            "explorer": 0,
            "challenger": 0,
            "growth": 0,
        }

        st.rerun()
