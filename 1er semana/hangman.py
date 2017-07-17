#importing the time module
import time

#welcoming the user
nombre = input("Cuál es tu nombre: ")

print ("Hola, " + nombre, "Juguemos ahorcado")
print ("")

#wait for 1 second
time.sleep(1)

print ("Comienza a adivinar las letras...")
time.sleep(0.5)

#here we set the secret
palabra = "hola pinche putita"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for letra in palabra:      

    # see if the character is in the players guess
        if letra in guesses:    
    
        # print then out the character
            print (letra),    

        else:
    
        # if not found, print a dash
            print ("_"),     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("Ganaste")  

    # exit the script
        break              

    print("")

    # ask the user go guess a character
    guess = input("Adivina el caracter: ") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in palabra:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Incorrecto")     
    # how many turns are left
        print ("Tienes otras", + turns, 'oportunidades')
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Loose"
            print ("Perdiste")  