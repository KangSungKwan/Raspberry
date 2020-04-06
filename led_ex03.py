import RPi.GPIO as GPIO
import time

ledPin = 12
buttonPin = 16
light_on = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def button_callback():
	#global light_on
	if light_on == False:
		GPIO.output(ledPin, 1)
		print("LED ON")
	else:
		GPIO.output(ledPin, 0)
		print("LED OFF")
	light_on = not light_on
	
GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=button_callback, bouncetime=300)
      
while 1:
	time.sleep(0.1)
     
