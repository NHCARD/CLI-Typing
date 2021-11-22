import os
from time import time

# import replit
# import keyboard
from hgtk.text import decompose


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

    return cor_count



def short(now_short, lan):
    print("=========================================")
    stime = time()
    print(now_short)
    pre_input = input()
    etime = time()
    pre_short = now_short

    # replit.clear() #  linux, unix
    # os.system('cls') # window

    while 1:

        print("\n==================\033[032mprevious\033[0m===============")
        print(pre_short)

        for i in range(len(pre_short) + 1):
            if pre_short[i:i + 1] == pre_input[i:i + 1]:
                print(f"{pre_input[i:i + 1]}", end='')
            else:
                print('\033[31m%s\033[0m' % pre_input[i:i + 1], end='')

        cor_per = correct(pre_short, pre_input, lan) / (len(decompose(pre_short, compose_code='')) + 1) * 100
        spd = (correct(pre_short, pre_input, lan) / (etime-stime)) * 60

        print(f"\n\n걸린 시간 : {(etime - stime):.1f} \n정확도 : {cor_per:.1f} \n속도 : {spd:.1f}")

        print("===================\033[04m\033[34mnow\033[0m===================")
        print(now_short)
        stime = time()
        now_input = input()
        etime = time()

        pre_input = now_input
        pre_short = now_short

        # if lan == "ko":
        #     now_short = choice(ko_srt)
        # elif lan == "en":
        #     now_short = choice(srt)

        # replit.clear()
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