import os

# import replit
import keyboard

from short import correct

from articloid import national_anthem

from hgtk.text import decompose

from time import time, sleep

from fun import  red

def an_previous(list1, original, page_num, line_num, lan):
    # noinspection SpellCheckingInspection
    if page_num != '':
        print(f"================ {line_num + 1} / {page_num} ================")

    red(original, list1, lan, 'long')

def def_anthem(num, lan):

    global etime
    if num == 1:

        list1 = []

        # noinspection SpellCheckingInspection
        stime = time()
        for i in range(len(national_anthem) + 1):

            match i:
                case 0:
                    print(f'\033[36m{national_anthem[i]}\033[0m')

                    ipt = input()
                    list1.append(ipt)

                    # replit.clear()
                    os.system('cls')
                    # print('------------------------')
                case 1 | 2 | 3:
                    # replit.clear()
                    os.system('cls')

                    if i == 1 or 2 or 3:

                        an_previous(list1, national_anthem, '', '', lan)

                        print(f'\033[36m{national_anthem[i]}\033[0m')
                        ipt = input()
                        etime = time()
                        list1.append(ipt)

                case 4:
                        # replit.clear()
                        os.system('cls')

                        an_previous(list1, national_anthem, '', '', lan)
                        print('------------------------')

        cor_count = 0

        for i in range(len(national_anthem)):
            cor_count += correct(national_anthem[i], list1[i], 'ko')

        length = 0

        for i in range(len(national_anthem)):
            length += len(decompose(national_anthem[i], compose_code=''))

        print(f"시간 :{etime-stime:.1f}")
        cor_per = ((cor_count) / length) * 100
        spd = (cor_count) / (etime - stime) * 60
        print(f"속도 : {spd:.1f}")

        print(f'정확도 : {cor_per:.1f}%')

        print('메뉴로 돌아가려면 엔터키를 누르시오')
        while 1:
            if keyboard.read_key() == 'enter':
                break

def long(num, lan, title):

    if num == 1:
        length = (len(title[1]) // 22) + 1
        page_num = length // 4

        cor_count = 0
        total_cor = 0
        total_len = 0
        line_length = 0

        line_num = 0


        print(title[0])

        title_ipt = input()

        os.system('cls')

        print(f'\033[36m{title[0]}\033[0m')

        total_time = 0

        for i in range(len(title[0]) + 1):
            if title[0][i:i+1] == title_ipt[i:i+1]:
                print(title_ipt[i:i+1], end='')
            elif title[0][i:i+1] != title_ipt[i:i+1]:
                print(f'\033[31m{title_ipt[i:i+1]}\033[0m', end='')

        print('')

        # print(f"\n================ 1 / {page_num} ================")

        list1 = []
        original1 = []

        line_stime = time()

        for i in range(length):

            if i % 4 == 0 and i != 0:
                line_stime = time()
                # print(line_stime)

            original = title[1][i*22:i*22+22]

            if i == 0:
                print(f"================ {line_num + 1} / {page_num} ================")

            print(f'\033[36m{title[1][i*22:i*22+22]}\033[0m')
            ipt = input()
            original1.append(original)
            list1.append(ipt[:22])
            # print(original1)
            # print(list1)

            os.system('cls')
            an_previous(list1, original1, page_num, line_num, lan)
            cor_count += correct(title[1][i*22:i*22+22], ipt, lan)
            line_length += len(decompose(title[1][i*22:i*22+22], compose_code=''))

            if i % 4 == 3:
                print("========================================================")

                line_etime = time() - line_stime
                print(f'페이지 시간 : {line_etime:.1f}')
                line_cor_per = (cor_count) / line_length * 100
                print(f'페이지 정확도 : {line_cor_per:.1f}')
                spd = (cor_count) / line_etime * 60
                print(f'페이지 속도 : {spd:.1f}')

                total_cor += cor_count
                total_len += line_length
                total_time += line_etime
                total_spd = (total_cor) / total_len * 60

                line_num += 1

                while 1:

                    if line_num < page_num:
                        ques = input("계속 하시겠습니까?\n1. yes\n2.no\n")
                    elif line_num == page_num:
                        sleep(2)
                        os.system('cls')
                        end(total_time, total_cor, total_len, total_spd, i)

                        print('메뉴로 돌아가려면 엔터키를 누르시오')
                        while 1:
                            if keyboard.read_key() == 'enter':
                                break

                    # print(ques)

                    if ques == '1':
                        cor_count = 0
                        os.system('cls')

                        break
                    elif ques == '2':
                        os.system('cls')
                        end(total_time, total_cor, total_len, total_spd, i)

                        print('메뉴로 돌아가려면 엔터키를 누르시오')
                        while 1:
                            if keyboard.read_key() == 'enter':
                                break
                        return

                list1 = []
                original1 = []

                os.system('cls')

                if line_num + 1 <= page_num:
                    print(f"================ {line_num + 1} / {page_num} ================")

# def_anthem(1)

# long(1, 'ko')

# print(len(counting_star[1]))

def end(time, cor, len, spd, i):
    print(f"총 시간 : {time:.1f}")
    print(f'총 정확도 : {((cor) / len * 100):.1f}')
    print(f'총 속도 : {spd:.1f}')

