from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
root  = Tk()
root.title("posts")
root.geometry("1900x1080")

#creating a main frame 
main_frame = Frame(root)
main_frame.pack(fill = BOTH, expand = 1)


#creating a canvas

my_canvas = Canvas(main_frame)
my_canvas.pack(side = LEFT, fill = BOTH, expand = 1)

#creating a scrollbar

my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
my_scrollbar.pack(side = RIGHT, fill = Y)

#configure the canvas 
my_canvas.configure(yscrollcommand = my_scrollbar.set)

my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

#creating another frame 

second_frame =  Frame(my_canvas)

#add that new frame to the canvas in the window

my_canvas.create_window((0,0), window = second_frame, anchor = "nw")





imgList = ["assets/machine1.jpg", "assets/farmingdrone.webp", "assets\machine_seeder.jpg", "assets/tractor.jpg" ]

for i in range(4):
    img1 = ImageTk.PhotoImage(Image.open(imgList[i]).resize((600, 300), Image.LANCZOS))
    label1 = Label(second_frame, image = img1, )
    label1.refImg = img1
    label1.pack()
    despLabel1 = Label(second_frame, text = "Tractor\n 1 Year Used \n In perfectly fine condition", font=(20))

    despLabel1.pack()
    priceLabel1 = Label(second_frame, text = "10000/-", font = (20) )
    priceLabel1.pack()


def popup():
    popupwindow = Toplevel(root)
    popupwindow.title("Upload.....!")
    popupwindow.geometry("700x500+450+150")
    
    nameLabel = Label(popupwindow, text = "Name:")
    nameLabel.place(x = 100, y = 20)
    
    nameEntry = Entry(popupwindow, width = 50)
    nameEntry.place(x = 200, y=20)
    
    contactLabel = Label(popupwindow, text = "Contact No.:")
    contactLabel.place(x = 100, y = 70)
    
    contactEntry = Entry(popupwindow, width = 50)
    contactEntry.place(x = 200, y=70)
    
    locationLabel = Label(popupwindow, text = "Location:")
    locationLabel.place(x = 100, y = 120)
    
    locationEntry = Entry(popupwindow, width = 50)
    locationEntry.place(x = 200, y=120)
    
    uploadImageLabel = Label(popupwindow, text = "Upload Image:")
    uploadImageLabel.place(x=100, y = 170)
    
    uploadImageButton = Button(popupwindow, text="Select Image!", command = openFileDialogBox)
    uploadImageButton.place(x=200, y=170)
    
    descrptionLabel = Label(popupwindow, text = "Description about product:", font= (30))
    descrptionLabel.place(x = 150, y = 220)
    
    descriptionEntry = Text(popupwindow, height=10, width = 50)
    descriptionEntry.place(x = 100, y = 250)
    
    submitBtn = Button(popupwindow, text = "Submit", bg = "green", command = None),
    submitBtn.place(x=00, y = 320)
    
def openFileDialogBox():
    filePath = filedialog.askopenfilename()
    return 
    
    
    
    



Button(root, text="upload", command = popup).place(x = 1400, y = 20)

# img1 = ImageTk.PhotoImage(Image.open("assets/machine1.jpg"))
# btn1 = Label(second_frame, image = img1, height= 300, width=600)
# btn1.pack()
# despLabel1 = Label(second_frame, text = "Farming Machine \n 1 Year Used \n In perfectly fine condition", font=(20))
# despLabel1.pack()
# priceLabel1 = Label(second_frame, text = "20000/-", font = (20) )
# priceLabel1.pack()
    

# img2 = ImageTk.PhotoImage(Image.open("assets/farmingdrone.webp"))
# btn2 = Label(second_frame, image = img2, height= 300, width=600)
# btn2.pack()
# despLabel2 = Label(second_frame, text = "Farming Drone\n 1.3 Year Used \n In perfectly fine condition", font=(20))
# despLabel2.pack()
# priceLabel2 = Label(second_frame, text = "11000/-", font = (20) )
# priceLabel2.pack()    

    

# img3 = ImageTk.PhotoImage(Image.open("assets\machine_seeder.jpg"))
# btn3 = Label(second_frame, image = img3, height= 300, width=600)
# btn3.pack()
# despLabel3 = Label(second_frame, text = "Machine Seeder \n 6 Months Used \n In perfectly fine condition", font=(20))
# despLabel3.pack()
# priceLabel3 = Label(second_frame, text = "7000/-", font = (20) )
# priceLabel3.pack()    


# img4 = ImageTk.PhotoImage(Image.open("assets/tractor.jpg"))
# btn4 = Label(second_frame, image = img4, height= 300, width=600)
# btn4.pack()
# despLabel4 = Label(second_frame, text = "Tractor\n 1 Year Used \n In perfectly fine condition", font=(20))
# despLabel4.pack()
# priceLabel4 = Label(second_frame, text = "50000/-", font = (20) )
# priceLabel4.pack()  

root.mainloop()