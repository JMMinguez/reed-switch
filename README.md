# P6-ReedSwitch

## Introducción
El objetivo de esta práctica es unificar nuestros conocimientos ya aprendidos con lo eventos junto con un sensor nuevo. Para esta práctica, nos basaremos en los programas creados en la [práctica p3](https://github.com/clases-julio/p3-interruptions-rsanchez2021) donde teníamos dos interruptores y dos leds.

## Circuito y componentes
Para crear el circuito se ha utilizado una resistencia en *pull up* para así poder utilizar un pin GPIO para comprobar el estado del interruptor. La organización **pull up** se basa en polarizar el voltaje de fuente, de esta forma cuando el pulsador esta abierto o en reposo, el voltaje en la entrada será de 5V. Cuando el pulsador es presionado, la corriente circula por la resistencia y luego por el pulsador, de esta forma tenemos que el voltaje en la entrada es de Tierra o 0V. Esto se 
traduce en que cuando el pulsador está en reposo lee 1 y cuando "presionamos" leerá 0. Para más información os recomendamos esta [página web](https://naylampmechatronics.com/blog/39_resistencias-pull-up-y-pull-down.html) que nos ha servido para crear el circuito y de donde hemos sacado la siguiente foto explicativa:

![Pull up](https://github.com/rsanchez2021/Image/blob/main/pull_up.PNG)

Componentes utilizados:
- Resistencia 10K Ω
- Resistencia 220 Ω
- Led verde
- [Reed switch](https://standexelectronics.com/wp-content/uploads/OKI_Reed_Switch_ORD213.pdf)

El circuito se queda pues:

![circuito p6 sensores](https://github.com/rsanchez2021/Image/blob/main/p6_bb_terminado.png)

## Ejercicio

Primero de todo nos pide un programa que muestre constantemente el estado del interruptor, lo primero que hicimos fue hacerlo con inputs pero no terminaba de ser muy eficiente. El primer programa se queda así:
```python
while True:
  input = GPIO:input(PIN_SITCH)
  print (input)
  time.sleep(1)
```

Finalmente, para realizar el código decidimos utilizar el comando add_event_detect pues nos permite realizar mientras tanto otras cosas y así no cargar mucho el procesador. Una vez se ha detectado que se ha "pulsado" el interruptor, el callback controla si se ha soltado o no. 

```python
def callbackBotonPulsado (canal):
    pulsado = False
    while True:
        #Si el switch está activo
        if not GPIO.input(PIN_SWITCH):
            if not pulsado:
                print("Puerta cerrada")
                GPIO.output(LED_VERDE, GPIO.HIGH)
                pulsado = True 
        else:
            pulsado = False
            GPIO.output(LED_VERDE, GPIO.LOW)
            continue
```

Finalmente, como algo importante e interesante, hay veces que el led se activa cuando se aleja el imán y no tendría, esto se debe al rebote que hacen las lenguetas al juntarse y separarse.
