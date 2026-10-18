
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("File Editor Application")
window.geometry('600x500')

window.rowconfigure(1, weight=1)     
window.columnconfigure(0, weight=1)  
window.columnconfigure(1, weight=1)  

def open_letter():
    filepath = askopenfilename(
        title="Open a Saved Letter",
        filetypes=[("Text files", "*.txt"), ("All Files", "*.*")]
    )
    
    if not filepath:
        return
        
    letter_box.delete(1.0, END)
    

    with open(filepath, "r") as input_file:
        letter_content = input_file.read()
        letter_box.insert(END, letter_content)
        
    window.title(f"File Editor - {filepath}")

def save_letter_as():
    """Saves the current text body under a brand new file name."""
    filepath = asksaveasfilename(
        title="Save Letter As...",
        defaultextension="txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        letter_content = letter_box.get(1.0, END)
        output_file.write(letter_content)
        
    window.title(f"File Editor - {filepath}")

btn_open = Button(window, text="Open A File", command=open_letter, bg="#de5d5d", fg="black")
btn_save = Button(window, text="Save File", command=save_letter_as, bg="#de5d5d", fg="black")

letter_box = Text(window, wrap="word", font=("Arial", 11))

btn_open.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
btn_save.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

letter_box.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

# Start the application loop
window.mainloop()
