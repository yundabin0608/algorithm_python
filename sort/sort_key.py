array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

# setting 에 아무것도 안주는거 넘 신기
result = sorted(array, key=setting)
print(result)

# @@ key = lamde a: 이용한 정렬 

# sort 함수는 원본을 변형시켜 정렬하고 변수.sort()형태로 사용함
#            정렬 기준은 알파벳, 가나다순, 숫자는 오름차순이 기본
# sorted 함수는 정렬된 결과를 반환하며 원본을 변형시키진 않는다.
#            정렬 기준은 문자열은 알파벳, 가나다순, 숫자는 오름차순이 기본

# 두함수 모드 key와 reverse 매개변수를 가진다. 둘다 reverse=False(오름차순) 기본값
# key는 정렬 목적으로 하는 함수를 값으로 넣으며 lamda를 씀