import random 
# All responses or using the random module#
greeting = random.choice(["Hello there, what is your name? ", "Greetings, Haven't talked to anyone in a while. What is your name? ", "Nice to Meet you, can you tell me your name? "])
current_day = random.choice(["So first off, how would you say your day has been on a scale of 1-10? ", "From a range of 1-10, how has your day been? "])
second_question = random.randint(1,3)
fourth_question = random.randint(1,3)
### All leading open ended questions ^^^
### All leading yes/no or boolean type questions: below ##
first_question = random.randint(1,3)
third_question = random.randint(1,3)
# Random responses to certain answer ##
spark1 = random.choice([" Really? I have laways wanted to visit that country!", ", I have heard the weather is lovely at this time of the year.",", Always wanted to visit their Capital, maybe one day!" ])

# Start of program ##
name = str(input(greeting))
print(f' \n Hello there {name}, I am Spark, a bot that enjoys talking to humans!')
day = int(input(f' \n {current_day}'))
if day == 1 or day == 2 :
  print("\n Sorry to hear, hopefully I can make it better. :(")
elif day == 3 or day == 4 :
  print("\n Some days are better than other, :{ ")
elif day == 5 or day == 6 :
  print("\n Just an average day, huh. Have a lot of those personally. :/")
elif day == 7 or day == 8 :
  print("\n Sounds like you are having a good day. :)")
elif day == 9 or day == 10 :
  print(" \n :0 Love to hear it, wish all days were like that.")
elif day > 10 :
  print("\n Your day has been that good? Amazing ! :>")
else: 
  print("\n Not really sure what that means, but I hope its good.")

print(" \n I will be asking you more questions to get to know you, if at any point you are tired of talking to me, just respond with 'stop' to my questions!")
### Discussions/questions, responses are in the format "res_question number_ random choice selection" ####
if first_question == 1:
  res_1_1 = str(input("\n Have you ever visited a different country, yes or no? ")
  if res_1_1 == yes or res_1_1 == Yes:
    country = str(input("\n What country was that, if you visited more than one, which was your favorite? ")
    print(f'\n {country},{spark1}')
                       
if first_question == 2:
    res_1_2 = str(input("\n Have you ever visited a different country, yes or no? ")
if first_question == 3:
    res_1_3 = str(input("\n Have you ever visited a different country, yes or no? ")






#Guessing Game##

# # ########
#number = random.randint(1,100)
#guess = int(input("Guess any number from 1-100: "))
#if number != guess:
  #print("\n Incorrect")
  
#while number != guess:
 # guess = int(input("\nGuess another number from 1-100: "))
  #if guess > number:
   # print("\t \n Your guess is larger than the number!")
  #if guess < number:
   # print("\t \n your guess is smaller than the number!")

#if number == guess:
 # print(f'\n\tCorrect, {guess} was the number!')
#####