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
## Preprocesamiento
Se obtiene la medición a partir del software OpenSignals de Bitalino, a la cual se aplica la transformada de Fourier para obtener la frecuencia presente que origina el ruido de la señal. Con ello, se definen las frecuencias de corte. Para definir el orden de filtro, se emplea una lista de valores de orden de filtro. El código carga una señal de ECG y establece valores de frecuencia de corte para todos los filtros FIR. Luego, ejecuta un bucle para aplicar el filtro FIR con diferentes órdenes a la señal original. Las señales filtradas se trazan en una misma gráfica junto con la señal sin filtrar para comparar cómo diferentes órdenes afectan la señal.
![Alt text](<Imágenes/Preprocesamiento/1 comparacion.png>)

El filtro FIR resultante se aplica con un orden de 60 al conjunto de datos con una frecuencia de muestreo de 1000 Hz y las frecuencias de corte 0.5 y 35. Luego, la señal filtrada resultante se visualiza en el siguiente gráfico.
![Alt text](<Imágenes/Preprocesamiento/2 señal filtrada.png>)

## Procesamiento y extracción de características
Se utilizaron dos librerías: Neurokit2 y Biosignals en Python para extraer las características más importantes de la señal ECG. Es importante destacar que el codigo empleado se encuentra en la carpeta "codigo" del laboratorio 9 para más información sobre que comandos se han utilizado.


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