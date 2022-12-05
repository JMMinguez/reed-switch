#------------------------------
#Ejercicio: Práctica p6 sensores y actuadores --> Reed switch
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 7/12/22
#Objetivo: conocer el estado del interruptor en todo momento
#------------------------------

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#establecer pines
PIN_SWITCH = 15
LED_VERDE = 14
	      
#establecer saslidas y entradas
GPIO.setup(PIN_SWITCH, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_VERDE, GPIO.OUT)

while True:
	input = GPIO.input(PIN_SWITCH)
	print (input)
	time.sleep(1)
