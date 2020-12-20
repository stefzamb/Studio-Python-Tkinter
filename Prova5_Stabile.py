# !/usr/bin/python3
from tkinter import * #importa tutto (Per Python3)
import time
import pyfirmata
#-------------------------------------------------------------------------------

#lancio comunicazione con Arduino Uno
if __name__ == '__main__':
	# Initiate communication with Arduino
	board = pyfirmata.Arduino('/dev/ttyACM0')
	print("Communication Successfully started")
	# Create bunch of useful variables
	pulsante = board.digital[5]
	LED1 = board.digital[13]
    # Start iterator to receive input data
	it = pyfirmata.util.Iterator(board)
	it.start()
    
    # Setup LEDs and button
	pulsante.mode = pyfirmata.INPUT


# FUNZIONI

def esci():			# chiude tutto
	print('BYE')
	r.destroy
	
def scrivi() :		#scrive il contenuto della Entry nella Label uno
	dato=d1.get()
	l1.config(text=dato)
	print('Ciao '+dato)


def leggiscala1(valore1):
	print('Valore della scala=',valore1)
	l2.config(text= valore1)
	valore2=int(valore1,10)
	l3.config(text= 1+valore2)

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

def ingresso():
	#time.sleep(1.01)
    # Get button current state
	pulsante_state=pulsante.read()
	#print(pulsante_state)
	if pulsante_state == False:
		li5.config(bg='green')	
	if pulsante_state == True:
		li5.config(bg='red')
	clock.after(100, ingresso)
	

#-------------------------------------------------------------------------------
r = Tk()            #Costruttore dell'oggetto (Container)

# VARIABILI
valore1=DoubleVar()
valore2=int()
time1 = ''

# Cosruzione della finestra principale e sua chiusura
r.title ('Mia Finestra')
r.resizable(width=False, height=False)
r.geometry ('400x500+100+100')
r.config (bg='light blue')   #colore sfondo
r.title ('Zambelli Stefano')
uscita= Button(r, text='EXIT', activebackground='yellow', 
		activeforeground='red', relief='raised', command= r.destroy)
uscita.place(x=330, y=450)	

# costruzione della cornice zero
cornice = Frame(r,relief=RAISED,bd=4)  # relief = FLAT RAISED SUNKEN GROOVE RIDGEN
cornice.place(x=20,y=20,height=100,width=300)
cornice.config(bg='yellow')
etichetta = Label( cornice, text = 'Cornice0', relief = RAISED )
etichetta.pack()

# Costruzione della cornice uno
cornice1 = Frame(r,relief=RAISED,bd=3)  
cornice1.place(x=20,y=150,height=100,width=300, )
cornice1.config (bg='light green')
etichetta1 = Label( cornice1, text = 'Cornice1', relief = RAISED )
etichetta1.pack()

# OROLOGIO
clock = Label(r, font=('times', 12, 'bold'), bg='green')
clock.place(x=2, y=450)
#clock.place(fill=BOTH, expand=1)

# Costruzione dell'etichetta input
li5=Label(r, width=3,relief=RAISED, bg='blue')
li5.place(x=5, y=350)



# Costruzione di una finestra di scrittura
d1=Entry(cornice, width=10,relief=RAISED,bg='white')
d1.place(x=1, y=20)	
	
# Costruzione dell'etichetta uno
l1=Label(cornice, width=10,relief=RAISED, bg='white')
l1.place(x=200, y=20)

# Costruzione dell' etichetta due
l2=Label(cornice1, width=10,relief=RAISED, bg='white')
l2.place(x=1, y=1)

# Costruzione dell' etichetta tre
l3=Label(cornice1, width=10,relief=RAISED, bg='white')
l3.place(x=1, y=25)



# Costruzione di un pulsante per leggere il dato in ingresso
# e scriverlo nell'etichetta
leggi= Button(cornice, text='LEGGI', activebackground='blue', 
		activeforeground='white', relief='raised', command= scrivi)
leggi.place(x=110, y=51)

# Costruzione di una slide
slide1=Scale(cornice1, orient=HORIZONTAL, relief=RAISED, length=270, 
		command=leggiscala1)
slide1.place(x=1,y=50)


#----------------

tick()	# Funzione controllo e visualizzazione orologio
ingresso()

r.mainloop()
