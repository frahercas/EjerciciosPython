import PyPDF2
import pyttsx3

pdf_reader = PyPDF2.PdfReader(open(r'C:\Users\herca\OneDrive\Documentos\PDFs General\George1984.pdf', 'rb'))

speaker = pyttsx3.init()
engine = pyttsx3.init()
speaker.setProperty('rate', 140)

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
    
    # Guardar el texto en un archivo de audio
    audio_file = fr'C:\Users\herca\Music\Audiolibros\page_{page_num}.mp3'
    engine.save_to_file(text, audio_file)
    engine.runAndWait()

speaker.stop()
engine.stop()

