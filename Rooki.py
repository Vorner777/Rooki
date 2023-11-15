from tkinter import *
import socket
import os
from tkinter import messagebox
import urllib.request
import smtplib
import os
import requests
from email.mime.text import MIMEText
import socket
from requests import get
import time
from time import sleep
import pyscreenshot
hostname = socket.gethostname()
#Айпи
public_ip = urllib.request.urlopen('http://ip-address.ru/show').read().decode('utf-8')







#Нажатие кнопки
def cemd():

    username = username_entry.get()
    password = pass_entry.get()
    #TigerPooh
    if username == 'TigerPooh':
        if password == '17239827':
            if public_ip == '23.129.64.221':
                message = f"Тигр вошёл с айпи: {public_ip}, и имнем пк: {hostname}"
                print(send_email(message=message))
                messagebox.showinfo('Тигр успешно вошёл!')

            elif public_ip == '46.242.15.22':
                message = f"Админ вошёл в акк тигра с айпи: {public_ip}, и имнем пк: {hostname}"
                print(send_email(message=message))
                messagebox.showinfo('Админ зашёл на акк Тигра', 'Ага')

            else:
                messagebox.showerror('Ошибка!', 'Вы не TiggerPooh!!!')


    elif username == 'admin':
        if password == '132':
            if public_ip == '46.242.15.22':
                messagebox.showinfo('Привет', 'qwerty1234')
                message = "Админ вошёл"
                print(send_email(message=message))
            else:
                messagebox.showerror('Неа', 'Вы не админ!')
        else:
            messagebox.showerror('Неа', 'Даже не надейся')



    #если ваще нету
    else:
        messagebox.showerror('Ошибка!', 'Проверьте свой пароли или логин. (Заглавные и строчные буквы учитываються)')








def send_email(message):
    sender = "vorner02@gmail.com"
    # your password = "your password"
    password = "jsstthlwhwvrtbej"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = f"Инфа о {public_ip}"
        server.sendmail(sender, sender, msg.as_string())

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


# Отправка сообщений
# def main():
#     message = f"IP: {public_ip}, Local ip: {local_ip}, hostname: {hostname}"
#     print(send_email(message=message))
#     sleep(5)


#
root = Tk()
root.title('----  By Vorner  ----')
root.geometry('300x600')
root.resizable(width=False, height=False)
root['bg'] = 'orange'

main_label = Label(root, text='Авторизация', font='Arial 30 bold', bg='orange', fg='red')
main_label.pack()

useranem_label = Label(root, text='Логин', font='Arial 30', bg='orange', fg='black', padx=10, pady=8)
useranem_label.pack()

username_entry = Entry(root, bg='orange', fg='dark red', font='impact 12')
username_entry.pack()

password_label = Label(root, text='Пароль', font='Arial 30', bg='orange', fg='black', padx=10, pady=8)
password_label.pack()

pass_entry = Entry(root, bg='orange', fg='lime', font='impact 15 bold', show="●")
pass_entry.pack()


send_btn = Button(root, text='Войти', command=cemd)
send_btn.pack()
root.mainloop()