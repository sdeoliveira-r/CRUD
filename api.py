from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Path

# Base de dados
app = FastAPI()

menu = [
	{ 'id': 1,
	  'name': 'coffe',
	  'price': 2.5
	},
	{ 'id': 2,
          'name': 'cake',
          'price': 10
        },
	{ 'id': 3,
          'name': 'tea',
          'price': 3.2
	},
	{ 'id': 4,
          'name': 'croissant',
          'price': 5.79
	}
]

# BaseModel do pydantic (biblioteca para validação de dados e gerenciamento 
# de configurações, utiliza as anotações de tipo do próprio Python. Ela força 
# as anotações de tipos do Python em tempo de execução e provê as respectivas 
# mensagens de erro de sua violação)
class Item(BaseModel):
	name: str
	price: float

class UpdateItem(BaseModel):
	name: Optional[str] = None
	price: Optional[float] = None

# Hello World
@app.get("/")
def hello_word_root():
	return {"Hello": "World"}

# Obter item pelo id, método GET
@app.get('/get-item/{item_id}')
def get_item(
	item_id: int = Path(
		None,
		description = "Fill with ID of the item you want to view")):

	search = list(filter(lambda x: x["id"] == item_id, menu))

	if search == []:
		return {'Error': 'Item does not exist'}

	return {'Item': search[0]}

# Obter item pelo nome, método GET
@app.get('/get-by-name')
def get_item(name: Optional[str] = None):

	search = list(filter(lambda x: x["name"] == name, menu))

	if search == []:
		return {'item': 'Does not exist'}

	return {'Item': search[0]}

# Listar itens, método GET
@app.get('/list-menu')
def listar():
	return {'Menu': menu}

# Criar item, método POST
@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):

	search = list(filter(lambda x: x["id"] == item_id, menu))

	if search != []:
		return {'Error': 'Item exists'}

	item = item.dict()
	item['id'] = item_id

	menu.append(item)
	return item

# Atualizar item, método PUT
@app.put ('/update-item/{item_id}')
def update_item(item_id: int, item: UpdateItem):

	search = list(filter(lambda x: x["id"] == item_id, menu))

	if search == []:
		return {'Item': 'Does not exist'}

	if item.name is not None:
		search[0]['name'] = item.name

	if item.price is not None:
		search[0]['price'] = item.price

	return search

# Deletar item, método DELETE
@app.delete('/delete-item/{item_id}')
def delete_item(item_id: int):

	search = list(filter(lambda x: x["id"] == item_id, menu))

	if search == []:
		return {'Item': 'Does not exist'}

	for i in range(len(menu)):
		if menu[i]['id'] == item_id:
			del menu[i]
			break
	return {'Message': 'Item deleted successfully'}
