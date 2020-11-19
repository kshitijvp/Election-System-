import tkinter as tk
from PIL import ImageTk ,Image

HEIGHT = 6000
WIDTH = 6000
a=0
b=0
c=0
d=0
e=0

def hide_widgets():
    widgets = [button_joe, button_modi, button_rahul, button_trump, label_joe, label_modi, label_rahul, label_trump, button_result,label_click]
    for i in widgets:
        i.place_forget()

def modi_voted():
    global a
    a = a + 1
    print("Narendra Modi's result is" , a)
    
def rahul_voted():
    global b
    b = b + 1 
    print("Rahul Gandhi's result is" ,b )

def trump_voted():
    global c
    c = c + 1
    print(" Donald Trump's result is " , c)

def joe_voted():
    global d
    d = d + 1 
    print("Joe Biden's result is " , d)

def openNewWindow():
    hide_widgets()
    modi_votes.place(relx=0 , rely=0 , relwidth=0.5 , relheight=0.5)
    modi_votes.config(text = "Narendra Modi got " + str(a) + " votes")

    trump_votes.place(relx=0.25 , rely =0.3 , relwidth=0.5 , relheight=0.5)
    trump_votes.config(text = "Donald Trump got " + str(c) + " votes")

    rahul_votes.place(relx=0.5 , rely=0 , relwidth=0.5 , relheight=0.5)
    rahul_votes.config(text = "Rahul Gandhi got " + str(b) + " votes")

    joe_votes.place(relx=0.25 , rely=0.6 , relwidth=0.5 , relheight=0.5)
    joe_votes.config(text = "Joe Biden got " + str(d) + "votes")

root=tk.Tk()
root.title('Election System')
root.state('zoomed')

canvas=tk.Canvas(root , height=HEIGHT , width=WIDTH , bg="dodgerblue2")
canvas.pack()

photo= tk.PhotoImage(file="d:/Kshitij/modi.png" )

photo_2 = tk.PhotoImage(file="d:/Kshitij/rahul.png")

photo_3 = tk.PhotoImage(file="d:/Kshitij/donal.png")

photo_4 = tk.PhotoImage(file="d:/Kshitij/joe.png")

button_modi = tk.Button(root , bg="blue" ,bd=10 ,  image=photo , command=modi_voted)
button_modi.place(relx=0.005 , rely=0.1 , relwidth=0.2 , relheight=0.5)

button_rahul = tk.Button(root , bg="green" ,bd=10, image=photo_2 ,  command=rahul_voted )
button_rahul.place(relx=0.28 , rely=0.1 , relwidth=0.2 , relheight=0.5)

button_trump = tk.Button(root , bg="orange" ,bd=10 , image=photo_3 , command=trump_voted)
button_trump.place(relx=0.55 , rely=0.1 , relwidth= 0.2 , relheight=0.5)

button_joe = tk.Button(root , bg="violet" ,bd=10 , image=photo_4 , command = joe_voted)
button_joe.place(relx=0.8 , rely=0.1 , relwidth= 0.2 , relheight=0.5)

label_modi = tk.Label(root , bg="black" , fg="white" , text="Narendra Modi" , font=1000 )
label_modi.place(relx=0.005 , rely=0.7 , relwidth=0.2 , relheight=0.1)

label_rahul = tk.Label(root , bg="black" , fg="white" , text="Rahul Gandhi" , font=1000 )
label_rahul.place(relx=0.28 , rely=0.7 , relwidth=0.2 , relheight=0.1)

label_trump = tk.Label(root , bg="black" , fg="white" , text="Donald Trump" , font=1000 )
label_trump.place(relx=0.55 , rely=0.7 , relwidth=0.2 , relheight=0.1)

label_joe = tk.Label(root , bg="black" , fg="white" , text="Joe Biden" , font=1000 )
label_joe.place(relx=0.8 , rely=0.7 , relwidth=0.2 , relheight=0.1)

modi_votes = tk.Label(root , bg="black" , fg="white", font=10000000) 
trump_votes = tk.Label(root, bg="black" , fg="white", font=10000000)
rahul_votes = tk.Label(root , bg="black" , fg="white" , font=10000000)
joe_votes = tk.Label(root , bg="black" , fg="white" , font=100000000)

button_result = tk.Button(root , bg="violet" ,bd=10 , text="Get Result", command = openNewWindow , font=1000000)
button_result.place(relx=0.8 , rely=0.86 , relwidth= 0.2 , relheight=0.15)

label_click = tk.Label(root , bg="dodgerblue2" , bd=0 , text="Click on image to vote" , font=100000000000000 )
label_click.place(relx=0.25 , rely=0 , relwidth=0.5 , relheight=0.1)

root.mainloop()