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

## Filtro con Wavelets
    El filtrado con la técnica de Wavelets es utilizado para analizar señales (continuas o discretas) tanto en el dominio del tiempo como en la frecuencia. Los filtros wavelet  permiten eliminar ruido y extraer características de la señal. Existen diferentes familia de wavelets tales como Haar, Daubechies, Coiflets, Symlets, Biortogonales, Meyer, Mexican hat, Shannon y Morlet.
  ![Alt text](<Imágenes/Tipos de filtro/Wavelet.png>)
  Figura 3. Wavelet

En este laboratorio se realizará un filtrado del ruido causado por la corriente eléctrica (60 Hz )de las señales ECG, EMG y EEG obtenidas previamente utilizando los siguientes métodos de filtros: FIR y IIR. Posteriormente, se hará una comparación entre los resultados obtenidos para determinar el mejor filtro.

# Materiales
- Datos para procesar: Señales EMG, ECG y EEG
- Herramientas para filtrar señales: Python (scipy.signal)

# Metodología
## Filtro IIR
- Para el desarrollo de un filtro IIR, se siguió una metodología compuesta por varias etapas. Inicialmente, se realizó la lectura de datos desde un archivo de texto, extrayendo señales relacionadas con EMG, ECG y EEG junto con sus frecuencias de muestreo respectivas (Fs). A continuación, se efectuó un análisis espectral de cada señal mediante una FFT para visualizar sus características en el dominio de frecuencia. Este análisis espectral permitió determinar los parámetros necesarios para el diseño del filtro.

  Se optó por un filtro Butterworth debido a su capacidad para suprimir componentes de alta frecuencia no deseados, apropiado para el procesamiento de señales fisiológicas. Los valores de frecuencia de corte (wp y ws), la pérdida en bandas de paso (gpass), y la atenuación en bandas de rechazo (gstop) se emplearon en el diseño. El orden del filtro (N_ord) y la frecuencia de corte (Wc) se calcularon utilizando la función signal.buttord para luego definir la respuesta del filtro. Posteriormente, se obtuvieron los coeficientes del filtro tanto en el dominio analógico como digital y se analizó su respuesta en frecuencia.

  La metodología se aplicó de manera sistemática a las señales de EMG, ECG y EEG, adaptando los parámetros del filtro según las particularidades de cada señal. El resultado fue la obtención de señales filtradas con notorias mejorías en las señales.
## Filtro FIR
- Para el desarrollo de un filtro FIR, se utilizo el método de muestreo de ventana (window sampling). Este enfoque implica la selección de una ventana específica, como la ventana de Hamming, Blackman, Hanning, entre otros. Las ventanas determinan la forma en que se ponderan los coeficientes del filtro en el dominio del tiempo. La elección de la ventana depende de los requisitos del filtro y los objetivos del diseño. Luego, se determinan los números de muestras del filtro en función de la resolución en frecuencia y la atenuación necesaria en las bandas de paso y de rechazo. Sin embargo, para este caso se priorizo con que ventana se utilizaba menor poder computacional para elegir el tipo de ventana, por lo que, si se obtiene un menor número de muestra se empleaba esa ventana. Una vez definidos estos parámetros, se calculan los coeficientes del filtro utilizando una función como scipy.signal.firwin en Python, y se aplica la ventana elegida a estos coeficientes.
  El resultado es un filtro FIR que cumple con las especificaciones deseadas, y su respuesta en frecuencia está influenciada por la forma de la ventana seleccionada.
  
## Filtro con Wavelets
- Para el filtrado con wavelets se importa las librerías necesarias: numpy, matplotlib y pywt. Luego, se define una función para calcular el umbral fijo y una función para aplicar el filtrado wavelet, usando la función wavedec para obtener los coeficientes de DWT. Posteriormente, se usa la función threshold para aplicar la umbralización y la función waverec para obtener la IDWT. Finalmente, se aplica el filtrado wavelet a la señal con ruido y se obtiene la grafica de la señal filtrada.
# Resultados y discusión
## Filtro IIR
- EMG: Se utilizo un frecuencia de muestreo de 1000 Hz, en función a esto se calculo las frecuencias correspondientes en radianes, estas frecuencias fueron calculadas en base a los requerimientos de nuestras señales. Dado a que se este tipo de señales operan en frecuencias bajas se optan por eliminar todas las frecuencias correspondientes a altas frecuecnias que puedan influir de manera significativa en la obtención y y visualización de los datos.

| Señal original EMG|![Alt text](<Imágenes/Tipos de filtro/IIR imagenes/IIR EMG sin procesar.png>)  | 
|----------|----------|
| Señal procesada usando Butterworth | ![Alt text](<Imágenes/Tipos de filtro/IIR imagenes/IIR EMG procesada.png>)| 

- ECG: Se utilizo una frecuencia de muestreo de 1000 Hz, ya que las frecuencias del ECG van hasta 100 Hz, entonces, para cumplir nyquist se eligio esa frecuencia.

| Señal original ECG|![Alt text](<Imágenes/Tipos de filtro/IIR imagenes/IIR ECG sin procesar.png>)
|----------|----------|
| Señal procesada usando Butterworth  | ![Alt text](<Imágenes/Tipos de filtro/IIR imagenes/IIR ECG procesada.png>)
- EEG: Las frecuencias que registra el EEG se dividen en los ritmos alfa, beta, theta y delta. Donde la mayor frecuencia es 60 Hz y para cumplir el criterio de Nyquist se empleo una frecuencia de muestreo de 1000 Hz.

| Señal original EEG|![Alt text](<Imágenes/Tipos de filtro/IIR imagenes/IIR EEG sin procesar.png>)
|----------|----------|
| Señal procesada usando Butterworth | ![Alt text](<Imágenes/Tipos de filtro/IIR imagenes/IIR EEG procesada.png>)

## Filtro FIR
- EMG: Se utilizo un frecuencia de muestreo de 1000 Hz, en función a esto se calculo el equivalente de 50 Hz y 150 Hz en radianes, las cuales forman el intervalo donde se encuentran las freuencias del EMG. Esto indica que será un filtro pasabandas.

| Señal original EMG|![Alt text](<Imágenes/Tipos de filtro/EMG_original_FIR.png>)  | 
|----------|----------|
| FIR usando ventana Hamming | ![Alt text](<Imágenes/Tipos de filtro/FIR_hamm_EMG.png>)| 
| FIR usando ventana Hanning | ![Alt text](<Imágenes/Tipos de filtro/FIR_hann_EMG.png>)  |

- ECG: Se utilizo una frecuencia de muestreo de 1000 Hz, ya que las frecuencias del ECG van hasta 100 Hz, entonces, para cumplir nyquist se eligio esa frecuencia.

| Señal original ECG|![Alt text](<Imágenes/Tipos de filtro/ECG.png>)
|----------|----------|
| FIR usando ventana Hamming | ![Alt text](<Imágenes/Tipos de filtro/FIR_hamm_ECG.png>)
| FIR usando ventana Hanning | ![Alt text](<Imágenes/Tipos de filtro/FIR_hann_ECG.png>)

- EEG: Las frecuencias que registra el EEG se dividen en los ritmos alfa, beta, theta y delta. Donde la mayor frecuencia es 60 Hz y para cumplir el criterio de Nyquist se empleo una frecuencia de muestreo de 1000 Hz.

| Señal original EEG|![Alt text](<Imágenes/Tipos de filtro/EEG.png>)
|----------|----------|
| FIR usando ventana Hamming | ![Alt text](<Imágenes/Tipos de filtro/FIR_hamm_EEG.png>)
| FIR usando ventana Hanning | ![Alt text](<Imágenes/Tipos de filtro/FIR_hann_EEG.png>)

## Wavelet
Para el filtrado de las señales EEG, ECG y EMG mediante la Transformada Discreta Wavelet (DWT) se utilizó la familia Daubechies ¨db6¨ y nivel de descomposición 5 para eliminar el ruido y comprimir las señales biomédicas.
- EEG

| Señal original EEG |![Alt text](<Imágenes/Wavelet/eeg_raw.png>)
|----------|----------|
| ECG Wavelet| ![Alt text](<Imágenes/Wavelet/eeg_w.png>)

- ECG

| Señal original ECG| ![Alt text](<Imágenes/Wavelet/ecg_raw.png>)
|----------|----------|
| ECG Wavelet | ![Alt text](<Imágenes/Wavelet/ecg_w.png>)

- EMG

| Señal original EMG | ![Alt text](<Imágenes/Wavelet/emg_raw.png>)
|----------|----------|
| EMG Wavelet | ![Alt text](<Imágenes/Wavelet/emg_w.png>)

# Conclusiones
1. Los filtros FIR no emplean una retroalimentación de la salida anterior, por lo que, no podran aprender acerca del comportamiento de la señal para seguir un patron y obtener un mejor filtrado. Sin embargo, al no tener una retroalimentación no habran picos dentro de la señal que pueden afectar a la señal.
2. Es importante escoger la frecuencia de muestreo correcta para convertir la frecuencia de Hz a radianes de manera correcta para así determinar las frecuencias de paso y "stop" adecuados, como la frecuencia de corte.
3. Un filtro IIR necesita de menos números de muestra del filtro en comparación al FIR, ya que ese número de muestras dependerá de que tan largo sea el intervalo entre la frecuencia de paso y stop. En cambio, los otros dependen de cada tipo de ventana.
4. Los filtros IIR mostraron ser eficaces en la eliminación de componentes de alta frecuencia no deseados en señales EEG, ECG y EMG, contribuyendo a la mejora de la calidad de los registros de las señales.
5. Tras aplicar el filtro IIR a la señal de ECG, no se observaron cambios notorios en la salida, lo que sugiere que la señal original puede haber estado relativamente libre de interferencias de alta frecuencia. Sin embargo, al utilizar el filtro FIR se mostro una notable mejoría en la visualización de la señal lo que sugiere que este tipo de filtros funcionan de mejor manera en el procesamiento de estas señales.
6. La aplicación del filtrado Wavelet ha demostrado ser altamente efectiva en la eliminación de ruidos y artefactos presentes en las señales biomédicas. En particular, se ha observado que la señal ECG muestra una calidad de filtrado excepcionalmente alta con esta técnica. Seguido de la señal EEG, que también presenta una mejora significativa tras el filtrado. Aunque la señal EMG muestra la menor mejora entre las tres, aún así se beneficia del uso del filtrado Wavelet. 
7. Se recomienda realizar más pruebas con una mayor cantidad de señales y los distintos filtros para obtener resultados significativos. Asimismo, es importante destacar que la adquisición de la data influye notablemente en los resultados de filtrado, por ello es importante realizar un protocolo riguroso.
# Bibliografía
1. Díaz Osornio, J. H. Capítulo 5. Filtrado de señales. (p. 20). http://www.ptolomeo.unam.mx:8080/xmlui/bitstream/handle/132.248.52.100/263/A7.pdf?sequence=7
2. MathWorks, “Choose a Wavelet - MATLAB & Simulink,” 2023. Available: https://www.mathworks.com/help/wavelet/gs/choose-a-wavelet.html. 
3. PyWavelets, “Discrete Wavelet Transform (DWT) — PyWavelets Documentation,” 2023.  Available: https://pywavelets.readthedocs.io/en/latest/ref/dwt-discrete-wavelet-transform.html.