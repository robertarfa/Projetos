import yfinance as yf

# Definindo a carteira de ações
carteira_yf = ['BBAS3.SA', 'SANB11.SA', 'AURE3.SA', 'TAEE11.SA', 'ITSA4.SA',
               'PETR4.SA', 'RENT3.SA', 'SUZB3.SA', 'VALE3.SA', 'WEGE3.SA']

# Carregando os dados da carteira
df = yf.download(carteira_yf, start="2022-08-01", end="2023-08-01")

# Passando os ativos para o multindex do df
cotacoes = df.stack(level=1)

# Resetando os índices e renomenado a coluna dos ativos
cotacoes = cotacoes.reset_index().rename(columns={'level_1': 'Ativo'})

# Organizando o df
cotacoes = cotacoes[["Ativo", "Date", "Open", "High", "Low", "Close"]]


del carteira_yf, df