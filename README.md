# Quantum Finance - Credit Score Predictor
Este projeto é uma aplicação web construída com Streamlit que utiliza um modelo de Machine Learning para prever o credit score de clientes com base em suas informações pessoais e financeiras. A aplicação se conecta a um endpoint de API para obter as previsões em tempo real, fornecendo uma interface amigável e intuitiva para a entrada de dados.

Funcionalidades
Predição de Credit Score: Recebe 14 variáveis de entrada e retorna uma das três classificações de score de crédito: "Good", "Standard" ou "Poor".

Interface Intuitiva: Layout otimizado com 5 colunas para uma melhor visualização dos campos de entrada.

Integração com API: Envia dados em formato JSON para um endpoint de API e processa a resposta.

Feedback Visual: Exibe o resultado da predição com ícones e cores diferentes para facilitar a interpretação.

Modo Escuro: A aplicação pode ser configurada para iniciar automaticamente no modo escuro através de um arquivo de configuração TOML.

Como Executar Localmente
Pré-requisitos
Certifique-se de ter o Python 3.7 ou superior instalado.

# 1. Clonar o Repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# 2. Instalar as Dependências
Crie um ambiente virtual (opcional, mas recomendado) e instale as bibliotecas necessárias:

## Crie e ative um ambiente virtual
python -m venv venv
### No Windows
venv\Scripts\activate
### No macOS/Linux
source venv/bin/activate

## Instale as dependências
pip install -r requirements.txt

# 3. Configurar Segredos da API
A aplicação requer credenciais de API. Crie um diretório .streamlit na raiz do projeto e, dentro dele, crie um arquivo chamado secrets.toml.

## .streamlit/secrets.toml
API-ENDPOINT = "SUA-URL-DA-API-AQUI"
API-KEY = "SUA-CHAVE-DA-API-AQUI"

Substitua "SUA-URL-DA-API-AQUI" e "SUA-CHAVE-DA-API-AQUI" pelas suas credenciais reais.

# 4. Rodar a Aplicação
Execute o seguinte comando no terminal para iniciar a aplicação:

streamlit run seu_arquivo_principal.py

(Substitua seu_arquivo_principal.py pelo nome do seu arquivo Python, se for diferente).

A aplicação será aberta automaticamente no seu navegador.

Modo Escuro por Padrão
Para configurar o tema escuro como padrão, crie o arquivo config.toml dentro do diretório .streamlit e adicione o seguinte conteúdo:

## .streamlit/config.toml
[theme]
base="dark"

Estrutura do Código
O código é dividido em seções claras para melhor organização:

Funções de Lógica: A função get_prediction() lida com a requisição à API e o tratamento de erros.

Configuração da Página: Define o título, ícone e layout da página.

Layout da Aplicação: Utiliza st.title, st.markdown, st.subheader, st.columns, e st.container para estruturar a interface do usuário.

Lógica de Predição e Resultado: Trata o evento do botão de previsão e exibe o resultado.

Tecnologias Utilizadas
Python: Linguagem de programação principal.

Streamlit: Framework para a criação da aplicação web.

requests: Biblioteca para fazer requisições HTTP.
