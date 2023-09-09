#  Informe de laboratorio
    
# Tabla de contenidos 
------------------------------------------------------------------------------------------------
- Objetivos del laboratorio
- Materiales
- OpenSignals
- Ploteo de señales en Python
- Archivo del codigo 
- Explicacion y resultados
---------------------------------------------------------------------------------------------------------------------------------------------------------------------    
 
## Objetivos del Laboratorio
- Adquirir señales biomédicas de EMG.
- Realizar una configuración adecuada con el modulo BITalino. 
- Obtener la información de las señales EMG del software OpenSignals (r)evolution.
## Materiales utilizados
- 1 cable de 2 hilos
- 1 cable de 3 hilos
- 5 electrodos
- 1 bateria
- 1 BITalino

<p align="center">
  <img width="200" height="300" src="https://github.com/daang04/Intro_se-ales/blob/main/imagen/material.png">
</p>

## Electromiografía
### ¿Qué es la técnica de electromiografía?
- La electromiografía (EMG) y los estudios de conducción nerviosa son pruebas que miden la actividad eléctrica de los músculos y nervios. Los nervios envían señales eléctricas para que los músculos reaccionen de ciertas maneras. Cuando reaccionan, emiten señales que pueden medirse.
### Fundamento de la Electriomiografía
- El fundamento radica en la medición de los biopotenciales musculares generados por la actividad muscular (contracción y relajación del músculo)
### Aplicaciones
- Lesiones musculares
- Evaluación de la función muscular
- Detección de enfermedades neuromusculares

## OpenSignals
### Musculos a analizar y conexiones realizadas
<p>
    <table>
        <tr>
            <th><div class="column">
                <p>BITalino-Cables</p>
    <img src="https://github.com/daang04/Intro_se-ales/blob/main/imagen/body_posic.png" alt="Snow" style="width:70%">
 </div></th>                
    </table>
 </p>
     
### Ploteo de la señal usada en OpenSignals
 <p>
    <table>
        <tr>
            <th><div class="column">
                <p>Señal en actividad </p>
    <img src="https://github.com/daang04/Intro_se-ales/blob/main/imagen/signal_no_filter.png" alt="Snow" style="width:90%">
 </div></th>                
    </table>
 </p>
        
## Ploteo de señales con procesamiento en Python

 <p>
    <table>
        <tr>
            <th><div class="column">
                <p>Señal en actividad </p>
    <img src="https://github.com/daang04/Intro_se-ales/blob/main/imagen/signal_filtered.png" alt="Snow" style="width:90%">
 </div></th>                
    </table>
 </p>
      

## Explicación y resumen del procedimiento y resultados:
Se llevó a cabo un experimento que consistió en recopilar y evaluar el movimiento del grupo muscular de los bíceps utilizando el dispositivo BitAlino y tres electrodos. Este estudio se centró en pruebas electromiográficas. Según los resultados obtenidos a través de la representación gráfica en "OpenSignals", se pueden extraer las siguientes conclusiones:
- En la fase inicial, se observa una señal en estado de reposo, donde no hay activación muscular y las fibras musculares se encuentran en un estado de inactividad. La información visualizada en esta etapa puede contener interferencias, posiblemente causadas por una conexión incorrecta de los electrodos u otras fuentes de error.
- Posteriormente, se inicia el período de activación muscular con la ejecución del movimiento de flexión del bíceps. Durante esta fase, la gráfica muestra un incremento en la amplitud de la señal, lo cual indica un aumento en la fuerza muscular.
        
