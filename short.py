import os
import random
from time import time, sleep

# import replit
# import keyboard
import keyboard
from hgtk.text import decompose
from articloid import srt, ko_srt


def correct(short, ipt, lan):

    cor_count = 0

    if lan == 'ko':
        sep_srt = decompose(short, compose_code='')
        sep_ipt = decompose(ipt, compose_code='')

        # print(sep_srt)

        for i in range(len(sep_srt)+1):
            if sep_srt[i:i+1] == sep_ipt[i:i+1]:
                cor_count += 1

    else:
        for i in range(len(short)):
            if short[i:i+1] == ipt[i:i+1]:
                cor_count += 1

    return cor_count-1

def red(short, ipt):

    print(short)

    for i in range(len(ipt)):
        if short[i:i + 1] == ipt[i:i + 1]:
            print(f"{ipt[i:i + 1]}", end='')
        else:
            print('\033[31m%s\033[0m' % ipt[i:i + 1], end='')

    print('')

def short(shorts, lan, repeat):

    while 1:

        print("=========================================")

        stime = time()

        print(shorts)
        ipt = input()

        etime = time()

        # os.system('cls')

        red(shorts, ipt)

        cor_per = correct(shorts, ipt, lan) / (len(decompose(shorts, compose_code='')) + 1) * 100
        spd = ((correct(shorts, ipt, lan))/ (etime-stime)) * 60

        print(f"\n\n걸린 시간 : {(etime - stime):.1f} \n정확도 : {cor_per:.1f} \n속도 : {3.12:.1f}")

        while 1:
            if keyboard.is_pressed('enter') == True:
                sleep(5)
                try:
                    break
                except ZeroDivisionError:
                    break

            elif keyboard.read_key() == 'esc':
                return
        # sleep(1.5)

        if lan == 'ko':
            short = random.choice(ko_srt)
        elif lan == 'en':
            short = random.choice(srt)

        os.system('cls')

'''while 1:

    print("언어를 선택하시오\n1. ko\n2.en")
    lan = input()

    if lan == "1":
        replit.clear()
        os.system('cls')
        short(choice(ko_srt), 'ko')

    elif lan == "2":
        replit.clear()
        os.system('cls')
        short(choice(srt), 'en')'''

'''lan = 'ko'

if lan == "ko":
    short(choice(ko_srt), lan)
elif lan == "en":
    short(choice(srt), lan)'''

# print(f'{"previous":<10}', end='')
# print(f'{"now":^10}', end='')
# print(f'{"next":>10}')