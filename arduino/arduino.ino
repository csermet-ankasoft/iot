
//Libraries
#include <SoftwareSerial.h>
#include <DHT.h>

//Constants
#define DHTPIN 2 
#define DHTTYPE DHT22  
#define AOUTpin A1   // MQT-135
#define RX 4   
#define TX 3   

//Variables
float hum;  //Stores humidity value
float temp; //Stores temperature value
int airQuality;
int FanLOW = 8;
int FanHIGH = 9;
int ConA = 10;// PWM DI/DO
int fanSpeed = 100;

//Define
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
SoftwareSerial BTserial(TX, RX); 

void runFan(int speed)
{
  digitalWrite(FanLOW, LOW); 
  digitalWrite(FanHIGH, HIGH);
  analogWrite(ConA, speed);
}

void setup() 
{
  Serial.begin(9600);

  //FAN
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);  
  pinMode(10, OUTPUT);

  //Sensors
  dht.begin();
  dht.readHumidity();
  BTserial.begin(9600);

  Serial.println("Ready");    
}

String readString;
void loop()
{
  delay(200);
  
  while (BTserial.available())
  {
    delay(3);  
    char c = BTserial.read();
    readString += c;
  }
  readString.trim();

  if (readString.length() >0) {
    Serial.println(readString);
    if (readString == "status"){
      hum = dht.readHumidity();
      temp = dht.readTemperature();
      airQuality = (analogRead(AOUTpin) * 1.25);

      BTserial.print("Humidity: ");
      BTserial.print(hum);
      BTserial.print("%, Temperature : ");
      BTserial.print(temp);
      BTserial.print(" C° ");
      BTserial.print(" Air Quality: ");  
      BTserial.print(airQuality); 
      BTserial.print("ppm.");
      BTserial.println("end;");
    }
    else if (readString == "getHumidity"){
      delay(200);
      hum = dht.readHumidity();
      BTserial.print(hum, 1);
      BTserial.print(";");
    }
    else if (readString == "getTemperature"){
      delay(200);
      temp = dht.readTemperature();
      BTserial.print(temp, 1);
      BTserial.print(";");
    }
    else if (readString == "getAirQuality"){
      delay(200);
      airQuality = (analogRead(AOUTpin)*0.125); 
      BTserial.print(airQuality);
      BTserial.print(";");
    }
    else if(readString.startsWith("fan"))
    {
      fanSpeed = readString.substring(3,7).toInt();
    }
    readString = "";
  }

  runFan(fanSpeed);
}