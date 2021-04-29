from tkinter import *


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

    count=0
    red_index=[] #file changed (metadata)
    blue_index=[] #file accessed
    green_index=[] #file created
    purple_index=[] # file modified (data)
    for line in content_lis:
        #print(line[36:40])
        if(line[39]=='b'):
            green_index.append(count)
        elif(line[38]=='c'):
            red_index.append(count)
        elif(line[36]=='m'):
            purple_index.append(count)
        elif(line[37]=='a'):
            blue_index.append(count)
        mylist.insert(END,line)
        count+=1

    for i in red_index:
        mylist.itemconfig(i, {'fg': "red"})
    for i in blue_index:
        mylist.itemconfig(i, {'fg': "blue"})
    for i in green_index:
        mylist.itemconfig(i, {'fg': "green"})
    for i in purple_index:
        mylist.itemconfig(i, {'fg': "purple"})



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
    parse_table(root, bottom, scrollbar_bottom, file)

    bottom.pack(side=BOTTOM, fill=BOTH)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar_bottom.pack(side=RIGHT, fill=Y)

    display_mactime(back, scrollbar, file)

    root.mainloop()

def main(argv):
    file=""
    if(len(argv)==0):
        print("Mactime Beautifier accepts standardized mactime tables in .txt format.")
        file = input("Enter the path to your file, or '-h' for help: ")
    else:
        file = argv[0]
    bool_run=True
    if(file=='-h'):
        print("\nMactime Beautifier is a tool for easy sorting and visualization of mactime tables.")
        print("It accepts a mactime table in text format by system argument or stdio.")
        print("The output is then sortable by several parameters, and color coded.")
        print("Green: File Created, Red: File Changed (metadata), Purple: File Modified, Blue: File Accessed.")
        print("Priority is given to the color coding in the above order.")
        bool_run=False
    if(bool_run):
        try:
            build_gui(file)
        except:
            print("\nInvalid input. Ensure that you entered the full path to your file, including the extension.")
            print("Enter '-h' for help.")

if __name__ == '__main__':
    main(sys.argv[1:])
