import tkinter as tk
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
from psd_tools import PSDImage
from tkinter.filedialog import askopenfilename


def getfile():
    filename = askopenfilename(filetypes=[('PSD files', '.psd')])
    psd = PSDImage.load(filename)
    # print(psd)
    layers = psd.layers
    for layer in layers:
        layer_image = layer.as_PIL()
        print(layer_image, 'original')

        cropped = layer_image.crop((100, 100, 420, 420))
        print(cropped, 'Square')

        cropped1 = layer_image.crop((100, 100, 400, 700))
        print(cropped1, 'Half Page')

        cropped2 = layer_image.crop((100, 100, 340, 500))
        print(cropped2, 'Potrait')

        new = cropped.save('new.psd', 'PSD').upper()
        print(new)
        # arr = np.array(layer)
        # img = Image.fromarray(arr)
        # print(type(img))


if __name__ == '__main__':
    top = Tk()
    top.geometry("1100x600")
    top.resizable(0,0)
    # top.iconbitmap('reflowicon.ico')
    top.title("Banner ad Reflow")
    top.configure(background="White")
    ban_img = Image.open("reflowuikit.png")
    reflowuikit = ImageTk.PhotoImage(ban_img)
    image1 = Label(top, image=reflowuikit)
    image1.image = reflowuikit
    image1.place(relx=.5, rely=.3, anchor="c")

    label = ttk.Label(top, text="Generate ad banners in an easy way")
    label1 = ttk.Label(top, text="Customize your own templates to reflow banners more quickly,"
                                  " easily, and creatively")

    label.place(relx=.5, rely=.5, anchor="c")
    label1.place(relx=.5, rely=.6, anchor="c")

    choose_btn = Button(top, text="Choose File", command=getfile)
    choose_btn.place(relx=.5, rely=.7, anchor="c")

    top.mainloop()
