# conditional statements
print("An ogre approaches, and you need to defend yourself")
action = input("What do you do?")

if 'attack' in action:
    print("You slash your sword down and defeat the ogre!")
elif "defend" in action: # else if
    print("You block incoming attacks")
elif "run" in action:
    print("you run into a tree")
else:
    print("You flail around. Nice one.")
    
   