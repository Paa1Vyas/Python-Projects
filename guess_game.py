import random

words = ["tiger", "tree", "underground", "giraffe", "chair", "parachute", "hello", "bank", "fire", "reign"]
movies = ["Pathaan", "K.G.F", "RRR", "Salaar", "Brahmastra", "Vikram", "Kantara", "Pushpa", "Vikrant Rona", "GOTG-3"]
games = ["chess", "cricket", "football", "basketball", "kabbadi", "kho-kho", "badminton", "BGMI", "minecraft", "asphalt9"]

flag = 0

print("Hello and Welcome to the Hangman Game......")
print('''Enter 1 for normal words
         Enter 2 for movies
         Enter 3 for games''')
choice = int(input("Enter your choice:"))

if choice == 1:
    word_s = random.choice(words)
    for i in range(5):
        value = input("Enter your guess.....")
        if value == word_s:
            print("You have guessed the right word,Congratulations")
            exit()

        else:
            print("Sorry you have guessed the wrong word please try again....")
            if i == 4:
                flag = flag + 1

            if flag == 1:
                print("Sorry you were unable to guess the right word and have used maximum amount of tries...")
                print("The right guess was " + word_s)

elif choice == 2:
    movie_s = random.choice(movies)
    for i in range(5):
        value = input("Enter your guess.....")
        if value == movie_s:
            print("You have guessed the right word,Congratulations")
            exit()

        else:
            print("Sorry you have guessed the wrong word please try again....")
            if i == 4:
                flag = flag + 1

            if flag == 1:
                print("Sorry you were unable to guess the right word and have used maximum amount of tries...")
                print("The right guess was " + movie_s)


elif choice == 3:
    game_s = random.choice(games)
    for i in range(5):
        value = input("Enter your guess.....")
        if value == game_s:
            print("You have guessed the right word,Congratulations")
            exit()

        else:
            print("Sorry you have guessed the wrong word please try again....")
            if i == 4:
                flag = flag + 1

            if flag == 1:
                print("Sorry you were unable to guess the right word and have used the maximum amount of tries...")
                print("The right guess was " + game_s)
