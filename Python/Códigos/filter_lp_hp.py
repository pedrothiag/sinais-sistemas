import numpy as np
from numpy.fft import fft, fftshift
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

#Cria uma funcao que retorna a estimativa para a transformada de Fourier em tempo contínuo de um sinal
def ctfs (x,Ts):
    Xk = fftshift(fft(x))
    FreqAxis = (1/Ts)*np.arange(-0.5,0.5,1/len(Xk))
    return Xk, FreqAxis

#Parametros de Simulacao. Passo = 1e-4. Tempo de simulacao = 1 segundo
Ts = 1e-4
Fs = 1/Ts
t = np.arange(0, 1.0, Ts)

#Parametros para visualizacao dos graficos no dominio do tempo. Como os sinais são de alta frequência, entao
#visualizado apenas uma pequena parte desses sinais
timeView_start = 0.05       #Tempo inicial para visualizacao
timeView_end = 0.1          #Tempo final para visualizacao
indexView_start = np.where(t == timeView_start)[0][0]       #Encontra no vetor t o index correspondente
indexView_end = np.where(t == timeView_end)[0][0]

#Cria o sinal, composto por uma componente de alta frequencia e outra de baixa frequencia.
f1 = 100
f2 = 500
x = np.cos(2*np.pi*f1*t) + np.cos(2*np.pi*f2*t)
Xk, FreqAxis = ctfs(x,Ts)

#Plot do sinal e do seu espectro
plt.figure()
plt.subplot(211)
plt.plot(t[indexView_start:indexView_end],x[indexView_start:indexView_end])
plt.title('x(t)')
plt.xlabel('t (segundos)')
plt.subplot(212)
plt.plot(FreqAxis,np.abs(Xk))
plt.title('X(\omega)')
plt.xlabel('Frequência (Hz)')
plt.tight_layout()

#Parametros do Filtro Passa-baixas
fc = 200                # frequência de corte
ordem = 10              # ordem do filtro
fc_norm = fc / (Fs/2)   # frequência de corte normalizada
b, a = butter(ordem, fc_norm, btype='lowpass')  # cálculo dos coeficientes do filtro
y1 = filtfilt(b, a, x)  #Filtragem
Y1k, FreqAxis = ctfs(y1,Ts) #Calcula o espectro

#Plot do sinal filtro passa-baixas e do seu espectro de magnitude
plt.figure()
plt.subplot(211)
plt.plot(t[indexView_start:indexView_end],y1[indexView_start:indexView_end])
plt.title('Sinal Filtrado Passa-Baixas')
plt.xlabel('t (segundos)')
plt.subplot(212)
plt.plot(FreqAxis,np.abs(Y1k))
plt.title('Magnitude')
plt.xlabel('Frequência (Hz)')
plt.tight_layout()

#Parametros do Filtro Passa-altas
fc = 200                # frequência de corte
ordem = 10              # ordem do filtro
fc_norm = fc / (Fs/2)   # frequência de corte normalizada
b, a = butter(ordem, fc_norm, btype='highpass')  # cálculo dos coeficientes do filtro
y2 = filtfilt(b, a, x)  #Filtragem
Y2k, FreqAxis = ctfs(y2,Ts) #Calcula o espectro

#Plot do sinal filtro passa-altas e do seu espectro de magnitude
plt.figure()
plt.subplot(211)
plt.plot(t[indexView_start:indexView_end],y2[indexView_start:indexView_end])
plt.title('Sinal Filtrado Passa-Altas')
plt.xlabel('t (segundos)')
plt.subplot(212)
plt.plot(FreqAxis,np.abs(Y2k))
plt.title('Magnitude')
plt.xlabel('Frequência (Hz)')
plt.tight_layout()
plt.show()