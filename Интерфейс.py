from tkinter import *
from tkinter import messagebox
import pyperclip
import os

root = Tk()
def btn_click():
    if textInput.get() == '' and numInput.get() != '':
        messagebox.showerror(title='Ошибка', message='Введите текст')
    if numInput.get() == '' and textInput.get() != '':
        messagebox.showerror(title='Ошибка', message='Введите сдвиг')
    if numInput.get() == '' and textInput.get() == '':
        messagebox.showerror(title='Ошибка', message='Введите текст и сдвиг')

    text = textInput.get()
    num = int(numInput.get())

    list_text = list(text)
    list_text1 = list(text)
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
                'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
                'э', 'ю', 'я']

    for i in range(0, (len(list_text))):
        if list_text[i] in alphabet:
            list_text[i] = alphabet[alphabet.index(list_text[i]) + num]
        else:
            if list_text[i].lower() in alphabet:
                list_text[i] = alphabet[alphabet.index(list_text[i].lower()) + num].upper()

    textOutput.delete(0, END)
    textOutput.insert(0, ''.join(list_text))

def btn_click1():
    if textInput.get() == '' and numInput.get() != '':
        messagebox.showerror(title='Ошибка', message='Введите текст')
    if numInput.get() == '' and textInput.get() != '':
        messagebox.showerror(title='Ошибка', message='Введите сдвиг')
    if numInput.get() == '' and textInput.get() == '':
        messagebox.showerror(title='Ошибка', message='Введите текст и сдвиг')

    text = textInput.get()
    num = int(numInput.get())
    
    list_text1 = list(text)
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з',
                'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
                'э', 'ю', 'я']

    for i in range(0, (len(list_text1))):
        if list_text1[i] in alphabet:
            list_text1[i] = alphabet[alphabet.index(list_text1[i]) - num]
        else:
            if list_text1[i].lower() in alphabet:
                list_text1[i] = alphabet[alphabet.index(list_text1[i].lower()) - num].upper()

    textOutput.delete(0, END)
    textOutput.insert(0, ''.join(list_text1))


def paste():
    textInput.insert(0, pyperclip.paste())
def copy():
    textOut = textOutput.get()
    command = 'echo | set /p nul=' + textOut + '| clip'
    os.system(command)

def clear():
    textInput.delete(0, END)
    textOutput.delete(0, END)
    numInput.delete(0, END)

root['bg'] = 'white'
root.title('Шифр Цезаря')
root.geometry('800x350')

root.resizable(width=False, height=False)

frame = Frame(root, bg='white')
frame.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.8)


text1 = Label(frame, text="Введите текст:")
text1.grid(row=2, column=2)
text2 = Label(frame, text="Введите сдвиг:")
text2.grid(row=4, column=2)
text3 = Label(frame, text="Результат:")
text3.grid(row=6, column=2)
btn1 = Button(frame, text='Зашифровать', bg='yellow', command=btn_click, width=25, height=5)
btn1.grid(row=1, column=1)
btn2 = Button(frame, text='Разшифровать', bg='yellow', command=btn_click1, width=25, height=5)
btn2.grid(row=1, column=3)
btn3 = Button(frame, text='Вставить', bg='yellow', command=paste, width=10, height=1)
btn3.grid(row=3, column=4)
btn4 = Button(frame, text='Копировать', bg='yellow', command=copy, width=10, height=1)
btn4.grid(row=7, column=4)
btn5 = Button(frame, text='Очистить', bg='yellow', command=clear, width=10, height=1)
btn5.grid(row=9, column=2)


textInput = Entry(frame, bg='white', width=70)
textInput.grid(row=3, column=1, columnspan=3)
numInput = Entry(frame, bg='white', width=5)
numInput.grid(row=5, column=1, columnspan=3)
textOutput = Entry(frame, bg='white', width=70)
textOutput.grid(row=7, column=1, columnspan=3)


root.mainloop()
