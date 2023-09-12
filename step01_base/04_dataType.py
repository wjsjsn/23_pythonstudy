'''
  튜플 : 리스트와 비슷한 자료형
        리스트는 [], 튜플은 () 사용
        리스트는 요소 값 변경(수정, 삭제, 생성) 가능
        튜플은 요소 값 변경 x

t1 = () : 빈 값이 들어있는 상태
t2 = (1,)
t3 = (10, 20, 30, 40)
t4 = 10, 20, 30
t5 = ("국제시장", "명량", (10, 20, 30))
'''

t1 = ("국제시장", "명량", (10, 20, 30))
print(t1[0]) # 국제시장
print(t1[-1]) # (10, 20, 30)

# 튜플 연산(+, * : 반복)
t2 = ('a', 'b', 'c')
print(t1 + t2) # ('국제시장', '명량', (10, 20, 30), 'a', 'b', 'c')
print(t2 * 3) # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# 수정 x => 오류 남
# t2[1] = 'k'

# 삭제 x => 오류 남
# del t2[1]

# 블린(참과 거짓)
# 문자열 : "aaa" -> 참, "" -> 거짓
# 리스트 : [1,2,3] -> 참, [] -> 거짓
# 튜플 : (1,2,3) -> 참, () -> 거짓
# 딕셔너리 : {1,2,3} -> 참, {} -> 거짓
# 숫자 : 1(참), 0(거짓)
# None : 거짓
