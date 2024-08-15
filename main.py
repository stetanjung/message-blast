import pywhatkit
import datetime
import pyautogui
import tkinter

import sys

from urllib.parse import quote

from pywhatkit.core import core

# win = tkinter.Tk()
# screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
# screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor

# print(screen_width, screen_height) # prints your monitor's resolution

args = sys.argv
print(args[1])
nama_tamu = args[1]

link_undangan = "https://angelaharis.viding.co?name=Cornelia+Claudia+%26+Christopher+Reinhard"

message = f"""
Dear {nama_tamu},

We are overjoyed to invite you to celebrate our wedding day and request your presence at the wedding of

Elia Kevin Satria
&
Vivian Dianti

The Holy Matrimony & Wedding Reception will be held on :
*Saturday, 6 January 2024 at Pullman Bandung Grand Central*
 
Wedding Reception at *17:00 WIB*

Our Party will not be the same without your presence. Please kindly RSVP if you can attend as soon as you receive this invitation on this form:

{link_undangan}

We look forward to celebrating our wedding with you. 
With warm regards the from happy family, 

Mr. Benyamin Budi Satria 
& Mrs. Soelistyo Rini

Mr. Tjen Tjiap Siong & Mrs. Sherlyna
"""

phone_no = args[2]
# message = "hello"

now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

# pywhatkit.sendwhatmsg(phone_no, message, now.hour, now.minute, 10, True)

# pywhatkit.sendwhatmsg_instantly(phone_no, message)

# pyautogui.moveTo(screen_width * 0.5, screen_height* 0.5) # Moves the cursor the the message bar in Whatsapp
# pyautogui.click() # Clicks the bar
# pyautogui.press('enter')

message_encoded = quote(message)

# print(message_encoded)

core.send_message(message=message, receiver=phone_no, wait_time=10)
core.close_tab(wait_time=3)

# for i in range(2):
#     core.send_message(message=message, receiver=phone_no, wait_time=10)
#     core.close_tab(wait_time=3)
