# FindWordCount function building
# Mitchell Long
# CSCI 102 -- Section B
# Week 12 - Part A

def PrintOutput(a):
    print("OUTPUT", a)

def LoadFile(filename):
    f = open(filename)
    b = f.readlines()
    f.close()
    return b

def UpdateString(string, letter, index):
    newString = string[:index-1] + letter + string[index+1:]
    print("OUTPUT", newString)


def FindWordCount(a, string):
    word_count = a.count(string)
    return word_count

def ScoreFinder(players, scores, player):
    player = player.lower()
    first_letter = player[0].upper()
    player = player.replace(player[0], first_letter)
    index = players.find(player)
    score = scores[index]
    print("OUTPUT", player, "got a score of", score)
    
