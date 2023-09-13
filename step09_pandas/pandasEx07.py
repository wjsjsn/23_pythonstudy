import pandas as pd

e_list = [[100, '이도', 'CEO'],
          [110, '마루치', 'IT_PROG'],
          [121, '홍길동', 'IT_PROG'],
          [227, '둘리', 'IT_PROG'],
          [247, '공실이', 'Manager']]

s_name = ['empno', 'name', 'job_id']

df = pd.DataFrame(e_list, columns=s_name)
print(df)
print('-' * 50)

# empno가 200 이상인 사람의 정보
# print(df[df.empno >= 200])
print(df.query('empno >= 200'))
print('-' * 50)

# empno가 200이상이면서 직종(job_id)이 'IT_PROG'인 사람의 정보
# print(df[(df.empno >= 200) & (df.job_id == 'IT_PROG')])
print(df.query('empno >= 200 and job_id == "IT_PROG"'))
print('-' * 50)

# drop : 행과 열 삭제(원본 삭제 x)
# 보통 행을 삭제할 경우 index 번호를 가지고 삭제
# 첫 번째 행과 세 번째 행 삭제
# print(df.drop([0, 2]))
res = df.drop([0, 2])
print(res)
print(type(res))
print('-' * 50)

print(df)
print('-' * 50)

# 특정 컬럼 삭제
res2 = df.drop(columns='empno')
print(res2)