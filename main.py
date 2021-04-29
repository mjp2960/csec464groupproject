from tkinter import *

#depricated?
mac_entry = "Thu Aug 21 2003 01:20:38      512       m.c.       -/-rwxrwxrwx     0        0        4        /file1.dat"

def parse_table(root, frame, scrollbar):
    parsing = [
        "Date/Time",
        "Size",
        "Activity Type",
        "Unix Permissions",
        "User ID",
        "Group ID",
        "inode",
        "File Name"
    ]
    variable = StringVar(root)
    variable.set("Filter Output")

    parsed = OptionMenu(frame, variable, *parsing)
    parsed.config(width=20)
    parsed.pack(side="top")

    listboxTest = Listbox(frame, yscrollcommand=scrollbar.set, width=100, height=5, bg="white", fg="black")
    listboxTest.pack(side=LEFT, fill=BOTH, expand=TRUE)
    scrollbar.config(command=listboxTest.yview)

    def getDateTime():
        show_date = mac_entry[0:26]
        return show_date

    def getSize():
        show_size = mac_entry[28:34]
        return show_size

    def getActivityType():
        show_activity_type = mac_entry[36:46]
        return show_activity_type

    def getUnixPermissions():
        show_unix_permissions = mac_entry[49:64]
        return show_unix_permissions

    def getUserId():
        show_user_id = mac_entry[68:70]
        return show_user_id

    def getGroupId():
        show_group_id = mac_entry[75:78]
        return show_group_id

    def getInode():
        show_inode = mac_entry[85:89]
        return show_inode

    def getFileName():
        show_file_name = mac_entry[93:107]
        return show_file_name

    def callback(*args):
        if variable.get() == "Date/Time":
            listboxTest.delete(0, END)
            for _ in range(100):
                listboxTest.insert(END, getDateTime())
        elif variable.get() == "Size":
            listboxTest.delete(0, END)
            for _ in range(100):
                listboxTest.insert(END, getSize())
        elif variable.get() == "Activity Type":
            listboxTest.delete(0, END)
            for _ in range(100):
                listboxTest.insert(END, getActivityType())
        elif variable.get() == "Unix Permissions":
            listboxTest.delete(0, END)
            for _ in range(100):
                listboxTest.insert(END, getUnixPermissions())
        elif variable.get() == "User ID":
            listboxTest.delete(0, END)
            for _ in range(100):
                listboxTest.insert(END, getUserId())
        elif variable.get() == "Group ID":
            listboxTest.delete(0, END)
            for _ in range(100):
                listboxTest.insert(END, getGroupId())
        elif variable.get() == "inode":
            listboxTest.delete(0, END)
            for _ in range(100):
                listboxTest.insert(END, getInode())
        elif variable.get() == "File Name":
            listboxTest.delete(0, END)
            for _ in range(100):
                listboxTest.insert(END, getFileName())

    variable.trace("w", callback)

    
def content_reader(path):
    f = open(path)
    line = f.readline()
    content_lis=[]
    adate = ''
    while line:
        strlis = line.split()
        if(len(strlis) >= 12):
            adate = ' '.join([i for i in strlis[:5]])
            strlis = strlis[5:]
            afile = ''.join([i for i in strlis[6:]])
            strlis = strlis[:6]
            acontent = ''.join([atab(i) for i in strlis])
            acontent = atab(adate) + acontent + atab(afile)
        else:
            afile = ''.join([i for i in strlis[6:]])
            strlis = strlis[:6]
            acontent = ''.join([atab(i) for i in strlis])
            acontent = atab(adate) + acontent + atab(afile)
        content_lis.append(acontent)
        line = f.readline()
    f.close()
    return content_lis

# try make tab in window
def atab(s):
    leng = len(s)
    if (leng < 3):
        leng += 3
    tb = ((leng//4)+1)*4
    return s.ljust(tb)

def display_mactime(frame, scrollbar, path):
    content_lis = content_reader(path)
    mylist = Listbox(frame, yscrollcommand=scrollbar.set, width=100, height=5, bg="white", fg="black",font=("DejaVu Sans Mono",9))
    for line in content_lis:
        mylist.insert(END,line)

    mylist.pack(side=LEFT, fill=BOTH, expand=TRUE)
    scrollbar.config(command=mylist.yview)

def build_gui(file):
    #Mactime variables go here
    root = Tk()
    # Code to add widgets will go here...

    root.title("Mactime Beautifier")
    root.resizable(TRUE, TRUE)

    back = Frame(root)
    back.pack(expand=True, fill=BOTH)


    scrollbar = Scrollbar(back)

    # Frame used to hold filter listbox and scrollbar
    bottom = Frame(root)

    scrollbar_bottom = Scrollbar(bottom)

    # Creates filter listbox
    parse_table(root, bottom, scrollbar_bottom)

    bottom.pack(side=BOTTOM, fill=BOTH)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar_bottom.pack(side=RIGHT, fill=Y)

    display_mactime(back, scrollbar, file)


    root.mainloop()

def main(argv):
    file=""
    if(len(argv)==0):
        print("Mactime Beautifier accepts standardized mactime tables in .txt format.")
        file = input("Enter the path to your file: ")
    else:
        file = argv[0]
    build_gui(file)

if __name__ == '__main__':
    main(sys.argv[1:])
