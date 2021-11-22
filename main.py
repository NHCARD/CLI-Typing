# from keyboard import read_key
from time import sleep
import word as wd
from random import choice
import os
# import replit
from short import short
from articloid import ko_srt, srt
from long import def_anthem, long

global Nwinput

red = '\033[31m'

lan = 'ko'

def Word(previous, n, nxt, Pinput):

    while 1:

        print('=====================================')

        print('previous        now        next')

        for i in range(3):
            if i == 0:
                print(previous, end='')
            elif i == 1:
                for j in range(16 - len(previous)):
                    print(' ', end='')
                print(n, end='')
            elif i == 2:
                for j in range(11 - (len(n))):
                    print(' ', end='')
                print(nxt)

        for i in range(2):
            if i == 0:
                if previous == Pinput:
                    print(previous, end='')
                elif previous != Pinput:
                     for j in range(len(previous) + 1):
                         if previous[j:j+1] != Pinput[j:j+1]:
                             print('\033[31m%s\033[0m' % (Pinput[j:j+1]), end='')
                         elif previous[j:j+1] == Pinput[j:j+1]:
                             print(Pinput[j:j+1], end='')

            elif i == 1:
                for j in range(16 - len(previous)):
                    print(' ', end='')

                Nwinput = input()

        print('\033[0m')

        # print('종료하려면 ESC를 누르십시오')

        Pinput = Nwinput
        previous = n
        n = nxt

        if lan == 'ko':
            nxt = choice(wd.ko_Word)
        elif lan == 'en':
            nxt = choice(wd.Word)
        # sleep(1)
        # replit.clear()
        os.system('cls')

def Start():

    print(" \033[31m 고르시오 \033[0m ")
    print("1. 낱말 연습")
    print("2. 짧은글 연습")
    print("3. 긴글 연습")
    print("4. 언어 선택")
    print(f"현재 언어 : {lan}")

    a = input()

    match a:
        case '1':
            print('낱말 연습을 선택하였습니다.')
            sleep(1.5)

            # replit.clear()
            os.system('cls')

            if lan == 'ko':
                Word('', choice(wd.ko_Word), choice(wd.ko_Word), '')
            elif lan == 'en':
                Word('', choice(wd.Word), choice(wd.Word), '')
        case '2':

            if lan == "ko":
                # replit.clear()
                os.system('cls')
                short(choice(ko_srt), 'ko')

            elif lan == "en":
                # replit.clear()
                os.system('cls')
                short(choice(srt), 'en')

            # replit.clear()
            os.system('cls')
        case '3':
            os.system('cls')
            long_choice(lan)
        case '4':
            os.system('cls')
            # replit.clear()

            lan_choice()

        case _:
            # replit.clear()
            os.system('cls')
            print("\033[31m1, 2, 3, 4중 선택\033[0m")
            Start()

def lan_choice():
    # replit.clear()
    os.system('cls')

    print("4) \033[32m언어 선택\033[0m\n")
    print("1. Ko")
    print("2. En")

    match input():
        case '1':
            global lan
            lan = "ko"
            # replit.clear()
            os.system('cls')
            Start()
        case '2':
            lan = "en"
            # replit.clear()
            os.system('cls')
            Start()
        case _:
            lan_choice()

def long_choice(lan):

    if lan == 'ko':
        print('1. 애국가')
        print('2. 별 헤는 밤')

        long_ipt = input('\n==========\n숫자 입력 : ')

        match long_ipt:
            case '1':
                def_anthem(1, lan)
            case '2':
                long(1, lan)
            case _:
                print("1, 2 만 가능")
                long_choice(lan)



    '''if keyboard.read_key() == "1":
        print("낱말 연습 선택")
        # word()
        break
    elif keyboard.read_key() == "2":
        print("짧은글 연습 선택")
        # short()
        break
    elif keyboard.read_key() == "3":
        print("긴글 연습 선택")
        # long()
        break'''

Start()
