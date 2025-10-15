import random

DIGITS = "0123456789"
NUM_DIGITS = 3
MAX_TRIES = 10

#get secret number
def get_secret_num():
   return random.sample(DIGITS, NUM_DIGITS)
    
# ask for guess
def get_guess():
    while True:
        guess = input(f"Enter a {NUM_DIGITS}-digit number without repeating digits: ")
        if len(guess) != NUM_DIGITS \
              or not guess.isdigit() \
                or len(set(guess)) != NUM_DIGITS:
            print("Please enter a valid guess.")
        else:
            return guess
        
#compare numbers
def get_clues(guess, secret_num):
    clues = []
    for i in range(NUM_DIGITS):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")
    if not clues:
        clues.append("Bagels")
    return ' '.join(clues)
                

def main():
    print("Welcome to the Bagels game!")
    print(f"I have thought up a {NUM_DIGITS}-digit number. Try to guess it.")
    print("Here are some clues:")
    print("When I say:    That means:")
    print("  Pico         One digit is correct but in the wrong position.")
    print("  Fermi        One digit is correct and in the right position.")
    print("  Bagels       No digit is correct.")
    print(f"You have {MAX_TRIES} attempts to guess the number.")
    secret_num = get_secret_num()
    tries = 0
    while tries < MAX_TRIES:
        guess = get_guess()
        tries += 1
        if guess == ''.join(secret_num):
            print(f"Congratulations! You've guessed the number {''.join(secret_num)} in {tries} tries!")
            break
        else:
            clues = get_clues(guess, secret_num)
            print(clues)
        if tries == MAX_TRIES:
            print(f"You've used all your attempts. The number was {''.join(secret_num)}.")

if __name__ == "__main__":
    main()