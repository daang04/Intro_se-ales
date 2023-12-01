# Monitoreo de lesiones en el ligamento cruzado anterior en futbolistas de 18 a 40 años utilizando técnicas de procesamiento de señales EMG**

## Participantes
- Daniel Alejandro Aquije Niño de Guzman
- Nataly Diaz
- Giovani Taco
- Piero Miranda 

## Introducción
## Planteamiento del problema
## Estado del arte
## Metodología
1.
2.
3.

4. **Extracción de características**
En el proceso de extracción de características, se persiguió la determinación de la media de las señales como un indicador revelador de la señal basal tanto en individuos sanos como lesionados. Posteriormente, se procedió a identificar los valores máximos y mínimos con el propósito de obtener referencias de la amplitud de cada señal, permitiendo así comparaciones significativas. Se puso especial énfasis en el cálculo de la raíz media cuadrática (RMS) para cada grupo muscular en ambos estados de salud: sano y en rehabilitación. Este enfoque nos brinda la oportunidad de evaluar la activación de grupos musculares y la potencia que estos exhiben, proporcionando insights valiosos sobre la respuesta muscular en diferentes condiciones de salud. [6]
5. **Análisis estadístico**
En el análisis estadístico, se realizó la prueba de Shapiro-Wilk para evaluar la normalidad de las muestras de electromiografía (EMG), necesaria para confirmar la aleatoriedad en la distribución de los picos en la señal. Posteriormente, se llevó a cabo una prueba de ANOVA para diferenciar las medias de cada grupo muscular en los estados de salud: sano y en rehabilitación, con el objetivo de evidenciar diferencias notables entre los grupos. Finalmente, se aplicó la prueba de Wilcoxon, específica para comparar muestras pareadas, con el fin de confirmar la presencia de diferencias significativas entre ambos estados de salud, ofreciendo así una validación precisa de las disparidades identificadas.


## Resultados

A.  **Extracción de características de electromiografìa de una persona sana**

En los resultados derivados del análisis estadístico de electromiografía en una persona sana, se reveló una notable elevación en los valores máximos de milivoltios en los grupos musculares específicos examinados, tales como el vasto medial, vasto lateral, gastrocnemius y bíceps femoral. Estos resultados indican una destacada actividad eléctrica en dichos músculos durante la evaluación. Además, al considerar el valor de la raíz media cuadrática (RMS), que representa la potencia de la señal, se constata una medida significativa de la fuerza y la intensidad de la actividad muscular registrada. Este hallazgo subraya la robustez y la eficacia de la actividad eléctrica en los músculos analizados en el contexto de la persona sana. Cabe resaltar que no solo los valores máximos, sino también la media y la mediana de la actividad eléctrica en estos músculos son notablemente altos, reflejando así una consistencia y fuerza muscular destacadas en la persona evaluada.

![Alt text](Imagenes/8f9fdc44-0815-4dc3-b0ce-6fc4411d4f2f.jpg)
**Tabla 1. Resultados estadísticos de electromiografía de una persona sana**


B. **Extracción de características de electromiografìa de una persona lesionada**

En los resultados de electromiografía (EMG) para una persona lesionada, se evidenció una marcada disminución en los valores en comparación con aquellos de una persona sana. Tanto el máximo valor como la media y la mediana de la señal registraron niveles significativamente inferiores. Específicamente, al analizar la raíz media cuadrática (RMS), se observó que este indicador era prácticamente la mitad del valor correspondiente en una persona sin lesiones. Esta reducción en los valores de EMG y, en particular, en el RMS, sugiere una disminución sustancial en la actividad eléctrica y la potencia de la señal muscular en el individuo lesionado en comparación con su contraparte saludable.
![Alt text](Imagenes/b3473b4c-c096-4995-b3c9-a7e2cd5ee81f.jpg)
**Tabla 2.  Resultados estadísticos de electromiografía de una persona en rehabilitación**

C. **Pruebas estadísticas realizadas**

- **Prueba de Shapiro-Wilk:** Se lograron obtener valores de
p < 0.001, lo cual conduce al rechazo de la hipótesis nula. Este resultado sugiere que la muestra de la señal obtenida no se adhiere a una distribución normal, una observación coherente dada la naturaleza de la señal de electromiografía. La falta de regularidad en la ocurrencia de los picos, que indican la contracción muscular, contribuye a la no conformidad con una distribución normal. En el contexto de la electromiografía, la imprevisibilidad en el momento de las contracciones musculares respalda la significativa diferencia respecto a una distribución normal, justificando así el rechazo de la hipótesis nula.

![Alt text](Imagenes/6c94376c-4c04-44f5-a90a-acb9bccf753d.jpg)

**Tabla 3. Resultados de la prueba de Shapiro-Wilk**

- **Prueba de Anova:** Los resultados de la prueba ANOVA revelaron valores de p<0.001, lo que lleva al rechazo de la hipótesis nula. Dentro del marco de esta prueba, se evidencia de manera concluyente la presencia de diferencias significativas al comparar las medias de los grupos musculares entre individuos saludables y aquellos en proceso de rehabilitación. 

![Alt text](<Imagenes/Captura de pantalla 2023-11-30 204727.png>)

**Tabla 4. Resultados de la prueba de ANOVA**

- **Prueba de Wilcoxon:** En relación con la prueba de Wilcoxon, diseñada específicamente para muestras pareadas, se ha obtenido un valor de p < 0.001. Esta significativa diferencia conduce al rechazo de la hipótesis nula. Dentro del marco de esta prueba, se establece de manera concluyente que existen disparidades significativas entre las muestras de una persona en proceso de rehabilitación por una lesión de ligamento cruzado anterior y una persona completamente sana.

![Alt text](<Imagenes/Captura de pantalla 2023-11-30 204727.png>)

**Tabla 5. Resultados de la prueba de Wilcoxon**

## Conclusiones
- Se evidencio estadísticamente que existe una diferencia significativa entre pacientes en rehabilitación después de una lesión de ligamento cruzado anterior y los sanos.
- Se puede evaluar el estado de salud de un paciente en rehabilitación con la técnica de electromiografía mediante la extracción de características seleccionadas.
## Referencias 
