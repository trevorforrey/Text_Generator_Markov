import random

# Reads text file and puts contents in one string
file = open("TextFile.txt")
base_text = ""
for line in file:
    base_text += line
base_text.replace('\n', ' ').replace('\r', '')

prefix_num = 10
prefixes = {}

# Generates a set amount of randomly generated text
def generateText(amount_of_generated_text):

    # Grab the first "gram" of the text (based on prefix limit)
    currentGram = base_text[0:prefix_num]
    result = currentGram

    # For each character group in the size of the generated text
    for character_group in range(0,amount_of_generated_text):
        #print("For generation: " + currentGram)

        # Grab collection of all possible suffixes based on current prefix
        try:
            possible_characters = prefixes[currentGram]
        except:
            #print("I Broke")
            continue

        # Randomly choose the next text node to add to the generated text
        next_character = random.choice(possible_characters)

        # Add character to the result generated text
        result += next_character
        length = len(result)

        # Grab the next node to process
        currentGram = result[length - prefix_num:length]

    print(result)



# For every text "node" of text in the file
for character in range(0,len(base_text) - prefix_num):

    # Grab the next "node" of text
    gram = base_text[character:character + prefix_num]

    #print("For Creation: " + gram)

    # If the text node hasn't been seen before, create a collection for it
    if gram not in prefixes:
        prefixes[gram] = []

    # Append the next node in the substring to the substring collection
    prefixes[gram].append(base_text[character + prefix_num])

#    for key in prefixes:
#        print(key)
#        for value in key:
#            print(value)

generateText(1000)
