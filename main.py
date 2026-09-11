import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="알파벳 상큼 과일 추천!",
    page_icon="🍓",
    layout="centered"
)

# 커스텀 CSS (파스텔톤 디자인)
st.markdown("""
    <style>
    .main {
        background-color: #FFF9FB;
    }
    .stSelectbox label {
        font-size: 1.2rem !important;
        color: #FF7B9C !important;
        font-weight: bold;
    }
    .title-text {
        text-align: center;
        color: #FF5A85;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 2.3rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .subtitle-text {
        text-align: center;
        color: #FFAAA5;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .recommend-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0px 8px 16px rgba(255, 182, 193, 0.4);
        border: 2px solid #FFD3E0;
        text-align: center;
    }
    .fruit-title {
        color: #FF407D;
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 10px;
    }
    .fruit-desc {
        color: #666666;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-top: 15px;
    }
    .stButton>button {
        background-color: #FF7B9C;
        color: white;
        border-radius: 15px;
        border: none;
        padding: 10px 25px;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0px 4px 10px rgba(255, 123, 156, 0.3);
    }
    .stButton>button:hover {
        background-color: #FF5A85;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 헤더 영역
st.markdown("<p class='title-text'>✨ 알파벳 달콤 과일 추천 ✨</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>좋아하는 알파벳을 고르면 상큼한 과일을 팡팡! 🍎</p>", unsafe_allow_html=True)

# 알파벳별 과일 데이터베이스
fruit_data = {
    "A": {"name": "Apple (사과)", "emoji": "🍎", "badge": "아삭아삭 매력 만점", "desc": "새콤달콤 매일 먹어도 질리지 않는 사과! 비타민이 풍부해 피로 회복에 딱이에요."},
    "B": {"name": "Banana (바나나)", "emoji": "🍌", "badge": "부드럽고 든든한 에너자이저", "desc": "달콤하고 부드러운 바나나! 에너지 충전이 필요할 때 최고의 간식이 되어줄 거예요."},
    "C": {"name": "Cherry (체리)", "emoji": "🍒", "badge": "작고 귀여운 과일계의 보석", "desc": "통통하고 진한 붉은빛의 체리! 진한 달콤함으로 기분까지 좋게 만들어 줍니다."},
    "D": {"name": "Dragon Fruit (용과)", "emoji": "🐉", "badge": "신비롭고 화려한 비주얼", "desc": "화려한 겉모습 속 촉촉하고 담백한 반전 매력! 깔끔하고 시원한 맛이 매력적이에요."},
    "E": {"name": "Elderberry (엘더베리)", "emoji": "🫐", "badge": "건강을 지켜주는 앙증맞은 베리", "desc": "작지만 영양이 가득한 엘더베리! 따뜻한 차나 잼으로 즐기면 더욱 맛있답니다."},
    "F": {"name": "Fig (무화과)", "emoji": "🧁", "badge": "은은하고 고급스러운 달콤함", "desc": "톡톡 씹히는 씨앗과 부드러운 과육이 조화를 이루는 무화과! 고급스러운 디저트로 제격이에요."},
    "G": {"name": "Grape (포도)", "emoji": "🍇", "badge": "톡 터지는 즙이 매력적인 과일", "desc": "한 알씩 쏙쏙 빼먹는 재미가 있는 포도! 입안 가득 퍼지는 달콤한 과즙을 느껴보세요."},
    "H": {"name": "Honeydew (허니듀 멜론)", "emoji": "🍈", "badge": "꿀처럼 달달한 수분 충전기", "desc": "은은한 초록빛 과육에 꿀을 바른 듯 달콤한 멜론! 시원하게 먹으면 입안이 깔끔해져요."},
    "I": {"name": "Ichigo (딸기)", "emoji": "🍓", "badge": "사랑스러움의 대명사", "desc": "보는 것만으로도 행복해지는 딸기! 향긋함과 달콤함으로 언제나 인기가 최고예요."},
    "J": {"name": "Jackfruit (잭푸르트)", "emoji": "🍍", "badge": "열대 과일계의 거인", "desc": "거대한 크기 속에 쫄깃하고 달콤한 과육이 숨어있는 매력적인 열대 과일이에요."},
    "K": {"name": "Kiwi (키위)", "emoji": "🥝", "badge": "새콤달콤 비타민 톡톡", "desc": "톡톡 터지는 씨앗과 새콤한 맛이 매력적인 키위! 기분 전환이 필요할 때 강력 추천해요."},
    "L": {"name": "Lemon (레몬)", "emoji": "🍋", "badge": "상큼함 끝판왕", "desc": "찌릿찌릿 상큼한 에너지 레몬! 음료나 디저트에 곁들이면 기분이 톡톡 깨어납니다."},
    "M": {"name": "Mango (망고)", "emoji": "🥭", "badge": "부드러운 열대 과일의 왕", "desc": "입안에서 사르르 녹아내리는 부드러운 망고! 진한 달콤함에 풍당 빠져보세요."},
    "N": {"name": "Nectarine (천도복숭아)", "emoji": "🍑", "badge": "매끈하고 아삭한 새콤함", "desc": "털 없이 매끈하고 속은 달콤 아삭한 천도복숭아! 한 입 베어 물면 행복해져요."},
    "O": {"name": "Orange (오렌지)", "emoji": "🍊", "badge": "비타민C 톡톡 탄산 같은 과일", "desc": "동글동글 주황빛 예쁜 오렌지! 팡팡 터지는 과즙으로 하루의 활력을 충전하세요."},
    "P": {"name": "Peach (복숭아)", "emoji": "🍑", "badge": "말랑말랑 분홍빛 감성", "desc": "향긋한 향기만으로도 기분 좋아지는 복숭아! 말랑말랑 달콤한 과육이 일품이에요."},
    "Q": {"name": "Quince (모과)", "emoji": "🍐", "badge": "향기로운 차 한 잔의 여유", "desc": "은은하고 깊은 향을 가진 모과! 따뜻한 청으로 만들어 마시면 마음까지 따뜻해져요."},
    "R": {"name": "Raspberry (라즈베리)", "emoji": "🍒", "badge": "새콤달콤 귀여운 베리", "desc": "동글동글 작고 예쁜 라즈베리! 요거트나 케이크 위에 올리면 완벽한 포인트가 됩니다."},
    "S": {"name": "Strawberry (딸기)", "emoji": "🍓", "badge": "달콤함이 팡팡 터지는 왕", "desc": "새빨간 빛깔에 달콤함이 가득! 누구에게나 사랑받는 최고의 인기 과일이에요."},
    "T": {"name": "Tangerine (귤)", "emoji": "🍊", "badge": "손이 멈추지 않는 겨울 필수품", "desc": "까먹다 보면 어느새 한 박스 뚝딱! 새콤달콤 손이 자꾸 가는 친근한 과일이에요."},
    "U": {"name": "Ugli Fruit (어글리 프루트)", "emoji": "🍊", "badge": "못생겨도 맛은 최고", "desc": "겉모습은 울퉁불퉁해도 속은 자몽과 오렌지가 섞여 달콤하고 시원한 반전 과일이에요."},
    "V": {"name": "Vanilla Bean (바닐라)", "emoji": "🍦", "badge": "달콤한 향기의 마법사", "desc": "디저트의 풍미를 더욱 깊게 만들어주는 바닐라! 달콤하고 포근한 향을 선물해 줍니다."},
    "W": {"name": "Watermelon (수박)", "emoji": "🍉", "badge": "시원함이 팡팡 터지는 과일", "desc": "아삭한 과육과 시원한 과즙이 가득한 수박! 한 조각이면 더위도 싹 달아나요."},
    "X": {"name": "Ximenia (시메니아)", "emoji": "🟡", "badge": "희귀하고 특별한 야생 과일", "desc": "자연 그대로의 매력을 간직한 희귀 과일! 새콤하고 자두와 비슷한 맛이 특징이에요."},
    "Y": {"name": "Yuzu (유자)", "emoji": "🍋", "badge": "향긋하고 톡 쏘는 상큼함", "desc": "상큼한 향이 매력적인 유자! 유자차로 마시면 감기도 뚝 떨어지는 기분이에요."},
    "Z": {"name": "Zucchini Fruit (애호박 열매)", "emoji": "🥒", "badge": "담백하고 순한 식재료", "desc": "채소 같지만 과일로 분류되는 애호박! 부드럽고 담백한 맛으로 다양한 요리에 쓰여요."}
}

# 알파벳 선택 옵션
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    selected_alphabet = st.selectbox(
        "✨ 알파벳을 하나 고르고 과일을 확인하세요!",
        list(fruit_data.keys()),
        index=0  # 기본값 A
    )
    
    submit_btn = st.button("💖 과일 추천받기 💖", use_container_width=True)

st.write("")

# 결과 출력 영역
if submit_btn or selected_alphabet:
    data = fruit_data[selected_alphabet]
    
    st.balloons()  # 귀여운 풍선 애니메이션
    
    st.markdown(f"""
        <div class="recommend-box">
            <div style="font-size: 3.5rem;">{data['emoji']}</div>
            <div style="color: #FF8EA5; font-weight: bold; margin-top: 5px;">[{data['badge']}]</div>
            <div class="fruit-title">{data['name']}</div>
            <div class="fruit-desc">{data['desc']}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("<p style='text-align: center; color: #BBB; font-size: 0.8rem;'>Made with 💕 using Streamlit</p>", unsafe_allow_html=True)
