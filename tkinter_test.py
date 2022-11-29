def hello():
 print('Привет!')


from tkinter import *
tk=Tk()
canvas=Canvas(tk, width=400, height=400, bg='blue')
canvas.pack()
canvas.create_line(0,0,400,400)
canvas.create_rectangle(20,20,360,360)
canvas.create_oval(10,10,90,90,fill='red',outline='yellow')
btn=Button(tk, text='Click', command=hello)
btn.pack()
tk.mainloop()
