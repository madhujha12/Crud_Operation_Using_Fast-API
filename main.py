# uvicorn main:blog --reload
from fastapi import FastAPI,status,HTTPException
from sqlalchemy import create_engine, Column, Integer, String,text
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector
from mysql.connector import errorcode

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.responses import JSONResponse


blog = FastAPI()

##HOW TO GET OUR DATA:
# engine = mysql.connector.connect(host="localhost",
#   user="test",password="1211",database="students")
# @blog.get(f"/data")
# async def get_students():
#     try:
#         mycursor = engine.cursor(dictionary=True)
#         print(mycursor)
#         sql="select * from customer2"
#         mycursor.execute(sql)
#         result=mycursor.fetchall()
#         print(result)
#         return result
#     except Exception as e:
#         print(e)



# #HOW TO GET DATA BY ID:
# db = mysql.connector.connect(host="localhost",
#   user="test",password="1211",database="students")

# @blog.get("/items/{item_id}")
# async def read_id(item_id: int):
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM customer2 WHERE id = %s", (item_id,))
#     result = cursor.fetchone()
#     return result



# @blog.get("/")
# def root():
#     return {"message": "Hello World"}



# @blog.get("/")
# def root():
#     return "todooo"

# @blog.post("/todo",status_code=status.HTTP_201_CREATED)
# def create_todo():
#     return "create todo item"

# @blog.get("/todo/{id}")
# def read_todo(id: int):
#     return "read todo item with id {id}"

# @blog.put("/todo/{id}")
# def update_todo(id: int):
#     return "update todo item with id {id}"

# @blog.delete("/todo/{id}")
# def delete_todo(id: int):
#     return "delete todo item with id {id}"

# @blog.get("/todo")
# def read_todo_list():
#     return "read todo list"


# class Blog(BaseModel):
#     name:str
#     address:str
# @blog.post('/blog')
# def  create (request:Blog):
#     return request



# CRUD_OPERATION_USING_Fast API:

#CREATE DATA USING POST:
cnx = mysql.connector.connect(user='test',password='1211',host='localhost',database='students')

class User(BaseModel):
    name: str
    address: str


@blog.post("/users")
async def create_user(user: User):
    cursor = cnx.cursor()
    query = "INSERT INTO customer2 (name, address) VALUES (%s, %s)"
    values = (user.name, user.address)
    cursor.execute(query, values)
    cnx.commit()
    return {"message": "User created successfully"}



# HOW TO CREATE OF DATA BY USING ID:
db=mysql.connector.connect(user='test',password='1211',host='localhost',database='students')
class item_id(BaseModel):
    name: str
    address:str


@blog.post("/items/{item_id}")
async def create_item(item_id: int):
    cursor = db.cursor()
    cursor.execute("INSERT INTO customer2 (id, name, address) VALUES (%s, %s, %s)", (item_id.name, item_id.address))
    db.commit()
    # return {"id": item_id, **item.dict()}
    return ("user created successfuly")




#READ A DATA USING GET METHOD:
mydb=mysql.connector.connect(user='test',password='1211',host='localhost',database='students')
@blog.get("/read_data/{id}")
async def read_data(id: int):
    cursor = mydb.cursor(dictionary=True)
    sql = "SELECT * FROM customer2 WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    return {"data": result}


#UPDATE DATA USING PUT METHOD:

mydb=mysql.connector.connect(user='test',password='1211',host='localhost',database='students')

@blog.put("/update_data/{id}")
async def update_data(id: int, name: str):
    cursor = mydb.cursor()
    sql = "UPDATE customer2 SET name = %s WHERE id = %s"
    val = (name, id)
    cursor.execute(sql, val)
    mydb.commit()
    return {"message": "Data updated successfully"}



#DELETE DATA USING DELETE METHOD:

mydb=mysql.connector.connect(user='test',password='1211',host='localhost',database='students')

@blog.delete("/delete_data/{id}")
async def delete_data(id: int):
    cursor = mydb.cursor()
    sql = "DELETE FROM customer2 WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    mydb.commit()
    return {"message": "Data deleted successfully"}

