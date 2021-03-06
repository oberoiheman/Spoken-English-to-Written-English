# Installing Word2 number library
!pip install word2number

from word2number import w2n
import re

#Converts words to numbers 
def word_to_num(string):
    ''' Converts english words to numbers such as hundred to 100 '''
    words = string.split()
    numbers=[]
    for word in words:
      try:
        numbers.append( (word,w2n.word_to_num(word) ))
      except:
        numbers.append((word,'none'))

    temp = 0
    new_numbers=[]
    old_num_index = []
    for i in range(len(numbers)):
        if type(numbers[i][1])==int:
            temp=temp+1
        else:
            if temp >=2:
              new_number_string  = ''
              for j in range(temp,0,-1):
                  new_number_string = new_number_string+" " + numbers[i-j][0]
                  old_num_index.append(i-j)
              new_numbers.append((new_number_string.strip(),w2n.word_to_num(new_number_string)))
            temp = 0
    temp = 0
    for i in old_num_index:
        del numbers[i-temp]
        temp+=1
    numbers.extend(new_numbers)

    for i in range(len(numbers)-1,-1,-1):
        if type(numbers[i][1])==int:
            string = string.replace(numbers[i][0],str(numbers[i][1]))
    return string

#Dollar Rule
def dollar_rule(string):
    ''' Converts dollar or dollars to dollar sign i.e $ '''
    regx_dollar = r'\d+\s+dollars|\d+\s+dollar'
    list_of_matches = re.findall(regx_dollar,string)
    for match in list_of_matches:
      converted_string = '$'+str(match.split()[0])
      string = string.replace(match,converted_string)
    
    return string

#abbreviations rule
def abbreviations_rule(string):
    ''' Converts some abbreviations to their original form such as: double a to aa'''

    custom_w2n = {"single":1,
                  "double":2,
                  "triple":3,
                  "quadruple":4,
                  "quintuple":5,
                  "sextuple":6,
                  "septuple":7,
                  "octuple":8,
                  "nonuple":9,
                  "decuple":10
                          }
    for word in custom_w2n:
        list_of_matches = re.findall(word + '\s+\w',string)
        for match in list_of_matches:
            n_times = custom_w2n[word]
            converted_string = n_times*str(match.split()[1])
            string = string.replace(match,converted_string)

    list_of_matches = re.findall(r'\s[a-zA-Z]\s[a-zA-Z]\s',string)
    for match in list_of_matches:
        converted_string = ' '+match.split()[0]+match.split()[1]+' '
        string = string.replace(match,converted_string)


    return string

#Spoken English To Written English Conversion class.
class SpokenToWritten:

    def __init__(self):

        self.dollar_rule=dollar_rule
        self.word_to_num =  word_to_num
        self.abbreviations_rule = abbreviations_rule


    def Convert(self,input_string):
        temp_string = self.word_to_num(input_string)
        temp_string = self.dollar_rule(temp_string)
        output_string = self.abbreviations_rule(temp_string)
        return output_string

input_string = input("Enter Spoken English Text: ")
output_string = SpokenToWritten().Convert(input_string)
print("Written English Text Output : ",output_string)
