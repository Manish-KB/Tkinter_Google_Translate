import tkinter
from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
import pyttsx3
from PIL import Image, ImageTk
import customtkinter

app = customtkinter.CTk()  
app.geometry("400x240")
app.title('Google Translate')



customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")




app.geometry("880x310")
sent1=''
sent2=''
def translate_it():

	translated_text.delete(1.0, END)

	try:

		for key, value in languages.items():
			if (value == original_combo.get()):
				from_language_key = key

		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		words = textblob.TextBlob(original_text.get(1.0, END))
		global sent1
		sent1 = words
		words = words.translate(from_lang=from_language_key , to=to_language_key)
		global sent2
		sent2 = words
		translated_text.insert(1.0, words)


  
	except Exception as e:
		messagebox.showerror("Translator", e)

def clear():

	original_text.delete(1.0, END)
	translated_text.delete(1.0, END)
	global sent1
	sent1 = ''
	global sent2
	sent2 = ''
 
def audio1():
	engine=pyttsx3.init()
	engine.say(sent1)
	engine.runAndWait()
def audio2():
	engine=pyttsx3.init()
	engine.say(sent2)
	engine.runAndWait()

languages = googletrans.LANGUAGES

language_list = list(languages.values())

# original_text = Text(app, height=10, width=40)
# original_text.grid(row=1, column=0, pady=20, padx=10)
original_text = customtkinter.CTkTextbox(app,width=300)
original_text.grid(row=1, column=0, pady=5, padx=10)

translate_button = customtkinter.CTkButton(master=app, text="Translate", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=1, column=3, padx=10)

translated_text = customtkinter.CTkTextbox(app,width=300)
translated_text.grid(row=1, column=1, pady=5, padx=10)


def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)
# original_combo = ttk.Combobox(app, width=50, value=language_list)
# original_combo.current(21)
# original_combo.grid(row=0, column=0,pady=20,padx=10)
original_combo = customtkinter.CTkComboBox(master=app, width=300, values=language_list)
original_combo.grid(row=0, column=0,padx=20, pady=10)
original_combo.set("english") 


translated_combo = customtkinter.CTkComboBox(master=app, width=300, values=language_list)
translated_combo.grid(row=0, column=1)
translated_combo.set("french") 

clear_button = customtkinter.CTkButton(master=app, text="Clear",font=("Helvetica", 24), command=clear)
# clear_button.grid(row=2, column=3)
clear_button.place(relx=0.84, rely=0.7, anchor=tkinter.CENTER)


image = Image.open("speaker.png")
image = image.resize((25, 25), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

audio1_button = Button(app, image=image,width=25,height=25,command=audio1)
audio1_button.grid(row=3, column=0)

audio2_button = Button(app,image=image,width=25,height=25, command=audio2)
audio2_button.grid(row=3, column=1)




app.mainloop()