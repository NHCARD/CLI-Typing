import replit

from articloid import *
from random import choice
from fun import red


class Main:
    def __init__(self):
        self.now = choice(Word)
        self.next = choice(Word)
        self.previous = ''
        self.pinput = ''

    def word(self):
        ipt = ''

        while True:

            n_space = len(self.previous)
            nxt_space = len(self.now)

            print('previous        now        next')

            for i in range(3):
                if i == 0:  # 이전 단어 출력
                    print(self.previous, end='')
                elif i == 1:  # 현재 단어 출력
                    for j in range(16 - n_space):  # now글씨와 시작점 맞추려고 일정 횟수 띄어쓰기
                        print(' ', end='')
                    print(self.now, end='')  # 현재 단어 출력
                elif i == 2:
                    for j in range(11 - nxt_space):  # next글씨와 맞추려고 일정 횟수 띄어쓰기
                        print(' ', end='')
                    print(self.next)  # 다음 단어 출력

            red(self.previous, self.pinput, 'en', 'word')

            for i in range(16 - (len(self.previous)  - (len(self.previous)-len(self.pinput)))):
                print(' ', end='')


            ipt = input()

            self.previous = self.now
            self.now = self.next
            self.next = choice(Word)
            self.pinput = ipt

            replit.clear()

wd = Main()
wd.word()