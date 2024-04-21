//Libraries
#include <SoftwareSerial.h>
#include <DHT.h>

//Constants
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
#define AOUTpin A4   // DHT 22  (AM2302)
#define RX 4   // DHT 22  (AM2302)
#define TX 3   // DHT 22  (AM2302)

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
  delay(10);
  
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

}