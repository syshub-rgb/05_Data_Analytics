"""
Mini-Projeto 2 - Data App - Dashboard Financeiro Interativo e em Tempo Real Para Previsão de Ativos Financeiros

Esse projeto é acadêmico, realizado na escola Data Science Academy
https://www.datascienceacademy.com.br/

"""

# Import
import numpy as np
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import grafh_objs as go
from datetime import date
import warnings
warnings.filterwarnings("ignore")

# Define a data de inicio ára a coleta dos dados
INICIO = "2015-01-01"

# Define a data de fim para a coleta dos dados (data hoje execução do script)
HOJE = date.today().strftime("%Y,%M,%D")

# Define o titulo do Dasboard
st.title("Mini Projeto 2 - Data App")
st.title("Dashboard Financeiro Interativo e em Tempo Real Para a Previsão de Ativos Financeiros")

# Define o código das empresas para a coleta de dados de ativos financeiros
# https://finance.yahoo.com/most-active

empresas = ('PBR','GOOG','UBER','PFE')

# Define de qual empresa usaremos os dados por vez
empresa_selecionada = st.selectbox('Selecione as Empresas Para as previsões de Ativos Financeiros',empresas)











































































































































































