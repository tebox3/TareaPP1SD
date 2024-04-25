from flask import Flask, request, jsonify
import pymysql
app = Flask(__name__)

def buscar_nombre(parte_nombre):
    conn = pymysql.connect(host='localhost', user='root', password='root', db='documentosd')
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT Titulo FROM Tesis WHERE Titulo LIKE %s", ('%{}%'.format(parte_nombre),))
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
    tipo = request.args.get('tipo')
    print("El titulo del esclavo1: ",tipo)
    if tipo:
        conn = pymysql.connect(host='localhost', user='root', password='root', db='documentosd')
        try:
            with conn.cursor() as cursor:
                print("BBB")
                cursor.execute("SELECT * FROM Tesis")
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
        app.run(host="localhost", port="5001", debug=True)