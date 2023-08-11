a = input("Abhinav:")
b = input("Ajali:")
play = { "Rock":"Scissors", "Paper":"Rock", "Scissors":"Paper"}
if a==b :
    print("Tie")
elif (play[a] == b):
    print("Abhinav Wins")
else:
    print("Anjali Wins")