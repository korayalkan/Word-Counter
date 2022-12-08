#Take user's input and make it lowercase
def stringFormatting(userInput):

    return userInput.lower()



#Take user's input and remove 'spaces, regular expressions'
def wordSplitter(userInput):

    characters2remove = "!'^+%&/()=?_*-£><#$½{[]}\|.,:;é@₺€´`"

    userInput = ' '.join(userInput.split())
    userInput = ''.join(word for word in userInput if word not in characters2remove)
    userInput = userInput.split(' ')

    # Cleaning spaces here
    while ' ' in userInput:
        userInput.remove(' ')
        if ' ' not in userInput:
            break

    while '' in userInput:
        userInput.remove('')
        if '' not in userInput:
            break

    inputLenght = len(userInput)
    print(inputLenght)



#It's the main function
def main():

    userData = input("Enter your data: ")
    userData = stringFormatting(userData)
    userData = wordSplitter(userData)



main()