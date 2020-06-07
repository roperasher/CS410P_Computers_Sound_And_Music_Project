#CS410P_Computers_Sound_And_Music_Project
#Asher Roper
#Jordan Co
#Alexander Wallace

import os
import psutil
import wire
import profiles
import globals 
from tkinter import *
from tkinter import messagebox
import types
import sounddevice as sd

window = Tk()
stream = False

def populate_list():
	effects_list.delete(0, END)
	for profile in globals.profiles:
		effects_list.insert(END, profile[2])

def populate_speaker():
    speaker_list.delete(0,END)
    for speaker in sd.query_devices():
        if speaker['max_output_channels'] > 0:
            speaker_list.insert(END, speaker['name'])

def populate_mic():
    mic_list.delete(0,END)
    for mic in sd.query_devices():
        if mic['max_input_channels'] > 0:
            mic_list.insert(END, mic['name'])

def add_item():
    funcs = [str(i).split(' ')[1] for i in getFunctions(profiles)[1:]]
    print(funcs)
    print(selected_item.replace("Default: ",""))
    if arg1_text.get() == '' or arg2_text.get() == '' or selected_item.replace("Default: ","") not in funcs:
        messagebox.showerror('ERROR', 'Please include all fields and make sure to select a default effect to edit')
        return
    globals.profiles.append([arg1_text.get(),arg2_text.get(),name_text.get(),selected_item.replace("Default: ","")])
    effects_list.delete(0, END)
    effects_list.insert(END, (arg1_text.get(), arg2_text.get()))
    clear_text()
    populate_list()

def startUp():
    global selected_item
    globals.mic = sd.query_devices(kind='input')['name']
    globals.speaker = sd.query_devices(kind='output')['name']

    for fun in getFunctions(profiles)[1:]:
        name_entry.insert(END, "Default: "+str(fun).split(' ')[1])
        selected_item = str(fun).split(' ')[1]
        arg1_entry.insert(END, 0)
        arg2_entry.insert(END, 0)

        add_item()
    update_item()

def select_item(event):
    try:
        global selected_item
        index = effects_list.curselection()[0]
        selected_item = effects_list.get(index)
        print("Selected Profile: "+ selected_item)
        globals.vocalProfile = index +1

        arg1_entry.delete(0, END)
        arg1_entry.insert(END, globals.profiles[index][0])
        arg2_entry.delete(0, END)
        arg2_entry.insert(END, globals.profiles[index][1])
        name_entry.delete(0, END)
        name_entry.insert(END, selected_item)

        restart_stream()
    except IndexError:
        pass

def select_mic(event):
    try:
        global selected_mic
        index = mic_list.curselection()[0]
        selected_mic = mic_list.get(index)
        globals.mic = selected_mic
        restart_stream()
    except IndexError:
        pass

def select_speaker(event):
    try:
        global selected_speaker
        index = speaker_list.curselection()[0]
        selected_speaker = speaker_list.get(index)
        globals.speaker = selected_speaker
        restart_stream()
    except IndexError:
        pass

def remove_item():
    globals.profiles.remove(globals.vocalProfile)
    clear_text()
    populate_list()

def update_item():
    populate_list()
    populate_mic()
    populate_speaker()

def getFunctions(module):
    funcs = []
    for key, value in module.__dict__.items():
        if type(value) is types.FunctionType:
            funcs.append(value)
    return funcs

def clear_text():
    arg1_entry.delete(0, END)
    arg2_entry.delete(0, END)
    name_entry.delete(0, END)

def toggle_stream():
    global stream
    if not stream:
        stream = wire.startStream()
        globals.firstTime = False
    else:
        stream.close()
        stream = False
    print(stream)

def restart_stream():
    global stream
    if stream:
        toggle_stream()
        toggle_stream()

def breakout():
    for proc in psutil.process_iter():
        #print(proc)
        try:
            # Check if process name contains the given name string.
            if "sox" in proc.name().lower():
                print("proc: ", proc.pid)
                os.kill(proc.pid, 9)
                return print("Killed process with PID: ", proc.pid) 
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return print("No process with cmd that begins with 'sox'") 

def helloworld():
    print("helloworld")

# arg1 text
arg1_text = StringVar()
arg1_label = Label(window, text='Level (1-10):', font=('bold', 14), pady=20, padx=20)
arg1_label.grid(row=0, column=0, sticky=W)
arg1_entry = Entry(window, textvariable=arg1_text)
arg1_entry.grid(row=0, column=1)
# arg2 text
arg2_text = StringVar()
arg2_label = Label(window, text='Other variable:', font=('bold', 14),padx=20)
arg2_label.grid(row=0, column=2, sticky=W)
arg2_entry = Entry(window, textvariable=arg2_text)
arg2_entry.grid(row=0, column=3)

# name text
name_text = StringVar()
name_label = Label(window, text='Effect Name:', font=('bold', 14),padx=20)
name_label.grid(row=1, column=0, sticky=W)
name_entry = Entry(window, textvariable=name_text)
name_entry.grid(row=1, column=1)

# Effects List
effects_list = Listbox(window, height=8, width=40, border=0)
effects_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

scrollbar = Scrollbar(window)
scrollbar.grid(row=3, column=2, rowspan=6)

effects_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=effects_list.yview)

effects_list.bind('<<ListboxSelect>>', select_item)

# Mic and Speaker Select
mic_list = Listbox(window, height=4, width=50, border=0)
mic_list.grid(row=4, column=3, columnspan=3, rowspan=1, pady=5, padx=15)
speaker_list = Listbox(window, height=4, width=50, border=0)
speaker_list.grid(row=6, column=3, columnspan=3, rowspan=1, pady=5, padx=15)
scrollbar = Scrollbar(window)

mic_list.bind('<<ListboxSelect>>', select_mic)
speaker_list.bind('<<ListboxSelect>>', select_speaker)

# Labels 
effect_label = Label(window, text='Effects', font=('bold', 14), padx=20)
effect_label.grid(row=3, column=0, sticky=W)
mic_label = Label(window, text='Microphone:', font=('bold', 14))
mic_label.grid(row=3, column=3, sticky=W)
speaker_label = Label(window, text='Speaker:', font=('bold', 14))
speaker_label.grid(row=5, column=3, sticky=W)

# Buttons
add_btn = Button(window, text='Add New Profile', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20, padx=5)

remove_btn = Button(window, text='Remove Item', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(window, text='Update List', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(window, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

stream_btn = Button(window, text='Start/stop', width=12, command=toggle_stream)
stream_btn.grid(row=2, column=4)

break_button = Button(window, text= 'Break', width=12, command=breakout)
break_button.grid(row=2, column=5)

hello_btn = Button(window, text='hello', width=12, command=helloworld)
hello_btn.grid(row=2, column=6)

window.title("Vocal Boss")
window.geometry("775x375")

def main():
    startUp()
    window.mainloop()

if __name__ == "__main__":
	main()
