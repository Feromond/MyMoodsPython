import tkinter as tk
import tkinter.ttk as ttk
import io
import sys

class MyMoodsCMD:

    def __init__(self) -> None:
        pass


    
    def isFloat(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    
    def isInt(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False


