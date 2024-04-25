from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

urls_esclavos = [
    "http://localhost:5001/buscar_titulo",
    "http://localhost:5002/buscar_titulo",
    "http://localhost:5003/buscar_titulo",
    "http://localhost:5004/buscar_titulo"
    ]

urls_esclavos_tipo = [
    "http://localhost:5001/buscar_tipo",
    "http://localhost:5002/buscar_tipo",
    "http://localhost:5003/buscar_tipo",
    "http://localhost:5004/buscar_tipo"
    ]

@app.route('/query', methods=['GET'])
def query():
    titulo = request.args.get('titulo')
    tipo = request.args.get('tipo_doc')
    valor = list(request.args.keys())
    valor = valor[0]
    respuestas = []
    print("El valor del parametro es: ",valor)
    print("El titulo del main: ",titulo)
    if(valor=='titulo'):
        parametros = {'titulo': titulo}
        print("AAA")
        try:
            for url_esclavo in urls_esclavos:
                respuesta = requests.get(url_esclavo, params=parametros, timeout=5)
                print("AAA")
                if respuesta.status_code == 200:
                    if respuesta.json()!={'error': 'No se encontraron resultados'}:
                        print(respuesta.json())
                        respuestas.append(respuesta.json())
                else:
                    print("Error en la solicitud:", respuesta.status_code)
            if respuestas == []:
                return jsonify("No se encontraron resultados")
            return respuestas
        except requests.Timeout:
            print("Tiempo de espera agotado")
        except Exception as e:
            print("Error en la solicitud:", e)
            return None
    elif(valor=='tipo_doc'):
        print("El tipo del main: ",tipo)
        parametros = {'tipo': tipo}
        print("BBB")
        try:
            if tipo and 'tesis' in tipo:
                print("BBB")
                respuesta = requests.get(urls_esclavos_tipo[0], params=parametros, timeout=5)
                if respuesta.status_code == 200:
                    print("BBB")
                    print(respuesta.json())
                    respuestas.append(respuesta.json())
                    print("BBB")
            if tipo and 'presentacion' in tipo:
                print("BBB")
                respuesta = requests.get(urls_esclavos_tipo[1], params=parametros, timeout=5)
                if respuesta.status_code == 200:
                    print("BBB")
                    print(respuesta.json())
                    respuestas.append(respuesta.json())
                    print("BBB")
            if tipo and 'video' in tipo:
                print("BBB")
                respuesta = requests.get(urls_esclavos_tipo[2], params=parametros, timeout=5)
                if respuesta.status_code == 200:
                    print("BBB")
                    print(respuesta.json())
                    respuestas.append(respuesta.json())
                    print("BBB")
            if tipo and 'paper' in tipo:
                print("BBB")
                respuesta = requests.get(urls_esclavos_tipo[3], params=parametros, timeout=5)
                if respuesta.status_code == 200:
                    print("BBB")
                    print(respuesta.json())
                    respuestas.append(respuesta.json())
                    print("BBB")
            if respuestas == []:
                return jsonify("No se encontraron resultados")
            return respuestas
        except requests.Timeout:
            print("Tiempo de espera agotado")
        except Exception as e:
            print("Error en la solicitud:", e)
            return None
    else:
        print("Tipo de query incorrecto")
        return jsonify('Tipo de query incorrecto, debe ser tipo_doc o titulo')

""" 
@app.route('/query', methods=['GET'])
def query_tipo():
    print("BBB")
    tipo = request.args.get('tipo_doc')
    respuestas = []
    print("El tipo del main: ",tipo)
    parametros = {'tipo': tipo}
    print("BBB")
    try:
        if(tipo == 'tesis'):
            respuesta = requests.get(urls_esclavos_tipo[0], params=parametros, timeout=5)
            if respuesta.status_code == 200:
                print(respuesta.json())
                respuestas.append(respuesta.json())
        else:
            print("Error en la solicitud:", respuesta.status_code)
            return jsonify("Error en la solicitud, intente nuevamente")
        if respuestas == []:
            return jsonify("No se encontraron resultados")
        return respuestas

        respuesta = requests.get(url_esclavo, params=parametros, timeout=5)
        print("AAA")
        if respuesta.status_code == 200:
            if respuesta.json()!={'error': 'No se encontraron resultados'}:
                print(respuesta.json())
                respuestas.append(respuesta.json())
        else:
            print("Error en la solicitud:", respuesta.status_code)
        if respuestas == []:
            return jsonify("No se encontraron resultados")
        return respuestas
    except requests.Timeout:
        print("Tiempo de espera agotado")
    except Exception as e:
        print("Error en la solicitud:", e)
        return None """

if __name__ == '__main__':
    with app.app_context():
        app.run(host="localhost", port="5000", debug=True)