#brad hidles code bank.remove the three speech marks to use the code
#asks the user for a number and if the answer is not a number it will respond to that
'''while True:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("Error: Not a number. Try again...")'''
#asks the user for two numbers and adds them together
'''while True: 
    num=input("please enter a number:")
    num2=input("please enter another number:")
    answer = float(num) + float(num2)
    print("the answer is",answer)'''
#gives the average of two numbers
'''while True:
    print("what number do you want me to average")
    number_1=float(input())#input for first number
    print("what is the next number")
    number_2=float(input())#input for the second number
    print("your answer is....")
    answer=number_1+number_2#adds the given numbers up
    print(answer/2)#then divides the answer when added by two and gives it to the user'''
#gives the user the area of a rectangle
'''while True:
    print("please enter your height for the rectangle")
    height=float(input())#input for the height
    print("please enter the width of the rectangle")
    width=float(input())#input for the width
    print("the area for this rectangle is....")
    area=height*width#does the calculations to find the area
    print(area)#shows the answer'''
#divides two numbers and gives the answer as a reminder or a division
'''while True:
    print("hello welcome to the divider")
    print("would you like to calculate.yes or no.")
    menu=input()
    if menu=="no":
        print("GOODBYE")
        break
    else:
        print("would you like the remainders as your answer.yes or no")
        r=input()
        if r=="no":
            print("now what is the first number you want to divide")
            number1=int(input())
            print("and tell me the divider")
            number2=int(input())
            print(number1/number2)
            print("this is your answer")
            print("would you like to calculate again")
            repeat=input()
            if repeat=="no":
                break
            
        else:
            print("now what is the first number you want to divide")
            number1=int(input())
            print("and tell me the divider")
            number2=int(input())
            print(number1%number2)
            print("this is your answer")
            print("would you like to calculate again")
            repeat=input()
            if repeat=="no":
                break'''
#rock paper scissors game
'''#Brad Hidle rock paper scissors game
#imports
from random import randint
 
#create a list of play options
t = ["Rock", "Paper", "Scissors", "Nuke"]
 
#assign a random play to the computer
computer = t[randint(0,2)]
 
#set player to True
player = True
 
while player == True:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    if player == "Nuke":
        print("you win beacause there is nothing left")
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be True so the loop continues
    player = True
    computer = t[randint(0,2)]'''
#this program responds to how much ours they spend watching TV.
'''while True:
    print("Hi there, how long do you  watch TV a day")
    hours = int(input())
    if hours <= 2:
        print("That shouldn’t rot your brain too much")
    elif hours <= 4:
        print("arnt you getting square eyes")
    elif  hours <= 8:
        ("your hole head has probaly gone square by now")
    else:
        print("fresh air beats channel flicking")'''
#Brad Hidle asks the user for their name nd if it is mine it outputs thats a cool name
'''while True:
    print("what is your first name")
    name = input()
    name = (name[0].upper()+name[1:].lower())
    if name == "Brad":
        print("thats a cool name")
    elif name == "Darb":
        print("uno switch card")
    else:
        print("nice to meet you" , name)'''
#answers to what is your favourite subject
'''print("hello there what you name.")
name = input()
print("hi" , name , "what is your favourite subject")
subject = input()
if subject =="computer science":
    print("good choice")
elif subject =="maths":
    print("what is 4327439824722 x 6578675587")
elif subject =="english":
    print("my favourite language is python")
elif subject =="pe":
    print("let's get physical")
elif subject =="rs":
    print("i want to be a pope when im older")
elif subject =="religious studies":
    print("i want to be a pope when im older")
elif subject =="pshce":
    print("stop bullying yea, it's really not nice")
elif subject =="it":
    print("close enough")'''
#Brad Hidle,this program tells the user there grade depending on their score
'''while True:
    print("what was the score of the student")
    score=int(input()) #asks the user for the score
    if score >= 75:
        print("the grade is A.")#responds depending on the score
    elif score >= 60:
        print("the grade is B.")#responds depending on the score
    elif score >= 35:
        print("the grade is C.")#responds depending on the score
    elif 0<= score <= 35:
        print("the grade is D.")#responds depending on the score
    else:
        print("that is not a correct answer,try again.")#if the answer is something unacceptible it will ask the user to try again
    #end of code'''








    


