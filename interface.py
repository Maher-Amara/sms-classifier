# importations
import base64
import sys
from tkinter import *
from classifier import classifier


def intermediate():
    # faire quelque chause
    SMS = SMS_input.get()
    var_label.set(classifier(SMS))


# creer une fenetre personalisé
window = Tk()
window.title("SMS classifier")
window.geometry("1366x741")
window.minsize(480, 360)

if sys.platform == 'win32':
    window.iconbitmap("icon.ico")

window.config(background='#0C6CAE')

# frames
# frame_1 = Frame(window, bg='#0C6CAE', bd=1, relief=SUNKEN) #bd=1, relief=SUNKEN #(afiicher)
frame_2 = Frame(window, bg='#0C6CAE')

# sub frames
subframe_1 = Frame(frame_2, bg='#0C6CAE')
subframe_2 = Frame(frame_2, bg='#0C6CAE')

# les textes
label_text_1 = Label(subframe_2, text="Ecrire votre SMS ici :", font=("courrier", 15), bg='#0C6CAE', fg='white')
label_text_1.pack()

# ajouter un zone texte
SMS_input = Entry(subframe_2, font=("courrier", 15), bg='#0C6CAE', fg='white', width=50)
SMS_input.pack()

# ajouter bouton
button = Button(subframe_2, text="process", font=("Courrier", 25), bg='white', fg='#0C6CAE',
                command=intermediate)
button.pack(pady=30)  # pady=20, fill=X(can add)

# ajouter image
width = 300
height = 300
logo = PhotoImage(file="logo.png")  # .zoom(35).subsample(32)
canvas = Canvas(subframe_1, width=width, height=height, bg="#0C6CAE", bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=logo)
canvas.pack()

width = 1361
height = 272
titre = PhotoImage(file="header.png")  # .zoom(35).subsample(32)
canvas = Canvas(window, width=width, height=height, bg="#0C6CAE", bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=titre)
canvas.pack()

# label modifiable
var_label = StringVar()
label = Label(subframe_2, textvariable=var_label, font=("courrier", 15), bg="#0C6CAE", fg='white')
var_label.set("")
label.pack()

# afficher ajouter frame
subframe_1.grid(row=0, column=0)
subframe_2.grid(row=0, column=1)
# frame_1.pack(expand=YES)
frame_2.pack(expand=YES)

# afficher
window.mainloop()
