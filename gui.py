from tkinter import *

#Mactime variables go here

root = Tk()
# Code to add widgets will go here...

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

back = Frame(root)
back.pack(expand=True)

mylist = Listbox(back, yscrollcommand = scrollbar.set, width=100, height=5, bg="white", fg="black")
for line in range(100):
    mylist.insert(END, "Thu Aug 21 2003 01:20:38      512       m.c.       -/-rwxrwxrwx     0        0        4        /file1.dat")

mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = mylist.yview)


root.mainloop()


'''
box=Frame(top, width=5000)
box.pack()
box2=Frame(top)
box2.pack(side = BOTTOM)
entry = Message(box, text="Thu Aug 21 2003 01:20:38      512       m.c.       -/-rwxrwxrwx     0        0        4        /file1.dat")
entry.pack(side = BOTTOM)
entry2 = Message(box2, text="Second Mactime entry goes here")
entry2.pack(side = BOTTOM)
'''