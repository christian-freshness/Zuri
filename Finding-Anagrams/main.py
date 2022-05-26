# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagrams(w1, w2):
    if(sorted(w1) == sorted(w2)):
        return True
    else:
        return False

print(find_anagrams("check", "hello"))
print(find_anagrams("below", "elbow"))