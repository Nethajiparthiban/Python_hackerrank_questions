url="https://www.hackerrank.com/challenges/new-year-chaos/problem"
q=[1,2,3,4,5,6,7,8]
def minimumBribes(q):
    bribe=0
    for i in range(len(q)-1,0,-1):
        if q[i]==i+1:
            if q[i-1]!=i+1:
                bribe+=1
                q[i-1],q[i]=q[i],q[i-1]
            elif q[i-2]==q[i+1]:
                bribe+=2
                q[i-2],q[i-1],q[i]=q[i-1],q[i],q[i-2]
            else:
                print("too chaotic")
                return
    print(bribe)
q=[1,2,3,4,5,6,7,8]
minimumBribes(q)
