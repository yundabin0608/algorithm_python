array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

# setting 에 아무것도 안주는거 넘 신기
result = sorted(array, key=setting)
print(result)