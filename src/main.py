#main.py
from fastapi import FastAPI, Body
from src import schemas

app = FastAPI()

data ={
    1:{'name':'Rahul'},
    2:{'lastname':'Gurjar'},
    3:{'age':'25'},
}
 
#Get all data 
@app.get("/")
def getItems():
    return ['Item 12', 'Item 2', 'Item 3']


#Get data by id   
@app.get("/{id}")
def getItemById(id:int):
    return data[id]

#Create data with static value
# @app.post("/")
# def addItem(task:str):
#     newId = len(data.keys()) + 1
#     data[newId] = {"phone_number":1111111111}
#     return data



#Create data with request value
@app.post("/")
def addItem(item:schemas.Item):
    newId = len(data.keys()) + 1
    data[newId] = {"task":item.task}
    return data


#Update data 
@app.put("/{id}")
def updateItem(id:int, item:schemas.Item):
    data[id]['task'] = item.task 
    return data


@app.delete("/{id}")
def deleteItem(id:int):
    del data[id]
    return datas