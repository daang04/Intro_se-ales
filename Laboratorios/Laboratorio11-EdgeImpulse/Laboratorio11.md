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
La metodología seguida se centró en la extracción de características de las señales EMG utilizando la plataforma Edge Impulse. Primero, se llevó a cabo el proceso de extracción de características, centrándose en aspectos clave como RMS y media. Estas características se utilizaron para entrenar modelos de clasificación capaces de reconocer patrones en las señales EMG. El enfoque práctico se basó en la aplicación de conocimientos previos sobre procesamiento de señales y aprendizaje automático para lograr resultados efectivos en la clasificación de señales EMG.

![primer](https://github.com/daang04/Intro_se-ales/assets/45319820/fd452017-5015-4096-ab19-03644f5d972c)
<p style="text-align: center;">Figura 1. Adquisición de data en splits de 100ms</p>

# Resultados
Se observó lo siguiente:

![sa_settings](https://github.com/daang04/Intro_se-ales/assets/45319820/39c5cbc5-26ec-4b9a-b5aa-85a1f0b4c499)
<p style="text-align: center;">Figura 2. Parámetros seteados para el análisis</p>

![sa_raw_data](https://github.com/daang04/Intro_se-ales/assets/45319820/bc1f0475-2df1-4683-8c36-a5afafe4e8ce)
<p style="text-align: center;">Figura 3. Raw data ingresada</p>

![parameter_sfeationes](https://github.com/daang04/Intro_se-ales/assets/45319820/2bf52cd5-58fa-4688-bc43-136d8aedbb63)}
<p style="text-align: center;">Figura 4. Spectral Features para la raw data</p>

![sa_sp_after](https://github.com/daang04/Intro_se-ales/assets/45319820/ac61437a-9c29-4118-99da-ab24a130611e)
<p style="text-align: center;">Figura 5. Spectral Faeatures para la data procesada</p>


# Discusiones

La Transformada Rápida de Fourier (FFT) resultó ser un enfoque altamente efectivo en el análisis de señales EMG, permitiendo una clara visualización de la distribución de energía en diversas bandas de frecuencia presentes en estas señales. Su capacidad para identificar patrones frecuenciales específicos facilitó la revelación de componentes espectrales cruciales, siendo vital para discernir cambios significativos en la actividad muscular y extraer características relevantes para aplicaciones médicas y de control. La elección de la FFT sobre los wavelets se sustentó en su simplicidad y eficiencia para resaltar patrones de frecuencia relevantes en las señales EMG, aunque los wavelets, con su habilidad para representar ambas dimensiones temporal y frecuencial, siguen siendo valiosos en otros contextos donde se requiera un análisis más detallado de las señales.

Es esencial resaltar que la selección entre la FFT y los wavelets depende de las particularidades de las señales EMG y los objetivos de la aplicación. Aunque la FFT demostró su eficacia en este estudio específico, los wavelets mantienen su utilidad en escenarios que demandan un análisis exhaustivo en ambos dominios, temporal y frecuencial.


# Conclusiones
Se puede apreciar que la integración de Edge Impulse para el procesamiento de señales EMG demostró ser eficaz en la extracción de características clave y la capacitación de modelos de clasificación. Este enfoque simplificado enriqueció la comprensión de patrones en señales EMG, destacando el potencial de Edge Impulse en aplicaciones de aprendizaje automático en el ámbito de la biomecánica.

# Bibliografía

[1] Medina, B., Sierra, J. E., & Barrios Ulloa, A. (2018). Extraction techniques of EEG signals characteristics in motion imagination for BCI systems. Espacios, 39(22), 36. https://www.revistaespacios.com/a18v39n22/a18v39n22p36.pdf

[2] Makowski, D., Pham, T., Lau, Z. J., Brammer, J. C., Lespinasse, F., Pham, H.,
Schölzel, C., & Chen, S. A. (2021). NeuroKit2: A Python toolbox for neurophysiological signal processing.
Behavior Research Methods, 53(4), 1689–1696. https://doi.org/10.3758/s13428-020-01516-y

[3] Puertas Martínez, P. (2018). Estimación de Estados Cognitivos en Base a Ondas Cerebrales: Aplicación Práctica con Redes Neuronales. Universidad Politécnica de Madrid
