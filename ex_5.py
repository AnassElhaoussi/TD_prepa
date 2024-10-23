x = 20
guessed_num_ = int(input("Devine! : "))

while True:
    if guessed_num_ == x:
        print("Bien joué!")
        break
    elif guessed_num_ > x:
        guessed_num_ = int(input("Votre nombre est plus grand que le nombre à deviner, devine de nouveau : "))
    elif guessed_num_ < x:
        guessed_num_ = int(input("Votre nombre est plus petit que le nombre à deviner, devine de nouveau ! : "))
