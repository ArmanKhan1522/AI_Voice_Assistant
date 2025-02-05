from tkinter import *
from PIL import Image, ImageTk
import Assistant

root = Tk()
root.title("AI VIRTUAL ASSISTANT")
root.geometry("810x680")
# root.resizable(False, False)
root.config(bg="#EEDFCC")


def ask():
    user_query = entry.get()
    response = Assistant.process_query(user_query)
    text.insert(END, response + "\n")


def send():
    query = entry.get()
    text.insert(END="You: " + query + "\n")
    entry.delete(0, END)
    Assistant.process_query(query)


def del_text():
    text.delete(1.0, END)


# frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#EEDFCC")
frame.grid(row=0, column=1, padx=55, pady=10)

# text label
text_label = Label(frame, text="AI ASSISTANT", font=("Arial", 15, "bold"), bg="#CDC0B0")
text_label.grid(row=0, column=0, padx=20, pady=10)

# image
image = ImageTk.PhotoImage(Image.open("C:\\Users\\arman\\Pictures\\assistant1.jpg"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)

# entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=150, y=660, width=500, height=30)

# text widget
text = Text(root, font=("Arial", 10, "bold"), bg="#CDC0B0")
text.grid(row=2, column=0)
text.place(x=200, y=550, width=400, height=100)

# button
Button1 = Button(
    root,
    text="ASK",
    bg="#CDC0B0",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=ask,
)
Button1.place(x=50, y=720)

Button3 = Button(
    root,
    text="SEND",
    bg="#CDC0B0",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=send,
)
Button3.place(x=640, y=720)

Button2 = Button(
    root,
    text="DELETE",
    bg="#CDC0B0",
    pady=16,
    padx=40,
    borderwidth=3,
    relief=SOLID,
    command=del_text,
)
Button2.place(x=330, y=720)

root.mainloop()
