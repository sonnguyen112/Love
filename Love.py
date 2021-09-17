from tkinter import *
import time
import sys
import playsound

class Object():
    def __init__(self,canvas, x, y, xVeclocity, yVeclocity, photo, canPass):
        self.canvas = canvas
        self.image = canvas.create_image(x, y, image = photo, anchor = NW)
        self.canPass = canPass
        self.xVeclocity = xVeclocity
        self.yVeclocity = yVeclocity
        self.photo = photo
        self.x = x
        self.y = y
    def move(self):
        coordinates = self.canvas.coords(self.image)
        if (self.canPass == True):
            if (coordinates[1] < -300):
                self.canvas.delete(self.image)
                self.image = canvas.create_image(self.x, self.y, image=self.photo, anchor=NW)
        if (self.canPass == False):
            if coordinates[0] >= self.canvas.winfo_width() - self.photo.width() or coordinates[0] < 0:
                self.xVeclocity = -self.xVeclocity
            if coordinates[1] >= self.canvas.winfo_height() - self.photo.height() or coordinates[1] < 0:
                self.yVeclocity = -self.yVeclocity
        self.canvas.move(self.image, self.xVeclocity, self.yVeclocity)
        window.update()
        time.sleep(0.01)

times = 0

timesOfYes = 0
def love():
    global timesOfYes
    timesOfYes += 1
    if (timesOfYes == 1):
        timesOfYes += 1
        label.config(text="Hii I love you very\n 😍very much😍")
        window.update()
        but1.config(text="Close")
    else:
        sys.exit(0)

def disable_event():
   label.config(text = "Don't stop 😭\n Click Yes Pleaseee🥺")
   window.overrideredirect(1)

def run(event):
    global times
    times += 1
    if times > 4:
        times = 1
    if times == 1:
        x = 786
        y = 497
    elif times == 2:
        x = 165
        y = 603
    elif times == 3:
        x = 454
        y = 346
    else:
        x = 750
        y = 180
    widget = event.widget
    widget.place(x = x, y = y)


window = Tk()

window.protocol("WM_DELETE_WINDOW", disable_event)
window.config(bg = "white")
window.title("Do you love me?")
window.geometry("1000x800")
# window.minsize(1000, 1000)
# window.maxsize(1000, 1000)
window.resizable(False, False)
canvas = Canvas(window, width = 1000, height = 800)
background = PhotoImage(file = "background.png")
canvas.create_image(0, 0, image = background, anchor = NW)

label = Label(window,
              text = "Do you love me? 🥰",
              font = ("Ink Free", 50, "bold", "italic"),
              bg = "white",
              fg = "#ff0066")
but1 = Button(window,
              text = "Yes",
              font = ("Ink Free", 50, "bold", "italic"),
              bg = "pink",
              fg = "#ff3300",
              width = 4,
              height = 1,
              command = love)
but2 = Button(window,
              text = "No",
              font = ("Ink Free", 50, "bold", "italic"),
              bg = "pink",
              fg = "#4d4d33",
              width=4,
              height=1)
label.pack()
canvas.pack()
but1.place(x = 100, y = 180)
but2.place(x = 750, y = 180)

but2.bind("<Enter>", run)

photo1 = PhotoImage(file = "em1.png").subsample(2, 2)
photo2 = PhotoImage(file = "em2.png").subsample(5, 5)
photo3 = PhotoImage(file = "em3.png").subsample(5, 5)

object1 = Object(canvas, 150, 600, 0, -3, photo1, True)
object2 = Object(canvas, 450, 600, 0, -6, photo1, True)
object3 = Object(canvas, 750, 600, 0, -4, photo1, True)
object4 = Object(canvas, 0, 0, 6, 8,photo2, False)
object5 = Object(canvas, 500, 500, 8, 6, photo3, False)

playsound.playsound("sound.wav", False)
while True:
    object1.move()
    object2.move()
    object3.move()
    object4.move()
    object5.move()
    if timesOfYes == 3:
        break
window.mainloop()