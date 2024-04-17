from tkinter import messagebox
from time import sleep
from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime
from tkinter import*
from tkinter import ttk 
import webbrowser
get_url=webbrowser.open('https://calendar.google.com/calendar/embed?src=rg5h3e4es68mg3urvlevblqn9k%40group.calendar.google.com&ctz=America%2FBogota')


CLIENT_SECRET_FILE='secreto.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)


# print(dir(service))

# Crear Calendario--------------------------------------------------------------
# calendario={
#     'summary': 'Calendario BOGOTA'
# }

# crear_calendario = service.calendars().insert(body=calendario).execute()

# print (crear_calendario['id'])

#Eliminar Calendario-----------------------------------------------------------
# service.calendars().delete(calendarId='9p5mhqtp3cr7mmebn22phta55k@group.calendar.google.com').execute()

#Listar todos los calendarios---------------------------------------------------

# respuesta=service.calendarList().list().execute()

# calendario=respuesta.get('items')[3]

# print(calendario['summary'])

#Colores de calendarios y eventos-----------------------------------------------
# colorperfiles=service.colors().get().execute()
# pprint(colorperfiles)

#Actualizar información de calendario--------------------------------------------
# respuesta=service.calendarList().list().execute()

# calendario=respuesta.get('items')[3]

# print(calendario['summary'])
# print(calendario['id'])

# calendario['summary']="Calendario MEDELLIN"
# calendario['description']="en este calendario se enlistan todos los eventos de la ciudad de MEDELLIN"

# service.calendars().update(calendarId=calendario['id'], body=calendario).execute()

#--------------------------------------------------------------------------------




ventana=Tk()
ventana.title("Registro de citas Suplimed")
imagenFondo=PhotoImage(file="misupli.gif")
ventana.config(bg="blue")
ventana.geometry('800x800')

pestañas=ttk.Notebook(ventana)
pestañas.pack(fill='both',expand='yes')
pestaña1=ttk.Frame(pestañas)
pestaña2=ttk.Frame(pestañas)
pestaña3=ttk.Frame(pestañas)
pestañas.add(pestaña1, text='Registro')
pestañas.add(pestaña2, text='Editar')
pestañas.add(pestaña3, text='Eliminar')

lblimagen=Label(pestaña1,image=imagenFondo,width=800, height=800).place(x=0,y=0)

miframe=Frame(pestaña1).config(bg="red")


numdocumento=StringVar()
losNombres=StringVar()
losApellidos=StringVar()
laDireccion=StringVar()
elCorreo=StringVar()
elTelefono=StringVar()



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

txNumDoc=Label(pestaña1,text='Numero de documento: ',padx=5, pady=20,background="white").grid(row=0,column=2,sticky="e")
inpNumDoc=Entry(pestaña1,width=30,textvariable=numdocumento).grid(row=0,column=3,sticky="w",columnspan=20)

txNombre=Label(pestaña1,text='Nombres: ',padx=5, pady=20,background="white").grid(row=3,column=0,sticky="e")
inpNombres=Entry(pestaña1,width=40,textvariable=losNombres).grid(row=3,column=1,sticky="w")

txApellidos=Label(pestaña1,text='Apellidos: ',padx=5, pady=20,background="white").grid(row=3,column=2,sticky="e")
inpApellidos=Entry(pestaña1,width=40,textvariable=losApellidos).grid(row=3,column=3,sticky="w",columnspan=20)

txDireccion=Label(pestaña1,text='Direccion: ',padx=5, pady=20,background="white").grid(row=5,column=0,sticky="e")
inpDireccion=Entry(pestaña1,width=40,textvariable=laDireccion).grid(row=5,column=1,sticky="w")

txCorreo=Label(pestaña1,text='Correo: ',padx=5, pady=20,background="white").grid(row=5,column=2,sticky="e")
inpCorreo=Entry(pestaña1,width=40,textvariable=elCorreo).grid(row=5,column=3,sticky="w",columnspan=20)

txTel=Label(pestaña1,text="Telefono: ",padx=5, pady=20,background="white").grid(row=7,column=0,sticky="e")
inptel=Entry(pestaña1,width=30,textvariable=elTelefono).grid(row=7,column=1,sticky="w")

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


losDias=StringVar()
losMeses=StringVar()
losAños=StringVar()
lasHoras=StringVar()
losMinutos=StringVar()

txFechaApli=Label(pestaña1,text="Fecha de Aplicación: ",padx=0, pady=10,background="white").grid(row=9,column=3,sticky="w",columnspan=20)
inpDia=Entry(pestaña1,width=3,justify="center",textvariable=losDias)
inpDia.insert(0,"Día")
inpDia.grid(row=10,column=3,sticky="e")

inpDia.bind("<FocusIn>", lambda event:inpDia.delete(0,"end") if inpDia.get()=="Día" else None)
inpDia.bind("<FocusOut>",lambda event:inpDia.insert(0,"Día") if inpDia.get()==''else None)

inpmes=Entry(pestaña1,width=4,justify="center",textvariable=losMeses)
inpmes.insert(0,"Mes")
inpmes.grid(row=10,column=4,sticky="e")

inpmes.bind("<FocusIn>", lambda event:inpmes.delete(0,"end") if inpmes.get()=="Mes" else None)
inpmes.bind("<FocusOut>",lambda event:inpmes.insert(0,"Mes") if inpmes.get()==''else None)

inpAño=Entry(pestaña1,width=5,justify="center",textvariable=losAños)
inpAño.insert(0,"Año")
inpAño.grid(row=10,column=5,sticky="w",padx=6)

inpAño.bind("<FocusIn>", lambda event:inpAño.delete(0,"end") if inpAño.get()=="Año" else None)
inpAño.bind("<FocusOut>",lambda event:inpAño.insert(0,"Año") if inpAño.get()==''else None)

txHoraApli=Label(pestaña1,text="Hora de Aplicación: ",padx=0, pady=10,background="white").grid(row=11,column=3,sticky="w",columnspan=20)
txHoras=Label(pestaña1,text="Horas:",padx=0, pady=0,background="white").grid(row=12,column=3,sticky="e")
inpHora=Entry(pestaña1,width=3,justify="center",textvariable=lasHoras)
inpHora.grid(row=12,column=4,sticky="w")

txMin=Label(pestaña1,text="Min:",padx=0, pady=0,background="white").grid(row=12,column=5,sticky="e")
inpMin=Entry(pestaña1,width=3,justify="center",textvariable=losMinutos)
inpMin.grid(row=12,column=6,sticky="w")





def CreaEvento():
    arrayVacunas=[intVacuna1.get(),intVacuna2.get(),intVacuna3.get(),intVacuna4.get(),intVacuna5.get()]
    arrayDosis=[intDosis1.get(),intDosis2.get(),intDosis3.get(),intDosis4.get()]
    inteldia=int(losDias.get())
    intelmes=int(losMeses.get())
    intelaño=int(losAños.get())
    intelhora=int(lasHoras.get())
    intelmin=int(losMinutos.get())
    for vacuna in arrayVacunas:

        print(vacuna)
        print(inteldia-2)
        if vacuna != "Seleccione...":
            print(arrayVacunas.index(vacuna))
            # Crear Eventos-------------------------------------------------------------------
            id_calendario_MEDELLIN='rg5h3e4es68mg3urvlevblqn9k@group.calendar.google.com'

            ajustedetiempo_colombia=5

            evento_cuerpodeSolicitud={
                'start':{
                    'dateTime':convert_to_RFC_datetime(2023,intelmes,inteldia,intelhora + ajustedetiempo_colombia,intelmin),
                    'timeZone':'America/Bogota'
                },
                'end':{
                    'dateTime':convert_to_RFC_datetime(2023,intelmes,inteldia,intelhora + ajustedetiempo_colombia,intelmin),
                    'timeZone':'America/Bogota'
                },
                'summary':f'{numdocumento.get()}/\n{losNombres.get()} {losApellidos.get()}',
                'description':f'{inpTipoDoc.get()} / {numdocumento.get()} / {losNombres.get()} / {losApellidos.get()} / {elCorreo.get()} / {elTelefono.get()} / {inpEps.get()} / {vacuna} / {arrayDosis[arrayVacunas.index(vacuna)]}',
                'colorId':9,
                'status':'confirmed',
                'transparency':'opaque',
                # 'visibility':'public',
                'location':laDireccion.get()
            
            }

            maxAttendees=5
            sendNotification=True
            sendUpdate='none'
            supportsAttachments=False


            respuesta=service.events().insert(
                calendarId=id_calendario_MEDELLIN,
                maxAttendees=maxAttendees,
                sendNotifications=sendNotification,
                sendUpdates=sendUpdate,
                supportsAttachments=supportsAttachments,
                body=evento_cuerpodeSolicitud
            ).execute()
    
    mensajeexitoso=messagebox.showinfo("Carga Exitosa","Registro cargado exitosamente!")       
     
botonAgendar=Button(pestaña1,width=15, height=2, text="Agendar",command=CreaEvento).grid(row=16,column=3,sticky="e",columnspan=30)

def AbreCalendario():
    get_url=webbrowser.open('https://calendar.google.com/calendar/embed?src=rg5h3e4es68mg3urvlevblqn9k%40group.calendar.google.com&ctz=America%2FBogota')

def AbreSpreads():
    get_url=webbrowser.open('https://docs.google.com/spreadsheets/d/161Q1tiDGoLyfoy3AEeFnYE6lpJfCAEzL5djfLM_b-bo/edit?usp=sharing')
    

botonCalendario=Button(pestaña1,width=15,height=2,text="Calendario",command=AbreCalendario).grid(row=16,column=0,sticky="e")

botonExcel=Button(pestaña1,width=15,height=2,text="Excel",command=AbreSpreads).grid(row=16,column=1,sticky="w")

ventana.mainloop()
# pprint(respuesta['id'])
# eventId=respuesta['id']

#Actualizar eventos---------------------------------------------------------
# ajustedetiempo_colombia=5
# eventoId='pgn3uvlqsmtqqrmrengfro8190'
# Id_deCalendario='rg5h3e4es68mg3urvlevblqn9k@group.calendar.google.com'
# evento = service.events().get(calendarId=Id_deCalendario, eventId=eventoId).execute()

# start_datetime=convert_to_RFC_datetime(2023,3,7,16 + ajustedetiempo_colombia,30)
# end_datetime=convert_to_RFC_datetime(2023,3,7,18 + ajustedetiempo_colombia,30)

# evento['start']['dateTime']=start_datetime
# evento['end']['dateTime']=end_datetime
# evento['summary']='Cena CON MI FAMILIA'
# evento['description']='Es una comida en la noche sin frisoles'


# service.events().update(
#     calendarId=Id_deCalendario,
#     eventId=evento['id'],
#     body=evento).execute()

#Eliminar eventos-----------------------------------------------------------
# try:
#     eventoId='aqacpc8de18fvca8d0ing141k0'
#     Id_deCalendario='rg5h3e4es68mg3urvlevblqn9k@group.calendar.google.com'
#     respuesta=service.events().delete(calendarId=Id_deCalendario, eventId=eventoId).execute()

#     pprint(respuesta)

# except:
#     print("ese tal evento no existe")








