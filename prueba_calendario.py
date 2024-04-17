from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime
from tkinter import*
from tkinter import ttk 
import webbrowser

CLIENT_SECRET_FILE='secreto.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

# page_token = None

# while True:
events = service.events().list(calendarId='rg5h3e4es68mg3urvlevblqn9k@group.calendar.google.com').execute()
for event in events['items']:
    try:
        mievento=event['start']
        # eventocompleto=mievento.split('/')
        # print (eventocompleto[0])
        print (mievento['dateTime'])
    except:
        pass

    # page_token = events.get('nextPageToken')
    # if not page_token:
    #     break

# id_calendario_MEDELLIN='rg5h3e4es68mg3urvlevblqn9k@group.calendar.google.com'

# ajustedetiempo_colombia=5

# evento_cuerpodeSolicitud={
#     'start':{
#         'dateTime':convert_to_RFC_datetime(2023,4,9,12 + ajustedetiempo_colombia,40),
#         'timeZone':'America/Bogota'
#     },
#     'end':{
#         'dateTime':convert_to_RFC_datetime(2023,4,9,12 + ajustedetiempo_colombia,40),
#         'timeZone':'America/Bogota'
#     },
#     'summary':'Hola soy yo',
#     'description':'Este es el texto de la descripcion',
#     'colorId':7,
#     'status':'confirmed',
#     'transparency':'opaque',
#     # 'visibility':'public',
#     'location':'mi direccion'

# }

# maxAttendees=5
# sendNotification=True
# sendUpdate='none'
# supportsAttachments=False


# respuesta=service.events().insert(
#     calendarId=id_calendario_MEDELLIN,
#     maxAttendees=maxAttendees,
#     sendNotifications=sendNotification,
#     sendUpdates=sendUpdate,
#     supportsAttachments=supportsAttachments,
#     body=evento_cuerpodeSolicitud
# ).execute()
