import random
import time
choise = ["k", "n", "b"]
count = [0, ":", 0]


def check_ans(t):
    if t == "k":
        print('камень')
    elif t == "b":
        print("бумага")
    elif t == "n":
        print("ножницы")


def check_winner(tu, ctu):
    if tu == 'k' and ctu == 'n' or tu == "b" and ctu == "k" or tu == "n" and ctu == "b":
        print("Игрок выиграл !")
        count[0] += 1
        print("Счет : ", *count)
    elif ctu == 'k' and tu == 'n' or ctu == "b" and tu == "k" or ctu == "n" and tu == "b":
        print("Комп выиграл !")
        count[2] += 1
        print("Счет : ", *count)
    else:
        print("Ничья !")
        print("Счет : ", *count)


def main():
    while True:
        turn = input("Введите ваш ход (k, n, b): ").lower()
        while turn not in "knb":
            turn = input("Выберите один из вариантов. Введите ваш ход (k, n, b) : ")
        if turn == "exit":
            break
        else:
            check_ans(turn)
        for i in range(3):
            time.sleep(0.4)
            print('. ', end="")
        c_turn = random.choice(choise)
        time.sleep(0.4)
        check_ans(c_turn)
        check_winner(turn, c_turn)
        if count[0] == 3 or count[2] == 3:
            if count[0] > count[2]:
                print("Игра окончена. Победил игрок !")
            else:
                print("Игра окончена. Победил комп !")
            break


def replay():
    opt = ["YES", "NO"]
    new_game = input("Хотите сыграть снова? (yes, no)").upper()
    while new_game not in opt:
        new_game = input("Выберите один из вариантов. Хотите сыграть снова? (yes, no) ").upper()
    if new_game == "YES":
        return True
    elif new_game == "NO":
        return False


main()


def main_2():
    while replay():
        count[0] *= 0
        count[2] *= 0
        main()
    else:
        print("Byee !")


main_2()