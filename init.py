from random import randint

# Creating the initial array for the party votes / Lager listen til å lagre partistemmer

PartyVotes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Function to calculate all the votes / Funksjon til å kalkulere alt

def in_range(_list, index, lower, upper):
  return _list[index] > lower and _list[index] <= upper

def voting():
    countedVotes = 0
    votes = 0 
    print("How many votes do you want to count?\n")
    countedVotes=int(input())
    print(f"Great! We shall be counting {countedVotes} votes for the upcoming election!")
    
    votes = [randint(0, 1000) for _ in range(countedVotes)]
    for x in range(0, countedVotes, 1): 
        if in_range(votes, x, -1, 41):
            PartyVotes[0] += 1
        elif in_range(votes, x, 42, 111):
            PartyVotes[1] += 1
        elif in_range(votes, x, 112, 152):
            PartyVotes[2] += 1
        elif in_range(votes, x, 153, 372):
            PartyVotes[3] += 1
        elif in_range(votes, x, 373, 554):
            PartyVotes[4] += 1
        elif in_range(votes, x, 555, 589):
            PartyVotes[5] += 1
        elif in_range(votes, x, 590, 623):
            PartyVotes[6] += 1
        elif in_range(votes, x, 624, 857):
            PartyVotes[7] += 1
        elif in_range(votes, x, 858, 982):
            PartyVotes[8] += 1
        else:
            PartyVotes[9] += 1
    
    print(f"The votes have now been counted!\nThe results are as follows:\n Red Party: {PartyVotes[0]}\n Socialist Left Party: {PartyVotes[1]}\n Greens: {PartyVotes[2]}\n Labour: {PartyVotes[3]}\n Center Party: {PartyVotes[4]}\n Christian People's Party: {PartyVotes[5]}\n Left: {PartyVotes[6]}\n Conservative: {PartyVotes[7]}\n Progress Party: {PartyVotes[8]}\n Other parties: {PartyVotes[9]}\n")
        
    print("Do you want to do this again?")
    answer1=input()
    if (answer1 in ["Yes", "yes"]):
        print("Lets get on with it then, shall we?")
        voting()
    else:
        pass




# What do you want to do? / Hva vil du gjøre?

print("What do you want to do?\nYou can pick between starting with voting, xxx or yyy")
answer=str(input())
if (answer in ["Voting", "voting"]):
    print("Lets get on with it then, shall we?")
    voting()
else:
    pass
