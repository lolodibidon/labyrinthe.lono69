
'''Auteurs : Nojan Kaweh et Loïc Villaroge-Scheepers
    Contact 	: nojan.kwyh@eduge.ch et loic.vllrg@eduge.ch
    Licence 	: collégiens
    Librairie 	: https://github.com/lolodibidon/labyrinthe.lono69
    Date 	    : 26 mars 2025
    Version     : 1
    Description :
    '''


#    /''''^''''\
#   /  L1 M R1  \
#  |             |
#  |L2         R2|
# o|.............|o


from maqueen import *
from microbit import *
import utime

# Constantes
WHITE = 0
BLACK = 1

# Variable globale
Init = True

def followLine(speed:int, speed_slow:int):
    ''' Fonction qui teste si on est sur la bande noire et commande les moteurs droite et gauche.
        Permet de rester sur une bande noire.
        params :
          speed (int) : vitesse donnée au(x) moteur(s). Pour tourner, le moteur le moins rapide sera speed-35
    '''
    # On teste si les capteurs infrarouge frontaux L1 et R1 détecte la bande noire
    if line_sensor(LineSensor.R1)==BLACK and line_sensor(LineSensor.M) == WHITE:
        print("M")
        display.show(Image.HAPPY)
        motor_run(Motor.LEFT, speed_slow)
        motor_run(Motor.RIGHT, speed_slow)

    elif line_sensor(LineSensor.M) and line_sensor(LineSensor.R1)==BLACK:        
        display.show("G")
        print("G")
        motor_stop(Motor.LEFT)
        motor_run(Motor.RIGHT, speed)
        utime.sleep_ms(300)

    elif line_sensor(LineSensor.R2)==BLACK and line_sensor(LineSensor.R1)==WHITE:
        display.show("D")
        print("D")
        motor_run(Motor.LEFT, speed)
        motor_stop(Motor.RIGHT)
        
    elif line_sensor(LineSensor.R2)and line_sensor(LineSensor.R1)==BLACK:
        display.show("M")
        print("M")
        motor_run(Motor.LEFT, speed)
        motor_run(Motor.RIGHT, speed)

    utime.sleep_ms(50)

while True:
    if Init:
        # Vitesse maximale des moteurs (min:0, max:255)
        speed:int = 30   #50
        speed_slow:int = 20 #15

        display.show("2")
        utime.sleep_ms(3000)
        Init = False
       
    print(line_sensor(LineSensor.L2), line_sensor(LineSensor.L1), line_sensor(LineSensor.M),line_sensor(LineSensor.R1),line_sensor(LineSensor.R2))
    followLine(speed, speed_slow)


