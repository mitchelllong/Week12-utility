# LoadFunction function building
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

