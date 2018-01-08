morseKey ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/" ,

        '1' : '._.'  ,
        '2' : '...' ,
        '3' : ':,.' ,  
        '4' : '_,,' ,
        '5' : ';._' , 
        '6' : '..' , 
        '7' : ',..' ,
        '8' : '::_' ,
        '9' : ',.,.' 
        }

def encrypt(message):
        encrypted_message = ''
        for item in message:
                if item.islower():
                        item = item.upper()
                        encrypted_message += morseKey[item]
                elif item not in morseKey:
                        encrypted_message += "..,'_'"
                else:
                      encrypted_message += morseKey[item]   


        print(encrypted_message)
        return encrypted_message

encrypt("Add message to encrypt here")
