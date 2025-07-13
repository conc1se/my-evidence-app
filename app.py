import streamlit as st
import streamlit.components.v1 as components

# 설정: 비밀번호
PASSWORD = "letmein"

# UI
st.set_page_config(page_title="Evidence Dashboard 🔐", layout="wide")
st.title("📊 Evidence Dashboard 로그인")

password = st.text_input("비밀번호를 입력하세요", type="password")

if password == PASSWORD:
    st.success("✅ 인증 성공! Evidence 리포트를 아래에서 확인하세요.")
    # Evidence index.html을 iframe으로 삽입
    components.html(
        """
        <iframe src="evidence/index.html" width="100%" height="900px" style="border:none;"></iframe>
        """,
        height=900,
    )
elif password:
    st.error("❌ 비밀번호가 틀렸습니다.")
