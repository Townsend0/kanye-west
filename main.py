import tkinter
import requests

x = requests.get(url = "https://api.kanye.rest/")
x.status_code

def txt():
    x = requests.get(url = "https://api.kanye.rest/")
    x.status_code
    b.itemconfig(f, text = x.json()["quote"])

a = tkinter.Tk()
a.geometry("400x600")

b = tkinter.Canvas(width = 300, height = 400, highlightthickness = 0)
b_img = tkinter.PhotoImage(file = "background.png")
b.create_image(150, 200, image = b_img)
f = b.create_text(150, 200, text = x.json()["quote"], font = ("normal", 13, "normal"), width = 225)
b.pack(pady = 25)

img = tkinter.PhotoImage(file = "kanye.png")
c = tkinter.Button(image = img, command = txt)
c.pack()

a.mainloop()