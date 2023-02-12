from tkinter import *

def logicalc(our_button):

    if our_button == 'C':
        lable1['text']= '0'
    elif our_button == 'DEL':
        lable1['text']= lable1['text'][0:-1]
    elif our_button == 'X^2':
        lable1['text']= str((eval(lable1['text']))**2)
    elif our_button == '=':
        lable1['text']= str(eval(lable1['text']))
    else:
        if lable1['text'] == '0':
            lable1['text'] = ''
        lable1['text'] = lable1['text'] + our_button

calc = Tk()
calc['background'] = 'gray'
calc.geometry('485x550')
calc.title('Супер калькулятор')
calc.resizable(True,True)

lable1 = Label(text= '0', font= 'Consolas 21 bold', bg= 'gray', foreground= 'blue')
lable1.place(x= 11, y= 50)

buttons = ["C", "DEL", "*", "=", "1", "2", "3", "/", "4", "5", "6", "+",
           "7", "8", "9", "-", "(", "0", ")", "X^2"]

x, y = 10, 140

for button in buttons:

    com = lambda x= button: logicalc(x) # 'заглушка', тк мы не можем вызвать оператор функции в параметре command

    Button(text= button, background= 'white', foreground= 'blue',
    font= 'Consolas 21 bold',
    command= com).place(x= x, y= y, width= 115, height= 80) # command= logicalc(button)

    x = x + 117

    if x > 400:
        y = y + 82
        x = 10

calc.mainloop()


