#Intro to Lists

modulesList = ['INF','MNB','FAC','ECS']

print("There first list item is:", modulesList[0])
print("There last list item is:", modulesList[-1])
print("There list is", len(modulesList), "items long\n")

print("Here is all the items in the list")
for n in range (len(modulesList)):
    print(modulesList[n])