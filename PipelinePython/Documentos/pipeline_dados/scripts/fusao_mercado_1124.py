from processamento_dados import Data

path_json = '../data_raw/dados_empresaA.json'
path_csv = "../data_raw/dados_empresaB.csv"

# #Iniciando leitura
data_companyA = Data(path_json, 'json')
print("Company A path: ", data_companyA.path)
print("Company A first line: ",data_companyA.dados[0])

data_companyB = Data(path_csv, 'csv')
print("Company B path: ", data_companyB.path)
print("Company A first line: ",data_companyB.dados[0])

print("Company A columns name: ",data_companyA.get_columns())
print("Company A rows number: ",data_companyA.rows_number)
print("Company B columns name: ",data_companyB.get_columns())
print("Company B rows number: ",data_companyB.rows_number)

# #tranformação dos dados
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

data_companyB.rename_columns(key_mapping)
print("Company B new columns name: ", data_companyB.columns_name)

fusion_data = Data.join(data_companyA, data_companyB)
print("Dados compilados:", fusion_data)
print("Fusao columns name: ",fusion_data.get_columns())
print("Fusao rows number: ",fusion_data.rows_number)

# # ##Salvando os dados
path_dados_final = '../data_processed/dados_final_prod_class.csv'
dados_fusao_tabela = fusion_data.save_data(path_dados_final)
