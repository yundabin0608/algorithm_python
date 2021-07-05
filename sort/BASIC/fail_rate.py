def solution(N, stages):
    answer = []
    temp=[]
    
    # 각 스테이지별
    for i in range(1,N+1):
        # 각 스테이지에 도달한사람과 아직 클리어하지 못한사람
        player,fail=0,0
        
        for j in range(len(stages)):
            if (stages[j]>=i):
                player+=1
                if (stages[j]==i):
                    fail+=1
        
        if player == 0:
            f_rate=0
        else:
            f_rate=fail/player

        print(player, fail)
        
        temp.append([f_rate, i])
        
    temp.sort(key=lambda a: (-a[0],a[1]))
    
    answer=[ i[1] for i in temp] 
    
    
    return answer

N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N,stages))
