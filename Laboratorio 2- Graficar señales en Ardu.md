# L2-ADQUISICIÓN DE SEÑALES Y GRAFICACIÓN EN ARDUINO
## Objetivos
- Adquirir señales conocidas como señal cuadrada, triangular, senoidal, rampa, etc.
- Entender los criterios de selección de la frecuencia de muestreo.
- Manipular y configurar adecuadamente una fuente de alimentación regulable; multímetro digital; 
Generador de señales y osciloscopio digital.
## Materiales
|Equipo | Modelo | Cantidad |
|----------|----------|----------|
| Generador de Señales     | AFG1022   | 1   |
| Osciloscopio Digital    | TBS 1000C Series  | 1  |
| Cable BNC Male-Male    | -  | 1  |
| Punta de osciloscopio con conector BNC (Male)    | -  | 1  |
| Par de cables Male -Male    | -   | 1  |
| Arduino 33 IoT    | SAMD   | 1  |

# Circuito
Se conecta un cable al pin analógico A1 de Arduino y con otro cable se conecta a tierra (GND). Posteriormente, se conecta la punta del osciloscopio a la salida del pin analógico y luego se conecta el cable de tierra del osciloscopio al Arduino.
## Circuito ensamblado 

# Ploteo de 3 señales en Arduino IDE provenientes del generador de señales
## Señal sinusoidal
Frecuencia:
 <img src ="imagen\generador_seno.jpeg">
Voltaje:
 <img src ="imagen\seno_osciloscopio.jpeg">
## Señal cuadrada
Frecuencia:
<img src ="imagen\generador_cuadrado.jpeg">
Voltaje:
<img src ="imagen\cuadrado_osciloscopio.jpeg">
## Señal triangular 
Frecuencia:
<img src ="imagen\generador_triangular.jpeg">
Voltaje:
<img src ="imagen\triangular_osciloscopio.jpeg">
# Gráficas de señales en Arduino cloud
## Señal sinusoidal
 <img src ="imagen\seno.jpeg">
## Señal cuadrada
<img src ="imagen\cuadrado.jpeg">
## Señal triangular 
<img src ="imagen\triangulo.jpeg">
# Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio
# Se puede apreciar ruido al momento de graficar las señales en el Arduino IDE. Para plotear las señales mostradas se aplico el criterio de Niquist al determinar que la frecuencia de muestreo es 2 veces la frecuencia más alta.