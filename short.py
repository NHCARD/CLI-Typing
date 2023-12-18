import os
import random
from time import time

# import replit

from hgtk.text import decompose
from articloid import srt, ko_srt
from fun import red
from fun import correct
from fun import hyphen

def short(short, lan):

    while 1:
        hyphen(short, lan)

        stime = time()
        print(short)
        ipt = input()
        etime = time()

        os.system('cls')

        red(short, ipt, lan, 'short')

        cor_per = correct(short, ipt, lan) / (len(decompose(short, compose_code='')) + 1) * 100
        spd = ((correct(short, ipt, lan))/ (etime-stime)) * 60

        print(f"\n\n걸린 시간 : {(etime - stime):.1f} \n정확도 : {cor_per:.1f} \n속도 : {spd:.1f}")

        print('=====================================================')
        print('계속 하려면 \033[36my 또는 ㅇ\033[0m을, 메뉴로 돌아가려면  \033[36mn 또는 ㄴ\033[0m을 누르시오')

        if lan == 'ko':
            short = random.choice(ko_srt)
        elif lan == 'en':
            short = random.choice(srt)

        while 1:
            a = input()

            if a == 'n':
                os.system('cls')
                return
            elif a == 'y':
                os.system('cls')
                break
            elif a == 'ㅇ':
                os.system('cls')
                break
            elif a == 'ㄴ':
                os.system('cls')
                return
            else:
                print('\033[31my or ㅇ or n or ㄴ 만 누르시오\033[0m')

        os.system('cls')