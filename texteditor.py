#import necessary packages
from tkinter import  *
from tkinter.filedialog import askopenfilename, asksaveasfilename

#setup root window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry('600x500')
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(0, minsize=800, weight=1)

#function to open a file
def open_file():
    """Open file for editing."""
    filepath = askopenfilename(filetypes = [("Text files", "*.txt"), ("All Files", "*.*")])
    
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    
    #if the file is opened then display the contents of the file
    with open(filepath, "r") as input_file:
        #read contents of the input file
        text = input_file.read
        #insert contents of the file into the editor box
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Codingal's Text Editor - {filepath}")
    
#function to save a file
def save_file():
    #save the current file as a new file
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes = [("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if not filepath:
        return
    with open(filepath, "w") as output_file:
       #read the edited content and update in the output file
       text = txt_edit.get(1.0, END)
       output_file.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")
    
#add widgets to the application
txt_edit = Text(window)
fr_buttons = Frame(window, relief= "raised", bd = 2)
btn_open = Button(fr_buttons, text= "Open", command = open_file)
btn_save = Button(fr_buttons, text = "Save as..", command =save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx = 5, pady = 5)
btn_save.grid(row=1, column=0, sticky="ew", padx = 5, pady = 5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

#start GUI event loop
window.mainloop()