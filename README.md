# Tarea4

## Parte 1

Para crear un esquema de modulación BPSK para los bits presentados, lo primero que se realiza es la forma de onda de la portadora. Esta portadora posee una forma sinusoidal, con frecuencua de 5000 Hz y amplitud unitaria. La forma de inda de la portadora se puede observar en "Portadora.png".

Luego se le asigna una onda sinusoidal normalizada para cada bit. Como se esta realizando modulación BPSK, para los bits que tengan un valor de 1 se les asigan una onda seno y para los bits que tengan valor de 0 se le asigna una onda seno defasada 180 (-seno).

En la gráfica de la figura "Transmitida.png" se puede ver la forma de onda para la señal transmitida tomando en cuenta solo 5 bits, donde se puede observar con claridad los bits que valen 1 y los bits que valen 0.

## Parte 2

Para calcular la potencia promedio de de la señal modulada, se calcula primero la potencia instantánea. La potencia instantánea se puede calcular fácilmente al elevar la señal analizada al cuadrado. La potencia promedio se calcula al integrar la potencia instantánea durante todo el intervalo de tiempo y dividirlo entre el perido. Al realizar lo anterior, se obtiene que la potencia promedio tiene un valor de 0.4875 W.

## Parte 3

En esta sección, se realiza un simulación de ruido aditivo blanco gaussiano o AWGN. En este caso, a la señal transmitida se le agrega ARGN con una relación señal ruido (SNR) desde -2 hasta 3 dB. Este ruido se el añade a la señal para  al calcular con la relación señal ruido el valor de la desviación estándar.

La relación señal ruido es SNRdB = 10log(Ps/Pn), donde Ps es la potencia de la señal y Pn es la potencia del ruido. A partir del valor de Pnse puede calcular el valor de la desviación estándar (sigma) como: sigma = sqrt(Pn). Al realizar todo lo anterior, se obtiene un sigma para cada valor de SNRdB. En la figura ""Recibida.png" se puede observar la señal que se recibiría al agregarle un SNR de -2 dB.

## Parte 4

A partir del método de Welch con SciPy, se grafican la densidad espectral para la potencia de la señal antes y después del ruido. En estas gráficas se presentan en las figuras "AntesDelCanalRuidoso" y "DespuesDelCanalRuidoso", y se puede observar en estas que antes del ruido se pueden identificar varias componentes de potencia con facilidad a lo largo de la frecuencia. En cambio para la señal después del ruido solo se puede identificar la primera componente de potencia, mientras que las otras son indetectables.

## Parte 5

Para demodular y decodificar la señal, se multiplica la señal recibida por seno para obtener el valor de potencia. Esto se hace para detectar la energía de todo los bits e identificar cual es cero y cual es 1. En este caso, se toma que un valor de la energía de la onda original (Es = sim(sin^2)) dividido entre 2, significa que está llegando un bit de valor 1. Esto se hace así para poder identificar de un forma razonable el bit si se presenta una enorme cantidad de ruido. Para valores que no cumplen lo anterior, se toma un valor de cero.

Con los bits ya contados, se calcula el error con respecto a los bits original y con esto se calcula la tasa de error por bits (BER). Para el caso de SNR= -2 dB, se obtiene 32 errores en 10000 bits con un BER de 0.0032. Conforme se aumenta los dB, el valor del BER se aproxima a cero, donde para 3 dB se obtiene 0 errores y un BER de 0.

## Parte 6

A partir de los resulatados anteriores, se grafica una curva de BER vs SNR, la cual se muestra en la figura "BErvsSNR.png". En esta curva se puede observar como disminuye el valor de BER al aumentar el valor de SNR.



