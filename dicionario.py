import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "Achachay": "se usa para indicar que hace frío"
            "Acolitar": "Acompañar o ayudar a alguien"
            "Aguaje": "Marea alta"                                           
            "Alhaja": "Bonito o simpático"

            }

while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
        print("---------------------------------------------------")
        time.sleep(0.5)
    else:
        print("Perdon, esa palabra no esta :(")
        print("---------------------------------------------------")
        time.sleep(0.5)
