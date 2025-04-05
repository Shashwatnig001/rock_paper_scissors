import tkinter as tk

# game setup
playerX = "X"
playerO = "O"
current_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
color_blue = "#0000FF"
color_green = "#008000"
color_black = "#000000"
color_light_grey = "#D3D3D3"
turn = 0
game_over = False


def set_title(row,column):
    global current_player
    if(game_over):
        return
    if board[row][column]["text"] != "":
        return
    board[row][column]["text"]=current_player
    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO
    label["text"] = f"{current_player}'s turn"
    check_winner()

def check_winner():
    global turn, game_over
    turn += 1
    # tie
    if(turn == 9):
        game_over = True
        label.config(text = "Tie!", foreground="red")
        return
    # diagonally
    if(board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] 
           and board[0][0]["text"] != ""):
            label.config(text=board[0][0]["text"]+" is the WINER!", foreground=color_green)
            for i in range(3):
                board[i][i].config(foreground=color_green)
            game_over = True
            return
    # antidiagonally
    if(board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] 
           and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"]+" is the WINER!", foreground=color_green)
        board[0][2].config(foreground=color_green)
        board[1][1].config(foreground=color_green)
        board[2][0].config(foreground=color_green)
        game_over = True
        return
    # horizontally
    for row in range(3):
        if(board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] 
           and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"]+" is the WINER!", foreground=color_green)
            for column in range(3):
                board[row][column].config(foreground=color_green)
            game_over = True
            return
    # vertically
    for column in range(3):
        if(board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] 
           and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"]+" is the WINER!", foreground=color_green)
            for row in range(3):
                board[row][column].config(foreground=color_green)
            game_over = True
            return

def new_game():
    global turn, game_over, current_player
    current_player = playerX
    turn = 0
    game_over = False
    label.config(text=current_player +"'s turn", foreground = "white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground = color_blue)


# window setup
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)
frame = tk.Frame(root)
label = tk.Label(frame, text = f"{current_player}'s turn", font = ("poppins", 20, "bold"),
                 background=color_black, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")
for row in range(3):
    for column in range(3):
        board[row][column] = tk.Button(frame, text="", font = ("poppins", 30, "bold"),
                 background=color_black, foreground=color_blue, width=4, height=1,
                 command= lambda row=row, column=column: set_title(row,column))
        board[row][column].grid(row=row+1, column=column)
button = tk.Button(frame, text = "Restart", font = ("poppins", 20, "bold"),
                 background=color_black, foreground="white", command=new_game)
button.grid(row=4,column=0, columnspan=3,sticky="we")
frame.pack()

# window to center
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


root.mainloop()