import random

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


guess = input("Guess the lowercase alphabet: ")
ans = random.choice(alpha)
times = 1


done = False
while not done:
    if guess not in alpha:
        print("Please enter a lowercase alphabet.")
        guess = input("Guess the lowercase alphabet: ")
    elif guess > ans:
        print("The alphabet you are looking for is alphabetically lower.")
        guess = input("Guess the lowercase alphabet: ")
    elif guess < ans:
        print("The alphabet you are looking for is alphabetically higher.")
        guess = input("Guess the lowercase alphabet: ")
    else:
        done = True
        print("Congratulations! You guess the alphabet \"%s\" in %d tries." % (ans, times))
    times += 1
    
print("Guess Histogram:" + "\n" + "a - d: " + "\n" + "e - h: " + "\n" + "i - l: " + "\n" + "m - p: " + "\n" + "q - t: " + "\n" + "u - x: " + "\n" + "y - z: " )

