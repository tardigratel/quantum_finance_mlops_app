import streamlit as st
import requests
import locale
import json

# --- Funções de Lógica ---
# Mantendo a função de predição exatamente como estava
def get_prediction(payload):
    """
    Envia os dados do usuário para a API e retorna a previsão do credit score.
    """
    try:
        # Acessa os segredos da API e do endpoint
        endpoint = st.secrets["API-ENDPOINT"]
        headers = {
            "Content-Type": "application/json",
            "x-api-key": st.secrets["API-KEY"]
        }

        # Realiza a requisição POST para a API
        response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
        
        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Retorna o credit score da resposta JSON
            return response.json()['Credit_Score']
        else:
            # Retorna 999 em caso de erro na requisição
            return "999"
    except requests.exceptions.RequestException as e:
        # Exibe uma mensagem de erro em caso de falha na conexão
        st.error(f"Erro de conexão: {e}")
        # Retorna 998 em caso de erro de conexão
        return "998"


# --- Configuração da Página ---
# Define a configuração inicial da página
st.set_page_config(
    page_title="Quantum Finance - Credit Score Predictor", 
    page_icon=":moneybag:", 
    layout="wide"
)

# --- Layout da Aplicação ---
st.title("Quantum Finance - Credit Score Predictor")
st.markdown(
    """
    Esta aplicação permite que você faça a predição do credit score de um cliente com base em suas 
    informações pessoais e financeiras. 
    **Preencha os campos abaixo e clique em "Fazer Previsão"** para obter o resultado.
    """
)
st.markdown("---")

# Captura de dados do usuário
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Usamos um container para agrupar visualmente todos os inputs
with st.container():
    st.subheader("Informações do Cliente")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.number_input("Idade do Cliente", min_value=18, max_value=100, value=30, step=1)
        annual_income = st.number_input("Renda Anual do Cliente (R$)", min_value=0, value=0, step=1000)
        monthly_inhand_salary = st.number_input("Salário Mensal Líquido (R$)", min_value=0, value=0, step=100)
        
    with col2:
        num_bank_accounts = st.number_input("Número de Contas Bancárias", min_value=0, value=1, step=1)
        num_credit_card = st.number_input("Número de Cartões de Crédito", min_value=0, value=1, step=1)
        interest_rate = st.number_input("Taxa de Juros Anual (%)", min_value=0.0, value=0.0, step=0.1)
        
    with col3:
        delay_from_due_date = st.number_input("Atraso em relação data de vencimento (dias)", min_value=0, value=0, step=1)
        num_of_delayed_payment = st.number_input("Número de Pagamentos Atrasados", min_value=0, value=0, step=1)
        changed_credit_limit = st.number_input("Limite de Crédito Alterado (R$)", min_value=0, value=0, step=100)
        
    with col4:
        num_credit_inquiries = st.number_input("Número de Consultas de Crédito", min_value=0, value=0, step=1)
        credit_utilization_ratio = st.number_input("Taxa de Utilização de Crédito (%)", min_value=0.0, value=0.0, step=0.1)
        total_emi_per_month = st.number_input("Total de EMI por Mês (R$)", min_value=0, value=0, step=100)
        
    with col5:
        amount_invested_monthly = st.number_input("Valor Investido Mensalmente (R$)", min_value=0, value=0, step=100)
        monthly_balance = st.number_input("Saldo Mensal (R$)", min_value=0, value=0, step=100)

# --- Lógica de Predição e Resultado ---
st.markdown("---")

# Montagem do payload para enviar os dados para a API
payload = {
    'Age': f'{age}',
    'Annual_Income': f"{annual_income}",
    'Monthly_Inhand_Salary': f"{monthly_inhand_salary}",
    'Num_Bank_Accounts': f"{num_bank_accounts}",
    'Num_Credit_Card': f"{num_credit_card}",
    'Interest_Rate': f"{interest_rate}",
    'Delay_from_due_date': f"{delay_from_due_date}", 
    'Num_of_Delayed_Payment': f"{num_of_delayed_payment}",
    'Changed_Credit_Limit': f"{changed_credit_limit}", 
    'Num_Credit_Inquiries': f"{num_credit_inquiries}",
    'Credit_Utilization_Ratio': f"{credit_utilization_ratio}", 
    'Total_EMI_per_month': f"{total_emi_per_month}",
    'Amount_invested_monthly': f"{amount_invested_monthly}",
    'Monthly_Balance': f"{monthly_balance}"
}

# Botão para fazer a previsão
if st.button("Fazer Previsão"):
    # Enviar os dados para o endpoint da API
    with st.spinner("Calculando..."):
        credit_score = int(get_prediction(payload))

        # Usamos um container para mostrar o resultado da predição
        with st.container():
            st.markdown("---")
            st.subheader("Resultado da Predição")
            if credit_score == 0:
                st.success("Credit Score: Good", icon="✅")
            elif credit_score == 1:
                st.error("Credit Score: Poor", icon="❌")
            elif credit_score == 2:
                st.warning("Credit Score: Standard", icon="⚠️")
            else:
                st.error("Erro ao fazer a previsão. Tente novamente.", icon="❗️")
            st.markdown("---")
            st.write("Payload enviado para a API:")
            st.json(payload)