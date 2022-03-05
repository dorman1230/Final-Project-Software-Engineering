import tkinter as tk
from generaetore import *
import rsa


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
        for F in (StartPage, RSA_main_page, AES_main_page, RSA_generate_keys_page, prime_numbers_page):
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


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)



        main_label = tk.Label(self, text="Encryption And Decryption System: ", fg="black", bg="yellow", font=main_labels_font)
        main_label.pack(pady=10)

        aes_label = tk.Label(self, text="Asymmetric encryption:", font=labels_font)
        aes_label.place(x=45, y=110)

        rsa_label = tk.Label(self, text="Symmetric encryption:", font=labels_font)
        rsa_label.place(x=635, y=110)

        rsa_button = tk.Button(self, text="RSA", bd='3', width=45, height=22, font=("Verdana", 14), command=lambda: controller.show_frame(RSA_main_page))
        rsa_button.place(x=35, y=180)

        aes_button = tk.Button(self, text="AES", bd='3', width=45, height=22, font=("Verdana", 14), command=lambda: controller.show_frame(AES_main_page))
        aes_button.place(x=620, y=180)


class RSA_main_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def set_dcrypted_text():
            rsa_private_key = text_box_private_key.get("1.0", "end")
            text_to_decrypt = text_box_text_to_decrypt.get("1.0", "end")

            text_decryption_encryption = decrypt(rsa_private_key, text_to_decrypt)

            text_box_after_decryption.delete(0, "end")
            text_box_after_decryption.insert(0, str(text_decryption_encryption))


        def set_encrypted_text():
            rsa_public_key = text_box_public_key.get("1.0", "end")
            text_to_encrypt = text_box_text_to_encrypt.get("1.0", "end")

            text_after_encryption = encrypt(rsa_public_key, text_to_encrypt)

            text_box_after_encryption.delete(0, "end")
            text_box_after_encryption.insert(0, str(text_after_encryption))


        def clear():
            text_box_text_to_encrypt.delete("1.0", "end")
            text_box_public_key.delete("1.0", "end")
            text_box_after_encryption.delete(0, "end")
            text_box_text_to_decrypt.delete("1.0", "end")
            text_box_private_key.delete("1.0", "end")
            text_box_after_decryption.delete(0, "end")


        mainlabel = tk.Label(self, text="RSA", font=main_labels_font)
        mainlabel.pack(pady=10)

        #Encryption staff
        encrypt_label = tk.Label(self, text="encrypt:", fg="black", bg="blue", font=("Verdana", 22))
        encrypt_label.place(x=200, y=100)

        text_to_encrypt_label = tk.Label(self, text="input:", fg="black", font=("Verdana", 18))
        text_to_encrypt_label.place(x=50, y=160)

        public_key_label = tk.Label(self, text="public key:", fg="black", font=("Verdana", 18))
        public_key_label.place(x=50, y=220)

        after_encryption_label = tk.Label(self, text="after encryption:", fg="black", font=("Verdana", 18))
        after_encryption_label.place(x=50, y=320)

        text_box_text_to_encrypt = tk.Text(self, width=35, height=2)
        text_box_text_to_encrypt.place(x=280, y=160)

        text_box_public_key = tk.Text(self, width=35, height=2)
        text_box_public_key.place(x=280, y=220)

        text_box_after_encryption = tk.Entry(self)
        text_box_after_encryption.place(x=280, y=320, width=285, height=35)

        button_get_text_to_encrypt = tk.Button(self, text="encrypt", bd='3', width=20, font=("Verdana", 12), command=lambda: set_encrypted_text())
        button_get_text_to_encrypt.place(x=180, y=275)

        #Decryption staff
        decryption_label = tk.Label(self, text="decryption:", fg="black", bg="green", font=("Verdana", 22))
        decryption_label.place(x=800, y=100)

        text_to_decrypt_label = tk.Label(self, text="encrypted input:", fg="black", font=("Verdana", 18))
        text_to_decrypt_label.place(x=650, y=160)

        private_key_label = tk.Label(self, text="private key:", fg="black", font=("Verdana", 18))
        private_key_label.place(x=650, y=220)

        after_decryption_label = tk.Label(self, text="after decryption:", fg="black", font=("Verdana", 18))
        after_decryption_label.place(x=650, y=320)

        text_box_text_to_decrypt = tk.Text(self, width=35, height=2)
        text_box_text_to_decrypt.place(x=880, y=160)

        text_box_private_key = tk.Text(self, width=35, height=2)
        text_box_private_key.place(x=880, y=220)

        text_box_after_decryption = tk.Entry(self)
        text_box_after_decryption.place(x=880, y=320, width=285, height=35)

        button_get_text_to_decrypt = tk.Button(self, text="decrypt", bd='3', width=20, font=("Verdana", 12), command=lambda: set_dcrypted_text())
        button_get_text_to_decrypt.place(x=780, y=275)

        #create keys button
        generate_keys_button = tk.Button(self, text="generate keys", bd='3', width=20, font=("Verdana", 14), command=lambda: controller.show_frame(RSA_generate_keys_page))
        generate_keys_button.place(x=470, y=390)

        #clear button
        clear_button = tk.Button(self, text="clear", bd='3', fg="red", width=20, font=("Verdana", 12), command=lambda: clear())
        clear_button.place(x=40, y=550)

        #exit button
        exit_button = tk.Button(self, text="exit", bd='3', fg="red", width=20, font=("Verdana", 12), command=lambda: controller.show_frame(StartPage))
        exit_button.place(x=40, y=600)


class RSA_generate_keys_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def number_one_get_text():
            number_one = text_box_prime_number_one.get("1.0", "end")
            return number_one

        def number_two_get_text():
            number_two = text_box_prime_number_two.get("1.0", "end")
            return number_two

        def clear():
            text_box_prime_number_one.delete("1.0", "end")
            text_box_prime_number_two.delete("1.0", "end")
            text_box_public_key.delete(0, "end")
            text_box_private_key.delete(0, "end")


        def set_keys():
            number1 = int(number_one_get_text())
            number2 = int(number_two_get_text())

            if(isPrime(number1) == False) or (isPrime(number2) == False):
                text_box_public_key.delete(0, "end")
                text_box_public_key.insert(0, str("You have a problem with the prime numbers fix it"))

                text_box_private_key.delete(0, "end")
                text_box_private_key.insert(0, str("You have a problem with the prime numbers fix it"))

            else:
                public_key_rsa, private_key_rsa = generateKey(number1, number2)

                text_box_public_key.delete(0, "end")
                text_box_public_key.insert(0, str(public_key_rsa))

                text_box_private_key.delete(0, "end")
                text_box_private_key.insert(0, str(private_key_rsa))


        main_label = tk.Label(self, text="Create Keys", fg="black", bg="pink", font=("Verdana", 22))
        main_label.pack(pady=10)

        number_one_label = tk.Label(self, text="Enter a prime number greater than 17:", fg="black", font=("Verdana", 18))
        number_one_label.place(x=50, y=120)

        number_two_label = tk.Label(self, text="Enter a different prime number greater than 17:", fg="black", font=("Verdana", 18))
        number_two_label.place(x=50, y=180)

        text_box_prime_number_one = tk.Text(self, width=35, height=2)
        text_box_prime_number_one.place(x=700, y=120)

        text_box_prime_number_two = tk.Text(self,  width=35, height=2)
        text_box_prime_number_two.place(x=700, y=180)

        button_to_see_list_of_prime_numbers = tk.Button(self, text="prime numbers", bd='3', width=20, font=("Verdana", 12), command=lambda: controller.show_frame(prime_numbers_page))
        button_to_see_list_of_prime_numbers.place(x=850, y=245)

        generate_button = tk.Button(self, text="generate", bd='3', width=20, font=("Verdana", 12), command=lambda: set_keys())
        generate_button.place(x=470, y=300)

        public_key_label = tk.Label(self, text="Public key for encryption:", fg="black", font=("Verdana", 18))
        public_key_label.place(x=50, y=370)

        private_key_label = tk.Label(self, text="Private key for decryption:", fg="black", font=("Verdana", 18))
        private_key_label.place(x=50, y=430)

        text_box_public_key = tk.Entry(self)
        text_box_public_key.place(x=700, y=370, width=350, height=35)

        text_box_private_key = tk.Entry(self)
        text_box_private_key.place(x=700, y=430, width=350, height=35)

        #clear button
        clear_button = tk.Button(self, text="clear", bd='3', fg="red", width=20, font=("Verdana", 12), command=lambda: clear())
        clear_button.place(x=40, y=550)

        #exit button
        exit_button = tk.Button(self, text="exit", bd='3', fg="red", width=20, font=("Verdana", 12), command=lambda: controller.show_frame(RSA_main_page))
        exit_button.place(x=40, y=600)


class prime_numbers_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lowPrimes = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
                     197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                     293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                     401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                     503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613,
                     617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727,
                     733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                     853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967,
                     971, 977, 983, 991, 997]
        len_lowprimes = len(lowPrimes)

        mainlabel = tk.Label(self, text="Prime Numbers", font=main_labels_font)
        mainlabel.pack(pady=10)

        myscroll = tk.Scrollbar(self)
        myscroll.place(x=2000, y=2000)

        prime_numbers_list_box = tk.Listbox(self, yscrollcommand=myscroll.set, width=150, height=30)
        prime_numbers_list_box.pack(pady=11)
        for line in range(0, len_lowprimes):
            prime_numbers_list_box.insert(tk.END, str(lowPrimes[line]))
        prime_numbers_list_box.pack()

        myscroll.config(command=prime_numbers_list_box.yview)

        #exit button
        exit_button = tk.Button(self, text="exit", bd='3', fg="red", width=20, font=("Verdana", 12), command=lambda: controller.show_frame(RSA_generate_keys_page))
        exit_button.place(x=40, y=600)


class AES_main_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        mainlabel = tk.Label(self, text="AES Main Page", font=main_labels_font)
        mainlabel.pack(pady=10)

        #exit button
        exit_button = tk.Button(self, text="exit", bd='3', fg="red", width=20, font=("Verdana", 12), command=lambda: controller.show_frame(StartPage))
        exit_button.place(x=40, y=600)


# Driver Code
app = tkinterApp()
app.title("Amit Dorman's Encryption And Decryption App")

menubar = tk.Menu(app)

rsa_menu = tk.Menu(menubar, tearoff=0)
rsa_menu.add_command(label="Algorithm", command=show_rsa_algorithm)
menubar.add_cascade(label="RSA", menu=rsa_menu)

aes_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="AES", menu=aes_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)
help_menu.add_command(label="About...", command=show_about)
menubar.add_cascade(label="Help", menu=help_menu)

app.config(menu=menubar)

app.geometry("1200x800")
app.mainloop()