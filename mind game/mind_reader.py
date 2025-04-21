import random

words = {
    "fruit": ["apple", "banana", "grape", "mango", "peach"],
    "color": ["green", "purple", "orange", "red", "white"],
    "book": ["harrypotter", "mobydick", "gatsby", "warandpeace", "catch22"],
    "city": ["paris", "london", "newyork", "tokyo", "sydney"]
}

# Pick category and word
category = random.choice(list(words.keys()))
word = random.choice(words[category])
hidden = ["_"] * len(word)
guessed_letters = []
lives = 6

print("🧠 Welcome to Mind Reader!")
print("Guess the word by entering one letter at a time or guess the entire word.")
print(f"Hint: It's a {category}")

while lives > 0:
    print("\nWord:", " ".join(hidden))
    print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    guess = input("Guess a letter or the word: ").lower()

    if guess == word:
        print(f"\n🎉 You Win! The word was: {word}")
        break

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only a single alphabetic letter or guess the entire word.")
        continue

    if guess in guessed_letters:
        print("You already guessed that!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct! ✅")
        for i, letter in enumerate(word):
            if letter == guess:
                hidden[i] = guess
    else:
        lives -= 1
        print(f"Wrong! ❌  ({lives} lives left)")

    if "_" not in hidden:
        print(f"\n🎉 You Win! The word was: {word}")
        break
else:
    print(f"\n💀 You Lost! The word was: {word}")
