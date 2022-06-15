#Create a GUI application for a mood tracker using Tkinter

# Import the Tkinter module
import tkinter as tk
import tkinter.ttk as ttk
import io
import sys

# Create the GUI application using the Tkinter module

window = tk.Tk()
window.title("Mood Tracker")
window.geometry("300x300")

# Create a label widget
label = tk.Label(window, text="Enter your mood:")
label.pack()
# Create a text box widget
text_box = tk.Entry(window)
text_box.pack()
# Create a button widget
button = tk.Button(window, text="Submit")
button.pack()

#Run the GUI
window.mainloop()
    