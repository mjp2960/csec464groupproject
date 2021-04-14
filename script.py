from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):   
    if(line<50):
        mylist.insert(END, "This is mactime entry " + str(line))
    else:
        mylist.insert(END, "This is mactime entry " + str(line))
   

mylist.pack( side = LEFT, fill = BOTH, ipadx=10)
scrollbar.config( command = mylist.yview )

mainloop()
