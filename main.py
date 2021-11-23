# from keyboard import read_key
from time import sleep

from random import choice
import os
# import replit
from short import short
from articloid import ko_srt, srt, counting_star, gold_axe, narcissus, Word, ko_Word
from long import def_anthem, long

lan = 'ko'

# 단어 출력 기능
def word(previous, n, nxt, pinput):

    global n_space, nxt_space, nwinput
    while 1:

        print('=====================================')

        print('previous        now        next')

        if lan == 'en':
            n_space = len(previous)
            nxt_space = len(n)
        elif lan == 'ko':
            n_space = len(previous)*2
            nxt_space = len(n)*2

        #이전, 현재, 다음 단어를 출력
        for i in range(3):
            if i == 0: # 이전 단어 출력
                print(previous, end='')
            elif i == 1: # 현재 단어 출력
                for j in range(16 - n_space): # now글씨와 시작점 맞추려고 일정 횟수 띄어쓰기
                    print(' ', end='')
                print(n, end='') # 현재 단어 출력
            elif i == 2:
                for j in range(11 - nxt_space): #next글씨와 맞추려고 일정 횟수 띄어쓰기
                    print(' ', end='')
                print(nxt) #다음 단어 출력

        for i in range(2): # 이전, 현재 입력값 출력
            if i == 0:
                if previous == pinput: # 단어와 이전 입력값이 같다면
                    print(previous, end='') #단어 출력

                elif previous != pinput: # 단어와 이전 입력값이 다르면
                    for j in range(len(previous)): # 단어 길이만큼 반복
                        if previous[j:j+1] != pinput[j:j+1]: # 이전 단어와 이전 입력이 다르면
                            print('\033[31m%s\033[0m' % (pinput[j:j+1]), end='') # 빨간 글씨로 글자 출력
                        elif previous[j:j+1] == pinput[j:j+1]: # 입력과 단어가 같으면
                            print(pinput[j:j+1], end='') # 흰글씨로 글자 출력


            elif i == 1: # 현재 입력 위치 맞추기
                if lan == 'en':
                    for j in range(16 - (len(previous) - (len(previous)-len(pinput)))): # 16 - 단어 길이만큼 띄어쓰기
                        print(' ', end='')

                elif lan == 'ko':
                    for j in range(16 - ((len(previous) - (len(previous)-len(pinput)))*2)): # 한글은 1.5칸 취급이기 때문에 *2를 해서 맞춰준다
                        print(' ', end='')

                nwinput = input() 

        print('\033[0m')

        # print('종료하려면 ESC를 누르십시오')

        pinput = nwinput[:len(n)] # 의도치 않은 상황 방지를 위해서 단어 길이 만큼만 입력값 적용
        previous = n
        n = nxt

        if lan == 'ko': # 언어가 한글이라면
            nxt = choice(ko_Word) # 한글 단어를 랜덤으로 넣기
        elif lan == 'en': #언어가 영어면
            nxt = choice(Word) # 영어 단어를 랜덤으로 넣기
        # sleep(1)
        # replit.clear()
        os.system('cls') # 터미널 지우개

def Start(): # 메인

   while 1:
        print(" \n\033[31m 고르시오 \033[0m ")
        print("1. 낱말")
        print("2. 짧은글")
        print("3. 긴글")
        print("4. \033[33/m언어 선택\033[0m")
        print('\n5. 종료')
        print(f"\033[36m----------------\033[0m\n현재 언어 : {lan}")

        a = input()

        match a:
            case '1': # 입력값이 1일때
                print('낱말 선택')
                sleep(1.5)

                # replit.clear()
                os.system('cls')

                if lan == 'ko': # 언어가 한글이면 한글 단어
                    word('', choice(ko_Word), choice(ko_Word), '')
                elif lan == 'en': #언어가 영어면 영어 단어
                    word('', choice(Word), choice(Word), '')
            case '2': # 입력값이 2일때
                print('짧은글 선택')

                sleep(1.5)

                if lan == "ko": # 언어가 한글이면
                    # replit.clear()
                    os.system('cls')
                    short(choice(ko_srt), 'ko') # short 함수 호출

                elif lan == "en": # 언어가 영어면
                    # replit.clear()
                    os.system('cls')
                    short(choice(srt), 'en') # short 함수 호출

            case '3': # 입력값이 3일때
                print('긴글 선택')

                sleep(1.5)
                os.system('cls')
                long_choice(lan) # 긴글 선택 함수
            case '4': # 입력값이 4일때
                os.system('cls')
                # replit.clear()

                lan_choice() # 언어 선택 함수 호출
            case '5': # 입력값이 5일때 메인 실행파일 호출하고 파이썬 파일 종료
                os.system("C:\\Users\\inuri64\\source\\repos\\final\\x64\Release\\final.exe")
                break
            case _: # 1, 2, 3, 4, 5를 제외한 나머지를 입력한 경우
                # replit.clear()
                os.system('cls')
                print("\033[31m1, 2, 3, 4중 선택\033[0m")
                continue # 반복문 시작점으로 보냄

def lan_choice():
    # replit.clear()    os.system('cls')

    print("4) \033[32m언어 선택\033[0m\n")
    print("1. Ko")
    print("2. En")

    match input():
        case '1': # 입력값이 1인 경우

            global lan # 전역변수 lan
            lan = "ko" # 한글로 설정
            # replit.clear()
            os.system('cls')
            Start() # start 함수 호출
        case '2': # 입력값이 2인 경우
            lan = "en" # 영어로 설정
            # replit.clear()
            os.system('cls')
            Start() # start 함수 호출
        case _:
            lan_choice() # 1, 2 외에 입력시 언어 선택 함수 재 호출

def long_choice(lan):

    if lan == 'ko':
        print('1. 애국가')
        print('2. 별 헤는 밤')
        print('3. 금도끼')

        long_ipt = input('\n==========\n숫자 입력 : ')

        match long_ipt:
            case '1':
                os.system('cls')
                def_anthem(1)
            case '2':
                os.system('cls')
                long(1, lan, counting_star)
            case '3':
                os.system('cls')
                long(1, lan, gold_axe)
            case _:
                print("1, 2, 3 만 가능")
                long_choice(lan)

    if lan == 'en':
        print('1. 양치기 소년')

        long_ipt = input('\n==========\n숫자 입력 : ')

        match long_ipt:
            case '1':
                os.system('cls')
                long(1, lan, narcissus)
            case _:
                print("1 만 가능")
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
