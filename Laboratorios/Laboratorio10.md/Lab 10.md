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

4. Se procesaron las señales en Python utilizando la librería de Neurokit2 para extraer las características principales de la señal EEG como el valor RMS, la amplitud, entre otros parámetros. 
5. Se analizaron las señales mediante las gráficas para visualizar el comportamiento de acuerdo a la actividad mental.

# Resultados
Con el propósito de aislar las bandas de interés asociadas a la señal de electroencefalograma (EEG), se llevó a cabo un proceso de filtrado utilizando frecuencias de corte correspondientes a cada una de las bandas características. En este contexto, se emplearon exclusivamente filtros pasabanda, ajustados con las frecuencias de corte distintivas de cada ritmo de EEG. Una vez concluido el proceso de adquisición y filtrado de las señales, se evidenciaron cambios significativos, como se observa en la figura 1, en relación con las diversas bandas que conforman la señal EEG. 

![Alt text](<Imagenes/señaleseegfiltradas.png>) 
   Figura 1. Señales filtradas

Una vez finalizado el procesamiento de cada señal,se procedió a la extracción de las características de cada señal, resultando en los siguientes valores para las respectivas señales:

1. Delta
- RMS (Delta): 83.07800683288704
- Amplitude (Delta): 649.8057934174266
- Area (Delta): -40985.155483688
- Power (Delta): 6901.955219325225
- Min Value (Delta): -335.2340339356023
- Max Value (Delta): 314.57175948182424
- Mean (Delta): -1.8235840284690013
- Median (Delta): -1.364009604115558
2. Theta
- RMS (Theta): 127.07103286093329
- Amplitude (Theta): 920.4630236153996
- Area (Theta): 8330.01862148968
- Power (Theta): 16147.047392344388
- Min Value (Theta): -449.48051099149006
- Max Value (Theta): 470.98251262390954
- Mean (Theta): 0.3747293767099355
- Median (Theta): -0.012287626898799838
3. Alpha
- RMS (Alpha): 101.50370298080828
- Amplitude (Alpha): 1044.983747396972
- Area (Alpha): 4831.293784882604
- Power (Alpha): 10303.001718816147
- Min Value (Alpha): -490.52193531571174
- Max Value (Alpha): 554.4618120812601
- Mean (Alpha): 0.21255353686886283
- Median (Alpha): 0.04107527284608937
4. Beta
- RMS (Beta): 66.52904510954
- Amplitude (Beta): 661.7179740760821
- Area (Beta): 2210.628060269558
- Power (Beta): 4426.113843187208
- Min Value (Beta): -346.54132461972534
- Max Value (Beta): 315.1766494563567
- Mean (Beta): 0.09781222166618311
- Median (Beta): 0.012361999371375285

# Discusiones
A modo de interpretar los resultados, resulta pertinente poder analizarlos de manera independiente, de lo anterior se llegaron a los siguientes análisis.

1. Delta:

RMS (Root Mean Square): La raíz cuadrada media indica la amplitud promedio de la señal en la banda Delta. Un valor alto podría sugerir una mayor actividad en el sueño profundo.
Amplitude: La amplitud representa la diferencia entre los valores máximo y mínimo en la banda Delta. Puede indicar la magnitud de las fluctuaciones en esta banda.
Area: La integral de la señal en la banda Delta. Un valor negativo puede deberse a la predominancia de valores negativos.
Power: La potencia en la banda Delta, que refleja la cantidad total de energía en esa frecuencia. Un valor alto puede relacionarse con una mayor actividad cerebral durante el sueño profundo.
Min y Max Value: Los valores mínimo y máximo en la banda Delta. Proporcionan información sobre la variabilidad de la señal en esta banda.
Mean y Median: El valor medio y la mediana en la banda Delta. Pueden dar una indicación de la tendencia central de la señal.

2. Theta:

RMS: La raíz cuadrada media indica la amplitud promedio de la señal en la banda Theta. Puede relacionarse con la actividad cerebral durante la relajación.
Amplitude: La diferencia entre los valores máximo y mínimo en la banda Theta. Puede indicar la magnitud de las fluctuaciones en esta banda.
Area: La integral de la señal en la banda Theta. Representa la acumulación total de la señal en esta frecuencia.
Power: La potencia en la banda Theta. Un valor alto podría relacionarse con la actividad cerebral durante procesos de memoria.
Min y Max Value: Los valores mínimo y máximo en la banda Theta. Proporcionan información sobre la variabilidad de la señal en esta banda.
Mean y Median: El valor medio y la mediana en la banda Theta. Pueden dar una indicación de la tendencia central de la señal.

3. Alpha:

RMS: La raíz cuadrada media indica la amplitud promedio de la señal en la banda Alpha. Un valor más alto podría relacionarse con un estado de relajación.
Amplitude: La diferencia entre los valores máximo y mínimo en la banda Alpha. Puede indicar la magnitud de las fluctuaciones en esta banda.
Area: La integral de la señal en la banda Alpha. Representa la acumulación total de la señal en esta frecuencia.
Power: La potencia en la banda Alpha. Un valor más alto podría sugerir un estado de relajación o atención sostenida.
Min y Max Value: Los valores mínimo y máximo en la banda Alpha. Proporcionan información sobre la variabilidad de la señal en esta banda.
Mean y Median: El valor medio y la mediana en la banda Alpha. Pueden dar una indicación de la tendencia central de la señal.

4. Beta:

RMS: La raíz cuadrada media indica la amplitud promedio de la señal en la banda Beta. Un valor más alto podría relacionarse con estados de alerta o procesos cognitivos.
Amplitude: La diferencia entre los valores máximo y mínimo en la banda Beta. Puede indicar la magnitud de las fluctuaciones en esta banda.
Area: La integral de la señal en la banda Beta. Representa la acumulación total de la señal en esta frecuencia.
Power: La potencia en la banda Beta. Un valor más alto podría sugerir una mayor actividad cerebral asociada con estados de alerta y procesos cognitivos.
Min y Max Value: Los valores mínimo y máximo en la banda Beta. Proporcionan información sobre la variabilidad de la señal en esta banda.
Mean y Median: El valor medio y la mediana en la banda Beta. Pueden dar una indicación de la tendencia central de la señal.

Asimismo, se tuvieron en cuenta las siguientes consideraciones:
- Se destaca de que el filtrado utilizado pese a que mostro mejorias, podría mejorarse aun mas dado a que se pueden utilizar tecnicas de enventanado para reducir los efectos secundarios no deseados, como las fugas espectrales, que pueden ocurrir al analizar segmentos finitos de una señal continua.
- Por otro lado, dado a que este laboratorio se enfoco principalmente en evaluar los resultado de las caracteristicas obtenidas de cada banda especifica de una señal electroencefalografica no se consideró utilizar o realizar un analisis de espectro sobre cada una de las bandas una vez finalizada su procesamiento. Cabe destacar que este tipo de análisis podría resultar altamente beneficioso al examinar y verificar efectivamente si la señal filtrada corresponde y opera dentro de la banda característica que se pretende analizar, ya sea Delta, Theta, Alpha, entre otras.
# Conclusiones
- Los valores obtenidos para las características de las señales EEG varían de acuerdo a la actividad cerebral, la cual está relacionada estrechamente con los tipos de ondas cerebrales. 
- Las medidas de amplitud, integral y potencia proporcionan información detallada sobre la naturaleza y la intensidad de la actividad cerebral en cada banda, ya sea Delta, Theta, Alpha o Beta.
- Las señales de EEG generalmente no presentan un patrón común como en el caso de ECG, por ello es importante realizar un preprocesamiento, procesamiento y análisis adecuado para interpretar sus características correctamente.
- La extracción de características permiten reconocer el tipo de actividad cerebral que realiza la persona, por lo que su aplicación para dispositivos biomédicos como el control de prótesis de extremidad superior puede ser útil.

# Bibliografía
[1] Medina, B., Sierra, J. E., & Barrios Ulloa, A. (2018). Extraction techniques of EEG signals characteristics in motion imagination for BCI systems. Espacios, 39(22), 36. https://www.revistaespacios.com/a18v39n22/a18v39n22p36.pdf

[2] Makowski, D., Pham, T., Lau, Z. J., Brammer, J. C., Lespinasse, F., Pham, H.,
Schölzel, C., & Chen, S. A. (2021). NeuroKit2: A Python toolbox for neurophysiological signal processing.
Behavior Research Methods, 53(4), 1689–1696. https://doi.org/10.3758/s13428-020-01516-y

[3] Puertas Martínez, P. (2018). Estimación de Estados Cognitivos en Base a Ondas Cerebrales: Aplicación Práctica con Redes Neuronales. Universidad Politécnica de Madrid
