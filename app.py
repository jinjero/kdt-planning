import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="스파르타 취업 역량 평가",
    page_icon="🧑🏻‍🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 메인 타이틀
st.title("🧑🏻‍🎓 스파르타 취업 역량 평가")
st.markdown("---")

# 사이드바
st.sidebar.header("MENU")

# 세션 상태 초기화
if 'current_page' not in st.session_state:
    st.session_state.current_page = "평가표"

# 버튼 메뉴
if st.sidebar.button("평가표", use_container_width=True):
    st.session_state.current_page = "평가표"
if st.sidebar.button("출제자 평가 템플릿", use_container_width=True):
    st.session_state.current_page = "출제자 평가 템플릿"
if st.sidebar.button("출제자 문제 템플릿", use_container_width=True):
    st.session_state.current_page = "출제자 문제 템플릿"

page = st.session_state.current_page

if page == "평가표":
    st.header("평가표")
    
    # 개발/비개발 토글
    job_type = st.selectbox("과목 선택", ["개발", "비개발"])
    
    if job_type == "개발":
        st.subheader("개발 평가표")
        # 계층 구조 정의 (예시)
        dev_hierarchy = {
            '코드': {
                '요구사항 해석': ['프로젝트 과제 목적에 맞게 구현했는가', '제공된 입출력 데이터를 통과하는가'],
                '알고리즘/로직': ['기본 문법(반복문, 조건문 등) 적절히 활용했는가', '효율적인 알고리즘 및 자료구조 사용했는가'],
                '코드 품질 및 최적화': ['적절한 함수 분리 및 모듈화가 되어있는가', '시간/공간복잡도 개선 노력이 있었는가', '중복 코드를 최소화하여 간결하게 작성했는가'],
                '예외 처리': ['예상 가능한 예외 사항을 고려했는가', 'try-catch-finally 구문을 적절히 사용했는가']
            },
            '프레임워크': {
                '구조 설계 이해도': ['프레임워크 구조 특성을 이해하고 적용했는가', '디렉토리 구조를 일관성있게 설계했는가'],
                '기능 구현 방식 적절성': ['프레임워크 방식에 맞춰 기능을 구현했는가', '내장 기능과 라이브러리를 알맞게 활용했는가'],
                '역할 분리 및 재사용성': ['로직, 서비스 등을 목적에 따라 분리했는가', '컴포넌트화, 모듈화 등을 통해 재사용을 할 수 있는가'],
                '상태 및 흐름 관리': ['상태 관리나 요청-응답 흐름을 일관되게 처리했는가', '프레임워크에 맞는 상태/라우팅 방식을 사용했는가'],
                '설정 및 의존성 관리': ['환경설정 파일(.env, web.xml 등)을 적절히 구성했는가', '외부 라이브러리, 모듈 의존성을 관리했는가'],
            }
        }
        # 표로 변환
        rows = []
        for 대분류, 중분류_dict in dev_hierarchy.items():
            for 중분류, 소분류_list in 중분류_dict.items():
                for 소분류 in 소분류_list:
                    rows.append({'대분류': 대분류, '중분류': 중분류, '소분류': 소분류})
        df = pd.DataFrame(rows)

    else:
        st.subheader("비개발 평가표")
        # 계층 구조 정의 (예시)
        biz_hierarchy = {
            '기획': {
                '문제 정의': ['해결해야 할 문제와 핵심 이슈를 제대로 설정했는가'],
                '요구사항 분석': ['고객/시장/업무의 요구사항을 잘 분석했는가', '다양한 관계자의 니즈를 반영했는가', '충돌되는 요구사항을 조율했는가'],
                '목표 설정': ['달성 가능한 목표/지표를 설계했는가', '핵심 기능 또는 가치 요소를 제대로 도출했는가'],
                '전략 및 기획': ['목표를 달성하기 위한 구체적인 전략을 수립했는가', '전개 방식이 일관되고 설득력있는 전략/기획인가'],
            },
            '완성도': {
                '결과물 완성도': ['계획한 목표를 달성했는가', '목표 달성 과정이 설득력있게 정리되었는가'],
                '문제 해결력': ['정성적/정량적 데이터를 적절히 활용했는가', '데이터 해석이 설득력을 갖고 판단의 근거로 기능했는가'],
                '전문성': ['직무에 맞는 툴을 목적에 맞게 활용했는가', '직무 용어 및 개념을 올바르게 사용했는가'],
                '성과 분석': ['결과물에 대한 성과 분석을 수행했는가', '문제점과 긍정적인 성과 모두를 도출했는가'],
                '개선 제안': ['수행 과정을 바탕으로 개선 방향을 논리적으로 제시했는가']
            },
            '소프트스킬': {
                '협업 및 전달력': ['다른 직무 담당자와의 협업을 고려했는가', '기획 의도, 결과물을 명확하게 설명했는가'],
                '창의성': ['결과물을 도출하기 위한 과정이 창의적으로 진행됐는가', '다른 수험생들과 비교되는 지점이 있는가'],
            }
        }
        # 표로 변환
        rows = []
        for 대분류, 중분류_dict in biz_hierarchy.items():
            for 중분류, 소분류_list in 중분류_dict.items():
                for 소분류 in 소분류_list:
                    rows.append({'대분류': 대분류, '중분류': 중분류, '소분류': 소분류})
        df = pd.DataFrame(rows)

    
    # 평가 표 편집 가능하게 표시
    # 드롭다운 옵션 준비
    dev_major_options = list(dev_hierarchy.keys()) if job_type == "개발" else []
    dev_mid_options = sum([list(v.keys()) for v in dev_hierarchy.values()], []) if job_type == "개발" else []
    dev_sub_options = sum([sum([vv for vv in v.values()], []) for v in dev_hierarchy.values()], []) if job_type == "개발" else []
    biz_major_options = list(biz_hierarchy.keys()) if job_type == "비개발" else []
    biz_mid_options = sum([list(v.keys()) for v in biz_hierarchy.values()], []) if job_type == "비개발" else []
    biz_sub_options = sum([sum([vv for vv in v.values()], []) for v in biz_hierarchy.values()], []) if job_type == "비개발" else []

    # 각 표에 맞는 옵션 지정
    if job_type == "개발":
        col_config = {
            "대분류": st.column_config.SelectboxColumn("대분류", options=dev_major_options, required=True),
            "중분류": st.column_config.SelectboxColumn("중분류", options=dev_mid_options, required=True),
            "소분류": st.column_config.TextColumn("소분류", width="large"),
        }
    else:
        col_config = {
            "대분류": st.column_config.SelectboxColumn("대분류", options=biz_major_options, required=True),
            "중분류": st.column_config.SelectboxColumn("중분류", options=biz_mid_options, required=True),
            "소분류": st.column_config.TextColumn("소분류", width="large"),
        }

    st.dataframe(df, use_container_width=True)

    # 멀티셀렉트로 행 선택 (인덱스 기준)
    selected_idx = st.multiselect(
        "추가할 행(들)을 선택하세요",
        options=df.index,
        format_func=lambda x: f"{x+1}행: {df.loc[x, '대분류']} / {df.loc[x, '중분류']} / {df.loc[x, '소분류']}"
    )

    # 9개 열 구성 (앞 3개: 대분류, 중분류, 소분류)
    template_columns = [
        "대분류", "중분류", "소분류",
        "평가 내용", "배점", "상", "중", "하", "배점 X"
    ]
    if st.button("평가 템플릿에 추가"):
        if selected_idx:
            selected = df.loc[selected_idx]
            selected_template = pd.DataFrame({
                "대분류": selected["대분류"].values,
                "중분류": selected["중분류"].values,
                "소분류": selected["소분류"].values,
                "평가 내용": "",
                "배점": "",
                "상": "",
                "중": "",
                "하": "",
                "배점 X": ""
            })
            if "template_table" not in st.session_state:
                st.session_state["template_table"] = pd.DataFrame(columns=template_columns)
            st.session_state["template_table"] = pd.concat([
                st.session_state["template_table"], selected_template
            ], ignore_index=True).drop_duplicates()
            st.success("평가 템플릿에 추가되었습니다!")
        else:
            st.warning("추가할 행을 먼저 선택해 주세요.")

elif page == "출제자 평가 템플릿":
    st.header("출제자 평가 템플릿")
    
    if "template_table" in st.session_state:
        # 텍스트 입력 가능한 컬럼 설정
        col_config = {
            "평가 내용": st.column_config.TextColumn("평가 내용", width="large"),
            "배점": st.column_config.NumberColumn("배점", width="small", format="%d"),
            "상": st.column_config.TextColumn("상", width="large"),
            "중": st.column_config.TextColumn("중", width="large"),
            "하": st.column_config.TextColumn("하", width="small"),
            "배점 X": st.column_config.TextColumn("배점 X", width="large"),
        }
        st.data_editor(
            st.session_state["template_table"],
            column_config=col_config,
            use_container_width=True,
            num_rows="dynamic"
        )
    else:
        st.info("아직 추가된 항목이 없습니다.")

elif page == "설정":
    st.header("⚙️ 설정")
    
    st.subheader("사용자 설정")
    
    name = st.text_input("이름", value="사용자")
    email = st.text_input("이메일", value="user@example.com")
    
    st.subheader("알림 설정")
    notifications = st.checkbox("알림 받기", value=True)
    email_updates = st.checkbox("이메일 업데이트", value=False)
    
    st.subheader("테마 설정")
    theme = st.selectbox("테마 선택", ["라이트", "다크", "자동"])
    
    if st.button("설정 저장"):
        st.success("설정이 저장되었습니다!")

# 푸터
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>KDT Planning Dashboard © 2024</p>
    </div>
    """,
    unsafe_allow_html=True
)
