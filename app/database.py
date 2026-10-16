import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

def connector():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_NAME")
            )
        print(f"Conexão realizada com sucesso!  ")
        return connection

    except Error as erro:
        print(f"Problema ao criar conexão com o servidor!\nERRO > {erro}")
        exit()