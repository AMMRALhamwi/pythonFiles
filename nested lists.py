# things = [["apples", "bananas"], ["milk", "water"]]
# things.append(["cake", "candy"])
# print(things)

nest = [['apples', 'bananas'], ['milk', 'water']]
print(nest)
input('press enter to change the content.....')
print('here is the updated basket')
# nest.remove(['apples', 'bananas'])
# nest.remove(['milk', 'water'])
nest[0].insert(0, 'orannge')
nest[0].insert(3, "kiwis")
nest[1].remove("water")
nest[1].insert(0, 'coffe')
nest[1].insert(2, 'tea')
nest.append([1, 2, 3])
# nest.append([1, 2, 3])
print(nest)
# ['orannges', 'apples', "bananas", "kiwis"],['coffe', 'milk', 'tea'], [1,2,3]
