import hashlib
import pyperclip
import clipboard
password = input("Password:").encode('utf-8')
passwordList = ['cf97dd1558cf4f9cbacadd55d0c5c8fb0af1ecd466c6a9d805ef38ac704597fb', 'e207ed17515aff71935e598e9b6bf6eb7d6953aa754d7e629572a93b159ef1b2', '78a4a165cac7fce6bd45b2c0e3c142b1225261213e9d7ac14e4c246d981c1e2e', 'd4a7f4c4c1c5324f9651b48afc4edbe4ca25dcc442d8a9fefaa70c333c14f18b', '2689367b205c16ce32ed4200942b8b8b1e262dfc70d9bc9fbc77c49699a4f1df', 'd3851b200b6f092cd57504c3cf5d604bc16c7cdd0998f96624c314620f28b212']
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Calphabet = ["Ø", "Æ", "%", "¿", "§", "₩", "?", "¢", "€", "≠", "Ł", "Ñ", "Ç", "Œ", "¡", "£", "{}", "…", "Ö", ">", "~", "»", "¥", "≈", "Å", "••"]
hashed = str(hashlib.sha256(password).hexdigest())
#print (str(hashed))
splitMessage = []
message = ''
mode = ''
final = []
finalMessage = ''
position = 0
good = False
nigger = ''
for i in passwordList:
  if (i == hashed):
    good = True
    mode = input("Does a nigga want to translate to English(1) or Chinnakondanese(2): ")

def toEnglish(bot):
  if (bot == ' '):
    return ' '
  else:
    position = 0
    for i in Calphabet:
      if (bot == i):
        return alphabet[position]
      position += 1

def toChinnakondanese(bot):
  if (bot == ' '):
    return ' '
  else:
    position = 0
    for i in alphabet:
      if (bot == i):
        return Calphabet[position]
      position += 1
    position = 0
    for i in capital:
      if (bot == i):
        return Calphabet[position]
      position += 1



if (good == False):
  print ("Nigga leave")
  nigger = input('')
elif (good == True):
  if (mode == 'English' or mode == 'english' or mode == '1'):
    message = clipboard.paste()
    splitMessage = [char for char in message]
    for i in splitMessage:
      final.append(toEnglish(i))
    finalMessage = ''.join(final)
    print (finalMessage)
    nigger = input('Press enter to close')
  elif(mode == 'Chinnakondanese' or mode == 'chinnakondanese' or mode == '2'):
    message = input('Enter the English my nigga: ')
    splitMessage = [char for char in message]
    for i in splitMessage:
      final.append(toChinnakondanese(i))
    finalMessage = ''.join(final)
    pyperclip.copy(finalMessage)
    print (finalMessage)
    
  else:
    print ("Nigga learn to spell")
    nigger = input('')

