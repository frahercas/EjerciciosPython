import PyPDF2
import pyttsx3

pdf_reader = PyPDF2.PdfReader(open(r'XXXX.pdf', 'rb')) # En lugar de "XXXX" escribe el path donde se ubica el archivo PDF que quieres abrir seguido de la extención .pdf

speaker = pyttsx3.init()
engine = pyttsx3.init()
speaker.setProperty('rate', 140)

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
    
    # Guardar el texto en un archivo de audio
    audio_file = fr'XXXX.mp3' #Eb lugar de "XXXX" escribe el path donde deseas guardar el audio generaado seguido de la extención .mp3
    engine.save_to_file(text, audio_file)
    engine.runAndWait()

speaker.stop()
engine.stop()

