#myDict = {}
myDict = {"Indispensible":"Absolutely necessary","Boisterous":"Scandalous",
          "Present":["Existing or occurring now","A gift"]}
addWords = True

while addWords == True:
    print("Would you like to add a word to your dictionary? (y/n)")
    answer = input().lower()
    if (answer == "y"):
        print("What is the word?")
        word = input().lower()
        print("What is the definition of the word?")
        definition = input().lower()

        myDict[word] = definition
    elif (answer == "n"):
        print("Your dictionary has been saved!")
        addWords = False
    else:
        print("Please enter 'y' or 'n'")

print("My Dictionary:")
print()
for item in myDict:

    print("Word:" + item)
    definition = myDict[item]
    defineType = type(definition)

    if (defineType == str):
        print("Definition:" + myDict[item])

    elif(defineType == list):

        for x in definition:
            print("-" + x)

        print()

