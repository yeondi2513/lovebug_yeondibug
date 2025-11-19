import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MBTI by Country", layout="wide")

st.title("🌍 국가별 MBTI 비율 시각화")
st.write("원하는 국가를 선택하면 MBTI 16유형 비율을 인터랙티브 바 차트로 확인할 수 있습니다.")

# CSV 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 국가 선택
countries = df["Country"].sort_values().tolist()
selected_country = st.selectbox("국가를 선택하세요", countries)

# 선택한 국가 데이터만 필터링
row = df[df["Country"] == selected_country].iloc[0]

# MBTI 데이터만 추출
mbti_cols = [c for c in df.columns if c != "Country"]
values = row[mbti_cols].values
mbti_df = pd.DataFrame({"MBTI": mbti_cols, "Value": values})

# 1등 MBTI 찾기
top_type = mbti_df.loc[mbti_df["Value"].idxmax(), "MBTI"]

# 색상 설정
colors = []
for mbti in mbti_df["MBTI"]:
    if mbti == top_type:
        colors.append("red")
    else:
        colors.append("rgba(0, 123, 255, 0.6)")  # 파란 계열 그라데이션 느낌

# Plotly 그리기
fig = px.bar(
    mbti_df,
    x="MBTI",
    y="Value",
    color=mbti_df["MBTI"],
    color_discrete_sequence=colors,
    title=f"{selected_country} MBTI 비율",
)

fig.update_traces(marker_line_width=1.5, marker_line_color="black")
fig.update_layout(showlegend=False)

st.plotly_chart(fig, use_container_width=True)
