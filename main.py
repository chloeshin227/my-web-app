import streamlit as st

# 페이지 설정 (귀여운 파비콘과 타이틀)
st.set_page_config(
    page_title="MBTI 퐁당 여행 떠나기!",
    page_icon="✈️",
    layout="centered"
)

# 커스텀 CSS로 파스텔톤 & 귀여운 스타일 적용
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
    .dest-title {
        color: #FF407D;
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 10px;
    }
    .dest-desc {
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
st.markdown("<p class='title-text'>✨ MBTI별 몽글몽글 여행지 추천 ✨</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>나의 성향과 딱 맞는 인생 여행지는 어디일까요? 🌸</p>", unsafe_allow_html=True)

# MBTI 데이터 베이스
mbti_data = {
    "ISTJ": {
        "title": "🇩🇪 독일 뮌헨",
        "badge": "📋 규칙적이고 완벽한 플래너",
        "desc": "정돈되고 체계적인 분위기 속에서 완벽한 일정대로 여행을 즐길 수 있는 곳이에요! 고풍스러운 건축물과 박물관 탐방을 추천해요. 🏰",
        "emoji": "🏰"
    },
    "ISFJ": {
        "title": "🇯🇵 일본 교토",
        "badge": "🌸 따뜻하고 조용한 힐링러",
        "desc": "고즈넉하고 평화로운 풍경 속에서 마음의 안정을 찾을 수 있어요. 차분한 정원과 따뜻한 료칸 온천이 완벽한 힐링을 선물할 거예요. 🍵",
        "emoji": "🍵"
    },
    "INFJ": {
        "title": "🇨🇭 스위스 인터라켄",
        "badge": "🌲 깊은 생각과 감성의 소유자",
        "desc": "웅장한 대자연을 바라보며 깊은 생각에 잠기기 좋은 곳이에요. 알프스의 아름다운 풍경이 영감을 듬뿍 줄 거예요. 🏔️",
        "emoji": "🏔️"
    },
    "INTJ": {
        "title": "🇬🇧 영국 런던",
        "badge": "🏛️ 지적 호기심 가득한 탐험가",
        "desc": "풍부한 역사와 수많은 대형 박물관, 미술관이 가득한 도시예요! 혼자서도 알차고 깊이 있는 여행을 즐기기에 제격이랍니다. 🖼️",
        "emoji": "🖼️"
    },
    "ISTP": {
        "title": "🇳🇿 뉴질랜드 퀸스타운",
        "badge": "🏄‍♂️ 쿨하고 액티브한 자율러",
        "desc": "번지점프, 스카이다이빙 등 익스트림 스포츠의 천국! 짜릿한 모험을 경험하며 자유로움을 만끽해 보세요! 🪂",
        "emoji": "🪂"
    },
    "ISFP": {
        "title": "🇮🇩 인도네시아 발리",
        "badge": "🎨 예술적 감성의 여유로운 모험가",
        "desc": "아름다운 석양과 예술적 풍경이 가득한 섬이에요. 발리의 감성 카페와 여유로운 해변에서 나만의 리듬대로 쉬어가세요. 🌴",
        "emoji": "🌴"
    },
    "INFP": {
        "title": "🇨🇿 체코 프라하",
        "badge": "🧸 동화 같은 낭만을 꿈꾸는 시인",
        "desc": "골목마다 낭만이 넘쳐나는 동화 같은 도시예요. 붉은 지붕과 돌다리를 거닐며 나만의 감성 여행 소설을 써보세요. 🏰",
        "emoji": "🎠"
    },
    "INTP": {
        "title": "🇮🇸 아이슬란드 레이캬비크",
        "badge": "🌌 호기심 가득한 오로라 연구가",
        "desc": "지구 같지 않은 신비로운 대자연과 오로라를 관찰할 수 있는 곳이에요. 독특한 자연 현상을 탐구하며 특별한 추억을 만들어보세요! 🌌",
        "emoji": "🌌"
    },
    "ESTP": {
        "title": "🇺🇸 미국 라스베이거스",
        "badge": "🎉 스릴과 즐거움을 쫓는 에너자이저",
        "desc": "화려한 조명과 스릴 넘치는 쇼가 끊이지 않는 에너제틱한 도시! 지루할 틈이 없는 순간들을 즐겨보세요! 🎰",
        "emoji": "🎰"
    },
    "ESFP": {
        "title": "🇪🇸 스페인 바르셀로나",
        "badge": "💃 세상에서 제일 흥이 많은 인싸",
        "desc": "열정적인 사람들, 맛있는 타파스, 화려한 가우디 건축물이 가득한 곳! 매일매일 축제 같은 여행을 만날 수 있어요. 💃",
        "emoji": "💃"
    },
    "ENFP": {
        "title": "🇹🇭 태국 방콕",
        "badge": "🎈 독창적이고 에너지 넘치는 입담꾼",
        "desc": "화려한 야시장, 다양한 먹거리, 생기 넘치는 밤문화가 가득한 곳! 늘 새로운 재미와 유쾌한 인연이 기다리고 있어요. 🥭",
        "emoji": "🥭"
    },
    "ENTP": {
        "title": "🇹🇼 대만 타이베이",
        "badge": "💡 색다른 재미를 찾아 나서는 아이디어왕",
        "desc": "북적이는 야시장 탐방부터 지우펀 골목길까지! 끊임없이 새로운 볼거리와 먹거리가 당신의 호기심을 자극할 거예요. 🧋",
        "emoji": "🧋"
    },
    "ESTJ": {
        "title": "🇸🇬 싱가포르",
        "badge": "🌆 정돈되고 알찬 모범 여행가",
        "desc": "깨끗하고 안전하며 모든 것이 효율적으로 정리된 도시국가예요! 알찬 일정으로 랜드마크를 정복하는 재미가 있어요. 🏙️",
        "emoji": "🏙️"
    },
    "ESFJ": {
        "title": "🇻🇳 베트남 다낭",
        "badge": "🥰 따뜻하고 친절한 분위기 메이커",
        "desc": "친절한 미소와 맛있는 음식, 편안한 리조트가 가득해요! 사랑하는 사람들과 함께 오순도순 가기에 가장 완벽한 여행지랍니다. 🥥",
        "emoji": "🥥"
    },
    "ENFJ": {
        "title": "🇮🇹 이탈리아 피렌체",
        "badge": "🎨 따스한 마음을 전하는 예술가",
        "desc": "르네상스의 예술과 따뜻한 감성이 살아있는 도시예요. 두오모 성당에 올라 확 트인 풍경을 보며 로맨틱한 추억을 만들어보세요! 🍕",
        "emoji": "🍕"
    },
    "ENTJ": {
        "title": "🇺🇸 미국 뉴욕",
        "badge": "👑 세상을 주도하는 열정 리더",
        "desc": "트렌드의 중심지! 밤에도 꺼지지 않는 도시의 빌딩 숲과 화려한 브로드웨이에서 넘치는 열정을 느껴보세요! 🗽",
        "emoji": "🗽"
    }
}

# 사용자 입력 영역
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    selected_mbti = st.selectbox(
        "✨ 당신의 MBTI를 선택해 주세요!",
        list(mbti_data.keys()),
        index=6  # 기본값 INFP
    )
    
    submit_btn = st.button("💖 추천 여행지 확인하기 💖", use_container_width=True)

st.write("")

# 결과 출력 영역
if submit_btn or selected_mbti:
    data = mbti_data[selected_mbti]
    
    st.balloons()  # 깜찍한 풍선 애니메이션 효과
    
    st.markdown(f"""
        <div class="recommend-box">
            <div style="font-size: 3rem;">{data['emoji']}</div>
            <div style="color: #FF8EA5; font-weight: bold; margin-top: 5px;">[{data['badge']}]</div>
            <div class="dest-title">{data['title']}</div>
            <div class="dest-desc">{data['desc']}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("<p style='text-align: center; color: #BBB; font-size: 0.8rem;'>Made with 💕 using Streamlit</p>", unsafe_allow_html=True)
