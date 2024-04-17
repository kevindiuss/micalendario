from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
from time import sleep

ventana=Tk()
ventana.title("Registro de citas Suplimed")
imagenFondo=PhotoImage(file="misupli.gif")
ventana.config(bg="blue")
pestañas=ttk.Notebook(ventana)
pestañas.pack(fill='both',expand='yes')
pestaña1=ttk.Frame(pestañas)
pestaña2=ttk.Frame(pestañas)
pestaña3=ttk.Frame(pestañas)
pestañas.add(pestaña1, text='Registro')
pestañas.add(pestaña2, text='Editar')
pestañas.add(pestaña3, text='Eliminar')

lblimagen=Label(pestaña1,image=imagenFondo,width=800, height=800).place(x=0,y=0)

txTipoDoc=Label(pestaña1,text='Tipo de Documento: ',padx=5, pady=20,background="white").grid(row=0,column=0,sticky="e")
inpTipoDoc=ttk.Combobox(pestaña1,width=30)
inpTipoDoc['values']=("Seleccione...",
"Cédula de Ciudadanía",
"Carné Diplomático",
"Cédula de Extranjería",
"Documento Extranjero",
"Pasaporte",
"Permiso Especial de Permanencia",
"Permiso por Protección Temporal",
"Registro Civil de Nacimiento",
"Salvoconducto",
"Tarjeta de Extranjería",
"Tarjeta de Identidad",
)
inpTipoDoc.grid(row=0,column=1,sticky="w")
inpTipoDoc.current(0)

losApellidos=StringVar()

txNumDoc=Label(pestaña1,text='Numero de documento: ',padx=5, pady=20,background="white").grid(row=0,column=2,sticky="e")
inpNumDoc=Entry(pestaña1,width=30).grid(row=0,column=3,sticky="w",columnspan=20)

txNombre=Label(pestaña1,text='Nombres: ',padx=5, pady=20,background="white").grid(row=3,column=0,sticky="e")
inpNombres=Entry(pestaña1,width=40).grid(row=3,column=1,sticky="w")

txApellidos=Label(pestaña1,text='Apellidos: ',padx=5, pady=20,background="white").grid(row=3,column=2,sticky="e")
inpApellidos=Entry(pestaña1,width=40,textvariable=losApellidos).grid(row=3,column=3,sticky="w",columnspan=20)

txDireccion=Label(pestaña1,text='Direccion: ',padx=5, pady=20,background="white").grid(row=5,column=0,sticky="e")
inpDireccion=Entry(pestaña1,width=40).grid(row=5,column=1,sticky="w")

txCorreo=Label(pestaña1,text='Correo: ',padx=5, pady=20,background="white").grid(row=5,column=2,sticky="e")
inpCorreo=Entry(pestaña1,width=40).grid(row=5,column=3,sticky="w",columnspan=20)

txTel=Label(pestaña1,text="Telefono: ",padx=5, pady=20,background="white").grid(row=7,column=0,sticky="e")
inptel=Entry(pestaña1,width=30).grid(row=7,column=1,sticky="w")

txEps=Label(pestaña1,text="Eps: ",padx=5, pady=20,background="white").grid(row=7,column=2,sticky="e")
inpEps=ttk.Combobox(pestaña1,width=30)
inpEps['values']=("Seleccione...",
"CCFC15 - COMFACOR(M)",
"CCFC20 - COMFACHOCÓ (M)",
"CCFC24 - COMFAMILIAR HUILA (M)",
"CCFC53 - COMFACUNDI UNICAJAS (M)",
"CCFC55 - CAJACOPI ATLÁNTICO (M)",
"EPS001 - ALIANSALUD",
"EPS002 - SALUD TOTAL",
"EPS005 - SANITAS",
"EPS008 - COMPENSAR",
"EPS010 - EPS SURA",
"EPS016 - COOMEVA",
"EPS017 - FAMISANAR",
"EPS018 - SERVICIO OCCIDENTAL DE SALUD S.O.S.",
"EPS023 - CRUZ BLANCA",
"EPS033 - SALUDVIDA",
"EPS037 - NUEVA EPS",
"EPS040 - SAVIA SALUD (M)",
"EPS041 - NUEVA EPS (M)",
"EPS042 - COOSALUD",
"EPS044 - MEDIMAS",
"EPSC22 - CONVIDA (M)",
"EPSC25 - CAPRESOCA (M)",
"EPSC33 - SALUDVIDA (M)",
"EPSC34 - CAPITAL SALUD (M)",
"EPSS44 - MEDIMAS (M)",
"ESSC02 - EMDISALUD E.S.S. (M)",
"ESSC07 - MUTUAL SER E.S.S. (M)",
"ESSC18 - EMSSANAR E.S.S. (M)",
"ESSC24 - COOSALUD E.S.S. (M)",
"ESSC33 - COMPARTA E.S.S. (M)",
"ESSC62 - ASMET SALUD E.S.S. (M)",
"ESSC76 - AMBUQ E.S.S",
"ESSC91 - ECOOPSOS E.S.S. (M)",
)

inpEps.current(0)
inpEps.grid(row=7,column=3,sticky="w",columnspan=20)

misVacunas=("Seleccione...","Bostrix","Rotarix","GC Flu","Varivax","Pneumovax","Prevenar 13","Sinflorix","Priorix","Tetavax","Vacuna Antitetánica","Fluarix","Vaxigrip","Influvac")

txVacunas=Label(pestaña1,text="Vacunas: ", pady=10,background="white").grid(row=9,column=1,sticky="w")
intVacuna1=ttk.Combobox(pestaña1,width=23)
intVacuna1['values']=misVacunas
intVacuna1.current(0)
intVacuna1.grid(row=10,column=1,sticky="w",pady=8)

intVacuna2=ttk.Combobox(pestaña1,width=23)
intVacuna2['values']=misVacunas
intVacuna2.current(0)
intVacuna2.grid(row=11,column=1,sticky="w",pady=8)

intVacuna3=ttk.Combobox(pestaña1,width=23)
intVacuna3['values']=misVacunas
intVacuna3.current(0)
intVacuna3.grid(row=12,column=1,sticky="w",pady=8)

intVacuna4=ttk.Combobox(pestaña1,width=23)
intVacuna4['values']=misVacunas
intVacuna4.current(0)
intVacuna4.grid(row=13,column=1,sticky="w",pady=8)

intVacuna5=ttk.Combobox(pestaña1,width=23)
intVacuna5['values']=misVacunas
intVacuna5.current(0)
intVacuna5.grid(row=14,column=1,sticky="w",pady=8)

misDosis=("...","RN","Única","Adicional","Primera","Segunda","Tercera","Cuarta","Quinta","1er Refuerzo","2do Refuerzo")

txDosis=Label(pestaña1,text="Dosis: ",padx=20, pady=10,justify="left",background="white").grid(row=9,column=1,sticky="e")
intDosis1=ttk.Combobox(pestaña1,width=9)
intDosis1['values']=misDosis
intDosis1.current(0)
intDosis1.grid(row=10,column=1,sticky="e",pady=8)

intDosis2=ttk.Combobox(pestaña1,width=9)
intDosis2['values']=misDosis
intDosis2.current(0)
intDosis2.grid(row=11,column=1,sticky="e",pady=8)

intDosis3=ttk.Combobox(pestaña1,width=9)
intDosis3['values']=misDosis
intDosis3.current(0)
intDosis3.grid(row=12,column=1,sticky="e",pady=8)

intDosis4=ttk.Combobox(pestaña1,width=9)
intDosis4['values']=misDosis
intDosis4.current(0)
intDosis4.grid(row=13,column=1,sticky="e",pady=8)

intDosis5=ttk.Combobox(pestaña1,width=9)
intDosis5['values']=misDosis
intDosis5.current(0)
intDosis5.grid(row=14,column=1,sticky="e",pady=8)



txFechaApli=Label(pestaña1,text="Fecha de Aplicación: ",padx=0, pady=10,background="white").grid(row=9,column=3,sticky="w",columnspan=20)
inpDia=Entry(pestaña1,width=3,justify="center")
inpDia.insert(0,"Día")
inpDia.grid(row=10,column=3,sticky="e")

inpDia.bind("<FocusIn>", lambda event:inpDia.delete(0,"end") if inpDia.get()=="Día" else None)
inpDia.bind("<FocusOut>",lambda event:inpDia.insert(0,"Día") if inpDia.get()==''else None)

inpmes=Entry(pestaña1,width=4,justify="center")
inpmes.insert(0,"Mes")
inpmes.grid(row=10,column=4,sticky="e")

inpmes.bind("<FocusIn>", lambda event:inpmes.delete(0,"end") if inpmes.get()=="Mes" else None)
inpmes.bind("<FocusOut>",lambda event:inpmes.insert(0,"Mes") if inpmes.get()==''else None)

inpAño=Entry(pestaña1,width=5,justify="center")
inpAño.insert(0,"Año")
inpAño.grid(row=10,column=5,sticky="w",padx=6)

inpAño.bind("<FocusIn>", lambda event:inpAño.delete(0,"end") if inpAño.get()=="Año" else None)
inpAño.bind("<FocusOut>",lambda event:inpAño.insert(0,"Año") if inpAño.get()==''else None)

txHoraApli=Label(pestaña1,text="Hora de Aplicación: ",padx=0, pady=10,background="white").grid(row=11,column=3,sticky="w",columnspan=20)
txHoras=Label(pestaña1,text="Horas:",padx=0, pady=0,background="white").grid(row=12,column=3,sticky="e")
inpHora=Entry(pestaña1,width=3,justify="center")
inpHora.grid(row=12,column=4,sticky="w")

txMin=Label(pestaña1,text="Min:",padx=0, pady=0,background="white").grid(row=12,column=5,sticky="e")
inpMin=Entry(pestaña1,width=3,justify="center")
inpMin.grid(row=12,column=6,sticky="w")

def laventana(event):

    # mensaje=messagebox.showinfo("Carga Exitosa","Registro cargado exitosamente!")
    print ("aqui estamos")
    while True:
        if losApellidos.get()== "":
            mensajeerror=messagebox.showinfo("Error","No se cargo el registro, corrija los siguientes errores: ")
            
            mensajeerror.replace("errores:","hola mundo")
            
            
            mensajeerror=messagebox.showinfo()
            break
        else:
            break      
        
   
    # emergente.destroy()
    
ventana.bind('<Return>',laventana)

botonAgendar=Button(pestaña1,width=15, height=2, text="Agendar",command=laventana).grid(row=16,column=3,sticky="e",columnspan=30)



# ---------------------------------pestaña3------------------------------------------------------------------

infoEliminacion=Label(pestaña3, text="Ingrese el # identificador del registro que desea eliminar y de click en 'Eliminar'",pady=20,font=("Arial Bold",12))
infoEliminacion.grid(row=4,column=0)

inpElimina=Entry(pestaña3,width=30)
inpElimina.grid(row=6,column=0)

# infro=Label(pestaña3,width=300, height=300,text="TOMA",bg='blue')
# infro.grid(row=8,column=5)






# para cambiar la transparencia de la raiz----------------------
# ventana.attributes('-alpha',0.8)


ventana.geometry('800x800')
# ventana.wm_attributes('-transparentcolor','blue')
ventana.mainloop()