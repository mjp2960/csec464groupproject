from tkinter import *

def parse_table():
    print("Here you go Steve")
    
def content_reader(path):
    f = open(path)
    line = f.readline()
    content_lis=[]
    adate = ''
    while line:
        strlis = line.split()
        entri_lis = []
        if(len(strlis) >= 12):
            adate = '_'.join([i for i in strlis[:5]])
            acontent = ' '.join([i for i in strlis])
        else:
            acontent = ' '.join([i for i in strlis])
            acontent = adate + ' ' + acontent
        content_lis.append(acontent)
        line = f.readline()
    f.close()
    return content_lis

def display_mactime(frame, scrollbar):
    content_lis = content_reader(path)
    mylist = Listbox(frame, yscrollcommand=scrollbar.set, width=100, height=5, bg="white", fg="black")
    for line in content_lis:
        mylist.insert(END,line)

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

def main():
    build_gui()

if __name__ == '__main__':
    main()
