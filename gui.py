#!/usr/bin/env python

# ----------------------------------
# gui.py
#
# Interfaz gráfica
# ----------------------------------

import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1280x720")
root.title("VSCode")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Ruby lexic and syntactic analyser")
label.pack(pady=12, padx=10)

text = customtkinter.CTkEntry(master=frame, placeholder_text="Enter ruby text here")
text.pack(pady=12, padx=10)


def callback():
    text = text_edit.get(0.3, END)
    print(text)


root.mainloop()
