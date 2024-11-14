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

### Lake Formation - Centralização dos dados

    5. Conectar ao bucket S3 via Python
      5.1 Configurar o IAM
      5.2 Usuários => Criar usuário
        5.2.1 Credenciais de segurança
        5.2.2 Criar Chave de acesso
          5.2.2.1 Código local

### Security Layer com IAM - utilizar um usuário que não seja root
