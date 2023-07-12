#!/usr/bin/env python

# ==============================================
#
# gui.py
#
# Graphical User Interface GUI
#
# ==============================================


import customtkinter
from customtkinter import filedialog
from lexical import lex_data, lex_file
from semantic import yacc_data, yacc_file

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1280x720")

global current_file
current_file = False

def open_new_file():
    global current_file
    with open('new_file.txt', mode="w+", encoding="utf8") as new_file:
        root.title('new_file.txt')
        current_file = new_file

def open_file():
    global current_file
    text_file = filedialog.askopenfilename(initialdir="~/Downloads/", title="Open Text File", filetypes=(("Text Files", "*.txt"), ))
    # Delete previous text
    code.delete("0.0", "end")
    with open(text_file, mode="r+", encoding="utf8") as text_file:
        current_file = text_file
        root.title(f"{text_file.name}")
        file_content = text_file.read()
        code.insert("0.0", file_content)


def save_file():
    global current_file
    if current_file:
        with open(current_file.name, mode="w", encoding="utf8") as saved_file:
            saved_file.write(code.get("0.0", "end"))
    


def btn_on_click():
    global current_file
    if current_file:
        save_file()
        result.configure(state="normal")
        result.delete("0.0", "end")
        result.insert("0.0", f"{lex_file(current_file.name)}\n{yacc_file(current_file.name)}")
        result.update()
        result.configure(state="disable")
        # print(lex_data(code.get("0.0", "end").strip()))


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(1, weight=1)

open_button = customtkinter.CTkButton(master=frame, corner_radius=9, command=open_file, text="Open File")
open_button.grid(row=2, column=0, padx=10, pady=10)

save_button = customtkinter.CTkButton(master=frame, corner_radius=9, command=save_file, text="Save File")
save_button.grid(row=2, column=1, padx=10, pady=10)

button = customtkinter.CTkButton(master=frame, corner_radius=9, command=btn_on_click, text="Run Code")
button.grid(row=0, column=0, padx=10, pady=10)

code = customtkinter.CTkTextbox(master=frame)
code.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

result = customtkinter.CTkTextbox(master=frame, wrap="word")
result.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

root.mainloop()
