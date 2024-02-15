from tkinter import *
import backend
# colors
background_dark = '#2A363B'
background_dark_res = '#14213D'
background_withe = '#F9F6EE'
background_withe_res = '#E5E5E5'
balck = '#222222'
light = '#DEE4E7'
blue_light = '#0049B7'
blue_daek = '#0070F7'
orang_t = '#FF847C'
orang_numbers = '#FCA311'
green_light = '#00C04B'
green_dark = '#228B22'
red = '#F60100'

win = Tk()
win.geometry("405x250+800+300")
# win.resizable(0, 0)
win.title("Library")
win.config(bg=light)


def clear_list():
    list1.delete(0, END)

def fill_list(books):
    for book in books:
        list1.insert(END, book)

# _________________________


l1 = Label(win,text='Title', bg=light)
l1.grid(row=0, column=0, pady=3)

title_text = StringVar()
e1 = Entry(win, textvariable=title_text, bg=background_dark, fg=light)
e1.grid(row=0, column=1, pady=3)
# _________________________


l2 = Label(win,text='Author', bg=light)
l2.grid(row=0, column=2, pady=3)

author_text = StringVar()
e2 = Entry(win, textvariable=author_text, bg=background_dark, fg=light)
e2.grid(row=0, column=3, pady=3)
# _________________________


l3 = Label(win,text='Year', bg=light)
l3.grid(row=1, column=0, pady=3)

year_text = StringVar()
e3 = Entry(win, textvariable=year_text, bg=background_dark, fg=light)
e3.grid(row=1, column=1, pady=3)

# _________________________


l3 = Label(win,text='SBN', bg=light)
l3.grid(row=1, column=2, pady=3)

sbn_text = StringVar()
e4 = Entry(win, textvariable=sbn_text, bg=background_dark, fg=light)
e4.grid(row=1, column=3, pady=3)
# _________________________


# Listbox & Scrollbar 
list1 = Listbox(win, width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, padx=9)

sc1 = Scrollbar(win, )
sc1.grid(row=2, column=2, rowspan=6, padx=0)

list1.configure(yscrollcommand=sc1.set)
sc1.configure(command=list1.yview)


def get_selected_row(event):
    global select_book
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        select_book = list1.get(index)


        # title 
        e1.delete(0, END)
        e1.insert(END, select_book[1])
        # author 
        e2.delete(0, END)
        e2.insert(END, select_book[2])
        # year 
        e3.delete(0, END)
        e3.insert(END, select_book[3])
        # sbn 
        e4.delete(0, END)
        e4.insert(END, select_book[4])
        # return select_book
        

        # print(event)
        print(index)
        # print(select_book)

list1.bind("<<ListboxSelect>>", get_selected_row)

# _________________________

def view_command():
    clear_list()
    books = backend.view()
    fill_list(books)

    

# Button View All
b1 = Button(win, text='View All', width=12, background=green_light,fg=background_withe, command=lambda: view_command())
b1.grid(row=2, column=3, pady=3)

# _________________________


def search_comand():
    clear_list()
    books = backend.search(title_text.get(), author_text.get(), year_text.get(), sbn_text.get())
    fill_list(books)

# Button Search Entry
b2 = Button(win, text='Search Entry', width=12, background='#DFFF00',fg=background_dark, command=search_comand)
b2.grid(row=3, column=3, pady=3)

# _________________________


def add_comand():
    backend.insertt(title_text.get(), author_text.get(), year_text.get(), sbn_text.get())
    view_command()


# Button Add Entry
b3 = Button(win, text='Add Entry', width=12, background=orang_t,fg=background_dark, command=add_comand)
b3.grid(row=4, column=3, pady=2)
# _________________________

def update_command():
    backend.upedate(select_book[0], title_text.get(), author_text.get(), year_text.get(), sbn_text.get())
    view_command()


# Button Update
b4 = Button(win, text='Update Selected', width=12, background=orang_numbers,fg=background_dark, command=update_command)
b4.grid(row=5, column=3, pady=3)


# _________________________


def delete_command():
    selected_id_book = select_book
    backend.delete(selected_id_book[0])
    view_command()

# Button Delete
b5 = Button(win, text='Delete Selected', width=12, background=red,fg=background_withe_res, command=delete_command)
b5.grid(row=6, column=3, pady=3)
# _________________________

def close_command():
    win.destroy()

# Button Close
b6 = Button(win, text='Close', width=12, command=close_command, background=background_dark_res,fg=background_withe_res)
b6.grid(row=7, column=3, pady=3)
# _________________________


view_command()
win.mainloop()
