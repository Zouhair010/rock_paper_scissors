import random
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk  # Import required libraries

# Function for the 'rock' button
def rock_choice():
    items = ['rock', 'paper', 'scissors']  # List of possible choices
    autoplayer = random.choice(items)  # Autoplayer randomly chooses one of the items
    player_choice = 'rock'  # Player's choice set to 'rock'

    # Check game outcomes
    if player_choice == autoplayer: # Autoplayer chose 'rock'
        messagebox.showinfo("", 'equal\ntry again')  # Display tie message
    elif autoplayer == items[1]:  # Autoplayer chose 'paper'
        messagebox.showerror("", "you lose\nlet's play one more time")
    elif autoplayer == items[2]:  # Autoplayer chose 'scissors'
        messagebox.showinfo("", "congratulations you win\nlet's do it again")

# Function for the 'paper' button
def paper_choice():
    items = ['rock', 'paper', 'scissors']
    autoplayer = random.choice(items)
    player_choice = 'paper'

    if player_choice == autoplayer:# Autoplayer chose 'paper'
        messagebox.showinfo("", 'equal\ntry again')
    elif autoplayer == items[2]:  # Autoplayer chose 'scissors'
        messagebox.showerror("", "you lose\nlet's play one more time")
    elif autoplayer == items[0]:  # Autoplayer chose 'rock'
        messagebox.showinfo("", "congratulations you win\nlet's do it again")

# Function for the 'scissors' button
def scissors_choice():
    items = ['rock', 'paper', 'scissors']
    autoplayer = random.choice(items)
    player_choice = 'scissors'

    if player_choice == autoplayer:
        messagebox.showinfo("", 'equal\ntry again')
    elif autoplayer == items[0]:  # Autoplayer chose 'rock'
        messagebox.showerror("", "you lose\nlet's play one more time")
    elif autoplayer == items[1]:  # Autoplayer chose 'paper'
        messagebox.showinfo("", "congratulations you win\nlet's do it again")

# Initialize the main application window
app = tkinter.Tk()
app.title('Rock Paper Scissors')  # Set window title
app.geometry('400x200')  # Set window dimensions

# Load and set icon for the window
app.iconbitmap("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\game_game_console_play_device_icon_133759.ico")

# Load and display background image
background_image = Image.open("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\rock-paper-scissors.png")
background_image = background_image.resize((400, 200), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create and place canvas with background image
canvas = tkinter.Canvas(app, width=app.winfo_screenwidth(), height=app.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Load images for buttons
image1 = Image.open("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\scissors.png").resize((64, 64))
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\new-document.png").resize((64, 64))
photo2 = ImageTk.PhotoImage(image2)

image3 = Image.open("C:\\Users\\dell\\Desktop\\rock_paper_scissors\\stone.png").resize((64, 64))
photo3 = ImageTk.PhotoImage(image3)

# Add a label as a title in the game interface
label = tkinter.Label(canvas, text="Let's play", font=('Arial', 15, 'bold'), fg='green')
label.grid(row=0, column=1, pady=(11, 16))

# Create buttons for 'rock', 'paper', and 'scissors' options with images
rock = tkinter.Button(canvas, text='rock', image=photo3, command=rock_choice)
rock.grid(row=1, column=0, padx=(55, 0))

paper = tkinter.Button(canvas, text='paper', image=photo2, command=paper_choice)
paper.grid(row=1, column=1, padx=(40))

scissors = tkinter.Button(canvas, text='scissors', image=photo1, command=scissors_choice)
scissors.grid(row=1, column=2, padx=(0, 55))

# Run the application loop
app.mainloop()
