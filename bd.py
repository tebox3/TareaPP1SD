import pymysql

# Establecer la conexión al servidor de MySQL
conn = pymysql.connect(host='localhost', user='root', password='root')
try:
    # Crear la base de datos api_test si no existe
    with conn.cursor() as cursor:
        cursor.execute("DROP DATABASE IF EXISTS DocumentoSD")
        cursor.execute("CREATE DATABASE IF NOT EXISTS DocumentoSD")
        print("Base de datos DocumentoSD creada exitosamente.")

    # Cambiar a la base de datos api_test
    conn.select_db('DocumentoSD')

    # Crear la tabla user si no existe
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Video (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Titulo VARCHAR(150)
            )
        """)
        print("Tabla Video creada exitosamente.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tesis (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Titulo VARCHAR(150)
            )
        """)
        print("Tabla Tesis creada exitosamente.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Paper (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Titulo VARCHAR(150)
            )
        """)
        print("Tabla Paper creada exitosamente.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Presentacion (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Titulo VARCHAR(150)
            )
        """)
        print("Tabla Presentacion creada exitosamente.")

    # Insertar datos ficticios en la tabla user
    with conn.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO Paper (Titulo) VALUES (%s)
        """, [
            ("Análisis de Algoritmos: Métodos y Técnicas"),
            ("Criptografía Moderna: Avances y Desafíos"),
            ("Redes Bayesianas: Modelos y Aplicaciones"),
            ("Procesamiento de Imágenes: Métodos y Herramientas")
                ])
        conn.commit()
        print("Datos insertados en la tabla Paper.")
    with conn.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO Presentacion (Titulo) VALUES (%s)
        """, [
            ("Ecuaciones diferenciales"),
            ("Algoritmos Genéticos: Teoría y Aplicaciones"),
            ("Fisica mecanica"),
            ("Fisica de ondas")
            ])
        conn.commit()
        print("Datos insertados en la tabla Presentacion.")
    with conn.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO Tesis (Titulo) VALUES (%s)
        """, [
            ("Criptografía Moderna: Avances y Desafíos"),
            ("Programación Dinámica en la Optimización de Rutas"),
            ("Inteligencia Artificial: Modelos y Métodos"),
            ("Algoritmos de Búsqueda Local: Teoría y Práctica"),
            ("Sistemas de Recomendación: Algoritmos y Implementación"),
            ("Lógica Computacional: Fundamentos y Aplicaciones")
                ])
        conn.commit()
        print("Datos insertados en la tabla Tesis.")
    with conn.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO Video (Titulo) VALUES (%s)
        """, [
            ("Introducción a la Teoría de Grafos"),
            ("Bases de Datos NoSQL: Principios y Prácticas"),
            ("Desarrollo de Aplicaciones Móviles: Estrategias y Herramientas"),
            ("Introducción a la Programación Orientada a Objetos"),
            ("Cálculo en varias variables")
                ])
        conn.commit()
        print("Datos insertados en la tabla Videos.")
except pymysql.MySQLError as e:
    print(f"Error al ejecutar el script: {e}")
finally:
    # Cerrar la conexión
    conn.close()
