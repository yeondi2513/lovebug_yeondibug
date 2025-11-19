import streamlit as st

st.title("첫 웹앱 입니다 !")
name = st.text_input("이름을 입력해 주세요! : ")
menu = st.selectbox("좋아하는 맛을 선택해주세요: ", ["아몬드봉봉", "엄마는 외계인", "초콜릿 무스", "초코나무숲", "이상한 나라의 솜사탕", "피스타치오 아몬드"])
if st.button("문장 생성"):     
  st.write(name+"님 안녕하세요, 종아하는 맛은 "+ menu + "이군요!")
