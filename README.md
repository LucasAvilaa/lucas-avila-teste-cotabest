# Teste empresa Cotabest

Framework utilizado - Django

- Crud Produtos
    - Barra de pesquisa de produtos

- Crud Carrinhos

- EndPoint que disponibiliza esses dados

- Teste unitários

Validação com regras de negócios
 - Quantidade mínima
 - Quantidade disponível
 - Quantidade selecionada múltipla da quantidade por pacote

Obs: O script python "data_products" utiliza a API de produtos para cadastrar 
os dados enviados de exemplo no email utilizando a biblioteca requests do Python

Passo A Passo para rodar o projeto (Comandos para Linux. Windows e Mac podem mudar um pouco)

Obs: Necessário ter o git instalado

1° Clonar o projeto
    Comando -> git clone https://github.com/LucasAvilaa/lucas-avila-teste-cotabest.git

2° Entrar na pasto do projeto
    Comando -> cd lucas-avila-teste-cotabest

3° Criar Ambiente Virtual (Venv)
    Comando -> python3 -m venv venv

4° Ativar Venv
    Comando -> source venv/bin/activate

5° Instalar Requirements
    Comando -> pip install -r requirements.txt

6° Criar DB
    Comando -> python manage.py makemigrations; python manage.py migrate

7° Iniciar serviço
    Comando -> python manage.py runserver

8° Acessar url: http://localhost:8000

9° (Opcional) Criar produtos utilizando o script "data_products" 
    Comando -> python data_products.py (Apos isso é só recarregar a tela)