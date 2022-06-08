#Вам предстоит написать программу, которая шифрует сообщения по следующему алгоритму: 
#она берёт текст и переставляет в нём каждые два подряд идущих символа.
#Если количество символов нечётное, то последний символ остаётся на своём месте:


def encrypt(word):
    if len(word) % 2 == 0:
        last_char = ""
    else:
        last_char = word[len(word) - 1]

    index = 0
    password = ""

    while index <= len(word) - 2: 
        if (index + 1) % 2 != 0:
            password += word[index + 1] + word[index]
        index += 1
    return password + last_char

print(encrypt("move"))
print(encrypt("attack"))
print(encrypt("go!"))