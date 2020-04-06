import RPi.GPIO as GPIO
import time

ledPin = 12
buttonPin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1:
	if GPIO.input(buttonPin) == GPIO.HIGH:
		GPIO.output(ledPin, GPIO.HIGH)
	else:
		GPIO.output(ledPin, GPIO.LOW)
	time.sleep(0.1)
	
GPIO.cleanup()		
