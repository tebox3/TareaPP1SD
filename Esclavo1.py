from flask import Flask, request, jsonify
import pymysql
import json
import argparse
app = Flask(__name__)
configuracion = {}
conn = ''
def cargar_configuracion():
    parser = argparse.ArgumentParser(description='Script para esclavo.')
    parser.add_argument('ruta_archivo', type=str, help='Ruta del archivo de configuración')
    args = parser.parse_args()
    ruta_configuracion = args.ruta_archivo
    print("LA RUTA: ",ruta_configuracion)
    with open(ruta_configuracion, 'r') as archivo:
        configuracion = json.load(archivo)
    return configuracion

def buscar_nombre(parte_nombre):
    try:
        with conn.cursor() as cursor:
            print("AQUI VIENEEEEEE")
            print(configuracion["tipo"])
            print(("SELECT Titulo FROM %s WHERE Titulo LIKE %s", (configuracion["tipo"],'%{}%'.format(parte_nombre),)))
            cursor.execute("SELECT Titulo FROM {} WHERE Titulo LIKE %s".format(configuracion["tipo"]), ('%{}%'.format(parte_nombre),))
            resultados = cursor.fetchall()
            return resultados
    except Exception as e:
        print("Error al buscar dato en esclavo1", e)
        return None
    finally:
        conn.close()
    
@app.route('/buscar_titulo', methods=['GET'])
def buscar_titulo():
    titulo = request.args.get('titulo')
    print("El titulo del esclavo1: ",titulo)
    if titulo:
        resultados = buscar_nombre(titulo)
        print("Los resultados del e1 son: ",resultados)
        if resultados:
            return jsonify(resultados)
        else:
            print("No se encontraron resultados")
            return jsonify({'error': 'No se encontraron resultados'})
    else:
        return jsonify({'error': 'Se requiere el parámetro "titulo" en la solicitud'})

@app.route('/buscar_tipo', methods=['GET'])
def buscar_tipo():
    configuracion=cargar_configuracion()
    tipo = request.args.get('tipo')
    print("El titulo del esclavo1: ",tipo)
    if tipo:
        conn = pymysql.connect(host='localhost', user='root', password='root', db='documentosd')
        try:
            with conn.cursor() as cursor:
                print("BBB")
                cursor.execute("SELECT * FROM %s",configuracion["tipo"])
                resultados = cursor.fetchall()
                print("BBB")
                print(resultados)
                return jsonify(resultados)
        except Exception as e:
            print("Error al buscar dato en esclavo1", e)
            return jsonify('Error')
        finally:
            conn.close()

if __name__ == '__main__':
    with app.app_context():
        configuracion = cargar_configuracion()
        conn = pymysql.connect(host=configuracion["dbConnConfig"]["host"], user=configuracion["dbConnConfig"]["user"], password=configuracion["dbConnConfig"]["pass"], db=configuracion["dbConnConfig"]["dbname"])
        #print("Configuración cargada desde:", ruta_configuracion)
        print("Variables de configuración:")
        print(configuracion)
        print("puerto", configuracion["host"])
        app.run(host="localhost", port=configuracion["port"], debug=True)