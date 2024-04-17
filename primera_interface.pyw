from tkinter import *


raiz=Tk()  

raiz.title("El gato con botas")
raiz.resizable(1,1)      #redimensionar recibe parametros booleanos que corresponden a width:ancho y height:alto
# raiz.iconbitmap(r"graficos\gato.ico")  #"graficos\gato.ico"
raiz.geometry("650x350")

raiz.config(bg="blue")


#los metodos de Frame se encuentran en documentación -- Handy Reference --- Setting Options


miFrame=Frame()
miFrame.pack(side="right", fill="y", expand=True)          #se empaqueta dentro de la raiz, con fill y expand se expande en y
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)                      #grueso del borde
miFrame.config(relief="groove")          #Tipo de borde
miFrame.config(cursor="pirate")          #tipo de cursor       



raiz.mainloop()

#cuando ejecutamos este script, desde afuera de VSC se abrira la consola detras. Para evitar esto cambiamos la extensión
#a pyw