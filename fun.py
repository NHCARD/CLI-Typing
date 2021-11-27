from hgtk.text import decompose

def hyphen(short, lan):
    global hy_len
    if lan == 'ko':
        hy_len = (len(short) * 2 - 7)
    elif lan == 'en':
        hy_len = len(short)

    for i in range(hy_len):
        print('=', end='')
    print('')

def red(short, ipt, lan, classify):

    if classify == 'long':
        for j in range(len(ipt)):
            # print(len(list1))

            print(f'\033[36m{short[j]}\033[0m')
            # print(f'list1: {list1}')

            for k in range(len(short[j]) + 1):

                if short[j][k:k + 1] == ipt[j][k:k + 1]:
                    print(short[j][k:k + 1], end='')
                elif short[j][k:k + 1] != ipt[j][k:k + 1]:
                    print(f"\033[31m{ipt[j][k:k + 1]}\033[0m", end='')

            print('')

    elif classify == 'short':
        hyphen(short, lan)
        print(short)

        for i in range(len(short) + 1):
            if short[i:i + 1] == ipt[i:i + 1]:
                print(f"{ipt[i:i + 1]}", end='')
            elif short[i:i + 1] != ipt[i:i + 1]:
                print('\033[31m%s\033[0m' % ipt[i:i + 1], end='')

    print('')


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

    if lan == 'ko':
        return cor_count-1
    elif lan == 'en':
        return  cor_count
