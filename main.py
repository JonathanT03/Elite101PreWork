import random 
# All responses or using the random module#
greeting = random.choice(["Hello there, what is your name? ", "Greetings, Haven't talked to anyone in a while. What is your name? ", "Nice to Meet you, can you tell me your name? "])
current_day = random.choice(["So first off, how would you say your day has been on a scale of 1-10? ", "From a range of 1-10, how has your day been? "])
number = random.randint(1,100)
second_question = random.randint(1,2)
fourth_question = random.randint(1,2)
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
    elif player == "Ronaldo" or "ronaldo":
      print("Fan favorite, his footwork is superb!")
    elif player == "Lewandowski" or "lewandowski":
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
if res_2_2.isnumeric():
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
  if res_3_1 == "yes":
    country = str(input("\n What country was that, if you visited more than one, which was your favorite? "))


    
   
    
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


