from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
secretAuction = {}
goOn = True
while goOn:
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  secretAuction[name] = bid
  decision = input("Are there other bids? ").lower()
  print(decision)
  if decision == "yes":
    clear()
  elif decision == "no":
    goOn = False
    highest = 0
    winner = ""
    for person in secretAuction:
      if secretAuction[person] > highest:
        highest = secretAuction[person]
        winner = person
    print(f"The winner is {winner} with a bid of {highest}")

  
