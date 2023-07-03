#!/usr/bin/env python

# ----------------------------------
# gui.py
#
# Interfaz gráfica
# ----------------------------------

import customtkinter
from lexic import lex_data, lex_file
from semtic import yacc_shell, yacc_file

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1280x720")
root.title("VSCode")


def btn_on_click():
    result.delete("0.0", "")
    result.insert("0.0", f"{lex_data(code.get('0.0', 'end').strip())}")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

button = customtkinter.CTkButton(master=frame, corner_radius=10, command=btn_on_click)
button.pack(pady=12, padx=10)

code = customtkinter.CTkTextbox(master=frame)
code.pack(pady=12, padx=10)

result = customtkinter.CTkTextbox(master=frame)
result.configure(state="disable")
result.pack(pady=12, padx=10)

root.mainloop()
