import RPi.GPIO as GPIO
import time
import picamera
import os
import sys
from PIL import Image

clr = lambda:os.system("clear")
    
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(4,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(21,GPIO.OUT)
camera = picamera.PiCamera()

cond = 1
safe = 0
acao = 1
nop = 0

p = GPIO.PWM(21,50)
p.start(10.5)

clr()
print("Programa ativado, aguardando captura")

try:
    
    while acao != 3:
        while nop == 0:
            cond = GPIO.input(4)
            if cond == 1:
                safe = GPIO.input(22)
                if safe == 0:
                    clr()
                    print("Especime capturado!\n")
                    p.ChangeDutyCycle(1.5)
                    camera.resolution = (1920, 1080)
                    camera.rotation = 180
                    camera.start_preview()
                    time.sleep(2)
                    camera.capture('/home/pi/Modelos/fotos/captura.jpeg')
                    camera.stop_preview()
                    nop = 1
                cond = 1
        print("Opcoes:\n1 - Abrir gaiola\n2 - Capturar nova imagem\n3 - Encerrar")
        acao = input()
        if acao == 1:
            clr()
            nop = 0
            p.ChangeDutyCycle(10.5)
            print("A gaiola foi aberta e o programa esta rodando novamente")
        if acao == 2:
            clr()
            camera.start_preview()
            camera.rotation = 180
            time.sleep(2)
            camera.capture('/home/pi/Modelos/fotos/captura.jpeg')
            camera.stop_preview()
            print("Uma nova foto foi tirada")
    clr()
    print("Programa encerrado")
    sys.exit()

except KeyboardInterrupt:
    p.stop()
    
    GPIO.cleanup()


        
        




