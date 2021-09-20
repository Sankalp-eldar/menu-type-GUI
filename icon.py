from tkinter import*
from PIL import ImageTk,Image


#relif = flat, groove, raised, ridge, solid, or sunken
op = "Logo2.png"
root= Tk()
root.wm_attributes("-topmost",True)
root.wm_attributes("-transparent","white")
#root.wm_attributes("-disabled",True)
root.config(bg="white")#"#000000")
root.geometry("+500+200")
#root.lift()
#root.config(border=0)
root.overrideredirect(True)


x = ImageTk.PhotoImage(Image.open(op))
can = Canvas(root,width=300,height=310,bg="white",highlightthickness=0)
can.create_image(0,0,anchor=NW,image=x)
can.pack()
Label(root,text="Loading...",bg="Black",fg="Red",font="None 14",width=0,pady=0).pack()
root.after(2000,root.destroy)
root.mainloop()
