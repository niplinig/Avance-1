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

global current_file, current_text
current_file, current_text = "", ""


def open_new_file():
    global current_file, current_text
    with open("new_file.txt", mode="w+", encoding="utf8") as new_file:
        root.title("new_file.txt")
        current_file = new_file
        current_text = code.delete("0.0", "end")


def open_file():
    global current_file, current_text
    text_file = filedialog.askopenfilename( 
        initialdir="~/Downloads/",
        title="Open Text File",
        filetypes=(("Text Files", "*.txt"),),
    )
    code.delete("0.0", "end")  # Delete previous text
    with open(text_file, mode="r+", encoding="utf8") as text_file:
        current_file = text_file
        root.title(f"{current_file.name}")
        current_text = current_file.read()
        code.insert("0.0", current_text)


def save_file():
    global current_file, current_text
    if current_file:
        with open(current_file.name, mode="w", encoding="utf8") as saved_file:
            current_file = saved_file
            current_text = code.get("0.0", "end")
            current_file.write(current_text)
    else:
        save_as_file()


def save_as_file():
    global current_file, current_text
    text_file = filedialog.askopenfilename(
        initialdir="~/Downloads/",
        title="Open Text File",
        filetypes=(("Text Files", "*.txt"),),
    )
    with open(text_file, mode="w", encoding="utf8") as saved_file:
        current_file = saved_file
        root.title(f"{current_file.name}")
        current_text = code.get("0.0", "end")
        current_file.write(current_text)


def lexical_analysis():
    global current_file, current_text
    if current_file:
        save_file()
        result.configure(state="normal")
        result.delete("0.0", "end")
        result.insert(
            "0.0", f"{lex_file(current_file.name)}"
        )
        result.update()
        result.configure(state="disable")
    else:
        save_as_file()


def semantic_analysis():
    global current_file, current_text
    if current_file:
        save_file()
        result.configure(state="normal")
        result.delete("0.0", "end")
        result.insert(
            "0.0", f"{yacc_file(current_file.name)}"
        )
        result.update()
        result.configure(state="disable")
    else:
        save_as_file()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(1, weight=1)

open_button = customtkinter.CTkButton(
    master=frame, corner_radius=9, command=open_file, text="Open File"
)
open_button.grid(row=2, column=0, padx=10, pady=10)

save_button = customtkinter.CTkButton(
    master=frame, corner_radius=9, command=save_file, text="Save File"
)
save_button.grid(row=2, column=1, padx=10, pady=10)

lex_button = customtkinter.CTkButton(
    master=frame, corner_radius=9, command=lexical_analysis, text="Lexical Analysis"
)
lex_button.grid(row=0, column=0, padx=10, pady=10)

sem_button = customtkinter.CTkButton(
    master=frame, corner_radius=9, command=semantic_analysis, text="Semantic Analysis"
)
sem_button.grid(row=0, column=1, padx=10, pady=10)

code = customtkinter.CTkTextbox(master=frame)
code.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

result = customtkinter.CTkTextbox(master=frame, wrap="word")
result.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

open_new_file()

root.mainloop()
