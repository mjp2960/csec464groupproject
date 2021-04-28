from tkinter import *

mac_entry = "Thu Aug 21 2003 01:20:38      512       m.c.       -/-rwxrwxrwx     0        0        4        /file1.dat"

def parse_table(root, frame, scrollbar, path):
    content_list = content_reader(path)
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
        show_date = [i.split()[0] for i in content_list]
        return show_date

    def getSize():
        show_size = [i.split()[1] for i in content_list]
        return show_size

    def getActivityType():
        show_activity_type = [i.split()[2] for i in content_list]
        return show_activity_type

    def getUnixPermissions():
        show_unix_permissions = [i.split()[3] for i in content_list]
        return show_unix_permissions

    def getUserId():
        show_user_id = [i.split()[4] for i in content_list]
        return show_user_id

    def getGroupId():
        show_group_id = [i.split()[5] for i in content_list]
        return show_group_id

    def getInode():
        show_inode = [i.split()[6] for i in content_list]
        return show_inode

    def getFileName():
        show_file_name = [i.split()[7:] for i in content_list]
        return show_file_name

    def callback(*args):
        if variable.get() == "Date/Time":
            listboxTest.delete(0, END)
            for line in getDateTime():
                listboxTest.insert(END, line)
        elif variable.get() == "Size":
            listboxTest.delete(0, END)
            for line in getSize():
                listboxTest.insert(END, line)
        elif variable.get() == "Activity Type":
            listboxTest.delete(0, END)
            for line in getActivityType():
                listboxTest.insert(END, line)
        elif variable.get() == "Unix Permissions":
            listboxTest.delete(0, END)
            for line in getUnixPermissions():
                listboxTest.insert(END, line)
        elif variable.get() == "User ID":
            listboxTest.delete(0, END)
            for line in getUserId():
                listboxTest.insert(END, line)
        elif variable.get() == "Group ID":
            listboxTest.delete(0, END)
            for line in getGroupId():
                listboxTest.insert(END, line)
        elif variable.get() == "inode":
            listboxTest.delete(0, END)
            for line in getInode():
                listboxTest.insert(END, line)
        elif variable.get() == "File Name":
            listboxTest.delete(0, END)
            for line in getFileName():
                listboxTest.insert(END, line)

    variable.trace("w", callback)

    
def content_reader(path):
    f = open(path)
    line = f.readline()
    content_lis=[]
    adate = ''
    while line:
        strlis = line.split()
        if(len(strlis) >= 12):
            adate = '_'.join([i for i in strlis[:5]])
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

def build_gui():
    #Mactime variables go here
    root = Tk()
    # Code to add widgets will go here...
    file_path = "flsMactime.txt"

    root.title("Mactime Beautifier")
    root.resizable(TRUE, TRUE)

    back = Frame(root)
    back.pack(expand=True, fill=BOTH)


    scrollbar = Scrollbar(back)

    # Frame used to hold filter listbox and scrollbar
    bottom = Frame(root)

    scrollbar_bottom = Scrollbar(bottom)

    # Creates filter listbox
    parse_table(root, bottom, scrollbar_bottom, file_path)

    bottom.pack(side=BOTTOM, fill=BOTH)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar_bottom.pack(side=RIGHT, fill=Y)

    display_mactime(back, scrollbar, file_path)


    root.mainloop()

def main():
    build_gui()

if __name__ == '__main__':
    main()
