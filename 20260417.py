import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data
def load_data():
    df = pd.read_csv('sales_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()
# 사이드바 필터
with st.sidebar:
    st.title(' 필터')
    selected_regions = st.multiselect('지역', df['region'].unique(), default=df['region'].unique())
    date_range = st.date_input('기간', value=[df['date'].min(), df['date'].max()])
# 필터 적용
df_f = df[
    df['region'].isin(selected_regions) &
    (df['date'] >= pd.Timestamp(date_range[0])) &
    (df['date'] <= pd.Timestamp(date_range[1]))
]
# KPI + 차트 — df_f 를 사용하도록 수정
col1, col2 = st.columns(2)
col1.metric('필터 적용 후 총 매출', f'₩{df_f["sales"].sum():,}')
col2.metric('주문 건수', f'{len(df_f):,}건')

