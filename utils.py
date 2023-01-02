import random ##esse aqui importa as libs
import time

## Função para escolher o nome a partir da lista e removê-lo
def escolher():

    frase = random.choice(sentences_list)
    f = open("editor.txt", "w")
    f.write(frase)
    f.close()
    sentences_list.remove(frase)
    time.sleep(7)
