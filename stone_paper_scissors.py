import random
choise = ["k", "n", "b"]

def check_ans(t):
    if t == "k":
        print('камень')
    elif t == "b":
        print("бумага")
    elif t == "n":
        print("ножницы")


def main():
    while True:
        turn = input("Введите ваш ход ('k', 'n', 'b'): ").lower()
        if turn == "exit":
            break
        else:
            check_ans(turn)
        c_turn = random.choice(choise)
        check_ans(c_turn)

        if turn == 'k' and c_turn == 'n' or turn == "b" and c_turn == "k" or turn == "n" and c_turn == "b":
            print('вы выиграли !')
        elif c_turn == 'k' and turn == 'n' or c_turn == "b" and turn == "k" or c_turn == "n" and turn == "b":
            print('комп выиграл !')

main()