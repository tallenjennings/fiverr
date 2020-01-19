from itertools import product
import pickle

bits= {}
# with open("bits.pickle", "rb") as f:
    # bits= pickle.load(f)

index = 1  
for i in range(100000):
    for number in product("01", repeat=i+1):
        bits[index] = ''.join(map(str, number))
        index += 1
        
with open("bits.pickle", "wb") as out:
    pickle.dump(bits, out) 
        
print(bits[15])

