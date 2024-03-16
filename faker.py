letters = "abcdefghijklmnopqrstuvwxyz"
filname = input("filname: ") # the file the encrypted is going to be saved
def alpha_to_number(alpha): # this is the function that converts a given letter to the number
    y = 0
    for x in letters:
        y = y + 1
        if alpha == x:
            return y
        else:
            pass
op = input(": ") # the input that is going to be encrypted
print(op)
y = 0 # now suppose the string 'abc' the first character is a and it is first so 1 * 1 = 1 similary 2nd is b which is 2 so 2 * 2 = 4
# another example 'hello' first is h so 1 * 8 = 8, for e 5 * 2 = 10, for l  12 * 3 = 36 and so on. if the multilplication number reaches 10 then after multilplying with 10 , the number will reset to 1
ftext = "" # the final outpuut of the encrypted text it is defined for now
for x in op: # this takes x as each character . for example if op is 'abc' then x will be a in the first iteration of the for loop in second iteration it will be b
    y = y + 1
    if y > 10:
        y = 1
    else:
        pass
    if x == " ": # because each word is seperated by space we will indicate the seperation of words in the encrypted text by " ,"
        ftext = ftext + " ,"
        z = 1
        y = y - 1 # to make up for the extra value of y
    else:
            alphanumber = alpha_to_number(x) # converts the character into number
            ftext = ftext + " " + str(alphanumber * y)  # adds the encyrpted number to ftext
ftext = ftext.replace(', ', ',')
print(ftext)
yesno = "" # the below confirms all the output
while not(yesno.lower() == "y" or yesno.lower() == "n"):
    yesno = input("confirm output?(y/n)")
if yesno == "y":
    with open("//home//actmine//faker//" + filname + ".txt", 'a') as fillpaint:
        fillpaint.write(ftext + " ")
else:
    print("!OUTPUT")
