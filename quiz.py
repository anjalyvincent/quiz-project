print("WELCOME TO QUIZ!")
playing = input("Do you want to play quiz?")
print("playing")
if playing != "yes":
    quit()
print("yeah let's go on:")
score = 0
answer=input("color of apple?")
if answer == "red":
    print("correct")
    score += 1

else:
    print("incorrect")
answer=input("your nation?")
if answer == "indian":
    print("correct")
    score += 1

else:
    print("incorrect")

answer=input("number of continents?")
if answer == "7":
    print("correct")
    score += 1

else:
    print("incorrect")
print("you got " +str(score) + " questions correct!")
print("you got " +str((score/3) * 100) + "%")





