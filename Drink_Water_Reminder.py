import time
import tkinter
import schedule

def water_reminder():
    # Main Window for GUI is called
    window = tkinter.Tk()
    window.title("Reminder")
    button = tkinter.Button(window, text='Thanks', width=25, command=window.destroy)
    button.pack()
    canvas_width = 700
    canvas_height = 450
    canvas = tkinter.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()
    filename = tkinter.PhotoImage(file="resources/ppg.png")
    canvas.create_image(25, 30, anchor=tkinter.NW, image=filename)
    reminder_message = 'Drink Water Incia'
    widget = tkinter.Label(window, text=reminder_message, font="10", bg="lightgreen")
    widget.pack()
    window.mainloop()


schedule.every().hour.do(water_reminder)
while True:
    schedule.run_pending()
    time.sleep(1)
