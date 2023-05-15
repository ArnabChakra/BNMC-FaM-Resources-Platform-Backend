from tkinter import *
from tkinter import filedialog
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from tkinter.ttk import Progressbar
import rsa
import pandas as pd

# Function for opening the
top = Tk()
top.geometry("450x350")

lbl1 = Label(top, text="File chosen : ")
lbl1.place(x=180, y=72)

lbl2 = Label(top, text="File chosen : ")
lbl2.place(x=180, y=142)

lbl3 = Label(top, text="File chosen : ")
lbl3.place(x=180, y=212)

master_file = None
private_key = None
encrypt_uri = None


# file explorer window
def browseFiles1():
    global master_file
    master_file = filedialog.askopenfilename(initialdir="/",
                                             title="Select Master Data File",
                                             filetypes=(("Text files",
                                                         "*.txt*"), ("all files",
                                                                     "*.*")))

    print(master_file)
    lbl1.configure(text="File chosen : " + master_file.split('/')[-1])


def browseFiles2():
    global private_key
    private_key = filedialog.askopenfilename(initialdir="/",
                                             title="Select Private Key File",
                                             filetypes=(("Text files",
                                                         "*.txt*"), ("all files",
                                                                     "*.*")))

    print(private_key)
    lbl2.configure(text="File chosen : " + private_key.split('/')[-1])


def browseFiles3():
    global encrypt_uri
    encrypt_uri = filedialog.askopenfilename(initialdir="/",
                                             title="Select Encrypted DB URI File",
                                             filetypes=(("Text files",
                                                         "*.txt*"), ("all files",
                                                                     "*.*")))

    print(encrypt_uri)
    lbl3.configure(text="File chosen : " + encrypt_uri.split('/')[-1])


def process():
    global private_key
    global master_file
    global encrypt_uri

    keydata = None
    encUri = None

    with open(encrypt_uri, mode='rb') as encUrifile:
        encUri = encUrifile.read()

    with open(private_key, mode='rb') as privatefile:
        keydata = privatefile.read()

    privkey = rsa.PrivateKey.load_pkcs1(keydata)

    uri = rsa.decrypt(encUri, privkey).decode()

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        label_response.configure(text="Successfully connected to Database!!")
    except Exception as e:
        print(e)
        label_response.configure(text="Failed to connect to Database.", fg="red")

    db = client['BNMC-FAM']
    collection = db['Resources']

    try:
        with client.start_session() as s:
            def cb(s):
                result = collection.delete_many({}, session=s)
                df = pd.read_csv(master_file, encoding="ISO-8859-1")
                df = df.fillna("")
                for index, row in df.iterrows():
                    data_entry = dict(row)
                    if data_entry['Zipcode'] != "":
                        data_entry['Zipcode'] = str(data_entry['Zipcode'])
                    collection.insert_one(data_entry, session=s)

            s.with_transaction(cb)

        label_response.configure(text="Successfully updated Database!!")
    except Exception as e:
        print(e)
        label_response.configure(text="Database update failed. Rolling back.", fg="red")

    # Create a File Explorer label


label_file_explorer = Label(top,
                            text="BNMC FAM Master Data Tool",
                            width=65, height=4,
                            fg="blue").place(x=20, y=10)

label_response = Label(top, text="", width=65, height=4, fg="green")
label_response.place(x=20, y=240)

button_explore1 = Button(top,
                         text="Browse Master Data File",
                         command=browseFiles1).place(x=20, y=70)

button_explore2 = Button(top,
                         text="Browse Private Key",
                         command=browseFiles2).place(x=20, y=140)

button_explore3 = Button(top,
                         text="Browse Encrypted DB URI",
                         command=browseFiles3).place(x=20, y=210)

button_submit = Button(top,
                       text="Submit",
                       command=process).place(x=150, y=300)

button_exit = Button(top,
                     text="Exit",
                     command=top.destroy).place(x=225, y=300)

top.mainloop()