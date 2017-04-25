/*************************************************
 * Project: Sticky Robot
 * File: motor_control
 * Author: Héloïse Boross
 * Last update: 20.04.2017
 *************************************************/

// note: changer digital en analog




//#include <PinChangeInterrrupt.h>
//#include <ros.h>
#include "SimpleTimer.h"

#define M1_PWM 2
#define M1_EN 3
#define M2_PWM 4
#define M2_EN 5
#define CONV_PWM 6
#define CONV_EN 7
#define ENC1_A 18 
#define ENC1_B 19
#define ENC2_A 24
#define ENC2_B 25
#define ENCC_A 26
#define ENCC_B 27

#define IMPULSION 48 //number of impulsion per round of the motor C?EST PEUT ETRE 12 PLUTOT...
#define REDUCTION 172 //reduction applied on the motor

#define R_WHEEL 75 //in mm

#define CONV_LOAD_SPEED 30
#define CONV_RELEASE_SPEED 40
#define MAX_SPEED 95 //normalement 95
#define STOP 0
#define LEFT 0
#define RIGHT 1

#define FREQ_SAMPLING 20

SimpleTimer timer; // Timer pour échantillonnage

unsigned int time = 0;

const int sampling_freq = 20;

int encoder1_pos = 0; //float marche mal mais ne devreit pas....
volatile unsigned int encoder2_pos = 0;
volatile unsigned int encoder3_pos = 0;

//remarque: changer cette façon de faire... car il faut 3x...
boolean Enc1_A_set = false;
boolean Enc1_B_set = false;


void setup()
{
  Serial.begin(9600);
  
  pinMode(M1_PWM,OUTPUT);
  pinMode(M1_EN,OUTPUT);
  pinMode(CONV_PWM, OUTPUT);
  pinMode(M2_PWM,OUTPUT);
  pinMode(M2_EN,OUTPUT);
  pinMode(CONV_EN, OUTPUT);

  pinMode(ENC1_A, INPUT);
  pinMode(ENC1_B, INPUT);
  pinMode(ENC2_A, INPUT);
  pinMode(ENC2_A, INPUT);
  pinMode(ENCC_A, INPUT);
  pinMode(ENCC_A, INPUT);
  digitalWrite(ENC1_A, HIGH);  // Resistance interne arduino ON
  digitalWrite(ENC1_B, HIGH); 
  digitalWrite(ENC2_A, HIGH);
  digitalWrite(ENC2_B, HIGH);
  digitalWrite(ENCC_A, HIGH);
  digitalWrite(ENCC_B, HIGH); 

  attachInterrupt(0, gestionInterruptEnc1A, CHANGE); // Interruption de l'encodeur 1 en sortie 0 (pin 2)
  attachInterrupt(1, gestionInterruptEnc1B, CHANGE); // Interruption de l'encodeur 1 en sortie 1 (pin 3)
/*  attachInterrupt(0, gestionInterruptEnc2, CHANGE); 
  attachInterrupt(1, gestionInterruptEnc2, CHANGE);
  attachInterrupt(0, gestionInterruptEncc, CHANGE); 
  attachInterrupt(1, gestionInterruptEncc, CHANGE);*/

  stopMoving();
  
  delay(100);

  timer.setInterval(1000/sampling_freq, tryMotorsETC);
}

/*void makeMotorTurn(int motor_number, int motor_speed) //dist à parcourir est en mm
{
   float req_rounds;
   
   if(motor_number == CONVEYOR_BELT)
      req_rounds = distance/14;
   else
      req_rounds = distance/150;
  
}*/

void stopMoving()
{
  digitalWrite(M1_PWM, STOP);
  digitalWrite(M2_PWM, STOP);

}

void moveForward(int motor_speed)
{
  if(motor_speed > MAX_SPEED)
      motor_speed = MAX_SPEED;
  if(motor_speed < 0)
      motor_speed = 0;
      
  analogWrite(M1_PWM, motor_speed);
  digitalWrite(M1_EN, LOW);
  digitalWrite(M2_PWM, motor_speed);
  digitalWrite(M2_EN, LOW);
}

void moveBackward(int motor_speed)
{
   if(motor_speed > MAX_SPEED)
      motor_speed = MAX_SPEED;
  if(motor_speed < 0)
      motor_speed = 0;
      
  analogWrite(M1_PWM, motor_speed);
  digitalWrite(M1_EN, HIGH);
  digitalWrite(M2_PWM, motor_speed);
  digitalWrite(M2_EN, HIGH);
}

void loadBottle()
{  
  digitalWrite(CONV_PWM, CONV_LOAD_SPEED);
  digitalWrite(CONV_EN, LOW);
}

void releaseBottle()
{  
  analogWrite(CONV_PWM, CONV_LOAD_SPEED);
  digitalWrite(CONV_EN, HIGH);
}

void turn(int motor_speed, int degree_rotation, int rot_direction)
{
  if(motor_speed > MAX_SPEED)
      motor_speed = MAX_SPEED;
  if(motor_speed < 0)
      motor_speed = 0;
      
  
  if(rot_direction == LEFT)
  {
    digitalWrite(M1_EN, HIGH);
    digitalWrite(M2_EN, LOW);
  }
  else
  {
    digitalWrite(M1_EN, LOW);
    digitalWrite(M2_EN, HIGH);
  }
  
  analogWrite(M1_PWM, motor_speed);
  analogWrite(M2_PWM, motor_speed);
  
}

void tryMotorsETC()
{
  float angular_pos1  = (float)encoder1_pos/IMPULSION/REDUCTION*360;
  //float angular_pos1  = encoder1_pos/IMPULSION*360;
  float distance_wheel1 = angular_pos1*3.14156/180*R_WHEEL;
  int given_dist = 10; //just for testing
  int given_dist2 = 10;
  
  time += sampling_freq;

//  while(distance_wheel1 < given_dist)
    moveForward(50);
//  delay(1000);
//  stopMoving();
 // delay(3000);

 // while(distance_wheel1 < given_dist2)
//    moveBackward(50);
//  delay(10000);

  Serial.print(Enc1_A_set);  
  Serial.print("encodeur pos = ");
  Serial.print(encoder1_pos);
  Serial.print(" ; ");
  Serial.print("angle deg = ");
  Serial.print(angular_pos1);
  Serial.print(" ; ");
  Serial.print("distance = ");
  Serial.print(distance_wheel1);
  Serial.print(" ; ");
  Serial.print("\n");
  //Serial.print("vitesse moteur = ");
  //Serial.println(vitMoteur);
}


void gestionInterruptEnc1A() // Interruption appelée à tous les changements d'état de A
{
  Enc1_A_set = digitalRead(ENC1_A) == HIGH;

  encoder1_pos += (Enc1_A_set != Enc1_B_set) ? -1 : +1; //modifie le compteur selon les deux états des encodeurs
}

void gestionInterruptEnc1B()
{
  Enc1_B_set = digitalRead(ENC1_B) == HIGH;

  encoder1_pos += (Enc1_A_set == Enc1_B_set) ? -1 : +1; //modifie le compteur selon les deux états des encodeurs
}



void loop()
{
//  Serial.print("begin ");
   timer.run(); 

}
