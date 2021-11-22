import os

# import replit

from articloid import national_anthem, counting_star

from short import correct

from hgtk.text import decompose

from time import time

def an_previous(list1, original, classify, page_num, line_num):
    # noinspection SpellCheckingInspection
    if classify == 'long':
        print(f"================ {line_num + 1} / {page_num} ================")

    for j in range(len(list1)):
        # print(len(list1))

        print(f'\033[36m{original[j]}\033[0m')
        # print(f'list1: {list1}')

        for k in range(len(original[j]) + 1):

            if original[j][k:k + 1] == list1[j][k:k + 1]:
                print(list1[j][k:k + 1], end='')
            elif original[j][k:k + 1] != list1[j][k:k + 1]:
                print(f"\033[31m{list1[j][k:k + 1]}\033[0m", end='')

        print('')

def def_anthem(num):

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

                        an_previous(list1, national_anthem, 'anthem', '', '')

                        print(f'\033[36m{national_anthem[i]}\033[0m')
                        ipt = input()
                        etime = time()
                        list1.append(ipt)

                case 4:
                        # replit.clear()
                        os.system('cls')

                        an_previous(list1, national_anthem, 'anthem', '', '')
                        print('------------------------')

        cor_count = 0

        for i in range(len(national_anthem)):
            cor_count += correct(national_anthem[i], list1[i], 'ko')

        length = 0

        for i in range(len(national_anthem)):
            length += len(decompose(national_anthem[i], compose_code=''))

        print(f"걸린 시간 :{etime-stime:.1f}")
        print(length)
        print(cor_count-4)
        cor_per = ((cor_count-4) / length) * 100
        spd = (cor_count-4) / (etime - stime) * 60
        print(f"spd : {spd:.1f}")

        print(f'{cor_per:.1f}%')

def long(num, lan):

    if num == 1:
        length = (len(counting_star[1]) // 22) + 1
        page_num = length // 4

        cor_count = 0
        total_cor = 0
        total_len = 0
        line_length = 0

        line_num = 0


        print(counting_star[0])

        title_ipt = input()

        os.system('cls')

        print(f'\033[36m{counting_star[0]}\033[0m')

        total_time = 0

        for i in range(len(counting_star[0]) + 1):
            if counting_star[0][i:i+1] == title_ipt[i:i+1]:
                print(title_ipt[i:i+1], end='')
            elif counting_star[0][i:i+1] != title_ipt[i:i+1]:
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

            original = counting_star[1][i*22:i*22+22]

            if i == 0:
                print(f"================ {line_num + 1} / {page_num} ================")

            print(f'\033[36m{counting_star[1][i*22:i*22+22]}\033[0m')
            ipt = input()
            original1.append(original)
            list1.append(ipt)
            # print(original1)
            # print(list1)

            os.system('cls')
            an_previous(list1, original1, 'long', page_num, line_num)
            cor_count += correct(counting_star[1][i*22:i*22+22], ipt, lan)
            line_length += len(decompose(counting_star[1][i*22:i*22+22], compose_code=''))



            # print(f"\n================ 1 / {page_num} ================")

            if i % 4 == 3:
                print("========================================================")

                line_etime = time() - line_stime

                print(f'시간 : {line_etime:.1f}')
                line_cor_per = (cor_count-4) / line_length * 100
                print(cor_count)
                print(line_length)
                print(f'{line_cor_per:.1f}')
                spd = (cor_count-4) / line_etime * 60
                print(f'spd : {spd:.1f}')

                total_cor += cor_count
                total_len += line_length

                total_time += line_etime
                total_spd = (total_cor-i) / total_len * 60

                line_num += 1

                while 1:

                    ques = input("계속 하시겠습니까? (ㅇ , ㄴ, y, n)")

                    print(ques)

                    if ques == 'y' or 'ㅇ':
                        break
                    elif ques == 'n' or 'ㄴ':
                        print(f"총 시간 : {total_time:.1f}")
                        print(f'총 정확도 : {(total_cor-i) / total_len * 100}')
                        print(f'총 속도 : {total_spd}')
                        return
                    else :
                        pass

                list1 = []
                original1 = []

                os.system('cls')

                if i <= page_num:
                    print(f"================ {line_num + 1} / {page_num} ================")




# def_anthem(1)

long(1, 'ko')

# print(len(counting_star[1]))

