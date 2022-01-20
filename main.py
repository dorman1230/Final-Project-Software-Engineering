import tkinter as tk
from tkinter import ttk

main_labels_font = ("Verdana", 40)
buttons_font = ("Verdana", 24)
labels_font = ("Verdana", 32)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, RSA_main_page, AES_main_page, InstructionPage):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_label = tk.Label(self, text="Encryption And Decryption System: ", fg="black", bg="yellow", font=main_labels_font)
        main_label.pack(pady=10)

        aes_label = tk.Label(self, text="Asymmetric encryption:", font=labels_font)
        aes_label.place(x=45, y=110)

        rsa_label = tk.Label(self, text="Symmetric encryption:", font=labels_font)
        rsa_label.place(x=635, y=110)

        rsa_button = tk.Button(self, text="RSA", bd='3', width=75, height=35, command=lambda: controller.show_frame(RSA_main_page))
        rsa_button.place(x=35, y=180)

        aes_button = tk.Button(self, text="AES", bd='3', width=75, height=35, command=lambda: controller.show_frame(AES_main_page))
        aes_button.place(x=620, y=180)

        instruction_button = tk.Button(self, text="Instruction", bd='3', width=15, command=lambda: controller.show_frame(InstructionPage))
        instruction_button.place(x=1050, y=750)


# second window frame page1
class RSA_main_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        label = ttk.Label(self, text="Page 1", font=main_labels_font)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))

        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text="Page 2", command=lambda: controller.show_frame(AES_main_page))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


# third window frame page2
class AES_main_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        label = ttk.Label(self, text="Page 2", font=main_labels_font)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Page 1", command=lambda: controller.show_frame(RSA_main_page))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)


class InstructionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_label = tk.Label(self, text="Instruction Page:", fg="black", bg="yellow", font=main_labels_font)
        main_label.pack(pady=10)

        button1 = tk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))
        button1.place(x=50, y=200)



# Driver Code
app = tkinterApp()
app.title("Amit Dorman's Encryption And Decryption app")
app.geometry("1200x800")
app.mainloop()
