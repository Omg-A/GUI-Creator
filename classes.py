from tkinter import *
from tkinter import messagebox as tkmb
from tkinter import ttk

root = Tk()
root.title("GUI Creator")
root.geometry("500x600")

options = ["Button", "Label", "Dropdown"]
dropdown_element = ttk.Combobox(root, state="readonly", values=options)
dropdown_element.pack()

class CreateElements:
    def __init__(self):
        print("This is CreateElemets class!!!")
    
    def createLabel(self):
        label = Label(root, text="Label", fg="red")
        label.pack()
    
    def createButton(self):
        button = Button(root, text="Button", command=self.Message)
        button.pack()
    
    def createDropdown(self):
        numbers = [1, 2, 3]
        dropdown = ttk.Combobox(root, state="readonly", values=numbers)
        dropdown.pack()
    
    def choose(self):
        global dropdown_element
        element_to_create = dropdown_element.get()
        
        if(element_to_create == "Label"):
            self.createLabel()
        elif(element_to_create == "Button"):
            self.createButton()
        elif(element_to_create == "Dropdown"):
            self.createDropdown()
        
    def Message(self):
        tkmb.showinfo("Show Info", "You clicked a button made by a class")

create_elements = CreateElements()

button_classes = Button(root, text="Create New Element", command=create_elements.choose)
button_classes.pack(padx=20, pady=10)

root.mainloop()