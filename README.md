# MOD PLANT

Este software mide los parámetros en los cultivos del arroz, se conecta por medio de un módulo el cual está ensamblado con sensores a travez de arduino. El módulo guarda los parámetros leidos en una base de datos por medio de un script.

La interfaz lee los datos desde la base de datos y los muestra en graficos. Cuando se requiere leer los datos en tiempo real se llama una funcion que recoge la información directamente desde el módulo y los muestra en pantalla.


<image align="right" src="screenshots/principal%20menu.png" alt="Principal menu"></image>

## Funciones
* Estadisticas
* Comparación de valores
* Datos en tiempo real

## Sensores del módulo
* Sensor de Ph
* Sensor de Temperaura
* Sensor Ultrasónico (Nivel del agua)
* Sensor de lluvia
* Sensor de Humedad (Salinidad)


# Estadisticas
Presenta graficos de los parámetros obtenidos de la base dedatos mosrando los niveles por día, semana o mes.

<image src="screenshots/grafics%20op1.png" alt="Estadisticas"></image>

# Comparación de valores
Lee los datos en tiempo real y muestra una tabla donde se comparan losparámetros actuales con los recomendados.

<image src="screenshots/values%20op2.png" alt="Comparación de valores"></image>

# Datos en tiempo real
Una simple lectura directa desde el módulo que grafica los parámetros obtenidos.

<image src="screenshots/trdata%20op3.png" alt="Datos en tiempo real"></image>

# Modo de ejemplo

Cuando el software no puede encontrar la base de datos ni la conexión con el Módulo, este entra en una fase de demostración la cual permitirá explorar las opciones mostrando datos deejemplo.

<image src="screenshots/connection%20error.png" alt="Datos en tiempo real"></image>

# Desarrolladores

<img align="left" src="https://img.icons8.com/bubbles/50/000000/github.png"/>
<a href="https://github.com/Tomvargas">Tomas Vargas</a>

<a href="https://github.com/Arturo0911">Arturo negreiros</a>

# 
github icon is used from <a href="https://icons8.com/icon/118553/github">Icons8</a>
