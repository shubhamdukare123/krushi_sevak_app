from tkinter import *
from PIL import ImageTk, Image

root  = Tk()
root.title("posts")
root.geometry("1900x1080")


img1 = ImageTk.PhotoImage(Image.open("assets/tractor.jpg"))
btn1 = Button(root, image = img1, command = None, height= 300,width = 600)

btn1.place(x=400, y=50)


despLabel1 = Label(root, text = "Tractor\n 1 Year Used \n In perfectly fine condition", font=(20))

despLabel1.place(x=400, y = 390)
priceLabel1 = Label(root, text = "10000/-", font = (20) )
priceLabel1.place(x = 800, y= 420)


# img2 = ImageTk.PhotoImage(Image.open("assets/tractor.jpg"))
# btn2 = Button(root, image = img2, command = None, height= 300,width = 600)

# btn2.place(x=400, y=500)

# #likebtnimg = ImageTk.PhotoImage(Image.open("assets/likewhite.png"), height = 10, width=20)


# despLabel2 = Label(root, text = "Tractor\n 1 Year Used \n In perfectly fine condition", font=(20))

# despLabel2.place(x=400, y = 390)
# priceLabel2 = Label(root, text = "10000/-", font = (20) )
# priceLabel2.place(x = 800, y= 420)


# img3 = ImageTk.PhotoImage(Image.open("assets/tractor.jpg"))
# btn3 = Button(root, image = img3, command = None, height= 300,width = 600)

# btn3.place(x=400, y=50)

# likebtnimg3 = ImageTk.PhotoImage(Image.open("assets/likewhite.png"), height = 10, width=20)


# despLabel3 = Label(root, text = "Tractor\n 1 Year Used \n In perfectly fine condition", font=(20))

# despLabel3.place(x=400, y = 390)
# priceLabel3 = Label(root, text = "10000/-", font = (20) )
# priceLabel3.place(x = 800, y= 420)


root.mainloop()