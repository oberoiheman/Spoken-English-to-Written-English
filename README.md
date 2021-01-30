# Spoken-English-to-Written-English
This is reusable python library which can be used to convert spoken english text into written english text.
It accounts for the following rules:
1. It can converts words to numbers such as hundred to 100.
2. It converts the word dollar/dollars to dollar sign i.e $ for example hundred dollars is converted to $100.
3. It accounts for the words such as double , triple etc and make the changes in text according to their literal meaning. such double five triple four changes to 55 444.
4. It also converts abbreviations such as p m  to pm.

This Library can be used by downloading the spoken_to_written.py file in your current working directory and importing it as follows :

from spoken_to_written.py import *
input_string = input("Enter Spoken English Text: ")
output_string = SpokenToWritten().Convert(input_string)
print("Written English Text Output : ",output_string)


