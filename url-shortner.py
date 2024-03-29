from tkinter import *
from tkinter import ttk
import pyshorteners
import webbrowser

root=Tk()
root.title("URL Shortner")
root.geometry("500x250")
root.resizable(0,0)
label=ttk.Label(root, text="URL Shortner", fon=("Popping", 25))
label.grid(row=0)

url_input=ttk.Label(root, text="Enter URL: ")
url_input.grid(row=1, column=0, pady=10)

url=StringVar()
url_entry=ttk.Entry(root, textvariable=url, width=40)
url_entry.grid(row=1, column=1, pady=10)

shortner_button=ttk.Button(root, text="Shorten", command= lambda: shorter_url(url.get()))
shortner_button.grid(row=2, column=0, pady=10)

shortner_url_label=ttk.Label(root, text="Shortened Url: ")
shortner_url_label.grid(row=4, column=0, pady=10)

output_url=StringVar()
output_url_entry=ttk.Entry(root, textvariable=output_url, width=40)
output_url_entry.grid(row=4, column=1, pady=10)

copy_button=Button(root, text="Copy", command= lambda: copy_url(output_url.get()))
copy_button.grid(row=5, column=0, pady=10)

open_button=ttk.Button(root, text="Open", command= lambda: open_url(url.get()))
open_button.grid(row=5, column=1, pady=10)

def shorter_url(url):
    try:
        short_url=pyshorteners.Shortener().tinyurl.short(url)
        output_url.set(short_url)
    except:
        print("Invalid URL")

def copy_url(url):
    try:
        url_entry.clipboard_clear()
        url_entry.clipboard_append(url)
        print("Url copied to clipboard")
    except:
        print("Invalid URL")

def open_url(url):
    try:
        webbrowser.open(url)
    except:
        print("Invalid URL")

root.mainloop()