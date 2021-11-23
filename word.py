Word = ['mouse', 'cat', 'dog', 'fox', 'wolf', 'snack', 'monitor', 'water', 'math', 'science', 'immune', 'EpikHigh','data','milk', 'human', 'science', 'math', 'water', 'chocolate', 'lilac', 'summer', 'spring', 'winter', 'fall']
ko_Word = ['닭', '한글', '세종대왕', '코코팜', '부채', '연필', '필통', '과자', '배배', '지우개', '종이', '단짝', '책', '모니터', '선풍기', '에어컨', '가방', '미적분', '창의공학설계', '수학', '물리학', '재미', '안약', '이어폰']

for i in Word:
    print(len(i))

import keyboard

while 1:
    print(keyboard.read_key())