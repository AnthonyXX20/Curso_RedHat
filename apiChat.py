from fastapi import FastAPI
import mysql.connector
from mensaje import mensaje

obj_Mensaje = mensaje("bienvenido")
app = FastAPI()
mi_Conexion = mysql.connector.connect(
    host = "172.60.10.212",
    user = "usr_chat",
    passwd = "Aa123456",
    db = "chat")

@app.get("/enviar_Mensaje")
def enviar_Mensaje(mensaje: str):
    cursor = mi_Conexion.cursor()
    mensaje_Encriptado = obj_Mensaje.codificar(mensaje)
    cursor.execute("insert into mensajes (Mensaje, Usuario) values('"+mensaje_Encriptado+"','Jeffrey')")
    mi_Conexion.commit()
    return "Jeffrey: " + mensaje 
@app.get("/listar_Mensajes")
def listar_Mensajes():
    cursor = mi_Conexion.cursor()
    cursor.execute("select * from mensajes")
    result = cursor.fetchall()
    return result
@app.get("/listar_Mensajes_De_Un_Usuario")
def listar_Mensajes_De_Un_Usuario(user1: str, user2: str):
    cursor = mi_Conexion.cursor()
    cursor.execute("select * from mensajes where Usuario in ('"+user1+"','"+user2+"')")
    result = cursor.fetchall()
    return result