import random
items = ['rock','paper','scissors']
while True:
    autoplayer = random.choice(items)
    player = str(input('choice rock, paper or scissors: '))
    if player == autoplayer:
        print('equal\ntry agian')
    elif player == items[0] and autoplayer == items[1]:
        print("you lose\nlet's playe one more time")
    elif player == items[0] and autoplayer == items[2]:
        print("congratulation you win\nlest's do it agian")
    elif player == items[1] and autoplayer == items[0]:
        print("congratulation you win\nlest's do it agian")
    elif player == items[1] and autoplayer == items[2]:
        print("you lose\nlet's playe one more time")
    elif player == items[2] and autoplayer == items[0]:
        print("you lose\nlet's playe one more time")
    elif player == items[2] and autoplayer == items[1]:
        print("congratulation you win\nlest's do it agian")
    elif player == "exit":
        break
    else:
        print("you have just 3 choices 'rock','paper','scissors'\ntry agian")
    