from fastapi import FastAPI #import uvicorn

nombre_pro_clientes = FastAPI() #nombre_pro_clientes = FastAPI(title="Proyecto de clientes", description="Este es un proyecto de clientes a desarrollar", version="1.0.0")
#PRIMER ENDPOINT MENSAJE
@nombre_pro_clientes.get("/") #@nombre_pro_clientes.get("/mensaje") #ruta para mostrar el mensaje
def mensaje():
    return{"mensaje": "Este es el proyecto de clientes a desarrollar"}#retorna el mensaje en formato JSON
#SEGUNDO ENDPOINT LISTA CLIENTES
@nombre_pro_clientes.get("/clientes")#ruta para mostrar la lista de clientes
def clientes():
    clientes = ["Jorge Alejandro Torres Paez","Sara Jasmin Cruz Calderon","Santiago Buitrago Goyeneche","Jonny Guerrero","Eddy Santiago Caro"] 
    return[clientes]   #return{"clientes": clientes} #retorna la lista de clientes en formato JSON
