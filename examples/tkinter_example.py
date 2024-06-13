import tkinter as tk

def clicking():
    label.config(text='Button clicked :D')

# Creating the main window
window = tk.Tk()
window.title('Tkinter Example')

# Adding a label 
label = tk.Label(window, text='Hello, Tkinter')
label.pack()

# Adding a button
button = tk.Button(window, text='Click me', command=clicking)
button.pack()

# Starting interface
window.mainloop()