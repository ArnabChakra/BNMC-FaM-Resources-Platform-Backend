import rsa
from tkinter import *
from tkinter import filedialog

# Function for opening the
top = Tk()
top.geometry("450x190")

label_file_explorer = Label(top,
                            text="BNMC FAM Encryption Tool",
                            width=62, height=4,
                            fg="blue").place(x=10, y=1)


def encrypt_it():
    uri = inputtxt.get(1.0, "end-1c")

    publicKey, privateKey = rsa.newkeys(1024)

    try:
        encUri = rsa.encrypt(uri.encode(), publicKey)

        print("original string: ", uri)
        print("encrypted string: ", encUri)

        # Export public key in PKCS#1 format, PEM encoded
        publicKeyPkcs1PEM = publicKey.save_pkcs1()
        print(publicKeyPkcs1PEM)
        # Export private key in PKCS#1 format, PEM encoded
        privateKeyPkcs1PEM = privateKey.save_pkcs1()
        print(privateKeyPkcs1PEM)

        with open('./bnmc_fam_backend/db_cred_uri.txt', mode='wb') as db_cred_file:
            keydata = db_cred_file.write(encUri)

        with open('public.pem', mode='wb') as publicfile:
            keydata = publicfile.write(publicKeyPkcs1PEM)

        with open('./bnmc_fam_backend/private.pem', mode='wb') as privatefile:
            keydata = privatefile.write(privateKeyPkcs1PEM)

        label_response.configure(text="Encryption complete!", fg="green")

    except Exception as e:
        print(e)
        label_response.configure(text="Encryption failed!", fg="red")


# TextBox Creation
inputtxt = Text(top,
                height=1,
                width=50)
inputtxt.place(x=25, y=50)

label_response = Label(top, text="", width=52, height=4, fg="green")
label_response.place(x=10, y=70)

button_submit = Button(top,
                       text="Submit",
                       command=encrypt_it).place(x=150, y=130)

button_exit = Button(top,
                     text="Exit",
                     command=top.destroy).place(x=225, y=130)

top.mainloop()