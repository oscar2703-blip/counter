from tkinter import*
import time
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
# or 
# root.minsize(500,500)

root.title("Time counters")

#Declare Variabless
hour = StringVar()
minute = StringVar()
second = StringVar()

#setting the default values as 0
hour.set('00')
minute.set("00")
second.set("00")

hourEntry = Entry(root, width=7, font=("Arial",18,""), textvariable=hour)
hourEntry.place(x=50, y=100)

minuteEntry = Entry(root, width=7, font=("Arial", 18,""), textvariable=minute)
minuteEntry.place(x=200, y=100)

secondEntry = Entry(root, width=7, font=("Arial", 18,""), textvariable=second)
secondEntry.place(x=350, y=100)

def submit():
    try:
        temp = (int(hour.get()) *3600) + (int(minute.get()) * 60) + int(second.get())
    except :
        print('plz enter correct value')
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 00
        if mins > 60:
            hours, mins = divmod(temp,60)
            
        hour.set("{00:2d}".format(hours))   
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))
        root.update()
        time.sleep(1)

        if (temp == 00):
            messagebox.showinfo("Countdown", "Time's UP")

        temp-=1

            
button = Button(root, text="Set Time Counter", bd=2,command=submit)
button.place(x= 200, y=300)
root.mainloop()