'''
    1. 사각형 2. 삼각형 3. 원 4. 종료
    선택하세요 : 1
    사각형을 선택하셨습니다.

    만약 4를 선택하면
    프로그램을 종료합니다.

    이 외 나머지는 입력값이 잘 못 되었습니다.
'''
import sys

# while문은 무한루프
while True :
    n = int(input('1. 사각형 2. 삼각형 3. 원 4. 종료\n선택하세요 : '))
    if n == 1 :
        print('사각형을 선택하셨습니다.')
    elif n == 2 :
        print('삼각형을 선택하셨습니다.')
    elif n == 3 :
        print('원을 선택하셨습니다.')
    elif n == 4 :
        print('프로그램을 종료합니다.')
        sys.exit(0)
    else : print('입력값이 잘 못 되었습니다.')
