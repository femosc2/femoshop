from tkinter import ttk, Frame, StringVar, Label, Tk, LEFT, RIGHT, X, Y, TOP, filedialog, messagebox
from PIL import Image, ImageFilter

root = Tk()

def blur(event):
    img = Image.open(root.file)
    blurred = img.filter(ImageFilter.GaussianBlur(radius=15))
    blurred.save("file.png")

def choose_image(event):
    root.file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
    filetypes = (("jpeg files","*.jpg"),("png files","*.png")))
    choosen_text.set(root.file)
    return root.file

def change_hue(event):
    img = Image.open(root.file)
    layer = Image.new('RGB', img.size, 'blue') # "hue" selection is done by choosing a color...
    hue = Image.blend(img, layer, 0.5)
    hue.save("file.png")
    




#****************** TkInter ********************
root.title("FeMoShop CS0")

frame = Frame(root)

choosen_text = StringVar()
choosen_text.set("No image chosen!")
choosen_image_label = Label(frame, textvariable=choosen_text)
choosen_image_label.pack()

action_text = StringVar()
action_text.set("Choose a filter!")
label = Label(frame, textvariable=action_text)
label.pack()



button1 = ttk.Button(frame, text="Blur")
button2 = ttk.Button(frame, text="Darken")
button3 = ttk.Button(frame, text="Brighten")
button4 = ttk.Button(frame, text="Change Hue")
button5 = ttk.Button(frame, text="Woo")
button6 = ttk.Button(frame, text="filler")

chooseImageButton = ttk.Button(frame, text="Choose Image!")
chooseImageButton.pack(side=TOP, fill=Y)

button1.bind("<Button-1>", blur)
chooseImageButton.bind("<Button-1>", choose_image)

button4.bind("<Button-1>", change_hue)
chooseImageButton.bind("<Button-1>", choose_image)

buttons = [
    button1,
    button2,
    button3,
    button4,
    button5,
    button6
]

for button in buttons:  
        button.pack(side=LEFT, fill=X)
frame.pack()




root.mainloop()