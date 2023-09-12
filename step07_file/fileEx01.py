'''
* 파일 처리
- 파일객체 : open(파일 이름, 모드)
    -- 모드
        1. 'r'(read) : 읽기모드
        2. 'w'(write) : 쓰기모드(파일이 존재하는 경우 : 원래 내용이 지워지고 열림)
                        (파일이 존재하지 않는 경우 : 새로운 파일 생성)
        3. 'a'(append) : 추가모드
'''

# fp = open("test01.txt", 'w')
# for i in range(1, 5):
#     content = "%d 번째 줄...\n" %i
#     fp.write(content)
# fp.close()

# fp = open("test01.txt", 'r')
# data = fp.readline() # 한 줄 읽기
# print(data)
# fp.close()

# 모든 정보 읽기
# fp = open("test01.txt", 'r')
# while True:
#     data = fp.readline()
#     if not data:
#         break
#     print(data, end='')
# fp.close()

# fp = open("test01.txt", 'r')
# # read() : 파일 내용 전체를 문자열로 return하는 함수
# data = fp.read()
# print(data)

# a 모드를 이용해서 기존 파일에 내용 추가
fp = open("test01.txt", 'a')
for i in range(5, 8):
    data = "%d 번째 줄...\n" %i
    fp.write(data)
fp.close()

fp = open("test01.txt", 'r')
data = fp.read()
print(data)

print("=" * 30)

# with문을 이용해서 파일 객체 다루기 : close를 할 필요가 없음
with open("test02.txt", 'w') as f:
    f.write("with문을 이용해서 파일 쓰기 테스트")