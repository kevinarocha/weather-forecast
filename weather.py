import sys
from requests_html import HTMLSession
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image # pip install Pillow



root = Tk()


def begin():
    global e1
    root.geometry("550x400")
    text=Label(root, text = "Please enter a city name. ", font = ('Times', 20, "bold"), fg="blue")
    text.place(x=80, y = 20)

    e1 = Entry(root, relief=SUNKEN)
    e1.place(x=170, y=80)

    begin=Button(root, text="Get Weather", relief = GROOVE)
    begin.place(x=200, y=150)
    begin.bind("<Button-1>", start_search)


def start_search(event):
    global e1
    h = e1.get()
    s = HTMLSession()
    query = h
    url = f'https://www.google.com/search?q=weather+{query}'
    # you can put dictionary separate and just have it passed into headers like that 
    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
    
    # first = true is for it to not making it return it as a list, since it's just one item.
    # we add the .text so then it would not show <Element 'title'> and instead show 
    # weather london - Google Search
    temp = r.html.find('span#wob_tm', first=True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
    desc = r.html.find('div.VQF4g', first = True).find('span#wob_dc', first = True).text

    window=Toplevel()
    window.geometry("350x200")
    hours=Label(window, text= f"The weather forecast for {query} is \n {temp} {unit} {desc}", font = ('Times', 12, "bold"))
    hours.place(x=30, y=20)


begin()

root.mainloop()
