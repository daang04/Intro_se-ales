import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
import pywt
from scipy import signal
from scipy.signal import firwin, lfilter

# Función para cargar y procesar señales
def cargar_y_procesar_senal(archivo, columna, Fs, limite):
    array = np.genfromtxt(archivo, delimiter="\t", skip_header=3, missing_values=0)
    senal = array[:, columna]
    senal = senal[:limite]
    Ts = 1 / Fs
    n = len(senal)
    t = np.arange(0, n * Ts, Ts)
    return t, senal

# Función para plotear señales
def plotear_senal(t, senal, titulo):
    plt.plot(t, senal, label="señal")
    plt.grid(linestyle=":")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend(loc="upper right")
    plt.title(titulo)
    plt.show()

# Función para aplicar el filtrado Wavelet
def filtrar_wavelet(senal, umbral, wavelet_name):
    coeficientes = pywt.wavedec(senal, wavelet_name, level=8)
    coeficientes_umbral = [pywt.threshold(c, umbral, mode='soft') for c in coeficientes]
    senal_filtrada = pywt.waverec(coeficientes_umbral, wavelet_name)
    return senal_filtrada

# Función para aplicar el filtrado Butterworth Bandpass
def filtrar_butterworth_bandpass(senal, Fs, FL, FH):
    butterworth_bandpass = signal.butter(4, [FL, FH], btype='band', analog=False, fs=Fs, output='ba')
    senal_filtrada = lfilter(butterworth_bandpass[0], butterworth_bandpass[1], senal)
    return senal_filtrada

# Función para aplicar el filtrado FIR
def filtrar_fir(senal, Fs, fc1, fc2, orden):
    filtro_fir = firwin(orden + 1, [fc1, fc2], pass_zero=False, fs=Fs, window='hamming')
    senal_filtrada = lfilter(filtro_fir, 1, senal)
    return senal_filtrada

# Procesar y plotear señales sin filtrar
t_ecg, signalecg = cargar_y_procesar_senal("daniel-brazo.txt", 5, 1000, 3000)
plotear_senal(t_ecg, signalecg, "Señal ECG - Sin Filtrar")

t_emg, signalemg = cargar_y_procesar_senal("piero-brazo.txt", 5, 100, 300)
plotear_senal(t_emg, signalemg, "Señal EMG - Sin Filtrar")

t_eeg, signaleeg = cargar_y_procesar_senal("taco-brazo.txt", 5, 1000, 3000)
plotear_senal(t_eeg, signaleeg, "Señal EEG - Sin Filtrar")

# Filtrar señales con Wavelet
umbral_wavelet = 0.022
wavelet_name_ecg = 'db9'
senal_filtrada_ecg = filtrar_wavelet(signalecg, umbral_wavelet, wavelet_name_ecg)
plotear_senal(t_ecg, senal_filtrada_ecg, "Señal ECG - Filtro Wavelet (db9)")

umbral_wavelet_emg = 0.022
wavelet_name_emg = 'db6'
senal_filtrada_emg = filtrar_wavelet(signalemg, umbral_wavelet_emg, wavelet_name_emg)
plotear_senal(t_emg, senal_filtrada_emg, "Señal EMG - Filtro Wavelet (db6)")

umbral_wavelet_eeg = 0.022
wavelet_name_eeg = 'sym3'
senal_filtrada_eeg = filtrar_wavelet(signaleeg, umbral_wavelet_eeg, wavelet_name_eeg)
plotear_senal(t_eeg, senal_filtrada_eeg, "Señal EEG - Filtro Wavelet (sym3)")

# Filtrar señales con Butterworth Bandpass
FL_ecg = 0.5
FH_ecg = 40
senal_filtrada_ecg = filtrar_butterworth_bandpass(signalecg, 1000, FL_ecg, FH_ecg)
plotear_senal(t_ecg, senal_filtrada_ecg, "Señal ECG - Filtro Butterworth Bandpass")

FL_emg = 20
FH_emg = 500
senal_filtrada_emg = filtrar_butterworth_bandpass(signalemg, 100, FL_emg, FH_emg)
plotear_senal(t_emg, senal_filtrada_emg, "Señal EMG - Filtro Butterworth Bandpass")

FL_eeg = 0.5
FH_eeg = 50
senal_filtrada_eeg = filtrar_butterworth_bandpass(signaleeg, 1000, FL_eeg, FH_eeg)
plotear_senal(t_eeg, senal_filtrada_eeg, "Señal EEG - Filtro Butterworth Bandpass")

# Filtrar señales con FIR
fc1_eeg = 0.5
fc2_eeg = 50
orden_fir_eeg = 56
senal_filtrada_eeg = filtrar_fir(signaleeg, 1000, fc1_eeg, fc2_eeg, orden_fir_eeg)
plotear_senal(t_eeg, senal_filtrada_eeg, "Señal EEG - Filtro FIR (Hamming)")

fc1_emg = 0.5
fc2_emg = 50
orden_fir_emg = 1000
senal_filtrada_emg = filtrar_fir(signalemg, 100, fc1_emg, fc2_emg, orden_fir_emg)
plotear_senal(t_emg, senal_filtrada_emg, "Señal EMG - Filtro FIR (Hamming)")

fc1_ecg = 0.5
orden_fir_ecg = 56
senal_filtrada_ecg = filtrar_fir(signalecg, 1000, fc1_ecg, fc2_ecg, orden_fir_ecg)
plotear_senal(t_ecg, senal_filtrada_ecg, "Señal ECG - Filtro FIR (Hamming)")


y = signaleeg
Fs = 1000


mean_y = np.average(y)
std_y = np.std(y)
#max
max_samp_val = np.max(y)
#min
min_samp_val = np.min(y)
#rms
rms = np.sqrt(np.sum(y*y))/len(y)

#area
area = np.trapz(y, dx=1/Fs)

time_param = {"Maximum EMG": max_samp_val, "Minimum EMG": min_samp_val,
              "Average EMG": mean_y, "Standard Deviation EMG": std_y, "RMS EMG": rms, "Area EMG": area}
print(time_param)
