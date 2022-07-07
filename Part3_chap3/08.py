import random as rd
import Bubble as sm

st = []
for i in range(20):
    st.append(rd.randint(170, 185))



sorted = sm.bubbleSort(st)
print(f' 정렬 전 학생 키 : {st}')
print(f' 정렬 후 학생 키 : {sorted}')