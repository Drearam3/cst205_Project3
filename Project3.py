##-----------------------PROJECT3---------------------------------------------
##  Names: Andrea Ramirez, Jose Garcia, Raeleen Watson
##  Due Date: 05/13/16
##  Class: CST205: Multimedia Design and Programming
##  Title: Project3.py
##  Description: This python program is a virtual piano that implements a tkinter GUI window and buttons to simulate a real piano.
##                  The user of the piano can both click on the buttons using the mouse and the keyboard. Each piano key corresponds 
##                  with a key on the keyboard and the corresponding button can be found on each individual key. The piano also records 
##                  notes the user plays at the start of the first key press. With this, the user can press the "playback" button and hear
##                  the notes that they previously played. Along with this, the user can also control the speed at which the playback is played. 
##                  The speed ranges from 1 to 7, in which 1 is the fastest and 7 is the slowest. 
##  Trello Link: https://trello.com/b/kF4Q4lu7/team-96-project-3-cst-205
##  GitHub Link: https://github.com/Drearam3/cst205_Project3


#------------------------MODULES------------------------------------
import pygame
import sys
import os
from tkinter import *


pygame.init()

record = []


##Functions to both play sounds and record them into an array for playback
def record_A2(event=None):
    global record
    record.append(value_A2)
    value_A2()
    return
def value_A2():
    num1.set("A2")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "A2.wav")
    sound.play()
    return
def record_As2(event=None):
    global record
    record.append(value_As2)
    value_As2()
    return
def value_As2():
    num1.set("A#2")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "A#2.wav")
    sound.play()
    return
def record_B2(event=None):
    global record
    record.append(value_B2)
    value_B2()
    return
def value_B2():
    num1.set("B2")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "B2.wav")
    sound.play()
    return
def record_C3(event=None):
    global record
    record.append(value_C3)
    value_C3()
    return
    value_C3()
def value_C3():
    num1.set("C3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "C3.wav")
    sound.play()
    return
def record_Cs3(event=None):
    global record
    record.append(value_Cs3)
    value_Cs3()
    return
def value_Cs3():
    num1.set("C#3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "C#3.wav")
    sound.play()
    return
def record_D3(event=None):
    global record
    record.append(value_D3)
    value_D3()
    return
def value_D3():
    num1.set("D3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "D3.wav")
    sound.play()
    return
def record_Ds3(event=None):
    global record
    record.append(value_Ds3)
    value_Ds3()
    return
def value_Ds3():
    num1.set("D#3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "D#3.wav")
    sound.play()
    return
def record_E3(event=None):
    global record
    record.append(value_E3)
    value_E3()
    return
def value_E3():
    num1.set("E3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "E3.wav")
    sound.play()
    return
def record_F3(event=None):
    global record
    record.append(value_F3)
    value_F3()
    return
def value_F3():
    num1.set("F3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "F3.wav")
    sound.play()
    return
def record_Fs3(event=None):
    global record
    record.append(value_Fs3)
    value_Fs3()
    return
def value_Fs3():
    num1.set("F#3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "F#3.wav")
    sound.play()
    return
def record_G3(event=None):
    global record
    record.append(value_G3)
    value_G3()
    return
def value_G3():
    num1.set("G3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "G3.wav")
    sound.play()
    return
def record_Gs3(event=None):
    global record
    record.append(value_Gs3)
    value_Gs3()
    return
def value_Gs3():
    num1.set("G#3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "G#3.wav")
    sound.play()
    return
def record_A3(event=None):
    global record
    record.append(value_A3)
    value_A3()
    return
def value_A3():
    num1.set("A3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "A3.wav")
    sound.play()
    return
def record_As3(event=None):
    global record
    record.append(value_As3)
    value_As3()
    return
def value_As3():
    num1.set("A#3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "A#3.wav")
    sound.play()
    return
def record_B3(event=None):
    global record
    record.append(value_B3)
    value_B3()
    return
def value_B3():
    num1.set("B3")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "B3.wav")
    sound.play()
    return
def record_C4(event=None):
    global record
    record.append(value_C4)
    value_C4()
    return
def value_C4():
    num1.set("C4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "C4.wav")
    sound.play()
    return
def record_Cs4(event=None):
    global record
    record.append(value_Cs4)
    value_Cs4()
    return
def value_Cs4():
    num1.set("C#4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "C#4.wav")
    sound.play()
    return
def record_D4(event=None):
    global record
    record.append(value_D4)
    value_D4()
    return
def value_D4():
    num1.set("D4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "D4.wav")
    sound.play()
    return
def record_Ds4(event=None):
    global record
    record.append(value_Ds4)
    value_Ds4()
    return
def value_Ds4():
    num1.set("D#4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "D#4.wav")
    sound.play()
    return
def record_E4(event=None):
    global record
    record.append(value_E4)
    value_E4()
    return
def value_E4():
    num1.set("E4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "E4.wav")
    sound.play()
    return
def record_F4(event=None):
    global record
    record.append(value_F4)
    value_F4()
    return
def value_F4():
    num1.set("F4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "F4.wav")
    sound.play()
    return
def record_Fs4(event=None):
    global record
    record.append(value_Fs4)
    value_Fs4()
    return
def value_Fs4():
    num1.set("F#4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "F#4.wav")
    sound.play()
    return
def record_G4(event=None):
    global record
    record.append(value_G4)
    value_G4()
    return
def value_G4():
    num1.set("G4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "G4.wav")
    sound.play()
    return
def record_Gs4(event=None):
    global record
    record.append(value_Gs4)
    value_Gs4()
    return
def value_Gs4():
    num1.set("G#4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "G#4.wav")
    sound.play()
    return
def record_A4(event=None):
    global record
    record.append(value_A4)
    value_A4()
    return
def value_A4():
    num1.set("A4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "A4.wav")
    sound.play()
    return
def record_As4(event=None):
    global record
    record.append(value_As4)
    value_As4()
    return
def value_As4():
    num1.set("A#4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "A#4.wav")
    sound.play()
    return
def record_B4(event=None):
    global record
    record.append(value_B4)
    value_B4()
    return
def value_B4():
    num1.set("B4")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "B4.wav")
    sound.play()
    return
def record_C5(event=None):
    global record
    record.append(value_C5)
    value_C5()
    return
def value_C5():
    num1.set("C5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "C5.wav")
    sound.play()
    return
def record_Cs5(event=None):
    global record
    record.append(value_Cs5)
    value_Cs5()
    return
def value_Cs5():
    num1.set("C#5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "C#5.wav")
    sound.play()
    return
def record_D5(event=None):
    global record
    record.append(value_D5)
    value_D5()
    return
def value_D5():
    num1.set("D5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "D5.wav")
    sound.play()
    return
def record_Ds5(event=None):
    global record
    record.append(value_Ds5)
    value_Ds5()
    return
def value_Ds5():
    num1.set("D#5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "D#5.wav")
    sound.play()
    return
def record_E5(event=None):
    global record
    record.append(value_E5)
    value_E5()
    return
def value_E5():
    num1.set("E5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "E5.wav")
    sound.play()
    return
def record_F5(event=None):
    global record
    record.append(value_F5)
    value_F5()
    return
def value_F5():
    num1.set("F5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "F5.wav")
    sound.play()
    return
def record_Fs5(event=None):
    global record
    record.append(value_Fs5)
    value_Fs5()
    return
def value_Fs5():
    num1.set("F#5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "F#5.wav")
    sound.play()
    return
def record_G5(event=None):
    global record
    record.append(value_G5)
    value_G5()
    return
def value_G5():
    num1.set("G5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "G5.wav")
    sound.play()
    return
def record_Gs5(event=None):
    global record
    record.append(value_Gs5)
    value_Gs5()
    return
def value_Gs5():
    num1.set("G#5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "G#5.wav")
    sound.play()
    return
def record_A5(event=None):
    global record
    record.append(value_A5)
    value_A5()
    return
def value_A5():
    num1.set("A5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "A5.wav")
    sound.play()
    return
def record_As5(event=None):
    global record
    record.append(value_As5)
    value_As5()
    return
def value_As5():
    num1.set("A#5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "A#5.wav")
    sound.play()
    return
def record_B5(event=None):
    global record
    record.append(value_B5)
    value_B5()
    return
def value_B5():
    num1.set("B5")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "B5.wav")
    sound.play()
    return
def record_C6(event=None):
    global record
    record.append(value_C6)
    value_C6()
    return
def value_C6():
    num1.set("C6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "C6.wav")
    sound.play()
    return
def record_Cs6(event=None):
    global record
    record.append(value_Cs6)
    value_Cs6()
    return
def value_Cs6():
    num1.set("C#6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "C#6.wav")
    sound.play()
    return
def record_D6(event=None):
    global record
    record.append(value_D6)
    value_D6()
    return
def value_D6():
    num1.set("D6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "D6.wav")
    sound.play()
    return
def record_Ds6(event=None):
    global record
    record.append(value_Ds6)
    value_Ds6()
    return
def value_Ds6():
    num1.set("D#6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "D#6.wav")
    sound.play()
    return
def record_E6(event=None):
    global record
    record.append(value_E6)
    value_E6()
    return
def value_E6():
    num1.set("E6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "E6.wav")
    sound.play()
    return
def record_F6(event=None):
    global record
    record.append(value_F6)
    value_F6()
    return
def value_F6():
    num1.set("F6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "F6.wav")
    sound.play()
    return
def record_Fs6(event=None):
    global record
    record.append(value_Fs6)
    value_Fs6()
    return
def value_Fs6():
    num1.set("F#6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "F#6.wav")
    sound.play()
    return
def record_G6(event=None):
    global record
    record.append(value_G6)
    value_G6()
    return
def value_G6():
    num1.set("G6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "G6.wav")
    sound.play()
    return
def record_Gs6(event=None):
    global record
    record.append(value_Gs6)
    value_Gs6()
    return
def value_Gs6():
    num1.set("G#6")
    directory = os.getcwd()
    path = directory + "/Notes/"
    sound = pygame.mixer.Sound(path + "G#6.wav")
    sound.play()
    return


## Plays back the notes that were pressed starting at the first note. 
def song():
    global record
    num = len(record)
    global v
    inputNum = v.get()
    if inputNum.strip():
        inputNum = int(inputNum)
    else:
        inputNum = 3  
    for i in range (0, num):
        record[i]()
        print(record[i])
        pygame.time.delay((inputNum) * 100)
    return
##Erases the notes that have been pressed. Allows the user to make a new song
def deleteSong():
    global record
    record = []
    return

root = Tk()
frame = Frame(root)
frame.pack()


root.title('Virtual Piano')

num1 = StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)

txtDisplay=Entry(frame, textvariable = num1, bd=20, insertwidth=1, font = 30, justify='center', width=4,)
txtDisplay.pack(side=TOP)


v = IntVar()
MODES = [
        ("1"),
        ("2"),
        ("3"),
        ("4"),
        ("5"),
        ("6"),
        ("7"),
        ]
v = StringVar()


frame.pack()
##Label for playback speed. Varies from 1, fast, and 7, slow.
label = Label (frame, text= "Playback Speed(1-7)")
label.pack(side = TOP)
for key in MODES:
    item= Radiobutton(frame, text=key, bd=4, width=12)
    item.config(indicatoron=0, variable=v, value=int(key))
    item.pack(side=LEFT)
#button to delete songs
button2 = Button(frame, padx=1, pady=2, width=9, height = 1, bd=8, text="Delete Song", activebackground="#ff4d4d", command=deleteSong)
button2.pack(side=RIGHT)
button00 = Button(frame, state=DISABLED, padx=0, height = 3, width=3, pady=0, relief=RIDGE)
button00.pack(side=RIGHT)
##button to playback the notes you pressed
button1 = Button(frame, padx=1, pady=2, width=9, height = 1, bd=8, text="Playback", activebackground="#ff4d4d", command=song)
button1.pack(side=RIGHT)

##piano key buttons
#----------------------------------------------------BLACK KEYS--------------------------------------------------------
button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=4, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button6 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="A#2 (1)", bg="black", fg="white", activebackground="#ff4d4d", command=record_As2)
button6.pack(side=LEFT)
root.bind('1', record_As2)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=4, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button7 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="C#3 (2)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Cs3)
button7.pack(side=LEFT)
root.bind('2', record_Cs3)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button8 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="D#3 (3)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Ds3)
button8.pack(side=LEFT)
root.bind('3', record_Ds3)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=4, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button9 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="F#3 (4)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Fs3)
button9.pack(side=LEFT)
root.bind('4', record_Fs3)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button10 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="G#3 (5)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Gs3)
button10.pack(side=LEFT)
root.bind('5', record_Gs3)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button11 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="A#3 (6)", bg="black", fg="white", activebackground="#ff4d4d", command=record_As3)
button11.pack(side=LEFT)
root.bind('6', record_As3)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=4, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button12 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="C#4 (7)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Cs4)
button12.pack(side=LEFT)
root.bind('7', record_Cs4)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button13 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="D#4 (8)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Ds4)
button13.pack(side=LEFT)
root.bind('8', record_Ds4)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=4, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button14 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="F#4 (9)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Fs4)
button14.pack(side=LEFT)
root.bind('9', record_Fs4)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button15 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="G#4 (0)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Gs4)
button15.pack(side=LEFT)
root.bind('0', record_Gs4)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button16 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength=30, justify=CENTER, text="A#4 (A)", bg="black", fg="white", activebackground="#ff4d4d", command=record_As4)
button16.pack(side=LEFT)
root.bind('a', record_As4)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=3, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button12 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength = 30, justify = CENTER, text="C#5 (S)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Cs5)
button12.pack(side=LEFT)
root.bind('s', record_Cs5)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button13 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8,wraplength = 30, justify = CENTER, text="D#5 (D)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Ds5)
button13.pack(side=LEFT)
root.bind('d', record_Ds5)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=3, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button14 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8,wraplength = 30, justify = CENTER, text="F#5 (F)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Fs5)
button14.pack(side=LEFT)
root.bind('f', record_Fs5)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button15 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8,wraplength = 30, justify = CENTER, text="G#5 (G)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Gs5)
button15.pack(side=LEFT)
root.bind('g', record_Gs5)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button16 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength = 30, justify = CENTER, text="A#5 (H)", bg="black", fg="white", activebackground="#ff4d4d", command=record_As5)
button16.pack(side=LEFT)
root.bind('h', record_As5)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=3, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button17 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8,wraplength = 30, justify = CENTER, text="C#6 (J)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Cs6)
button17.pack(side=LEFT)
root.bind('j', record_Cs6)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button18 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength = 30, justify = CENTER, text="D#6 (K)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Ds6)
button18.pack(side=LEFT)
root.bind('k', record_Ds6)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=3, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button19 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8,wraplength = 30, justify = CENTER, text="F#6 (L)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Fs6)
button19.pack(side=LEFT)
root.bind('l' ,record_Fs6)

button00 = Button(topframe, state=DISABLED, padx=0, height = 7, width=1, pady=0, relief=RIDGE)
button00.pack(side=LEFT)

button19 = Button(topframe, padx=3, pady=8, width=2, height = 6, bd=8, wraplength = 30, justify = CENTER, text="G#6 (;)", bg="black", fg="white", activebackground="#ff4d4d", command=record_Gs6)
button19.pack(side=LEFT)
root.bind(';', record_Gs6)





#-------------------------------------------------------WHITE KEYS----------------------------------------------------------                 

frame1 = Frame(root)
frame1.pack(side=TOP)

button8 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="A2 (Q)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=2, command=record_A2)
button8.pack(side=LEFT)
root.bind('q', record_A2)
button9 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="B2 (W)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_B2)                 
button9.pack(side=LEFT)
root.bind('w', record_B2)
button10 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="C3 (E)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_C3)
button10.pack(side=LEFT)
root.bind('e', record_C3)
button11 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="D3 (R)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_D3)
button11.pack(side=LEFT)
root.bind('r', record_D3)
button12 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="E3 (T)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_E3)
button12.pack(side=LEFT)
root.bind('t', record_E3)
button13 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="F3 (Y)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_F3)
button13.pack(side=LEFT)
root.bind('y', record_F3)
button14 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="G3 (U)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_G3)
button14.pack(side=LEFT)
root.bind('u', record_G3)
button15 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="A3 (I)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_A3)
button15.pack(side=LEFT)
root.bind('i', record_A3)
button16 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="B3 (O)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_B3)                 
button16.pack(side=LEFT)
root.bind('o', record_B3)
button17 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="C4 (P)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_C4)
button17.pack(side=LEFT)
root.bind('p', record_C4)
button18 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="D4 ([)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_D4)
button18.pack(side=LEFT)
root.bind('[', record_D4)
button19 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="E4 (])", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_E4)
button19.pack(side=LEFT)
root.bind(']', record_E4)
button20 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="F4 (\)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_F4)
button20.pack(side=LEFT)
root.bind('<\>', record_F4)
button21 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=30, justify=CENTER, text="G4 (+)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_G4)
button21.pack(side=LEFT)
root.bind('+', record_G4)
button22 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=45, justify=CENTER, text="A4 (L_Shift)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_A4)
button22.pack(side=LEFT)
root.bind('<Shift_L>', record_A4)
button23 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="B4 (Z)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_B4)
button23.pack(side=LEFT)
root.bind('z', record_B4)
button24 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER,text="C5 (X)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_C5)
button24.pack(side=LEFT)
root.bind('x', record_C5)
button18 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="D5 (C)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_D5)
button18.pack(side=LEFT)
root.bind('c', record_D5)
button19 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER,text="E5 (V)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_E5)
button19.pack(side=LEFT)
root.bind('v', record_E5)
button20 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="F5 (B)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_F5)
button20.pack(side=LEFT)
root.bind('b', record_F5)
button21 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER,text="G5 (N)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_G5)
button21.pack(side=LEFT)
root.bind('n', record_G5)
button22 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="A5 (M)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_A5)
button22.pack(side=LEFT)
root.bind('m', record_A5)
button23 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER,text="B5 (,)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_B5)
button23.pack(side=LEFT)
root.bind(',', record_B5)
button24 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="C6 (.)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_C6)
button24.pack(side=LEFT)
root.bind('.', record_C6)
button25 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=20, justify=CENTER, text="D6 (/)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_D6)
button25.pack(side=LEFT)
root.bind('/', record_D6)
button26 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=45, justify=CENTER, text="E6 (R_Shift)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_E6)
button26.pack(side=LEFT)
root.bind('<Shift_R>', record_E6)
button27 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=40, justify=CENTER, text="F6 (Left)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_F6)
button27.pack(side=LEFT)
root.bind('<Left>' , record_F6)
button28 = Button(frame1, padx=13, pady=16, width = 2, height=8, bd=0, wraplength=40, justify=CENTER,  text="G6 (Right)", fg="black", bg="white", activebackground="#ff4d4d", borderwidth=1, command=record_G6)
button28.pack(side=LEFT)
root.bind('<Right>', record_G6 )





root.mainloop()






