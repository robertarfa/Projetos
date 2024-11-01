#dados da saúde financeira das empresas
import fundamentus
import pandas as pd

# Definindo a carteira de ações
carteira = ['BBAS3', 'SANB11', 'AURE3', 'TAEE11', 'ITSA4',
               'PETR4', 'RENT3', 'SUZB3', 'VALE3', 'WEGE3']

df = pd.DataFrame()  # Initialize an empty DataFrame to store the results

for item in carteira:
    temp_df = fundamentus.get_papel(item)  # Get data for the current ticker
    df = pd.concat([df, temp_df])  # Concatenate with existing DataFrame

# print(df)

ind = df[['Setor', 'Cotacao', 'Min_52_sem', 
                                            'Max_52_sem', 'Valor_de_mercado',
                                            'Nro_Acoes', 'Patrim_Liq','Receita_Liquida_12m',
                                            'Receita_Liquida_3m',
                                            'Lucro_Liquido_12m', 'Lucro_Liquido_3m']]
# ind.head(4)

# ind.info()

#transformar o índice em coluna
ind = ind.reset_index()
ind = ind.rename(columns={"index":"Ativo"})

# Alterando colunas object para numeric
colunas = ['Cotacao', 'Min_52_sem', 'Max_52_sem', 'Valor_de_mercado', 'Nro_Acoes', 'Patrim_Liq',
           'Receita_Liquida_12m', 'Receita_Liquida_3m', 'Lucro_Liquido_12m', 'Lucro_Liquido_3m']

ind[colunas] = ind[colunas].apply(pd.to_numeric, errors='coerce', axis=1)
ind.head()
ind.info()

ind_2 = fundamentus.get_resultado_raw().reset_index()

ind_2 = ind_2.query('papel in @carteira')

#vai zerar o index
ind_2 = ind_2[['papel','P/L', 'Div.Yield','P/VP','ROE']].reset_index(drop=True)

#inplace é similar a colocar ind=ind
ind_2.rename(columns={'papel': 'Ativo','Div.Yield':'DY'}, inplace= True)
ind_2.head()

#concatenar os df
indicadores = ind.merge(ind_2, on="Ativo")

indicadores['LPA'] = (indicadores['Lucro_Liquido_12m'] / indicadores['Nro_Acoes']).round(2)
indicadores['VPA'] = (indicadores['Patrim_Liq'] / indicadores['Nro_Acoes']).round(2)

indicadores.to_csv("indicadores.csv", index=False, decimal='.')

del carteira, df