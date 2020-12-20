# !/usr/bin/python3
from tkinter import * #importa tutto (Per Python3)

r = Tk()            #Costruttore dell'oggetto (Container)

var = DoubleVar()

def sel(var):
   label.config(text= "Value = " + var)
   print(var)



scale = Scale( r, variable = var, command=sel )
scale.pack(anchor = CENTER)

#button = Button(r, text = "Get Scale Value", command = sel)
#button.pack(anchor = CENTER)

label = Label(r)
label.pack()

r.mainloop()



#----------------
	



