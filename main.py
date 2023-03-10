import random 
# All responses or using the random module#
greeting = random.choice(["Hello there, what is your name? ", "Greetings, Haven't talked to anyone in a while. What is your name? ", "Nice to Meet you, can you tell me your name? "])
current_day = random.choice(["So first off, how would you say your day has been on a scale of 1-10? ", "From a range of 1-10, how has your day been? "])
number = random.randint(1,100)
second_question = random.randint(1,2)
fourth_question = random.randint(1,1)
c = 0
### All leading open ended questions ^^^
### All leading yes/no or boolean type questions: below ##
first_question = random.randint(1,2)
third_question = random.randint(1,2)
# Random responses to certain answer ##
spark1 = random.choice([" Really? I have laways wanted to visit that country!", ", I have heard the weather is lovely there at this time of the year.",", Always wanted to visit their Capital, maybe one day!" ])
spark2 = random.choice(["I haven't either, :{ ", "Maybe one day!", "Same for me, I'm sure one day both of us will be able to explore the world. " ])
spark3 = random.choice([", definitely one of my favorites!", " A classic, wish I had one.", ", alright, my creator has a Great Pyrenees!" ])
spark4 = random.choice([" Fantastic player!", " Interesting choice!", " While I am just a bot, I am fond of Lewandowski!" ])
spark5 = random.choice([" Good choice, personally I really enjoy scanning soccer!", " Alright, not bad.!", " Not my favorite personally, but I can see why others like it. " ])
spark6 = random.choice([", lots of history with this religion, interesting.", ", Not a religion I'm too familiar with, but cool!", ", wow, maybe one day you can teach me more!" ])


# Start of program ##
name = str(input(greeting))
print(f' \n Hello there {name}, I am Spark, a bot that enjoys talking to humans!')
day = int(input(f' \n {current_day}'))
if day == 1 or day == 2 or day == 0 :
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
#####################################
### Discussions/questions, responses are in the format "res_question number_ random choice selection" ####
if first_question == 1:
  res_1_1 = str(input("\n Have you ever visited a different country, yes or no? ")).lower()
  if res_1_1 == "yes":
    country = str(input("\n What country was that, if you visited more than one, which was your favorite? "))
    if country == "stop":
      print(":(")
      exit()
    print(f'\n {country}{spark1}')
  elif res_1_1 == "no":
    print(f'\n {spark2}')
  elif res_1_1 == "stop":
    print(":(")
    exit()
  else:
    print("\n hmmm... Interesting!")                       
if first_question == 2:
  res_1_2 = str(input("\n Are you a cat or a dog person? ")).lower()
  if res_1_2 == "dog" or res_1_2 == "dog person":
    dog = str(input("\n I love dogs, what breed is your favorite? "))
    if dog == "stop":
      print(":(")
      exit()
    print(f'\n {dog}{spark3}')
  elif res_1_2 == "cat" or res_1_2 == "cat person":
    print("\n Gonna be honest, I don't like cats much. But good for you!")
  elif res_1_2 == "stop":
      print(":(")
      exit()
  else:
    ("\n Nice to know :)")
##########################
if second_question == 1:
  res_2_1 = str(input("\n What is your favorite sport? ")).lower()
  if res_2_1 == "soccer":
    player = str(input("\n My favorite Sport is also soccer, who is your favorite player? "))
    if player == "stop":
      print(":(")
      exit()
    elif player == "Messi" or player == "messi":
      print("\n One of the best to ever do it, deserved to win the World Cup!")
    elif player == "Ronaldo" or player == "ronaldo":
      print("\n Fan favorite, his footwork is superb!")
    elif player == "Lewandowski" or player == "lewandowski":
      print("\n Wow! He is also my favorite player! Wished Poland did better in the World Cup :/")
    else:
      print(f'\n {spark4}')
  elif res_2_1== "stop":
    print(":(")
    exit()
  else: 
    print(f'\n{spark5}')

if second_question == 2:
  res_2_2 = input("\n Not the most telling question, but what is your favorite number? ").lower()
  if res_2_2 .isnumeric():
    res_2_2 = int(res_2_2)
  if res_2_2 == "e" or res_2_2 == "pi":
    print(" \n One of the most interesting 'numbers' for sure!" )
  elif res_2_2 == 1 or res_2_2 == "one":
    print(" \n Great choice, safe number.")
  elif res_2_2 == 0 or res_2_2 == "zero":
    print(" \n Such a safe, but interesting number.")
  elif res_2_2 == 3 or res_2_2 == 13:
    print(" \n Full of different meanings!")
  elif res_2_2 == 666:
    print(" \n ...interesting...")
  elif res_2_2 == "stop":
    print(":(")
    exit()
  else:
    print("\n Unique!")
#########################
    
if third_question == 1:
  res_3_1 = str(input("\n Would you like to play a guessing game, yes or no? ")).lower()
  if res_3_1 == "no":
    print("\n Understandable, maybe next time.")
  elif res_3_1 == "stop":
    print(":(")
    exit()
  elif res_3_1 == "yes":
    print("\n The game is simple, I have picked a number from 1-100, lets see how many guesses it takes for you to pick my number. \n ")
    guess = int(input(" Guess any number from 1-100: "))
    if number != guess:
      print("\n Incorrect")
      while number != guess:
        guess = int(input("\n Guess another number from 1-100: "))
        c = c + 1
        if guess > number:
          print("\t \n your guess is larger than the number!")
        if guess < number:
          print("\t \n your guess is smaller than the number!")
        if number == guess:
          print(f'\n\t Correct, {guess} was the number!, it took you {c} tries!')
  else:
    print("\n Not sure what that means :{?")
if third_question == 2:
  res_3_2 = str(input("\n Are you religious in any way, yes or no? ")).lower()
  if res_3_2 == "yes" or res_3_2 == "i am":
    religion = str(input("\n What religion do you follow? "))
    if religion == "stop":
      print(":(")
      exit()
    print(f'\n {religion}{spark6}')
  elif res_3_2 == "no" or res_3_2 == "im not":
    print("\n OK, I'm programmed to be the same way.")
  elif res_3_2 == "stop":
      print(":(")
      exit()
  else:
    ("\n Nice to know :)")
####################
if fourth_question == 1:
  res_4_1 = str(input("\n For my last question, what is a skill that you are good at? ")).lower()
  if res_4_1 == "cooking" or res_4_1 == "baking":
    print(" \n A great skill that is tons of fun, nice!" )
    
  elif res_4_1 == "coding" or res_4_1 == "designing":
    print(" \n Very nice skill that take hard work, impressive!")
  elif res_4_1 == "drawing" or res_4_1 == "painting":
    print(" \n always wanted to be an artist myself :), nice.")
  elif res_4_1 == "writing" or res_4_1 == "typing":
    print(" \n excellent skill and takes forever to master I assume :)")
  elif res_4_1 == "nothing" or res_4_1 == "dont have any":
    print(" \n I'm sure you're good at something, maybe you just haven't found it yet.")
  elif res_4_1 == "stop":
    print(":(")
    exit()
  else:
    print("\n Wow, not an answer I expected, that's great!")
    
if fourth_question == 2:
  res_4_2 = str(input("\n To wrap things up, what is your favorite hobby? ")).lower()
  if res_4_2 == "cooking" or res_4_2 == "baking":
    print(" \n Love it, one of the most fun hobbies out there!" )
    
  elif res_4_2 == "coding" or res_4_2 == "designing":
    print(" \n Very nice hobby that take hard work, impressive!")
  elif res_4_2 == "drawing" or res_4_2 == "painting":
    print(" \n always wanted to be an artist myself :), nice.")
  elif res_4_2 == "writing" or res_4_2 == "journalism":
    print(" \n excellent skill and takes forever to master I assume :)")
  elif res_4_2 == "nothing" or res_4_2 == "dont have any":
    print(" \n That's fine, don't tell me then :)")
  elif res_4_2 == "stop":
    print(":(")
    exit()
  else:
    print("\n sounds like a great hobby!")
  ############## End of questions   
print(f'\n Well, {name} it was nice meeting you! I learned a few things about you, and maybe one day we we will meet again!! :]')


  





