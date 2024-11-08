import json
import csv

class Data:
  
  def __init__(self, path, data_type, encoding='UTF-8'):
    self.path = path
    self.data_type = data_type
    self.encoding = encoding
    self.dados = self.read_data()
    self.columns_name = self.get_columns()
    self.rows_number = self.__data_size() 
   
  ## Fazer as leituras
  def __read_json(self):
    with open(self.path, 'r', encoding=self.encoding) as file:
        dados_json = json.load(file)
        return dados_json
    
    #Substituindo o reader() por DictReader para transformar em dicionário
  def __read_csv(self):
    dados_csv = []
    with open(self.path, 'r', encoding=self.encoding) as file:
      spamreader =csv.DictReader(file,delimiter=',')
      for row in spamreader:
        dados_csv.append(row)
    return dados_csv

  def read_data(self):
    dados = []
    if(self.data_type == 'csv'):
      dados = self.__read_csv()
    
    elif (self.data_type == 'json'):
      dados = self.__read_json()
    
    elif(self.data_type == 'list'):
      dados = self.path
      self.path = 'memory_list'

    return dados  

  def get_columns(self):
    return list(self.dados[-1].keys())

  def rename_columns(self, key_mapping):
    new_dados = [
        {key_mapping[old_key]: value for old_key, value in old_dict.items()}
        for old_dict in self.dados
    ]
    self.dados = new_dados
    self.columns_name = self.get_columns()

  def __data_size(self):
    return len(self.dados)

#método estático não precisa receber o self
  def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA.dados)
    combined_list.extend(dadosB.dados)
    return Data(combined_list, 'list')

  def __data_table(self):
    dados_combinados_tabela = [self.columns_name] + [
        [row.get(coluna, 'Indisponível') for coluna in self.columns_name]
        for row in self.dados
    ]

    return dados_combinados_tabela

  def save_data(self, path):
    data_table = self.__data_table()
    with open(path,'w', encoding=self.encoding) as file:
      writer = csv.writer(file)
      writer.writerows(data_table)