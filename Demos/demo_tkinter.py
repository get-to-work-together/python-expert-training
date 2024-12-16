import tkinter as tk


class App(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.text1 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text1)
        w.pack(pady=(20, 0))

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.pack()

        w = tk.Button(master, text="Add", command=self.handle_add)
        w.pack()

        self.result = tk.StringVar()
        w = tk.Entry(master, textvariable=self.result)
        w.pack()

        self.message = tk.Label(master, text='', foreground='red')
        self.message.pack()

    def handle_add(self):
        try:
            self.message['text'] = ''
            number1 = int(self.text1.get())
            number2 = int(self.text2.get())
            self.result.set(str(number1 + number2))

        except:
            self.message['text'] = 'An error occured. Not a valid number.'


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x200+100+100')  # width x height + x_offset + y_offset
    root.title('tkinter demo')
    app = App(root)
    root.mainloop()
