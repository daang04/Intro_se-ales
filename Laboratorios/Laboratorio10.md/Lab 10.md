# Laboratorio 10 - Extracción de características EEG

## Tabla de contenido
- [Introducción](#Introducción)
- [Materiales](#Materiales)
- [Metodología](#Metodología)
- [Resultados y discusión](#Resultadosydiscusión)
- [Conclusiones](#Conclusiones) 
- [Bibliografía](#Bibliografía)

# Introducción
La extracción de características es ampliamente desarrollada en el procesamiento de señales, y se basa en la identificación de características notables en una señal, como la frecuencia, forma de onda y amplitud. Posteriormente, estas características pueden ser utilizadas para el reconocimiento de patrones en la señal, lo que puede servir para clasificar o predecir su comportamiento futuro. Las aplicaciones de extracción de características de señales EEG pueden ser útiles para diferenciar diferentes actividades cerebrales. 
Existen diferentes técnicas de extracción de características tales como análisis en el tiempo y frecuencia, transformada discreta de Wavelet, redes neuronales, entre otros. Sin embargo, en este laboratorio se realizará la extracción de características utilizando wavelets mediante librería Neurokit2.

# Materiales
- Una computadora con python
- Señal de ECG 
- Librerías instaladas: Neurokit 2 y Biosignals

# Metodología
1. Se cargaron los archivos csv adquiridos previamente mediante BITalino que contienen las señales EEG que serán analizadas.
2. Luego, se realizó un preprocesamiento de la señal EEG para eliminar artefactos y ruidos de la señal.
3. Posteriormente, se aplicaron filtros pasabanda para identificar los ritmos cerebrales y se utilizaron como referencia las siguientes frecuencias:
- Delta 0.5Hz - 4Hz
- Theta 4Hz - 7.5 Hz
- Alpha 8Hz - 12Hz
- Beta 14Hz - 26Hz
- Gamma >30Hz
- Sigma 12Hz - 15Hz

4. Se procesaron las señales en Python utilizando la librería de Neurokit2 para extraer las características principales de la señal EEG como frecuencia, amplitud, entre otros. 
5. Se analizaron las señales mediante las gráficas para visualizar el comportamiento de acuerdo a la actividad mental.

# Resultados y discusión


# Conclusiones
- La extracción de característica permiten reconocer el tipo de actividad cerebral que realiza la persona, por lo que su aplicación para dispositivos biomédicos como el control de prótesis de extremidad superior puede ser útil.
- Las señales de EEG generalmente no presentan un patrón común como en el caso de ECG, por ello es importante realizar un preprocesamiento, procesamiento y análisis adecuado para interpretar sus características correctamente.

# Bibliografía
[1] Medina, B., Sierra, J. E., & Barrios Ulloa, A. (2018). Extraction techniques of EEG signals characteristics in motion imagination for BCI systems. Espacios, 39(22), 36. https://www.revistaespacios.com/a18v39n22/a18v39n22p36.pdf

[2] Makowski, D., Pham, T., Lau, Z. J., Brammer, J. C., Lespinasse, F., Pham, H.,
Schölzel, C., & Chen, S. A. (2021). NeuroKit2: A Python toolbox for neurophysiological signal processing.
Behavior Research Methods, 53(4), 1689–1696. https://doi.org/10.3758/s13428-020-01516-y

[3] Puertas Martínez, P. (2018). Estimación de Estados Cognitivos en Base a Ondas Cerebrales: Aplicación Práctica con Redes Neuronales. Universidad Politécnica de Madrid
