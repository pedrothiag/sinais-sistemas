import numpy as np
from numpy.fft import fft, fftshift
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

#Cria uma funcao que retorna a estimativa para a transformada de Fourier em tempo contínuo de um sinal
def ctfs (x,Ts):
    Xk = (1/Ts)*fftshift(fft(x))
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

#Cria o sinal de mensagem e portadora
fm = 100
fc = 500
mesg = np.cos(2*np.pi*fm*t)
carrier = np.cos(2*np.pi*fc*t)

#Plot do sinal de mensagem e de portadora
plt.figure()
plt.subplot(211)
plt.plot(t,mesg)
plt.xlim(timeView_start,timeView_end)
plt.title('Mensagem')
plt.xlabel('t (segundos)')
plt.subplot(212)
plt.plot(t,carrier)
plt.xlim(timeView_start,timeView_end)
plt.title('Portadora')
plt.xlabel('t (segundos)')
plt.tight_layout()

#Cria o sinal AM e calcula a sua transformada de Fourier
x = mesg*carrier
Xk, FreqAxis = ctfs(x,Ts)

#Plot do sinal modulado e do seu espectro de magnitude
plt.figure()
plt.subplot(211)
plt.plot(t,x)
plt.xlim(timeView_start,timeView_end)
plt.title('x(t)')
plt.xlabel('t (segundos)')
plt.subplot(212)
plt.plot(FreqAxis,np.abs(Xk))
plt.title('Magnitude')
plt.xlabel('Frequência (Hz)')
plt.tight_layout()

#Primeiro passo da demodulacao - Multiplicacao pela portadora
w = x*carrier

#Os codigos abaixo devem ser descontados caso deseje verificar o erro de estimacao da frequencia da portadora
#e da fase da portadora.
#w = x*np.cos(2*np.pi*fc*t + np.pi/3)        #Erro de fase. Se pi/2 --> não há sinal demodulado
#w = x*np.cos(2*np.pi*(fc + 2)*t)            #Erro de frequencia
Wk, FreqAxis = ctfs(w,Ts)

#Plot do sinal re-modulado e do seu espectro de magnitude
plt.figure()
plt.subplot(211)
plt.plot(t,w)
plt.xlim(timeView_start,timeView_end)
plt.title('w(t)')
plt.xlabel('t (segundos)')
plt.subplot(212)
plt.plot(FreqAxis,np.abs(Wk))
plt.title('Magnitude')
plt.xlabel('Frequência (Hz)')
plt.tight_layout()

#Parametros do Filtro Passa-baixas
fc = 150                    # frequência de corte
ordem = 10                  # ordem do filtro
fc_norm = fc / (Fs/2)       # frequência de corte normalizada
b, a = butter(ordem, fc_norm, btype='lowpass')  # cálculo dos coeficientes do filtro

# Aplicação do filtro
r = 2*filtfilt(b, a, w)
Rk, FreqAxis = ctfs(r,Ts)

#Plot do sinal demodulado e do seu espectro de magnitude
plt.figure()
plt.subplot(211)
plt.plot(t,r)
plt.xlim(timeView_start,timeView_end)
plt.title('r(t)')
plt.xlabel('t (segundos)')
plt.subplot(212)
plt.plot(FreqAxis,np.abs(Rk))
plt.title('Magnitude')
plt.xlabel('Frequência (Hz)')
plt.tight_layout()

#Plot do sinal demodulado e do sinal original
plt.figure()
plt.subplot(211)
plt.plot(t,mesg)
plt.xlim(timeView_start,timeView_end)
plt.title('Mensagem')
plt.xlabel('t (segundos)')
plt.subplot(212)
plt.plot(t,r)
plt.xlim(timeView_start,timeView_end)
plt.title('Recuperado')
plt.xlabel('t (segundos)')
plt.tight_layout()
plt.show()