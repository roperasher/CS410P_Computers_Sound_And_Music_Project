#CS410P_Computers_Sound_And_Music_Project
#Asher Roper
#Jordan Co
#Alexander Wallace

import wire
import profiles
import globals 
from tkinter import *
from tkinter import messagebox
import types


window = Tk()
stream = False


	# userInput = input("Enter a value: ")
 #    globals.vocalProfile = int(userInput)
 #    wire.startStream()



def populate_list():
	parts_list.delete(0, END)
	for profile in globals.profiles.keys():
		parts_list.insert(END, profile)


def add_item():
    if part_text.get() == '' or customer_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    globals.profiles[selected_item] = [part_text.get(),customer_text.get()]
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get()))
    clear_text()
    populate_list()

def startUp():
    for fun in getFunctions(profiles)[1:]:
        global selected_item
        selected_item = str(fun).split(' ')[1]
        part_entry.insert(END, 0)
        customer_entry.insert(END, 0)
        add_item()
    update_item()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        print("Selected Profile: "+ selected_item)
        globals.vocalProfile = index +1

        part_entry.delete(0, END)
        part_entry.insert(END, globals.profiles[selected_item][0])
        customer_entry.delete(0, END)
        customer_entry.insert(END, globals.profiles[selected_item][1])

        if stream:
        	toggle_stream()
        	toggle_stream()
    except IndexError:
        pass


def remove_item():
    globals.profiles.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    # db.update(selected_item[0], part_text.get(), customer_text.get(),
    #           retailer_text.get(), price_text.get())
    populate_list()

def getFunctions(module):
    funcs = []
    for key, value in module.__dict__.items():
        if type(value) is types.FunctionType:
            funcs.append(value)
    return funcs

def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)

def toggle_stream():
	global stream
	if not stream:
		stream = wire.startStream()
	else:
		stream.close()
		stream = False
	print(stream)
	
# Part
part_text = StringVar()
part_label = Label(window, text='Pitch', font=('bold', 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(window, textvariable=part_text)
part_entry.grid(row=0, column=1)
# Customer
customer_text = StringVar()
customer_label = Label(window, text='Other variable', font=('bold', 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(window, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

# Parts List (Listbox)
parts_list = Listbox(window, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(window, text='Add New Profile', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(window, text='Remove Item', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(window, text='Update List', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(window, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

stream_btn = Button(window, text='Start/stop', width=12, command=toggle_stream)
stream_btn.grid(row=2, column=4)
window.title("Vocal Boss")
window.geometry("700x350")






def main():
    startUp()
    window.mainloop()

if __name__ == "__main__":
	main()