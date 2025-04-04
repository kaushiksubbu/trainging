Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    s=sorted(list(set(scorelist)))[1] 
    for i,j in sorted(Result):
        if j==s:
            print(i)
