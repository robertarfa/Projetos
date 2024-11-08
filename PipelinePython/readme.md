### Pipeline com Python

#### - Definir um ambiente em comum

- Linux(WSL)

#### - Criar as pastas base

- Criar pastas: Documentos > pipeline_dados
  => Local para armazenar os dados antes de serem transformados: data_raw
  => Local para armazenar os dados depois de processados: data_processed
  => Local para armazenar dados que serão explorados: notebooks
  => Local para armazenar os scripts: scripts

#### - Recuperar os dados

- cd data_raw => wget (acessa requisição e faz download dos dados)

#### - Criar um ambiente virtual

- sudo apt-get update
- sudo apt-get upgrade -y
- conda create -n pipelinePython python=3.10.12
- conda activate pipelinePython
- pip install notebook==7.0.3

#### - Utilizar o Jupyter notebook para explorar os dados

#### - Refatorar o código do Jupyter notebook e passar para um script

#### - Criar um arquivo para isolar as classes
