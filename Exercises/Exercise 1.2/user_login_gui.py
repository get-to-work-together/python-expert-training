from user import User

import tkinter as tk


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        tk.Label(master, text='Username').pack(pady=(16, 0))

        self.username = tk.StringVar()
        w = tk.Entry(master, textvariable=self.username)
        w.pack(pady=(0, 16))

        tk.Label(master, text='Password').pack()

        self.password = tk.StringVar()
        w = tk.Entry(master, textvariable=self.password)
        w.pack(pady=(0, 16))

        w = tk.Button(master, text="Login", command=self.handle_login)
        w.pack(pady=(0, 16))

        self.message = tk.Label(master, text='', foreground='red')
        self.message.pack()

    def handle_login(self):
        try:
            self.message['text'] = ''
            username = self.username.get()
            password = self.password.get()

            if User.valid_login(username, password):
                self.message['text'] = f'Welcome {username}!'
                self.message['foreground'] = 'green'
            else:
                self.message['text'] = f'Incorrect username or password!'
                self.message['foreground'] = 'red'

        except:
            self.message['text'] = 'An error occured.'


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    root.title('User Login')
    app = App(root)
    root.mainloop()
