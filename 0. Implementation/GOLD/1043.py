# 거짓말

# 파티에마다, 지민이는 이야기를 하며 있는 그대로 진실로 말하거나 과장해서 말함
# 되도록이면 과장해서 이야기하지만, 지민이는 거짓말쟁이가 되기는 싫다 
# 그 이야기의 진실을 아는 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기 
# 또한 어떤 사람이 어떤 파티에서는 진실을 듣고, 또 다른 파티에서는 과장된 이야기를 들어도 안됨.

# 사람의 수 N, 파티의 수 M 
# 이야기의 진실을 아는 사람이 주어지며 각 파티에 오는 사람들의 번호가 주어짐. 
# 지민이는 모든 파티에 참가하며 거짓말쟁이가 되지 않으면서 과장된 이야기를 할 수 있는 파티 개수의 최댓값 구할것

import sys
input = sys.stdin.readline

N, M = map(int, input().split())   # 둘다 50이하
answer = 0
party = [[] for _ in range(M)]
truth = []                         # 진실 아는 사람들을 적어둔 리스트

tmp = input().split()
if tmp[0]!=0: truth = truth+tmp[1:]

for m in range(M):
    party[m]=set(input().split()[1:])
truth = set(truth)
# 파티가 순차적으로 일어난다고 보면 안됨 순서 없다고 보고 뒤에서 진실 새롭게 안사람이 있고 앞에도 포함되면 그것도 다시 세어줘야함
for _ in range(M):
    for p in party:
        # 파티 참석한 사람과 진실아는사람 사이 교집합 있다면 = 진실 아는사람 한명이라 있다면
        # 그 파티에 참석한 사람들은 모두 진실 아는사람이 되며, 이때는 진실만 이야기함
        if p&truth : 
            truth = p|truth

for p in party:
    if (p&truth):
        continue
    answer +=1

print(answer)


# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# k = map(int, input().split())
# num = next(k)
# fact = list(k)
# counted = set(fact)
# linked = []
# for _ in range(m):
#     k = map(int, input().split())
#     num = next(k)
#     linked.append(set(k))
# while fact and linked:
#     i = fact.pop()
#     new_linked = []
#     for k in linked:
#         if i in k:
#             fact += list(k.difference(counted))
#         else:
#             new_linked.append(k)
#     linked = new_linked

# print(len(linked))

# import sys
# cnt_party = int(sys.stdin.readline().rstrip().split()[1])
# witness_set = set(sys.stdin.readline().rstrip().split()[1:])
# party_list = []
# possible_list = []
# for _ in range(cnt_party):
#     party_list.append(set(sys.stdin.readline().rstrip().split()[1:]))
#     possible_list.append(1)
# for _ in range(cnt_party):
#     for i, party in enumerate(party_list):
#         if witness_set.intersection(party):
#             possible_list[i] = 0
#             witness_set = witness_set.union(party)

# print(sum(possible_list))