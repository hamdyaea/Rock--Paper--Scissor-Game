import Tkinter # For Python3.0 --> import tkinter
import tkMessageBox
import random



top = Tkinter.Tk() # For Python3.0 --> top = tkinter.tk()
top.title("Rock | Paper | Scissor")



    
 
user_score = 0
comp_score = 0
def Rock():
    global user_score, comp_score
    
    comp = random.randint(1,3)
    #print("your choice: Rock")
    #print("Comp choice: "+str(comp))
    if comp == 3:
        comp = "Scissor"
        user_score+=1
        tkMessageBox.showinfo("Congratulation!!", "YOU WIN!!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==1:
        comp = "Rock"
        tkMessageBox.showinfo("Same pinch!!", "IT'S A TIE!! !!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))   
        
        
    else:
        comp = "Paper"
        comp_score+=1
        tkMessageBox.showinfo("Hard Luck!!", "YOU LOOSE!!\n"+"Your Choice:Rock"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    
    
def paper():
    global user_score, comp_score
    
    comp = random.randint(1,3)
    #print("your choice: paper")
    #print("Comp choice: "+str(comp))
    if comp == 1:
        comp = "Rock"
        user_score+=1
        tkMessageBox.showinfo("Congratulation!!", "YOU WIN!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==2:
        comp = "Paper"
        tkMessageBox.showinfo("Same pinch!!", "IT'S A TIE!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score)) 
        
        
    else:
        comp = "Scissor"
        comp_score+=1
        tkMessageBox.showinfo("Hard Luck!!", "YOU LOOSE!!\n"+"Your Choice:Paper"+"\nComp Choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
def scissor():
    global user_score, comp_score
    
    comp = random.randint(1,3)
    #print("your choice: scissor")
    #print("Comp choice: "+str(comp))
    if comp == 2:
        comp = "Paper"
        user_score+=1
        tkMessageBox.showinfo("Congratulation!!", "YOU WIN!!\nYour Choice: Scissor\n"+"Comp choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
    elif comp==3:
        comp = "Scissor"
        tkMessageBox.showinfo("Same pinch!!", "IT'S A TIE!!\nYour Choice: Scissor\n"+"Comp choice: "+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score)) 
        
        
    else:
        comp = "Rock"
        comp_score+=1
        tkMessageBox.showinfo("Hard Luck!!", "YOU LOOSE!!\nYour Choice: Scissor\n"+"Comp choice:"+comp+"\nYour Score: "+str(user_score)+"\nComputer Score: "+str(comp_score))
        
        
    
B1 = Tkinter.Button(top, text = "Rock",bg='red',height="10",width="20", command = Rock)
B2 = Tkinter.Button(top, text = "Paper",bg='green',height="10",width="20", command = paper)
B3 = Tkinter.Button(top, text = "Scissor",bg='blue',height="10",width="20", command = scissor)
B1.pack(side='left')
B2.pack(side='left')
B3.pack(side='left')

top.mainloop()