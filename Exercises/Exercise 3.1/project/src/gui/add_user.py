import tkinter as tk
import tkinter.font as tkFont

from ..models.user import User
from ..persistence.user_persistence import *


class App(tk.Frame):

    def __init__(self, master=None):
        
        options = {'padx':10, 'pady':3, 'sticky':'w'}

        bold_font = tkFont.Font(family="Helvetica", size=24, weight="bold")

        w = tk.Label(master, text="New User", font=bold_font, fg='green')
        w.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        w = tk.Label(master, text="Username:")
        w.grid(row=1, column=0, **options)

        self.username = tk.StringVar()
        w = tk.Entry(master, textvariable=self.username)
        w.grid(row=1, column=1, **options)

        w = tk.Label(master, text="Full Name:")
        w.grid(row=2, column=0, **options)

        self.name = tk.StringVar()
        w = tk.Entry(master, textvariable=self.name)
        w.grid(row=2, column=1, **options)

        w = tk.Label(master, text="E-mail:")
        w.grid(row=3, column=0, **options)

        self.email = tk.StringVar()
        w = tk.Entry(master, textvariable=self.email)
        w.grid(row=3, column=1, **options)

        w = tk.Label(master, text="Password:")
        w.grid(row=5, column=0, **options)

        self.password = tk.StringVar()
        w = tk.Entry(master, textvariable=self.password)
        w.grid(row=5, column=1, **options)

        w = tk.Button(master, text="Add", command=self.submit)
        w.grid(row=6, column=0, columnspan=2, padx=70, pady=20, sticky='ew')


    def submit(self):
        try:
            user = User(self.username.get(),
                        self.email.get(),
                        self.name.get())
            user.set_password(self.password.get())
        except Exception as ex:
            print(ex)

        else:
            insert_user(user)
            self.username.set(''),
            self.email.set(''),
            self.name.set('')
            self.password.set('')
            print(f'Added a new user to DB: ', user)


def main():
    root = tk.Tk()
    # root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    root.title('tkinter demo')
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
