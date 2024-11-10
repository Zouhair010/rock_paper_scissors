import random
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk

def rock_choice():
    items = ['rock','paper','scissors']
    autoplayer = random.choice(items)
    player_choice = 'rock'
    if player_choice == autoplayer:
        messagebox.showinfo("",'equal\ntry agian')
    elif autoplayer == items[1]:
        messagebox.showerror("","you lose\nlet's playe one more time")         
    elif autoplayer == items[2]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")        
    elif autoplayer == items[0]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")
    elif autoplayer == items[2]:
        messagebox.showerror("","you lose\nlet's playe one more time") 
    elif autoplayer == items[0]:
        messagebox.showerror("","you lose\nlet's playe one more time") 
    elif autoplayer == items[1]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")
    
def paper_choice():
    items = ['rock','paper','scissors']
    autoplayer = random.choice(items)
    player_choice = 'paper'
    if player_choice == autoplayer:
        messagebox.showinfo("",'equal\ntry agian')
    elif autoplayer == items[1]:
        messagebox.showerror("","you lose\nlet's playe one more time") 
    elif autoplayer == items[2]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")
    elif autoplayer == items[0]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")
    elif autoplayer == items[2]:
        messagebox.showerror("","you lose\nlet's playe one more time") 
    elif autoplayer == items[0]:
        messagebox.showerror("","you lose\nlet's playe one more time") 
    elif autoplayer == items[1]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")

def scissors_choice():
    items = ['rock','paper','scissors']
    autoplayer = random.choice(items)
    player_choice = 'scissors'
    if player_choice == autoplayer:
        messagebox.showinfo("",'equal\ntry agian')
    elif autoplayer == items[1]:
        messagebox.showerror("","you lose\nlet's playe one more time") 
    elif autoplayer == items[2]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")
    elif autoplayer == items[0]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")
    elif autoplayer == items[2]:
        messagebox.showerror("","you lose\nlet's playe one more time") 
    elif autoplayer == items[0]:
        messagebox.showerror("","you lose\nlet's playe one more time") 
    elif autoplayer == items[1]:
        messagebox.showinfo("","congratulation you win\nlest's do it agian")

app = tkinter.Tk()
app.title('rock paper scissors')
app.geometry('400x200')
app.iconbitmap("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\game_game_console_play_device_icon_133759.ico") #to change the default icon

background_image = Image.open("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\rock-paper-scissors.png") 
background_image = background_image.resize((400, 200), Image.LANCZOS)  
background_photo = ImageTk.PhotoImage(background_image)

canvas = tkinter.Canvas(app, width=app.winfo_screenwidth(), height=app.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

image1 = Image.open("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\scissors.png")
image1 = image1.resize((64,64))
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\new-document.png")
image2 = image2.resize((64,64))
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\stone.png")
image3 = image3.resize((64,64))
photo3 = ImageTk.PhotoImage(image3)

label = tkinter.Label(canvas,text="let's play",font=('Arial',15,'bold'),fg='red')
label.grid(row=0,column=1,pady=(11,16))
rock = tkinter.Button(canvas, text='rock', image=photo1,command=rock_choice)
rock.grid(row=1,column=0,padx=(55,0))
paper = tkinter.Button(canvas, text='paper', image=photo2,command=paper_choice)
paper.grid(row=1,column=1,padx=(40))
scissors = tkinter.Button(canvas, text='scissors', image=photo3,command=scissors_choice)
scissors.grid(row=1,column=2,padx=(0,55))

app.mainloop()