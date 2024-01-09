
st = input("ntr the string whoih you want to code in secret language:- ")
# encoded string
words = st.split(" ")
nword = []
for word in words:
    if(len(word)>=3):
        i1 = "koz"
        i2 = "ij5"
        stnew = i1 + word[::-1] + i2 + word[0]
        nword.append(stnew)
        print(" ".join(nword))
        

    
st2 = int(input('''do you want to decode the string which you given
    1. yes
    2. No || exit
        '''))
if (st2 == 1):
    for word in nword:
        nw = word[-1] + word[3:-4]
        print(nw)