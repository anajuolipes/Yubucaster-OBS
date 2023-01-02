import random
import time
import utils

##Frases##

file = open("Sentences.txt", "r")
sentences_list = []
for line in file:
        stripped_line = line.strip()
        sentences_list.append(stripped_line)

utils.sentences_list = sentences_list

while True:
        utils.escolher()
        if len(sentences_list) == 0:
                print("Encerrado")
                break