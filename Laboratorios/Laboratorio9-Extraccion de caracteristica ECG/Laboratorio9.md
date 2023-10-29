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
- Señal filtrada de ECG

# Metodología

Se adquirio la señal de ECG mediante el módulo del Bitalino para luego ser filtrada mediante el método de Wavelet y sus respectivos coeficientes. Desde este punto, se utilizo la libreria llamada neurokit en Python para extraer las características más importantes como las mnecionadas en la introudcción. Es importante destacar que el codigo empleado se encuentra en la carpeta "codigo" del laboratorio 9 para más información sobre que comandos se han utilizado.

# Resultados y discusión

# Conclusiones

# Bibliografía