import random

#base_text = "But Obama also emphasized that Trump's brand of populism is not a uniquely American phenomenon. And he said technology like social media was helping to create 'a volatile politics' by exposing differences within and between countries. 'In our globalized world, with the migration of people and the rapid movement of ideas and cultures and traditions, we see increasingly this blend of forces mixing together in ways that often enrich our societies but also cause tensions,' he said. 'Faced with this new reality where cultures clash, it's inevitable that some will seek a comfort in nationalism or tribe or ethnicity or sect.'And that, in turn, has created distrust between people and their governments, Obama said. 'There's a growing suspicion — or even disdain — for elites and institutions that seem remote from the daily lives of ordinary people. What an irony it is, at a time when we can reach out to people in the most remote corners of the planet, so many citizens feel disconnected from their own governments,' he said."
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
