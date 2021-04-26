from tkinter import *
import mysql.connector
import tkinter as tk

# Main Window
root = Tk()
root.geometry("800x500")
root.configure(bg="blanched almond")

# Heading
Label(root, text="Patient Records", font="ar 20 bold", bg="blanched almond").grid(row=2, column=4)


root.mainloop()