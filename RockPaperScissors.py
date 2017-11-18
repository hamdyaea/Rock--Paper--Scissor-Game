import tkinter as tk
import tkinter 
from tkinter import messagebox
import random

# Developer : Hamdy Abou El Anein

top = tkinter.Tk() 
top.title("Rock | Paper | Scissor")



    
 
user_score = 0
comp_score = 0
def Rock():
    global user_score, comp_score
    
    comp = random.randint(1,3)

    if comp == 3:
        comp = "Scissor"
        user_score+=1
        messagebox.showinfo("Congratulation!!", "YOU WIN!!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==1:
        comp = "Rock"
        messagebox.showinfo("Same pinch!!", "IT'S A TIE!! !!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))   
        
        
    else:
        comp = "Paper"
        comp_score+=1
        messagebox.showinfo("Hard Luck!!", "YOU LOOSE!!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    
    
def paper():
    global user_score, comp_score
    
    comp = random.randint(1,3)

    if comp == 1:
        comp = "Rock"
        user_score+=1
        messagebox.showinfo("Congratulation!!", "YOU WIN!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==2:
        comp = "Paper"
        messagebox.showinfo("Same pinch!!", "IT'S A TIE!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score)) 
        
        
    else:
        comp = "Scissor"
        comp_score+=1
        messagebox.showinfo("Hard Luck!!", "YOU LOOSE!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
def scissor():
    global user_score, comp_score
    
    comp = random.randint(1,3)

    if comp == 2:
        comp = "Paper"
        user_score+=1
        messagebox.showinfo("Congratulation!!", "YOU WIN!!\nYour Choice: Scissor\n"+"Comp choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==3:
        comp = "Scissor"
        messagebox.showinfo("Same pinch!!", "IT'S A TIE!!\nYour Choice: Scissor\n"+"Comp choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score)) 
        
        
    else:
        comp = "Rock"
        comp_score+=1
        messagebox.showinfo("Hard Luck!!", "YOU LOOSE!!\nYour Choice: Scissor\n"+"Comp choice:"+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
        
    
B1 = tkinter.Button(top, text = "Rock",bg='red',height="10",width="20", command = Rock)
B2 = tkinter.Button(top, text = "Paper",bg='green',height="10",width="20", command = paper)
B3 = tkinter.Button(top, text = "Scissor",bg='blue',height="10",width="20", command = scissor)
B1.pack(side='left')
B2.pack(side='left')
B3.pack(side='left')

top.mainloop()
