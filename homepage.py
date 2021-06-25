# Import Module
from tkinter import *
from playsound import playsound
from PIL import Image,ImageTk
import os

# Create Object
root = Tk()

# Add Title
root.title('LUCAS')
root.iconbitmap('lucasicon.ico')
root.configure(bg='black')

# Keep track of the button state on/off
# global is_on

is_on = True
canvas = Canvas(root, width = 600, height = 400)
canvas.pack()
#Give the entire file address along with the file name and gif extension
#Use \\ in the address

my_image = ImageTk.PhotoImage(Image.open("think.jpg"))
canvas.create_image(0, 0, anchor = NW, image=my_image)

# Create Label
my_label = Label(root,
	text = "Lucas at your service",
	fg = "orange",bg= "black",
	font = ("AppleGothic", 20),width=20)

my_label.pack(pady = 20)
def run():
    os.system('Lucas_main.py')
# Define our switch function
def switch():
	global is_on
	# Determin is on or off
	if is_on:
		playsound('closesound.mp3')
		on_button.config(image = off)
		my_label.config(text = "Goodbye, Master",	fg = "orange")
		run()
		is_on = False
		
	else:
		playsound('opensound.mp3')
		on_button.config(image = on)
		my_label.config(text = "Hello Master", fg = "steel blue")
		is_on = True
		exit()
		
		

# Define Our Images
on = ImageTk.PhotoImage(Image.open("on.jpg"))
off = ImageTk.PhotoImage(Image.open("off.jpg"))

# Create A Button 
on_button = Button(root, image = on,bg="white", border = 0,command = switch,width=80,height=80)
on_button.pack()

# Execute Tkinter
root.mainloop()
