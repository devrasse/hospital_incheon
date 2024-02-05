import streamlit as st

st.set_page_config(layout='wide')
# HTML 파일을 읽어오기
with open("hospital_incheon.html", "r",  encoding="utf-8") as f:
    html_code = f.read()

st.markdown('<div class="centered"><h1 style="text-align:center;">🏥 인천시 설 명절 비상진료 🏥</h1></div>', unsafe_allow_html=True)

with st.container(border=True,height=740):
    # Stremlit 앱에 HTML 표시
    with st.spinner("로딩 중..."):
        st.components.v1.html(html_code,  height=700, scrolling=False)

#st.write("참고: 정확한 진료 확인은 방문전 연락하여 확인하여 주시기 바랍니다.")
styled_text = '<p style="font-size: 20px; color: white;">참고: 정확한 진료 확인은 해당 병원에 문의하여 주시기 바랍니다.</p>'
st.write(styled_text, unsafe_allow_html=True)
