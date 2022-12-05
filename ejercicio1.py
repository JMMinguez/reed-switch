#------------------------------
#Ejercicio: Práctica p6 sensores y actuadores --> Reed switch
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 7/12/22
#Objetivo: conocer el estado del interruptor en todo momento
#------------------------------
#!/usr/bin/python

import RPi.GPIO as GPIO
import time


#establecer pines
PIN_SWITCH = 15
LED_VERDE = 14
BOUNCETIME= 100

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


if __name__=='__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PIN_SWITCH, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(LED_VERDE, GPIO.OUT)
    GPIO.output(LED_VERDE, GPIO.LOW)
    GPIO.add_event_detect(PIN_SWITCH, GPIO.FALLING,callback=callbackBotonPulsado, bouncetime = BOUNCETIME)
	
    while True:
        time.sleep(0.1)
		
if __name__=="__main__":
    main()
		
		
		
		
		
