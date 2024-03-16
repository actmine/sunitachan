letters = "abcdefghijklmnopqrstuvwxyz"
op = input(": ") # text that is going to be decypted
def FUNC_GET_ALPHA():
    with open("//home/actmine//faker//" + op + ".txt") as getterpaint:
        return getterpaint.read() # to get the decrypted text
output = FUNC_GET_ALPHA() # decrypted text
def ALPHA_TO_NUMBER(NUMBER_ALPHA, NUMBER_ALPHA_NUMBER): # func. to convert a given encrypted number into alphabet. takes to arguments the number and the multiplication number
    ALPHA_y = NUMBER_ALPHA / NUMBER_ALPHA_NUMBER
    checker_X = 0
    for x in letters:
        checker_X = checker_X + 1
        if checker_X == ALPHA_y:
            return x
        else:
            pass

y = 0 # multiplication number
number_currentFORX = "" # the number that is going to be sent to the ALPHA_TO_NUMBER func. for conversion to alphabet
ftext = "" # the final text
counter =0 # for debuggin purposes
output = output[1:] # this is done to remove the space at the starting
for x in output:
    counter = counter + 1 # for debugging purposes
    print("Output number:" + x) # the current number that is going to be send for conversion
    if x == ",": # indicates that there is a new word
        number_currentFORX = "" # resets the value of the current number
        ftext = ftext + " " # adds space to the final value to indicate new word
    elif x == " ": # the space in the output indicates a new alphabet
        y = y + 1
        if y > 10:# ensures that the multiplication number does not increase more than 10 
            y = 1
        else:
            pass
        final = ALPHA_TO_NUMBER(int(number_currentFORX), y) # the current number and the multiplicaiton number are send to the function for conversion to alphabet
        ftext = ftext + str(final) # updates the ftext
        number_currentFORX = "" # resets the current numbre
    else:
        number_currentFORX = number_currentFORX + x # now if there is no space or comma then the current x is added to the number_currentforx so that when there is a space this variable is send for conversion to alphabet
print(ftext + "\nthe length of is " + str(counter)) # prints the decrypted text and the str(counter) is for debuggin purposes
