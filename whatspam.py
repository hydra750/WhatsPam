import sys, os, time, tkinter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')

banner = """
WhatsPam
"""

def getText():
    global msg
    msg = T.get('1.0', tkinter.END)
    root.destroy()

print(banner)

print('[INFO] Write your message in the message box')
root = tkinter.Tk()
root.title('WhatsPam')
root.resizable(0, 0)
T = tkinter.Text(root, height=30, width=50)
T.pack()
T.insert(tkinter.END, 'Enter your message here ...')
okButton = tkinter.Button(root, text='Done', command=getText)
okButton.pack()
tkinter.mainloop()

while True:
    loop = input('\nNumber of loops [infinite=0]: ')
    try:
        loop = int(loop)
        break
    except ValueError:
        print('\n[ERROR] The loop should be an integer')

while True:
    delay = input('\nDelay in secs: ')
    try:
        delay = int(delay)
        break
    except ValueError:
        print('\n[ERROR] The delay should be an integer')

mode = '[loop: '+str(loop)+']'
if loop==0:
    mode = '[infinite]'

web = webdriver.Chrome(options=options)
web.get('https://web.whatsapp.com/')
print('\n\n[INFO] Connect your WhatsApp, and select the target')
input('\nPress ENTER to proceed\n')
print('\nSpamming {} ...'.format(mode))
elem = web.find_element_by_css_selector('._2S1VP')

i = 1
if loop==0:
    while True:
        try:
            elem.send_keys(msg + Keys.ENTER)
            print('Messages sent: {}'.format(i), end='\r')
            i+=1
            time.sleep(delay)
        except KeyboardInterrupt:
            print('\n\nOperation aborted')
            break

else:
    for _ in range(loop):
        elem.send_keys(msg + Keys.ENTER)
        print('Messages sent: '+str(i)+' out of '+str(loop), end='\r')
        i+=1
        time.sleep(delay)

print('\n\nAttack complete')
web.quit()