print ("testando...")

import speech_recognition as sr

import os


#FunÃ§Ã£o responsÃ¡vel por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuÃ¡rio
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:
        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)
        
        #Avisa o usuÃ¡rio que estÃ¡ pronto para ouvir
        print("Diga alguma coisa: ")
        
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)

    try:
        #Passa a variÃ¡vel para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase:
            os.system("start chrome.exe")
            return False
        
        elif "Excel" in frase:
            os.system("start excel.exe")
            return False
        
        elif "PowerPoint" in frase:
            os.system("start POWERPNT.exe")
            return False
        
        elif "Edge" in frase:
            os.system("start msedge.exe")
            return False
        
        elif "Fechar" in frase:
            os.system("exit")
            return True
    
        #Retorna a frase pronunciada
        print("VocÃª disse: " + frase)
    
    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")
    
    return False
    
while True:
    if ouvir_microfone():
        break