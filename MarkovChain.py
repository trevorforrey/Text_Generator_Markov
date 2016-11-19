import random

file = open("TextFile.txt")
base_text = ""
for line in file:
    base_text += line

prefix_num = 10
prefixes = {}

def generateText():

    currentGram = base_text[0:prefix_num]
    result = currentGram

    for character in range(0,1000):
        #print("For generation: " + currentGram)
        try:
            possible_characters = prefixes[currentGram]
        except:
            #print("I Broke")
            continue
        next_character = random.choice(possible_characters)
        result += next_character
        length = len(result)
        currentGram = result[length - prefix_num:length]

    print(result)

# This works just the way it should
for character in range(0,len(base_text) - prefix_num):
    gram = base_text[character:character + prefix_num]

    #print("For Creation: " + gram)

    if gram not in prefixes:
        prefixes[gram] = []

    prefixes[gram].append(base_text[character + prefix_num])

#    for key in prefixes:
#        print(key)
#        for value in key:
#            print(value)

generateText()
