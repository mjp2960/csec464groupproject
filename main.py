from tkinter import *
import sys

#tracks the data in the parse listbox dynamically
current_list = []

def enum_listbox(listbox):
    var = []
    for i in enumerate(listbox.get(0, END)):
        var.append(i[1].split())
    return var

def set_current_list(list):
    global current_list
    current_list = [i for i in list]

def numSort(data):
    num_data = []
    final_data = []
    for i in data:
        num_data.append(int(i))
    num_data.sort()
    for i in num_data:
        final_data.append(str(i))
    return final_data

def macToString(arr):
    line = macToString_Helper(arr)
    strlis = line.split()
    afile = ''.join([i for i in strlis[7:]])
    strlis = strlis[:7]
    acontent = ''.join([atab(i) for i in strlis])
    acontent = acontent + atab(afile)
    return acontent

def macToString_Helper(arr):
    out = ""
    for i in arr:
        if(out == ""):
            out = str(i)
        else:
            out = out + " " + str(i)
    return out

def color_listbox(listbox):
    for i in enumerate(listbox.get(0, END)):
        if(i[1][39] == 'b'):
            listbox.itemconfig(i[0], {'fg': "green"})
        elif(i[1][38] == 'c'):
            listbox.itemconfig(i[0], {'fg': "red"})
        elif(i[1][36] == 'm'):
            listbox.itemconfig(i[0], {'fg': "purple"})
        elif(i[1][37] == 'a'):
            listbox.itemconfig(i[0], {'fg': "blue"})

#sortby is the index at which to sort. 0 for time, 7 for filename, etc.
def sort_mac(listbox, sortby):
    sort_array = []
    tmp_array = []
    final_array=[]
    data = enum_listbox(listbox)
    if(sortby == 0):
        final_array = [i for i in current_list]
    else:
        for i in data:
            sort_array.append(i)
        for i in sort_array:
            tmp_array.append(i[sortby])
        if(sortby == 1 or sortby == 4 or sortby == 5 or sortby == 6):
            tmp_array = [i for i in numSort(tmp_array)]
        else:
            tmp_array.sort()

        for i in tmp_array:
            for j in sort_array:
                if(j[sortby]==i):
                    final_array.append(j)
                    sort_array.remove(j)
    listbox.delete(0, END)
    for line in final_array:
        listbox.insert(END, macToString(line))
    color_listbox(listbox)
    sort_array.clear()
    tmp_array.clear()
    final_array.clear()

def parse_table(root, frame, scrollbar, path):
    content_list = content_reader(path)
    activity_type = [
        "Modified",
        "Accessed",
        "Changed",
        "Birth Time",
        "Read Permissions",
        "Write Permissions",
        "Execute Permissions",
        "Reallocated/Deleted",
        "Original"
    ]

    variable1 = StringVar(root)
    variable1.set("Parse Information")

    parsed1 = OptionMenu(frame, variable1, *activity_type)
    parsed1.config(width=20)
    parsed1.pack(side="top")

    scrollbar.pack(side=RIGHT, fill=Y, anchor="sw")

    parsed_list = Listbox(frame, yscrollcommand=scrollbar.set,
                          width=100, height=5, bg="white", fg="black")
    parsed_list.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    scrollbar.config(command=parsed_list.yview)

    parse_mac = [i for i in content_list]

    # Parsing MAC times
    parse_modified = [s for s in parse_mac if "m" in s[2]]
    parse_accessed = [s for s in parse_mac if "a" in s[2]]
    parse_changed = [s for s in parse_mac if "c" in s[2]]
    parse_birth_time = [s for s in parse_mac if "b" in s[2]]

    # Parsing read/write/execute information
    parse_read = [s for s in parse_mac if "r" in s[3]]
    parse_write = [s for s in parse_mac if "w" in s[3]]
    parse_execute = [s for s in parse_mac if "x" in s[3]]

    # Parsing file information
    parse_reallocated = [s for s in parse_mac if "deleted" in s[7]]

    def callback(*args):
        if variable1.get() == "Modified":
            parsed_list.delete(0, END)
            for line in parse_modified:
                parsed_list.insert(END, macToString(line))
            color_listbox(parsed_list)
            set_current_list(parse_modified)
        elif variable1.get() == "Accessed":
            parsed_list.delete(0, END)
            for line in parse_accessed:
                parsed_list.insert(END, macToString(line))
            color_listbox(parsed_list)
            set_current_list(parse_accessed)
        elif variable1.get() == "Changed":
            parsed_list.delete(0, END)
            for line in parse_changed:
                parsed_list.insert(END, macToString(line))
            color_listbox(parsed_list)
            set_current_list(parse_changed)
        elif variable1.get() == "Birth Time":
            parsed_list.delete(0, END)
            for line in parse_birth_time:
                parsed_list.insert(END, macToString(line))
            color_listbox(parsed_list)
            set_current_list(parse_birth_time)
        elif variable1.get() == "Read Permissions":
            parsed_list.delete(0, END)
            for line in parse_read:
                parsed_list.insert(END, macToString(line))
            color_listbox(parsed_list)
            set_current_list(parse_read)
        elif variable1.get() == "Write Permissions":
            parsed_list.delete(0, END)
            for line in parse_write:
                parsed_list.insert(END, macToString(line))
            color_listbox(parsed_list)
            set_current_list(parse_write)
        elif variable1.get() == "Execute Permissions":
            parsed_list.delete(0, END)
            for line in parse_execute:
                parsed_list.insert(END, macToString(line))
            color_listbox(parsed_list)
            set_current_list(parse_execute)
        elif variable1.get() == "Reallocated/Deleted":
            parsed_list.delete(0, END)
            for line in parse_reallocated:
                parsed_list.insert(END, macToString(line))
            color_listbox(parsed_list)
            set_current_list(parse_reallocated)
        elif variable1.get() == "Original":
            parsed_list.delete(0, END)
            for line in content_list:
                parsed_list.insert(END, line)
            color_listbox(parsed_list)
            set_current_list(content_list)

    variable1.trace("w", callback)

    return parsed_list

def content_reader(path):
    f = open(path)
    line = f.readline()
    str_content_lis = []
    content_lis = []
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
        str_content_lis.append(acontent)
        line = f.readline()
    f.close()
    for i in str_content_lis:
        content_lis.append(i.split())
    return content_lis

# try make tab in window
def atab(s):
    leng = len(s)
    if (leng < 3):
        leng += 3
    tb = ((leng//4)+1)*4
    return s.ljust(tb)

def display_mactime(root, frame, scrollbar, path):
    parsing = [
        'Search ID',
        'Search Filename',
        'Search Time'
    ]
    content_list = content_reader(path)
    mylist = Listbox(frame, yscrollcommand=scrollbar.set, width=100,
                     height=5, bg="white", fg="black", font=("DejaVu Sans Mono", 9))

    for line in content_list:
        mylist.insert(END, macToString(line))

    color_listbox(mylist)

    mylist.pack(side=LEFT, fill=BOTH, expand=TRUE)
    scrollbar.config(command=mylist.yview)

    variable = StringVar(root)
    variable.set("Filter")

    parsed = OptionMenu(frame, variable, *parsing)
    parsed.config(width=20)
    parsed.pack(side="top")

    def callback(*args):
        pass

    variable.trace("w", callback)

def build_gui(file):
    # Mactime variables go here
    root = Tk()
    # Code to add widgets will go here...

    root.title("Mactime Beautifier")
    root.resizable(TRUE, TRUE)

    back = Frame(root)
    back.pack(expand=True, fill=BOTH)

    scrollbar = Scrollbar(back)

    # Frame used to hold parsing listbox and scrollbar
    bottom = Frame(root)

    scrollbar_bottom = Scrollbar(bottom)

    # Creates parsing listbox
    parsed_list = parse_table(root, bottom, scrollbar_bottom, file)

    bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Label for default listbox
    text = StringVar()
    mactime_label = Label(back, textvariable=text, anchor="w", justify=LEFT)
    mactime_label.pack(side=TOP, anchor="w")
    text.set("|               Data/Time                  |Size|Activity| Permissions | UID | GID | inode |                                File Name                                      |")

    display_mactime(root, back, scrollbar, file)

    # Sorting buttons for parsing listbox
    buttons = Frame(bottom)
    date_time_button = Button(buttons, text='Data/Time', command = lambda : sort_mac(parsed_list, 0))
    size_button = Button(buttons, text='Size', command = lambda : sort_mac(parsed_list, 1))
    activity_button = Button(buttons, text='Activity', command = lambda : sort_mac(parsed_list, 2))
    permissions_button = Button(buttons, text='Permissions', command = lambda : sort_mac(parsed_list, 3))
    uid_button = Button(buttons, text='UID', command = lambda : sort_mac(parsed_list, 4))
    gid_button = Button(buttons, text='GID', command = lambda : sort_mac(parsed_list, 5))
    inode_button = Button(buttons, text='inode', command = lambda : sort_mac(parsed_list, 6))
    filename_button = Button(buttons, text='File Name', command = lambda : sort_mac(parsed_list, 7))

    date_time_button.pack(side=LEFT)
    size_button.pack(side=LEFT)
    activity_button.pack(side=LEFT)
    permissions_button.pack(side=LEFT)
    uid_button.pack(side=LEFT)
    gid_button.pack(side=LEFT)
    inode_button.pack(side=LEFT)
    filename_button.pack(side=LEFT)

    buttons.pack(side=TOP, fill=X)

    root.mainloop()


# noinspection PyRedundantParentheses
def main(argv):
    if(len(argv) == 0):
        print("Mactime Beautifier accepts standardized mactime tables in .txt format.")
        file = input("Enter the path to your file, or '-h' for help: ")
    else:
        file = argv[0]
    bool_run = True
    if(file == '-h'):
        print("\nMactime Beautifier is a tool for easy sorting and visualization of mactime tables.")
        print("It accepts a mactime table in text format by system argument or stdio.")
        print("The output is then sortable by several parameters, and color coded.")
        print("Green: File Created, Red: File Changed (metadata), Purple: File Modified, Blue: File Accessed.")
        print("Priority is given to the color coding in the above order.")
        bool_run = False
    if(bool_run):
        try:
            build_gui(file)
        except:
            print(
                "\nInvalid input. Ensure that you entered the full path to your file, including the extension.")
            print("Enter '-h' for help.")
            print(file)


if __name__ == '__main__':
    main(sys.argv[1:])
