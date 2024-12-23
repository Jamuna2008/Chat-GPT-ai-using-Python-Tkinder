#Developing Chat Interface in Python with color
from tkinter import *
from tkinter import scrolledtext
def FunctionText():
    userinput=InputText.get('1.0',END)#1=line  0=character  till the end
    #print(userinput)
    DisplayText.config(state=NORMAL)
    DisplayText.insert(END,'you :'+userinput , 'user')
    DisplayText.insert(END,'Bot:'+"I am doing Good,Thanks"+"\n",'bot')
    DisplayText.config(state=DISABLED)
    InputText.delete('1.0',END)
    
root=Tk()
root.title("chat app")
root.geometry("500x600")
AppHeader=Label(root,text='Chat App',bg='grey',fg='black',font=("Georgia",25))
AppHeader.pack(fill=X,expand=True)

DisplayText=scrolledtext.ScrolledText(root,state=DISABLED,wrap=WORD)
DisplayText.pack(fill=BOTH,expand=True)

InputText=scrolledtext.ScrolledText(root,wrap=WORD,height=3)
InputText.pack(fill=BOTH,expand=True)

DisplayText.tag_config('user',foreground='Dark blue')
DisplayText.tag_config('bot',foreground='grey')

SendButton=Button(root,text='Send',font=('Georgia',10),command=FunctionText)
SendButton.pack()
root.mainloop()
