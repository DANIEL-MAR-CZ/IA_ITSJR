#Proyecto vision artificial
#ITSJR
# Daniel Margarito Cruz 

#LINK VIDEO DEMO : https://youtu.be/10FoS20gjbw

#Materiales Vision Artificial
#Arduino UNO , 2 SERVOS SG90, CAMARA WEB, W7 python 3 LIBS Open cv inmutils pyserial time

#Importamos las librerias

from __future__ import print_function
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import os
import serial

#iniciamos el seial con el arduino
ardino = serial.Serial('COM10', 9600)


#define Servos X y Y GPIOS

panServo = 1  #X
tiltServo = 2  #Y

# initialize LED GPIO para cuando detecta el objeto
redLed = 21

#position servos 
def positionServo (servo, angle):
    an = str(angle)
    serv = str(servo)
    angulo = an + serv
    print("He enviado: " + str(angulo))
    time.sleep(1)
    ardino.write(str(angulo).encode())
    print("[INFO] Positioning servo at GPIO {0} to {1} degrees\n".format(servo, angle))
     

# posiciona el servo en el centro de la vision(frame) de la camara
def mapServoPosition (x, y):
    global panAngle
    global tiltAngle
    if (x < 220):
        panAngle += 10
        if panAngle > 140:
            panAngle = 140
        positionServo (panServo, panAngle)
 
    if (x > 280):
        panAngle -= 10
        if panAngle < 40:
            panAngle = 40
        positionServo (panServo, panAngle)

    if (y < 160):
        tiltAngle += 10
        if tiltAngle > 140:
            tiltAngle = 140
        positionServo (tiltServo, tiltAngle)
 
    if (y > 210):
        tiltAngle -= 10
        if tiltAngle < 40:
            tiltAngle = 40
        positionServo (tiltServo, tiltAngle)

# inicializa la camara
print("[INFO] waiting for camera to warmup...")
vs = VideoStream(0).start()
time.sleep(2.0)

# definimos el rango de colo que va a adetectar en HSV

colorLower = (24, 100, 100)
colorUpper = (44, 255, 255)

# Start with LED off

ledOn = False

# inicialiszamos  alineamos todo en 90 grados tanto  xY
global panAngle
panAngle = 90
global tiltAngle
tiltAngle =90

# mandamos pocisionar
positionServo (panServo, panAngle)
positionServo (tiltServo, tiltAngle)

# inicia el ciclo de captura de frame para la deteccion de colores
while True:
	#toma el siguiente fotograma de la transmisión de video y convierte a HSV e
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	frame = imutils.rotate(frame, angle=180)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#cra una máscara para el color del objeto
	#para eliminar cualquier mancha en la mascara
	
	mask = cv2.inRange(hsv, colorLower, colorUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	#busca contornos objeto establecido en la máscara para inicializar 
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	center = None

	# si se encontró al menos un contorno
	if len(cnts) > 0:
		
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		if radius > 10:
			# dibuja el círculo y el centroide en el marco,
			# actualiza la lista de puntos rastreados
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			
			# manda a posicionar los servoas al centro del frame
			mapServoPosition(int(x), int(y))
			
			if not ledOn:
				
				ledOn = True

	
	elif ledOn:
		
		ledOn = False

	# despliega la pantalla del frame caputado por la ccamara en el monitos
	cv2.imshow("Frame", frame)
	
	# salir del programa
	key = cv2.waitKey(1) & 0xFF
	if key == 27:
            break


print("\n [INFO] Exiting Program and cleanup stuff \n")
positionServo (panServo, 90)
positionServo (tiltServo, 90)

cv2.destroyAllWindows()
vs.stop()
