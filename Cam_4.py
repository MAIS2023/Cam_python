import cv2
from tkinter import *
prog = Tk()
prog.title('Selfie Camera')
prog.geometry('350x450+400+100')
title = Label(prog,text='Selfie Camera',fg='white',bg='black')
title.pack(fill=X)
def cam():
    camm = cv2.VideoCapture(0)
    ret,img = camm.read()
    cv2.imwrite("D:\\cam.png",img)
    del(cam)
photo = PhotoImage(file="C:\\Users\\TOSHIBA\\Downloads\\images.png")
image = Label(prog,image=photo)
image.place(x=10,y=40,width=345,height=272)

btn1 = Button (prog,text="Take Photo",bg="black",fg="white",width=20,height=2,command=cam)
btn1.place(x=100,y=300)


btn2 = Button(prog,text="Close Program",bg="black",fg="white",width=20,height=2,command = prog.quit)
btn2.place(x=100,y=355)

prog = mainloop()