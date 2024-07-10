from tkinter import *

window = Tk()
window.title("Frame - GUI")
window.geometry("600x600")

top_frame = Frame(window)
bottom_frame = Frame(window)

label1 = Label(top_frame, text = "Label 1", background= "blue")
label2  = Label(top_frame, text = "Label 2", background="pink")
label3 = Label(bottom_frame, text = "Window label 1 ", background= "green")
label4 = Label(bottom_frame, text = "Last of the labels", background= "yellow")
button1 = Button(bottom_frame, text = "Button 1")
button2 = Button(bottom_frame, text = "Button 2")


label1.pack(fill = BOTH, side = "left" ,expand = True)
label2.pack(fill = BOTH, side = "right", expand = True)
top_frame.pack(fill = BOTH, expand= True)
label3.pack(side  = "top",fill = BOTH, expand = True)
label4.pack(side = "left")
button1.pack(side="left" )
button2.pack(side="right", padx = 10, pady = 15)

bottom_frame.pack( fill = BOTH,expand = True)

window.mainloop()