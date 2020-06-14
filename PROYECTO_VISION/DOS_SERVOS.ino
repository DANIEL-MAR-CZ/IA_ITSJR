// Daniel Margarito Cruz
//vision artificial

#include<Servo.h>

#define SER1 9 //Pin para el servo X PAN
#define SER2 10 //Pin para el servo Y TIL
//Creamos los objetos servo
Servo servo1; //X
Servo servo2; //Y
 
int enviado; //Aqui enviamos el numero completo
int num; //Numero del servo
int posicion; //Posicion del servo
 
void setup()
{
  //Inicializamos los Servos
  servo1.attach(SER1); //Pin para el servo X PAN
  servo2.attach(SER2); //Pin para el servo Y TIL
  
  //Inicializamos la comunicacion por Serial
  Serial.begin(9600);
}
 
void loop()
{
  if(Serial.available() >= 1)
  {

    enviado = Serial.parseInt(); //Leer entero por serial
    num = enviado%10; // Extraer el num del motor
    enviado = enviado/10; //Dividir el entero entre 10
    posicion = enviado; //Guardar el angulo
     
    //Hora de mover los servos!
    
    if(num == 1)  //Pin para el servo X PAN
    {
      servo1.write(posicion);
    }
    else if(num == 2)  //Pin para el servo Y TIL
    {
      servo2.write(posicion);
    }
  }
 
}
