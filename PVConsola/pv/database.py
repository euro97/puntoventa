import psycopg2
from jproperties import Properties

configs = Properties()


with open('app.properties', 'rb') as config_file:
    configs.load(config_file)


def connect():
    try:
        connection = psycopg2.connect(
            user=configs["DB_USER"].data,
            password=configs["DB_PWD"].data,
            host=configs["DB_HOST"].data,
            port=configs["DB_PORT"].data,
            database=configs["DB"].data
        )

        return connection

    except Exception as error:
        errores = "Error al conectar a la base de datos: ",error
        print("Error al conectar a la base de datos: ",error)

        return errores

def close(connection):

    if connection:
        connection.close()
        
        return "Conexión cerrada"

