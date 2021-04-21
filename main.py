from tkinter import *

def display_mactime(frame, scrollbar):
    mylist = Listbox(frame, yscrollcommand=scrollbar.set, width=100, height=5, bg="white", fg="black")
    for line in range(100):
        mylist.insert(END,
                      "Thu Aug 21 2003 01:20:38      512       m.c.       -/-rwxrwxrwx     0        0        4        /file1.dat")

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)

def build_gui():
    #Mactime variables go here
    root = Tk()
    # Code to add widgets will go here...

    scrollbar = Scrollbar(root)
    scrollbar.pack(side = RIGHT, fill = Y)

    back = Frame(root)
    back.pack(expand=True)

    display_mactime(back, scrollbar)

    root.mainloop()

def parse_table():
    print("Here you go Steve")

def main():
    build_gui()

if __name__ == '__main__':
    main()
