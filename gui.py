#!/usr/bin/env python

# ----------------------------------
# gui.py
#
# Interfaz gráfica
# ----------------------------------

import customtkinter
from lexic import lex_data, lex_file
from semtic import yacc_data, yacc_file

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1280x720")
root.title("VSCode")


def btn_on_click():
    result.configure(state="normal")
    result.delete("0.0", "end")
    code_input = code.get("0.0", "end").strip()
    result.insert("0.0", f"{lex_data(code_input)}\n{yacc_data(code_input)}")
    result.update()
    result.configure(state="disable")
    # print(lex_data(code.get("0.0", "end").strip()))


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(1, weight=1)

button = customtkinter.CTkButton(master=frame, corner_radius=9, command=btn_on_click)
button.grid(row=0, column=0, padx=10, pady=10)

code = customtkinter.CTkTextbox(master=frame)
code.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

result = customtkinter.CTkTextbox(master=frame)
result.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

root.mainloop()
