# Tarea 4
# Jorge Luis Sancho Chaverri
#B77150

import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt
import csv

bits = np.genfromtxt('bits10k.csv',delimiter=',')

#Parte 1

#Frecuencia de la portadora
f = 5000 #Hz

#Duración del periodo de cada símbolo
T = 1/f #ms

#Número de puntos de muestreo por periodo
p = 40

#Puntos de muestro para cada periodo
tp = np.linspace(0, T, p)

#Forma de onda de la portadora
sin = np.sin(2*np.pi*f*tp)

#Visualización de la forma de onda de la portadora
plt.plot(tp, sin)
plt.xlabel('Tiempo/s')
plt.savefig('Portadora.png')

#Frecuencia de muestreo
fs = p/T #kHz

#Línea temporal para toda la señal transmitida
t = np.linspace(0, len(bits)*T, len(bits)*p)

#Inicializar el vector de la señal
senal = np.zeros(t.shape)

#Creación de la señal modulada
for k, b in enumerate(bits):
    if b == 1:
        senal[k*p:(k+1)*p] = sin
    else:
        senal[k*p:(k+1)*p] = -sin

#Visualizacion de los primeros bits modulados
pb = 5
plt.figure()
plt.plot(senal[0:pb*p])
plt.savefig('Transmitida.png')

#Parte 2

#Se calcula la potencia instantánea
Pi = senal**2

print('La potencia instantánea es de:', Pi)

#Se calcula la potencia promedio a apartir de la instantánea
Ps = integrate.trapz(Pi, t)/(len(bits)*T)

print('La potencia promedio es de:', Ps)
#Parte 3

#Intervalo de SNR deseado
SNR = np.linspace(-2, 3, 6)
matriz = [] #Para acceder a un valor matriz[SNR][0][Valor de Rx]
for i in range(len(SNR)):
    # Potencia del ruido para SNR y señal dadas
    Pn = Ps / (10**(SNR[i]/10))
    #Desviación estándar del ruido
    sigma = np.sqrt(Pn)
    #Creación del ruido
    ruido = np.random.normal(0, sigma, senal.shape)
    #Simulación del canal
    matriz.append([])
    Rx = senal + ruido
    matriz[i].append(Rx)


#Visualizacion de los primeros bits recibidos
pb = 5
plt.figure()
plt.plot(matriz[0][0][0:pb*p]) #{Para SNR = -2 dB}
plt.savefig('Recibida.png')


#Parte 4

# Antes del canal ruidoso
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('AntesDelCanalRuidoso.png')

# Después del canal ruidoso
fw, PSD = signal.welch(matriz[0][0], fs, nperseg=1024) #Para SNR = -2
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig('DespuesDelCanalRuidoso.png')

#Parte 5
# Pseudo-energía de la onda original (esta es suma, no integral)
Es = np.sum(sin**2)
print('La energía de la onda original es:', Es)
matriz2 = [] #Matriz con los valores de BER

#Se calculan los valores para BER
for i in range(len(SNR)):
    matriz2.append([])
    bitsRx = np.zeros(len(bits))
    for k, b in enumerate(bits):
        #Calculo del valor de potencia por bit
        Ep = np.sum(matriz[i][0][k*p:(k+1)*p] * sin)
        if Ep > Es/2: #Se consideran valores mayores a 9.75 como positivos y el bit como 1
            bitsRx[k] = 1
        else: #Si no son mayores a 9.75, el valor se considera negativo y el bit como 0
            bitsRx[k] = 0
    #Se calcula el error de bits
    err = np.sum(np.abs(bits - bitsRx))
    #Se calcula la tasa de error de bits (BER)
    BER = err/len(bits)
    print('Hay un total de {} errores en {} bits para una tasa de error de {}.'.format(err, len(bits), BER))
    matriz2[i].append(BER)

#Parte 6
#Se grafica BER vs SNR
plt.cla()
plt.figure()
plt.title('Gráfica BER vs SNR')
plt.ylabel('$BER$')
plt.xlabel('$SNR$')
plt.plot(SNR, matriz2)
plt.savefig('BERvsSNR.png')
