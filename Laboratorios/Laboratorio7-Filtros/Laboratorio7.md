# Laboratorio 7 - Filtros de señales de EMG, ECG y EEG

## Tabla de contenido
- [Introducción](#Introducción)
- [Materiales](#Materiales)
- [Metodología](#Metodología)
- [Resultados y discusión](#Resultadosydiscusión)
- [Conclusiones](#Conclusiones) 
- [Bibliografía](#Bibliografía)

# Introducción 
Una de las fases del procesamiento de señales biomedicas es el filtrado, ya que permite eliminar o atenuar ciertas frecuencias de una señal para mejorar su calidad o extraer información útil.
## Filtro IIR
    Los filtros IIR (Infinite Impulse Response) utilizan una función de transferencia con una respuesta infinita, es decir, su salida depende tanto de las entradas actuales como de las entradas anteriores. Estos filtros son implementados mediante una retroalimentación de la señal de salida hacia la entrada, lo que permite que las señales de entrada pasen a través del filtro en tiempo real. Los tipos de filtros IIR se pueden clasificar en Bessel, Butterworth, Chebyshev o Elíptico, según sus características de frecuencia y fase.
   ![Alt text](<Imágenes/Tipos de filtro/IIR.PNG>) 
   Figura 1. Filtros IIR

## Filtro FIR
    Los filtros FIR (Finite Impulse Response) utilizan una función de transferencia con una respuesta finita, es decir, su salida sólo depende de las entradas actuales. Estos filtros no utilizan retroalimentación y en su lugar utilizan una secuencia de coeficientes finita para procesar la señal de entrada. Los filtros FIR se pueden diseñar mediante diferentes métodos de ventana, como Hanning, Hamming, Bartlett, rectangular o Blackman, según sus características de amplitud y fase.
   ![Alt text](<Imágenes/Tipos de filtro/FIR.PNG>)
   Figura 2. Ventanas para filtros FIR

En este laboratorio se realizará un filtrado del ruido causado por la corriente eléctrica (60 Hz )de las señales ECG, EMG y EEG obtenidas previamente utilizando los siguientes métodos de filtros: FIR y IIR. Posteriormente, se hará una comparación entre los resultados obtenidos para determinar el mejor filtro.

# Materiales
- Datos para procesar: Señales EMG, ECG y EEG
- Herramientas para filtrar señales: Python (scipy.signal)

# Metodología
## Filtro IIR

## Filtro FIR

# Resultados y discusión

# Conclusiones
1.
2.
3.
4.
# Bibliografía
1. Díaz Osornio, J. H. Capítulo 5. Filtrado de señales. (p. 20). http://www.ptolomeo.unam.mx:8080/xmlui/bitstream/handle/132.248.52.100/263/A7.pdf?sequence=7