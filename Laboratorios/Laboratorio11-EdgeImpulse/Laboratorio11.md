# Laboratorio 11 - Edge Impulse

## Tabla de contenido
- [Introducción](#Introducción)
- [Materiales](#Materiales)
- [Metodología](#Metodología)
- [Resultados](#Resultados)
- [Discusión](#Discusión)
- [Conclusiones](#Conclusiones) 
- [Bibliografía](#Bibliografía)

# Introducción
En el pasado, Edge Impulse se destacó como la principal plataforma de desarrollo para aprendizaje automático en dispositivos de borde, ofreciendo sus servicios de forma gratuita para desarrolladores y ganando la confianza de empresas a nivel mundial. Con un enfoque en aplicaciones de sensores, audio y visión por computadora, la misión de la empresa era proporcionar la mejor experiencia de desarrollo y implementación para el aprendizaje automático en el borde. Esta plataforma permitió a desarrolladores de software, ingenieros y expertos en dominios resolver problemas reales mediante el aprendizaje automático en dispositivos de borde, sin requerir un doctorado o habilidades avanzadas de ingeniería embebida[1].

En este contexto, se utilizó Edge Impulse para entrenar modelos de clasificación específicamente diseñados para señales electromiográficas (EMG). Anteriormente, se había llevado a cabo un extenso trabajo en la extracción de características en el procesamiento de señales, centrándose en identificar aspectos notables de una señal, como frecuencia, forma de onda y amplitud. Estas características extraídas posteriormente se emplean para el reconocimiento de patrones en la señal, facilitando la clasificación o predicción de su comportamiento futuro. En particular, en este laboratorio se extrajeron y filtraron señales EMG previamente adquiridas, enfocándose en características clave como RMS y media [2].

# Materiales
Para llevar a cabo este proceso, se utilizaron los siguientes materiales:

- Una computadora con acceso a Internet: Esencial para acceder y trabajar en la plataforma Edge Impulse y realizar tareas relacionadas con el aprendizaje automático.

- Señales EMG: Previamente adquiridas y filtradas en laboratorios anteriores, estas señales proporcionaron los datos necesarios para entrenar y evaluar los modelos de clasificación.

# Metodología
- La metodología seguida se centró en la extracción de características de las señales EMG utilizando la plataforma Edge Impulse. Primero, se llevó a cabo el proceso de extracción de características, centrándose en aspectos clave como RMS y media. Estas características se utilizaron para entrenar modelos de clasificación capaces de reconocer patrones en las señales EMG. El enfoque práctico se basó en la aplicación de conocimientos previos sobre procesamiento de señales y aprendizaje automático para lograr resultados efectivos en la clasificación de señales EMG.

# Resultados
Lorem Lorem 

![Alt text](<Imagenes/señaleseegfiltradas.png>) 
   Figura 1. Señales filtradas

# Discusiones
Lorem Lorem.

# Conclusiones
Lorem Lorem.

# Bibliografía
[1] 

[2] Medina, B., Sierra, J. E., & Barrios Ulloa, A. (2018). Extraction techniques of EEG signals characteristics in motion imagination for BCI systems. Espacios, 39(22), 36. https://www.revistaespacios.com/a18v39n22/a18v39n22p36.pdf

[3] Makowski, D., Pham, T., Lau, Z. J., Brammer, J. C., Lespinasse, F., Pham, H.,
Schölzel, C., & Chen, S. A. (2021). NeuroKit2: A Python toolbox for neurophysiological signal processing.
Behavior Research Methods, 53(4), 1689–1696. https://doi.org/10.3758/s13428-020-01516-y

[4] Puertas Martínez, P. (2018). Estimación de Estados Cognitivos en Base a Ondas Cerebrales: Aplicación Práctica con Redes Neuronales. Universidad Politécnica de Madrid
