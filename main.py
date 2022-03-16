import tkinter
import tkinter.messagebox

answer = 'no'

while answer == 'no':
    answer = tkinter.messagebox.askquestion(title='<3', message='Do you love me?')
    if answer == 'yes':
        tkinter.messagebox.showinfo(title='<3', message='I love u too :)')
    elif answer == 'no':
        tkinter.messagebox.showinfo(title='>:(', message='I Hate you')