from tkinter import *
from tkinter import messagebox
import random

count = 0
board_Double = [["","",""],
            ["","",""],
            ["","",""]]

board_Single = [["","",""],
            ["","",""],
            ["","",""]]

#Destruct a Window 
def destruct(master):
    master.destroy()

#Displaying the winner
def winner_display(string):
    win_disp = Tk()
    win_disp.geometry("600x200")
    win_disp.title("Congratulations☻")
    win_disp.configure(bg = "black")
    
    l1 = Label(win_disp, text = " Congratulations! The Winner Is ", bg = "black", fg = "green", font = ("TimesNewRoman",28))
    l1.pack()

    l2 = Label(win_disp, text = string, fg = "blue", bg = "black", font = ("TimesNewRoman",45))
    l2.pack()

    #Closes the winner window
    exit_btn = Button(win_disp, text = "EXIT", fg = "red", bg = "black", font = ("TimesNewRoman",20), command =lambda: destruct(win_disp))
    exit_btn.pack()

#Check the Winner by evaluating the board_Double
def winner_check():
    global count,board_Double

    #Condition for Player X to be the Winner
    if (board_Double[0][0]==board_Double[0][1]==board_Double[0][2]=="X" or board_Double[1][0]==board_Double[1][1]==board_Double[1][2]=="X" or board_Double[2][0]==board_Double[2][1]==board_Double[2][2]=="X" or
        board_Double[0][0]==board_Double[1][0]==board_Double[2][0]=="X" or board_Double[0][1]==board_Double[1][1]==board_Double[2][1]=="X" or board_Double[0][2]==board_Double[1][2]==board_Double[2][2]=="X" or
        board_Double[0][0]==board_Double[1][1]==board_Double[2][2]=="X" or board_Double[0][2]==board_Double[1][1]==board_Double[2][0]=="X"):
            winner_display("Player X")
    
    #Condition for Player O to be the Winner
    elif (board_Double[0][0]==board_Double[0][1]==board_Double[0][2]=="O" or board_Double[1][0]==board_Double[1][1]==board_Double[1][2]=="O" or board_Double[2][0]==board_Double[2][1]==board_Double[2][2]=="O" or
          board_Double[0][0]==board_Double[1][0]==board_Double[2][0]=="O" or board_Double[0][1]==board_Double[1][1]==board_Double[2][1]=="O" or board_Double[0][2]==board_Double[1][2]==board_Double[2][2]=="O" or
          board_Double[0][0]==board_Double[1][1]==board_Double[2][2]=="O" or board_Double[0][2]==board_Double[1][1]==board_Double[2][0]=="O"):
            winner_display("Player O")
    
    #Condition for Tie between Player X and Player O
    elif count==9:
        winner_display("NONE! IT IS A TIE!")

#Resets the Text value of Buttons and the values of the board_Double 
def reset(b1,b2,b3,b4,b5,b6,b7,b8,b9):
    
    #resetting the text values of the Buttons
    b1["text"]=""
    b2["text"]=""
    b3["text"]=""
    b4["text"]=""
    b5["text"]=""
    b6["text"]=""
    b7["text"]=""
    b8["text"]=""
    b9["text"]=""

    #resetting the board_Double values
    board_Double[0][0]=""
    board_Double[0][1]=""
    board_Double[0][2]=""
    board_Double[1][0]=""
    board_Double[1][1]=""
    board_Double[1][2]=""
    board_Double[2][0]=""
    board_Double[2][1]=""
    board_Double[2][2]=""

#Changes the Text value of the buttons and the values of the board_Single
#def changeVal_Single(button, boardValRow, boardValCol):
    #global count

    #condition for changing the text value of a button
    #if button["text"] == "":

        #condition for changing the text value of a button to X
        #if count % 2 == 0:
            #button["text"] = "X"
            #board_Single[boardValRow][boardValCol]
        
        #else:
            #pass

        #incrementing the count for the next move
        #count=count+1

        #condition to start checking for the winner 
        #if count>=5:
            #winner_check()
    #else:
        #pass


#Changes the text value of the buttons and the values of the board_Double
def changeVal_Double(button, boardValRow, boardValCol):
    global count

    #condition for changing the text value of a button
    if button["text"]=="":
        
        #Condition for changing the text value of a button to "X"
        if count%2==0:
            button["text"]="X"
            board_Double[boardValRow][boardValCol]="X"
        
        #Changing the text value of a button to "O" if condition fails 
        else:
            button["text"]="O"
            board_Double[boardValRow][boardValCol]="O"
        
        #incrementing the count for the next move
        count=count+1

        #condition to start checking for the winner 
        if count>=5:
            winner_check()
    else:
        pass

#Returns to the Main Menu
def home_return(master):
        master.destroy()
        Main_menu()

#for single player mode
#def Single_Player(master):
    
    #destroying the main menu
    #master.destroy()
    
    #creating a new window for single player
    #single = Tk()
    #single.geometry("300x400")
    #single.configure(bg = "black")

    #frame1 = Frame(single, width = 295, height = 395, borderwidth = 2, bg = "black")
    #frame1.pack()

    #return back to the main menu
    #back_btn = Button(single, text = "BACK", fg = "red", bg = "black", font = ("TimesNewRoman",12), command = lambda: home_return(single))
    #back_btn.place(x = 200, y = 350)

    #reset the text value of the buttons
    #reset_btn = Button(single, text = "RESET", fg = "pink", bg = "black", font = ("TimesNewRoman",12), command =lambda: reset(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9))
    #reset_btn.place(x = 50, y = 350)
    
    #you_lbl = Label(single, text = "Player", bg = "black", fg = "green", font = ("TimesNewRoman", 12))
    #you_lbl.place(x = 2, y = 2)
    
    #vs_lbl = Label(single, text = "VS", fg = "green", bg = "black", font = ("TimesNewRoman",12))
    #vs_lbl.place(x = 140, y = 2)

    #player2_lbl = Label(single, text = "Computer", bg = "black", fg = "green", font = ("TimesNewRoman",12))
    #player2_lbl.place(x = 226, y = 2)


    #creating 9 buttons for the board_Double to play

    #Row1
    #btn_1 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 0, 0))
    #btn_1.place(x = 10, y = 50)
    #btn_2 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 0, 1))
    #btn_2.place(x = 105, y = 50)
    #btn_3 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 0, 2))
    #btn_3.place(x = 200, y = 50)

    #Row2
    #btn_4 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 1, 0))
    #btn_4.place(x = 10, y = 145)
    #btn_5 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 1, 1))
    #btn_5.place(x = 105, y = 145)
    #btn_6 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 1, 2))
    #btn_6.place(x = 200, y = 145)

    #Row3
    #btn_7 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 2, 0))
    #btn_7.place(x = 10, y = 240)
    #btn_8 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 2, 1))
    #btn_8.place(x = 105, y = 240)
    #btn_9 = Button(single, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda : changeVal_Single(btn_1, 2, 2))
    #btn_9.place(x = 200, y = 240)


    #single.mainloop()

#for double player mode
def Double_player(master):

    #destroying the main menu
    master.destroy()

    #creating a new window for single player
    double = Tk()
    double.geometry("300x400")
    double.configure(bg = "black")
    
    frame1 = Frame(double, width = 295, height = 395, borderwidth = 2, bg = "black")
    frame1.pack()

    #return back to the main menu
    back_btn = Button(double, text = "BACK", fg = "red", bg = "black", font = ("TimesNewRoman",12), command = lambda: home_return(double))
    back_btn.place(x = 200, y = 350)

    #reset the text value of the buttons
    reset_btn = Button(double, text = "RESET", fg = "pink", bg = "black", font = ("TimesNewRoman",12), command =lambda: reset(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9))
    reset_btn.place(x = 50, y = 350)
    
    player1_lbl = Label(double, text = "Player 1 ", bg = "black", fg = "green", font = ("TimesNewRoman", 12))
    player1_lbl.place(x = 2, y = 2)
    
    vs_lbl = Label(double, text = "VS", fg = "green", bg = "black", font = ("TimesNewRoman",12))
    vs_lbl.place(x = 140, y = 2)

    player2_lbl = Label(double, text = "Player 2 ", bg = "black", fg = "green", font = ("TimesNewRoman",12))
    player2_lbl.place(x = 2, y = 2)


    #creating 9 buttons for the board_Double to play

    #Row1
    btn_1 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_1,0,0))
    btn_1.place(x = 10, y = 50)
    btn_2 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_2,0,1))
    btn_2.place(x = 105, y = 50)
    btn_3 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_3,0,2))
    btn_3.place(x = 200, y = 50)
    
    #Row2
    btn_4 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_4,1,0))
    btn_4.place(x = 10, y = 145)
    btn_5 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_5,1,1))
    btn_5.place(x = 105, y = 145)
    btn_6 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_6,1,2))
    btn_6.place(x = 200, y = 145)


    #Row3
    btn_7 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_7,2,0))
    btn_7.place(x = 10, y = 240)
    btn_8 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_8,2,1))
    btn_8.place(x = 105, y = 240)
    btn_9 = Button(double, text = "", bg = "black", fg = "grey", font = ("TimesNewRoman",35),width = 3, height = 1, command = lambda: changeVal_Double(btn_9,2,2))
    btn_9.place(x = 200, y = 240)


    double.mainloop()

#creating window for Main menu
def Main_menu():
    root = Tk()
    root.geometry("300x400")
    root.title("TIC TAC TOE")
    root.configure(background="black")
    frame1 = Frame(root, width = 295, height = 395, borderwidth = 2, background = "black")
    frame1.pack()
    title = Label(root, fg = "green", bg = "black", text = "TIC TAC TOE", font = ("TimesNewRoman",30))
    title.place(x = 25,y = 0)
    modes = Label(root, fg = "grey", bg = "black", text = "Select Mode", font = ("TimesNewRoman",25))
    modes.place(x = 60, y = 80)

    single_player = Button(root, text = "Single Player", fg = "blue", bg = "black", font = ("TimesNewRoman",20), command =lambda: Temp_Single(root))
    double_player = Button(root, text = "Double Player", fg = "blue", bg = "black", font = ("TimesNewRoman",20), command =lambda: Double_player(root))

    single_player.place(x = 55, y = 150)
    double_player.place(x = 50, y = 250)

    exit_btn = Button(root, text = "EXIT", fg = "red", bg = "black", font = ("TimesNewRoman",12), command = lambda: destruct(root))
    exit_btn.place(x = 130, y = 340)

    root.mainloop()

#As the Single player mode is under development you may not be able to access it 
# But soon .. the single player mode will be updated in the code
def Temp_Single(master):
    master.destroy()

    win_disp = Tk()
    win_disp.geometry("600x200")
    win_disp.title("Sorry ")
    win_disp.configure(bg = "black")

    l1 = Label(win_disp, text = "SORRY ☻", bg = "black", fg = "green", font = ("TimesNewRoman",28))
    l1.pack()

    l2 = Label(win_disp, text = "The Single Player Mode is under Development", fg = "blue", bg = "black", font = ("TimesNewRoman",20))
    l2.pack()

    l2 = Label(win_disp, text = "It will me updated Soon", fg = "blue", bg = "black", font = ("TimesNewRoman",20))
    l2.pack()

    back_btn = Button(win_disp, text = "BACK", fg = "red", bg = "black", font = ("TimesNewRoman",20), command =lambda: home_return(win_disp))
    back_btn.pack()


#Execution
if __name__=="__main__":
    Main_menu()