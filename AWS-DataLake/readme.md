# AWS Data Lake

## Definir orçamento na AWS

### Definir Dados a serem consumidos

### Criar S3

    1. Criar um bucket S3 - serviço de armazenamento
      1.1 Leste dos EUA (Norte da Virgínia) us-east-1
      1.2 ACLs desabilitadas (recomendado)
      1.3 Marcar Bloquear todo o acesso público
      1.4 Versionamento de bucket - Desativado
      1.5 Tags => para agrupar as informações
      1.6 Criptografia do lado do servidor com chaves gerenciadas do Amazon S3 (SSE-S3)
      1.7 Chave do bucket - para diminuir os custo de criptografia

### Construir camada Bronze - S3 - dados brutos

    2. Entrar no bucket criado
      2.1 Criar Pasta bronze
      2.2 Não especificar chave de criptografia

### Construir camada Silver - S3 - dados processados

    3. Entrar no bucket criado
      3.1 Criar Pasta silver
      3.2 Não especificar chave de criptografia

### Extrair os dados da base desejada

    4. Seguir Pipeline_AWS.py
      4.1 pip install boto3

### Conectar com o bucket S3 via Python

    5. Conectar ao bucket S3 via Python
      5.1 Configurar o IAM
      5.2 Usuários => Criar usuário
        5.2.1 Credenciais de segurança
        5.2.2 Criar Chave de acesso
          5.2.2.1 Código local

### Security Layer com IAM - utilizar um usuário que não seja root

### Melhorar a performance com Parquet

### Lake Formation - Centralização dos dados

      6. Configurar os usuários que poderão acessar e criar banco de dados
        6.1 Procurar por Lake Formation
        6.2 Data lake administrators
        6.3 Adicionar usuário IAM users and roles
        6.4 Data lake administrators selecionar o seu usuário
        6.5 Database creators Selecionar a opção com Create Database
        6.6 Clicar em Grant

        6.7 No menu selecionar Data lake locations
        6.8 Register location
        6.9 Colocar onde estão os dados
        6.10 Register location

### Ajustar permissões do Lake Formation para o Data Location

        7. No menu selecionar Data Locations
        7.1 Grant
        7.2 Escolher usuário
        7.3 Storage locations
        7.4 Grant

### Criar um banco de dados dentro do Lake Formation

        8. No Lake Formation
        8.1 No menu selecionar Databases
        8.2 Create Database
