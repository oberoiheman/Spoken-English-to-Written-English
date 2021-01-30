# Spoken-English-to-Written-English

This is reusable python library which can be used to convert spoken english text into written english text.
It accounts for the following rules:
1. It can converts words to numbers such as hundred to 100.
2. It converts the word dollar/dollars to dollar sign i.e $ for example hundred dollars is converted to $100.
3. It accounts for the words such as double , triple etc and make the changes in text according to their literal meaning. such double five triple four changes to 55 444.
4. It also converts abbreviations such as p m  to pm.

This Library can be used by downloading the spoken_to_written.py file in your current working directory and importing it as follows :

## from spoken_to_written.py import *

The user should input the spoken english string:
## input_string = input("Enter Spoken English Text: ")
### Enter Spoken English Text: Hey my name is Alexa, the current time is four p m , my contact number is quadruple five and i earn two million dollars per annum.

The Convert function of SpokenToWritten library converts the string into written english.
## output_string = SpokenToWritten().Convert(input_string

The output can be seen as follows:
## print("Written English Text Output : ",output_string)
### Written English Text Output :  Hey my name is Alexa, the current time is 4 pm , my contact number is 5555 and i earn $2000000 per annum.


Features Which can be implemented in Future:
1. Feature To handle dates and convert accordingly.
2. Feature for converting any country's currency into dollars.



