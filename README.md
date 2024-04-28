Para hacer funcionar el script es necesario crear la base de datos, esta se llama documentosd, se crea y agregan datos ejecutando el archivo bd.py usando python bd.py (python3 en linux)

Si ya se tiene creada seguir con los pasos siguientes

Despues de la creacion de la BD se debe ejecutar el script del maestro y esclavo en consolas diferentes, seran 5 consolas: 1 para el nodo maestro y 4 para los esclavos.

Los scripts se ejecutan con su respectivo archivo de configuracion, en este caso se encuentran en config/ por lo que solo debe agregar la ruta al ejecutar el programa, ejemplo: python esclavo1.py config/config1.json, dado que son 4 archivos de configuracion debe ejecutar el script con cada uno de ellos:

python esclavo1.py config/config1.json
python esclavo1.py config/config2.json
python esclavo1.py config/config3.json
python esclavo1.py config/config4.json

si la ruta es diferente en su equipo ejecutarlo con la ruta correspondiente.

El puerto usado sera el localhost:5000 por lo que para hacer peticiones se debera hacer en esta direccion.

Los datos de prueba ingresados son los siguientes:

De tipo Video:
("Introducción a la Teoría de Grafos"),
("Bases de Datos NoSQL: Principios y Prácticas"),
("Desarrollo de Aplicaciones Móviles: Estrategias y Herramientas"),
("Introducción a la Programación Orientada a Objetos"),
("Cálculo en varias variables")

De tipo presentacion:
("Ecuaciones diferenciales"),
("Algoritmos Genéticos: Teoría y Aplicaciones"),
("Fisica mecanica"),
("Fisica de ondas")

De tipo tesis:
("Criptografía Moderna: Avances y Desafíos"),
("Programación Dinámica en la Optimización de Rutas"),
("Inteligencia Artificial: Modelos y Métodos"),
("Algoritmos de Búsqueda Local: Teoría y Práctica"),
("Sistemas de Recomendación: Algoritmos y Implementación"),
("Lógica Computacional: Fundamentos y Aplicaciones")

De tipo paper:
("Análisis de Algoritmos: Métodos y Técnicas"),
("Criptografía Moderna: Avances y Desafíos"),
("Redes Bayesianas: Modelos y Aplicaciones"),
("Procesamiento de Imágenes: Métodos y Herramientas")
