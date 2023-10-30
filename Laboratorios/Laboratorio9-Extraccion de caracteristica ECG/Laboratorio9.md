# Laboratorio 9 - Extracción de características ECG

## Tabla de contenido
- [Introducción](#Introducción)
- [Materiales](#Materiales)
- [Metodología](#Metodología)
- [Resultados y discusión](#Resultadosydiscusión)
- [Conclusiones](#Conclusiones) 
- [Bibliografía](#Bibliografía)

# Introducción

La extracción de características es ampliamente desarrollada en el procesamiento de señales, y se basa en la identificación de características notables en una señal, como la frecuencia, forma de onda y amplitud. Posteriormente, estas características pueden ser utilizadas para el reconocimiento de patrones en la señal, lo que puede servir para clasificar o predecir su comportamiento futuro. Las aplicaciones de extracción de características de señales ECG están relacionadas con la evaluación de la actividad eléctrica del corazón y el diagnóstico de condiciones cardíacas.
En este laboratorio, se extraerán las principales características de la señal ECG previamente adquiridas y filtradas en estudios anteriores. Estas características pueden incluir el intervalo QRS, el segmento ST, el ritmo cardíaco, los picos R, asimismo, como la media de los intervalos mencionados, los cuales son esenciales para la evaluación y diagnóstico de afecciones cardíacas.

# Materiales

- Una computadora con python
- Señal de ECG
- Librerias instaladas: Neurokit 2 y Biosignals

# Metodología
La metodología para la extracción de las características más importantes del ECG se llevó a cabo en varios pasos. En primer lugar, se adquirió la data utilizando el módulo de bitalino para capturar la señal de ECG. Posteriormente, se procedió a procesar esta data utilizando el lenguaje de programación Python. Para la filtración de la señal, se aplicaron dos métodos en paralelo, de forma no secuencial. El primer método consistió en la transformación de wavelet con un umbral de 100, mientras que el segundo método empleó el filtro FIR disponible en la biblioteca Neurokit.
![Alt text](<Imágenes/Extraccion de caracteristicas/1 wavelet.png>)

Una vez que la señal fue filtrada, se procedió a la extracción de características utilizando las bibliotecas Neurokit y Biosignals. En el código utilizado para llevar a cabo este proceso, se pueden observar los comandos específicos que se emplearon para realizar la extracción de las características clave del ECG. Estos pasos permitieron identificar y analizar de manera efectiva las características más relevantes de la señal de ECG, lo que resulta fundamental en la evaluación y diagnóstico de trastornos cardíacos y otras aplicaciones médicas.

# Resultados y discusión
## Librería Biosignals
Resultados para amplitud, frecuencia cardiaca y picos-R en todo el tiempo de la señal ECG
![Alt text](<Imágenes/Extraccion de caracteristicas/1 scypy.jpg>)

Resultados para amplitud, frecuencia cardica y picos-R para 5 segundos de la señal ECG
![Alt text](<Imágenes/Extraccion de caracteristicas/1 scypy 5 seg.jpg>)

## Librería Neurokit2
Resultados utilizando el filtro de Neurokit(Average heart rate: 64.7 bpm)
![Alt text](<Imágenes/Extraccion de caracteristicas/2 filtro neurokit.jpg>)

Resultados utilizando el filtro de wavelets (Average heart rate: 64.4 bpm)
![Alt text](<Imágenes/Extraccion de caracteristicas/3 filtro wavelet.jpg>)

# Conclusiones

# Bibliografía
[1] V. Montes, G. Guarín y G. Castellanos, “Extracción de características en señales ECG normales y patológicas mediante wavelets y análisis no lineal de componentes principales”, Revista Ingeniería Biomédica, vol. 1, no. 1, pp. 7-16, 2007.