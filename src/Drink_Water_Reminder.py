import time
import tkinter
import schedule

def water_reminder():
    # Main Window for GUI is called
    window = tkinter.Tk()
    # Title of the window
    window.title("Reminder")
    # button widget for the Window where we say Thanks to the app for the reminder :)
    button = tkinter.Button(window, text='Thanks', width=25, command=window.destroy)
    button.pack()
    #Canvas details
    canvas_width = 700
    canvas_height = 450
    canvas = tkinter.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()
    # Attaching an image to the window - PNG works mostly
    filename = tkinter.PhotoImage(file="resources/ppg.png")
    canvas.create_image(25, 30, anchor=tkinter.NW, image=filename)
    # A reminder message as a label
    reminder_message = 'Drink Water Incia'
    widget = tkinter.Label(window, text=reminder_message, font="10", bg="lightgreen")
    widget.pack()
    # End of main Window
    window.mainloop()

# scheduler which schedules the same job hourly basis
schedule.every().hour.do(water_reminder)
while True:
    schedule.run_pending()
    time.sleep(1)
