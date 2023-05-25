import streamlit as st 
import pandas as pd
import plotly.express as xp
import openpyxl as op

st.set_page_config(page_title="DashBoard de Vendas",page_icon=":bar_chart:",layout="wide", initial_sidebar_state="expanded")
st.title(":green[DashBoard de Vendas]")
st.markdown("---")
df =pd.read_excel(
    io="Folha.xlsx",
    engine="openpyxl"
    )
DF = df.dropna()



################# SELECIONANDO OS NOMES DOS CLIENTES ################################
st.sidebar.header(":green[Produtos Por Categoria]")
category = st.sidebar.multiselect(":orange[Selecione uma Categorias]",options=DF['CATEGORIA'].unique(),
                                                default=DF['CATEGORIA'].unique())
selection_query =DF.query('CATEGORIA==@category ')

############################## SOMANDO OS TOTAIS DE CARTOES ###############################
total_profit=round(selection_query['LUCRO'].sum())
avg_rating =round(selection_query['MEDIA'].mean(),2)
############ COLUNAS ##############################
col1, col2 =st.columns(2)
with col1:
    st.markdown("### :green[TOTAL DE LUCRO]")
    st.subheader(f":orange[{total_profit} MZN]")
    
with col2:
    st.markdown("### :green[MEDIA]")
    st.subheader(f":orange[{avg_rating } MÉDIA]")
st.markdown("---")

############### SOMANDO LUCRO POR CATEGORIA ################################
profit_by_category= (selection_query.groupby(by=['CATEGORIA']).sum()[['LUCRO']])

profit_by_category_barchart = xp.bar(profit_by_category,x="LUCRO",y=profit_by_category.index, title="Lucro por Categoria", color_discrete_sequence=["#17f50c"],)
profit_by_category_barchart.update_layout(plot_bgcolor=("rgba(0,1,0,0)"),xaxis=(dict(showgrid=False)))

profit_by_category_piechart = xp.pie(profit_by_category,names=profit_by_category.index,values="LUCRO",title="Media Percentual %",hole=.3, color=profit_by_category.index,
                  color_discrete_sequence=xp.colors.sequential.RdPu_r)
coluna1, coluna2= st.columns(2)
coluna1.plotly_chart(profit_by_category_barchart , use_container_width=True)
coluna2.plotly_chart(profit_by_category_piechart,use_container_width=True)
st.markdown("---")
coluna3, =st.columns(1)
with coluna3:
    st.markdown("### :green[Linha de Lucro por Categoria]")
    st.line_chart(profit_by_category)
 
hide ="""
<style>
header {visibility:hidden}
footer {visibility:hidden}
</style>

"""
st.markdown(hide,unsafe_allow_html=True)