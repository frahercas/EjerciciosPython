from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import speech_recognition as sr# Reconoce la voz
import pyttsx3

 
import time 
global name 
name= 'asistente cultural'

# Creamos una instancia del Chatbot
chatbot = ChatBot(
                    name,
                    storage_adapter= 'chatterbot.storage.SQLStorageAdapter',
                    logic_adapters=[
                        {
                            'import_path': 'chatterbot.logic.BestMatch',
                            'default_response': 'Lo siento, no entiendo tu respuesta, intenta de nuevo',
                            'maximum_similarity_threshold': 0.95
                        }
                                ]
                )

#Generamos una instancia de entrenamiento para nuestro chatbot
trainer = ListTrainer(chatbot)

#Agregamos los dialogos 
trainer.train([
    "chatterbot.corpus.spanish",
##Dentro de esta seccion escribe lo que quieres que se entrenado dentro de este algorito dividido por comas, palabras de activacion y rspuesta en ese orden
    " asistente",
    """Hola, Yo soy un asistente virtual, intenta preguntarme algo sobre lugares culturales""",
    "dime tres museos en ciudad de mexico",
    "Museo de arte moderno, museo de Banco de mexico y museo del juguete",

    "ubicacion arte moderno",
    """Avenida Paseo de la Reforma sin numero Bosque de Chapultepec primera Seccion delegacion Miguel Hidalgo """,
    "asistir banco de mexico",
    "Avenida cinco de Mayo  numero 2 Centro Histórico de la ciudad de México",
    " dirigir juguetes ",
    "calle doctor olvera numero quince colonia doctores",

    "hora de Arte moderno",
    """horario de martes a domingo de diez a dicisiete treinta horas""",
    " banco de mexico horas",
    """horario de martes a domingo de once a dicisiete horas""",
    "juguetes horario",
    "horario de martes a domingo de nueve a dicisiete horas",

    "cuantos museos hay en Ciudad de Mexico",
    """Segun el Sistema de informacion cultural existe 170 miseos en ciudad de mexico""",
    "Cual es el museo mas antigua de la ciudad de mexico",
    """Uno de los museos más antiguos y emblemáticos no sólo de la capital, sino de todo el país, es el Museo Nacional de Historia. Se encuentra en el Castillo de Chapultepec y es un símbolo histórico del país, inaugurado como museo en 1944.""",
    "Que es un museo",
    """Un museo es una institución sin fines lucrativos, permanente, al servicio de la sociedad y de su desarrollo, abierta al público, que adquiere, conserva, investiga, comunica y expone el patrimonio material e inmaterial de la humanidad y su medio ambiente con fines de educación, estudio y recreo.""",
    "Que exhibicion tiene actualmente el museo del banco de mexico",
    """tiene la exhibicion llamada: Poéticas pictóricas a la distancia: ARTE/BILLETE/MACULATURA/REFINES/DISEÑO""",
    "Que exhibicion tiene actualmente el museo de arte moderno",
    """El museo de arte moderno actualemnete cuenta con 3 exposiciones temporales llamadas Paisajes fragmentados, dimension publica de la escultura y manifiestos del arte mexicano""",
    "cuantas salas tiene el museo del juguete",
     """Son 6 salas: lucha libre,juguetes antiguos,tradicionales, de coleccion, epoca industrial y carritos""",

     "que costo tiene asistr al museo del banco de mexico",
     """La entrada es libre con previa reservacion""",
     "Costo de visitar el museo de arte moderno",
     """La entrada general tien un costo de 70 pesos, pero para estudiantes, maestros e INAPAM la entrada es gratuita""",
     "Cuanto cuesta ir al museo del juguete",
     """La entrada general tiene un costo de 75 pesos, pero por promocion tiene un costo de 50 pesos""",
     
   
])


listener = sr.Recognizer ()
engine = pyttsx3.init ()# Hablar

voices = engine.getProperty ('voices') #Obtenenos la lista de voces
engine.setProperty ('voice ', voices [0].id)

# Introducción
engine.say ("""¡Hola!, Yo soy tu asistente virtual cultural Yo te puedo responder preguntas generales sobre diferentes museos de la ciudad de mexico""")
engine.runAndWait ()

 # Text 2 Speech
def talk ( text ):
    engine.say( text )
    engine.runAndWait ()

# Speech 2 Text
def listen ():
    flag=True
    try :
        with sr.Microphone () as source:
            print ("Hable")
            voice = listener.listen (source, timeout=3)# Escucha
            rec = listener.recognize_google ( voice,language = 'es-ES')
            # Pasa a texto lo escuchado
            rec = rec.lower ()
            print (rec)
            run(rec)
            if 'adiós' in rec:
                flag=False
    except Exception as e:
            print (e)
            time.sleep(10)
    return flag

# Chatbot
def run (rec):
    #Accedemos al chatbot previamente entrenado
    chatbot = ChatBot(name)
    # Obtiene una respuesta
    response = chatbot.get_response(rec)
    talk(response)
    return response

flag= True

while flag: 
    flag = listen()
    pass
