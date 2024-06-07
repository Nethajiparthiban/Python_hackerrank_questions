url="https://www.youtube.com/watch?v=lR7L0BheaXs"
candles=[4,4,1,3]
large=0
count=0
for i in range(len(candles)):
    if candles[i]>large:
        large=candles[i]
        count=1
    elif candles[i]==large:
        count+=1

print(count)

