# CRUD
API em python com o FastAPI, desenvolvimento CRUD com os métodos GET, PUT, POST e DELETE.

Certifique de ter instalado em sua máquina python 3.6 ou superior e também as bibliotecas 
FastApi e Uvicon. Para instalar as bibliotecas, executar no terminal o seguinte comando;

	pip install fastapi uvicorn

Passo 1: Criar uma pasta com o nome "CRUD-FastAPI-Python", abrir o terminal dentro desta pasta, 
criar um arquivo vazio com o nome "api.py" e inserir o código neste arquivo;

Passo 2: No terminal, executar o seguinte código para inicializar o ambiente virtual;

	python3 -m venv .venv 
	source .venv/bin/activate

Passo 3: No terminal, executar o seguinte código para iniciar o servidor Web ASGI (Asynchronous 
Server Gateway Interface) e rodar no navegador a FastAPI;

	uvicorn api:app --reload

Passo 4: Faça algumas requisições direto do navegador acessando o endereço <http://127.0.0.1:8000> p
or exemplo;

	http://127.0.0.1:8000/get-item/1
	http://127.0.0.1:8000/get-by-name?name=coffe

Passo 5: Acessar a interface grafica com a seguinte extensão "/docs" e também fazer requisições;

	http://127.0.0.1:8000/docs

Passo 6: Fazer requisições na interface grafica, click em (Try it out - Experimente) para 
consultar itens pelo id e pelo name, listar itens, criar itens, atualizar itens e deletar itens,
 

Passo 7: Para parar de executar a API pressione CTRL+C no terminal.
		
