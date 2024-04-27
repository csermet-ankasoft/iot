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
int ppm;

//Define
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
SoftwareSerial BTserial(TX, RX); 

void setup() 
{
  Serial.begin(9600);
  dht.begin();
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
    if (readString == "send"){
      hum = dht.readHumidity();
      temp= dht.readTemperature();
      ppm= analogRead(AOUTpin); 

      BTserial.print("Humidity: ");
      BTserial.print(hum);
      BTserial.print("%, Temperature : ");
      BTserial.print(temp);
      BTserial.print(" C° ");
      BTserial.print(" Air Quality: ");  
      BTserial.print(ppm); 
      BTserial.print("ppm.");
      BTserial.println("end;");
    }
    readString = "";
  } 
  ppm= (analogRead(AOUTpin)*1.25); 
  //BTserial.print(ppm); 
  //BTserial.println("ppm.");
  delay(200);
}