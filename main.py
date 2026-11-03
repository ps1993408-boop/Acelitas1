import tkinter as tk
from tkinter import messagebox
import random

# Janela principal
root = tk.Tk()
root.title('Acelitas1')
root.geometry('600x600')
root.configure(background='#ffc8dd')
root.resizable(False, False)

# Função para fazer o botão Não fugir
def move_button_1(e):
    if button_1.winfo_exists():
        bx = button_1.winfo_x()
        by = button_1.winfo_y()
        if abs(e.x - bx) < 70 and abs(e.y - by) < 50:
            x = random.randint(10, 450)
            y = random.randint(250, 520)
            button_1.place(x=x, y=y)

# Função do botão Sim
def accepted():
    messagebox.showinfo(
        "Meu amor ❤️",
        "Eu te amo, meu amor! Lanchinho mais tarde? 💗"
    )

# Função do botão Não
def denied():
    if button_1.winfo_exists():
        button_1.destroy()

# Título
margin = tk.Canvas(root, width=500, height=100, bg='#ffc8dd',
                   bd=0, highlightthickness=0)
margin.pack()

test_id = tk.Label(root, bg='#ffc8dd',
                   text='Quer namorar comigo?',
                   fg='#590d22', font=('Montserrat', 24, 'bold'))
test_id.pack(pady=30)

# Botão Sim
button_2 = tk.Button(root, text='Sim ❤️', bg='#ffb3c1', fg='#590d22',
                     relief=tk.RIDGE, bd=3, command=accepted,
                     font=('Montserrat', 14, 'bold'))
button_2.place(x=170, y=250, width=110, height=50)

# Botão Não
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', fg='#590d22',
                     relief=tk.RIDGE, bd=3, command=denied,
                     font=('Montserrat', 14, 'bold'))
button_1.place(x=320, y=250, width=110, height=50)

# Detecta o movimento do mouse
root.bind('<Motion>', move_button_1)

# Executa o programa
root.mainloop()
