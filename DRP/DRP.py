#Import the required Libraries
from tkinter import *
from tkinter import ttk
import time
import threading
import sys
import subprocess
import importlib.util
import os

# Install library if not installed
drp_library = importlib.util.find_spec("pypresence")
if drp_library is None:
    # implement pip as a subprocess:
    input("pypresence has not been found on this drive. Please press enter to install pypresence. ")
    print("Installing pypresence...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypresence'])
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)

# Import pypresence
from pypresence import Presence

#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of Tkinter frame
win.geometry("500x350")
win.title("Discord Rich Presence")

def send():
    client_id = url.get()
    if 'RPC' not in globals():
        global RPC
        RPC = Presence(client_id)
        RPC.connect()
    def update_loop():
        while True:
            time.sleep(10)
            RPC.update(state=state.get(), details=details.get(), large_image=img.get())
    threading.Thread(target=update_loop, daemon=True).start()



#Title of the program
label = Label(win, text="Discord Rich Presence", font=("poppins 15 bold"))
label.pack()

#Create an Entry widget to accept User Input
label = Label(win, text="Client ID",  font=("poppins"))
label.pack()
url = Entry(win, width= 40)
url.focus_set()
url.pack()

label = Label(win, text="State (Title)",  font=("poppins"))
label.pack()
state = Entry(win, width= 40)
state.focus_set()
state.pack()

label = Label(win, text="Details",  font=("poppins"))
label.pack()
details = Entry(win, width= 40)
details.focus_set()
details.pack()

label = Label(win, text="Image key (Large image only)",  font=("poppins"))
label.pack()
img = Entry(win, width= 40)
img.focus_set()
img.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Send",width= 20, command=send).pack(pady=20)
label = Label(win, text="(The script updates your status every 10 seconds to prevent it from crashing)", font=("poppins 10"))
label.pack()
win.mainloop()