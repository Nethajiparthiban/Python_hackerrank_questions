grades=[4,73,67,38,33]
res=[]
for grade in grades:
    if grade>=38:
        mod=grade%5

        if mod>=3:
            grade+=(5-mod)

    res.append(grade)
print(res)
