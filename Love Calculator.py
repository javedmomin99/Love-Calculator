print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2

combined_name_lower = combined_name.lower()
t = combined_name_lower.count("t")
r = combined_name_lower.count("r")
u = combined_name_lower.count("u")
e = combined_name_lower.count("e")

true = t + r + u + e

l = combined_name_lower.count("l")
o = combined_name_lower.count("o")
v = combined_name_lower.count("v")
e = combined_name_lower.count("e")

love = l + o + v + e

love_score = str(true) + str(love)
love_score_int = int(love_score)

if love_score_int<10 or love_score_int>90:
  print(f"your score is {love_score_int}, you go together like coke and mentos.")
elif love_score_int>=40 and love_score_int <=50:
  print(f"your score is {love_score_int}, you are alright together.")
else:
  print(f"your score is {love_score_int}.")