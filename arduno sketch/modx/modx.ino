#include <DHT.h>

//=========================================================================
const int SensorHumedadPin = A0;
int analgoValue; //  A3 -----   0 -- 1023 LLUvia
const int AnalogInpin = A1; //0 -- 1023 sensor de PH
int MedidorAguapin = A2;  // MEDIDOR DE AGUA DE LLUVIA
//=========================================================================
int sensorValue = 0;
int val = 0; // VARIABLE PARA EL MEDIDOR DE AGUA
unsigned long int avgValue;
float b;
int buf[10], temp; // pH 
//byte led= 13;  // LED ROJO PARA MOSTRAR ALERTAS
//byte led2= 12; // LED AZUL PARA INDICAR QUE ESTA OK
bool digitalValue;

//=========================================================================
const int Trigger = 7;
const int Echo  = 6;
int DataTemp = 5;
int Temp, humedad;
float X ; // VARIABLE QUE CONTIENE LOS VALORES DE CONDUCTIVIDAD EN μSiemens / cm o ml Siemens/cm
int Z;   // PORCENTAJE DE LA SALINIDAD


DHT dht(DataTemp, DHT11);


//=========================================================================

void setup() {

  Serial.begin(9600);
  //pinMode(led, OUTPUT);
  //pinMode(led2, OUTPUT);
  pinMode(MedidorAguapin, INPUT);
  pinMode(Trigger, OUTPUT); //pin como salida
  pinMode(Echo, INPUT);  //pin como entrada
  digitalWrite(Trigger, LOW);//Inicializamos el pin con 0
  dht.begin();

}


//=========================================================================

void loop() 
{
  int Arturin = 0;

  while (Arturin < 6)
  {
    Serial.println(AnalogInpin);
    //Serial.println("VICTORIA");
    
    if (AnalogInpin >= 15)
      {
        Serial.println("Sensor pH desconectado ");
      }
    else
      {
        for(int i = 0; i<10; i++)
        {
          buf[i] = analogRead(AnalogInpin);
          delay(10);
        }
        for(int i = 0; i<9; i++)
        {
          for(int j =i+1;j<10;j++)
          {
            if (buf[i] > buf[j])
            {
              temp = buf[i];
              buf[i] = buf[j];
              buf[j] = temp;
            }
          }
        }
        avgValue = 0;
        for (int i=2;i<8;i++)
        avgValue +=buf[i];
      
        
        long t; //timepo que demora en llegar el eco
        long d; //distancia en centimetros
        
        float pHVol = (float)avgValue*5.0/1024/6;
        float pHValue = -5.70* pHVol + 21.34;
      
        //=========================================================================
    
        int Humedad_salinidad = analogRead (SensorHumedadPin); 
        digitalWrite(Trigger, HIGH);
        delayMicroseconds(10);          //Enviamos un pulso de 10us
        digitalWrite(Trigger, LOW);
        t = pulseIn(Echo, HIGH); //obtenemos el ancho del pulso
        d = t/59;             //escalamos el tiempo a una distancia en cm
        humedad = dht.readHumidity();
        Temp = dht.readTemperature();
        
      
        //=========================================================================
        analgoValue = analogRead(3);
        MedidorAguapin = analogRead(2);
        int num =  (analgoValue);
        val = analogRead (MedidorAguapin);
        
      
      //================================== evalua si el nivel de ph es optimo
      /* 
       *  1- nivel de ph
       *  2- salinidad
       *  3- temperatura
       *  4- humedad ambiental
       *  5- nivel del agua
       *  6- lluvia
      */
      
        //Serial.println("- NIVEL DE pH: ");
        Serial.println (pHValue);
        
        //slinidad-----------------------------------------------
        
        float Y = 1.43457;  // FACTOR DE CONVERSION PARA LA SALINIDAD :v
        int Y1 ; // PORCENTAJE DE HUMEDAD
        Serial.println("------ ");
        X =  (Humedad_salinidad *0.5)/1000; // GUARDAMOS VALORES DE LA CONDUCTIVIDAD A PARTIR DE LA HUMEDAD
        float SAL = (Humedad_salinidad - X) * Y ;
        Z = map (SAL, 0, 1023, 100, 0); // PORCENTAJE DE SALINIDAD APARTIR DE LA FUNCION MAP
        Serial.println(Z);
        //Serial.println("%");
    
        
        Serial.println("------ ");
        
        //-------------------------------------------------------
    
        Serial.println(Temp);
        //Serial.println("C° temperatura");
    
        //Y1 =  map (Humedad_salinidad, 0, 1023, 100, 0) ; // PORCENTAJE DE HUMEDAD APARTIR DE LA FUNCION MAP
        //Serial.print(Y1);
        //Serial.println("%");
    
    
        
        
        //Serial.print("humedad:  ");
        Serial.println(humedad);
        //Serial.println("%");
        
        //Serial.println("- NIVEL DE AGUA");
        Serial.println(d);
        //Serial.println("cm");
        
        //Serial.println("- NIVEL DE LLUVIA: ");
        Serial.println(num);
    
        Arturin = Arturin + 1;
    
        delay(5000);  // AQUIESPERA 5 SEGUNDOS PARA QUE DE NUEVO EL LOOP SIGA
    }
    
    delay(10000);  

  }
}


  
  
