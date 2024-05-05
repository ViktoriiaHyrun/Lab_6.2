ST1 = input("Enter a string of up to 70 characters: ")

if len(ST1) > 70:
    print("ERROR: The string must contain no more than 70 characters.")
elif len(ST1) < 5:
    print("ERROR: The string must contain at least 5 characters.")
else:
    words = ST1.split()
    long_words = [word for word in words if len(word) > 5]
    
    ST2 = ' '.join(long_words)
    print("Words longer than 5 characters:", ST2)
