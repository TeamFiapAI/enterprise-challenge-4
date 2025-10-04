import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from repository.oracle import get_registros_dashboard

# Função para carregar dados
@st.cache_data
def load_data():
    df = get_registros_dashboard()
    df['DATA_COLETA'] = pd.to_datetime(df['DATA_COLETA'])
    return df

df = load_data()

# Menu lateral
st.sidebar.title("Menu")
page = st.sidebar.radio("Ir para:", ["Home", "Visão Geral", "Por Máquina", "Por Operador", "Detalhes de Registros"])

# Página: Home
if page == "Home":
    st.title("Dashboard de Monitoramento de Máquinas")
    st.markdown("""
    Este dashboard apresenta os registros coletados por máquinas através do ESP32.  

    Você pode explorar:
    - **Visão Geral**: Principais indicadores de performance e distribuição de temperatura e umidade.
    - **Por Máquina**: Desempenho e alertas individuais por máquina.
    - **Por Operador**: Performance e registros de cada operador.
    - **Detalhes de Registros**: Tabela completa e gráficos detalhados de alarmes.

    Os KPIs e gráficos ajudam a entender:
    - Temperatura média das máquinas e distribuição ao longo do tempo.
    - Umidade média e variações entre máquinas.
    - Ocorrência de alarmes por mês, semestre, hora e dia da semana.
    - Atividade de operadores e distribuição de registros por máquina.

    Cada gráfico possui uma seção de **vantagens**, mostrando padrões, tendências e insights para facilitar a interpretação.
    """)

# Página: Visão Geral
elif page == "Visão Geral":
    st.title("Visão Geral")

    total_registros = len(df)
    total_maquinas = df['ID_MAQUINA'].nunique()
    total_operadores = df['ID_OPERADOR'].nunique()
    total_alarme = df['ALARME'].sum()

    st.metric("Total de Registros", total_registros)
    st.metric("Máquinas Monitoradas", total_maquinas)
    st.metric("Operadores Ativos", total_operadores)
    st.metric("Alarmes Detectados", total_alarme)

    st.subheader("Temperatura e Umidade Médias")
    col1, col2 = st.columns(2)
    col1.metric("Temperatura Média", f"{df['TEMPERATURA'].mean():.2f} °C")
    col2.metric("Umidade Média", f"{df['UMIDADE'].mean():.2f} %")

    # Gráfico de temperatura
    st.subheader("Distribuição de Temperatura")
    plt.figure(figsize=(10,4))
    plt.hist(df['TEMPERATURA'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Quantidade de registros")
    st.pyplot(plt)

    st.markdown("""
    **Vantagens deste gráfico:**
    - Mostra a variação de temperatura entre todas as máquinas.
    - Ajuda a identificar picos de temperatura que podem indicar problemas.
    - Facilita comparação rápida da condição geral das máquinas.
    """)

# Por Máquina
elif page == "Por Máquina":
    st.title("Análise por Máquina")
    maquina = st.selectbox("Selecione a Máquina:", df['NOME_MAQUINA'].unique())
    df_maquina = df[df['NOME_MAQUINA'] == maquina]

    st.metric("Registros", len(df_maquina))
    st.metric("Alarmes", df_maquina['ALARME'].sum())
    st.metric("Temperatura Média", f"{df_maquina['TEMPERATURA'].mean():.2f} °C")
    st.metric("Umidade Média", f"{df_maquina['UMIDADE'].mean():.2f} %")

    st.subheader("Histórico de Temperatura")
    plt.figure(figsize=(10,4))
    plt.plot(df_maquina['DATA_COLETA'], df_maquina['TEMPERATURA'], marker='o')
    plt.xlabel("Data")
    plt.ylabel("Temperatura (°C)")
    st.pyplot(plt)

    st.markdown(f"""
    **Vantagens deste gráfico:**
    - Mostra como a temperatura desta máquina evolui ao longo do tempo.
    - Permite identificar momentos específicos em que a máquina pode ter sofrido picos ou falhas.
    - Facilita acompanhamento individual de cada equipamento.
    - Alarmes podem ser cruzados com a temperatura para investigar possíveis causas.
    """)
# Por Operador
elif page == "Por Operador":
    st.title("Análise por Operador")
    operador = st.selectbox("Selecione o Operador:", df['NOME_OPERADOR'].unique())
    df_operador = df[df['NOME_OPERADOR'] == operador]

    st.metric("Registros", len(df_operador))
    st.metric("Alarmes", df_operador['ALARME'].sum())
    st.metric("Temperatura Média", f"{df_operador['TEMPERATURA'].mean():.2f} °C")
    st.metric("Umidade Média", f"{df_operador['UMIDADE'].mean():.2f} %")

    st.subheader("Registros por Máquina")
    contagem_maquinas = df_operador.groupby('NOME_MAQUINA').size()
    st.bar_chart(contagem_maquinas)

    st.markdown(f"""
    **Vantagens deste gráfico:**
    - Permite ver como cada operador está distribuindo sua atividade entre as máquinas.
    - Facilita identificar operadores com mais registros ou com maior número de alarmes.
    - Ajuda na análise de performance individual e no planejamento de treinamentos.
    - Permite correlacionar alarmes com operadores para investigar possíveis causas.
    """)

# Detalhes de Registros
elif page == "Detalhes de Registros":
    st.title("Detalhes de Alarmes")

    # Preparação dos dados
    df['DIA'] = df['DATA_COLETA'].dt.date
    df['HORA'] = df['DATA_COLETA'].dt.hour
    df['MES_ANO'] = df['DATA_COLETA'].dt.to_period('M').astype(str)  # "2023-10", "2024-01"
    df_sorted = df.sort_values('DATA_COLETA')


    # Alarmes por mês e ano (barras)
    st.subheader("Alarmes por mês e ano")
    alarme_mes_ano = df.groupby('MES_ANO')['ALARME'].sum()
    st.bar_chart(alarme_mes_ano)
    st.markdown("""
    **Vantagens deste gráfico:**
    - Mostra claramente em quais meses os alarmes foram mais frequentes.
    - Permite identificar rapidamente tendências sazonais ou mudanças ao longo do ano.
    """)

    
    # Alarmes acumulados por semestre
    st.subheader("Alarmes acumulados por semestre")
    df['ANO'] = df['DATA_COLETA'].dt.year
    df['SEMESTRE'] = df['DATA_COLETA'].dt.month.apply(lambda x: 1 if x <= 6 else 2)
    df['SEMESTRE_LABEL'] = df['ANO'].astype(str) + "-S" + df['SEMESTRE'].astype(str)

    alarme_semestre = df.groupby('SEMESTRE_LABEL')['ALARME'].sum()
    st.bar_chart(alarme_semestre)
    st.markdown("""
    **Vantagens deste gráfico:**
    - Mostra tendências de médio prazo, agrupando dados por semestre.
    - Facilita comparação de períodos maiores, útil para planejamento e análise de desempenho.
    """)

    # Heatmap de hora x dia da semana
    st.subheader("Alarmes por hora x dia da semana (heatmap)")
    df['DIA_SEMANA'] = df['DATA_COLETA'].dt.day_name()
    alarme_hora_dia_semana = df.pivot_table(index='HORA', columns='DIA_SEMANA', values='ALARME', aggfunc='sum', fill_value=0)

    plt.figure(figsize=(12,6))
    plt.imshow(alarme_hora_dia_semana, aspect='auto', cmap='Reds')
    plt.colorbar(label='Número de Alarmes')
    plt.xlabel("Dia da semana")
    plt.ylabel("Hora")
    plt.yticks(range(0,24), range(0,24))
    plt.xticks(range(len(alarme_hora_dia_semana.columns)), alarme_hora_dia_semana.columns, rotation=45)
    plt.title("Heatmap de Alarmes por hora x dia da semana")
    plt.tight_layout()
    st.pyplot(plt)
    st.markdown("""
    **Vantagens deste gráfico:**
    - Mostra em quais dias da semana e horários os alarmes mais acontecem, independente do mês.
    - Facilita ver padrões repetitivos, por exemplo, segundas-feiras à tarde podem ter mais alarmes.
    - Ajuda a planejar manutenção ou operação em horários críticos.
    """)