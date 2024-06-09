subject=["free prize worth millions","ten tips for a carefree lifestyle"]
spam_words=["free","millions"]
for j in subject:
    #temp = []
    x = j.split(" ")
    for k in spam_words:
        if k in x:
            print("spam")
        else:
            print("not spam")
        break

