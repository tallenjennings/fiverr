from itertools import product
import pickle
import sys


with open("bits.pickle", "rb") as f:
    bits= pickle.load(f)

num = int(input("Number  >> "))
while num:
    print("\t>>", bits[num])
    num = int(input("Number  >> "))


#bits={}
#index = 1
#bit = 0
#while(index < sys.maxsize):
#    bit += 1
#    for number in product("01", repeat=bit):
#        bits[index] = ''.join(map(str, number))
#        index += 1
        
#with open("bits.pickle", "wb") as out:
#    pickle.dump(bits, out)

