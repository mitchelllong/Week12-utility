# UpdateString function building
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


