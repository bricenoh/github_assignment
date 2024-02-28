import streamlit as st
import pandas as pd
st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('data/kart_stats.csv')
df_kart = df_kart[['Body','Weight','Acceleration','Ground Speed','Ground Handling','Mini-Turbo']]
# st.write(df_kart)

st.dataframe(df_kart.style
             .highlight_max(color='lightgreen', axis=0, subset=['Weight','Acceleration','Ground Speed','Ground Handling','Mini-Turbo'])
             .highlight_min(color='red', axis=0, subset=['Weight','Acceleration','Ground Speed','Ground Handling','Mini-Turbo'])
             )

st.header('Kart Racing Qualities Based on Speed')
st.text('how speed influences ground racing qualities')
st.line_chart(df_kart, x='Ground Speed', y=['Acceleration','Ground Handling','Mini-Turbo'])


st.header('Kart Weights')
st.text('how much each kart body weighs')

# df_kart_sorted = df_kart.sort_values('Weight', ascending=False)
st.bar_chart (df_kart, x='Body', y='Weight')


# Create a Select Box for a drop down
st.header('Individual Kart Stats')
chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body']==chosen_kart]
df_single_kart =df_single_kart.drop(columns = ['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_kart,x='category',y='strength')


