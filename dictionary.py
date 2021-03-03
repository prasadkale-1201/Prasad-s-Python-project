FavoriteSong = {"Title":"Something Just Like this!", "Artist":"The Chainsmokers", "Album":"Memories....Do not open", "Release year":"2017", "Genre":"EDM,Pop"}
print(FavoriteSong)
def guess():
    for i in FavoriteSong:
        print(i)
        ans = input(" Please guess the mentioned thing : ")
        if ans == FavoriteSong[i]:
            output = True
            print(output)
        else:
            output = False
            print(output)
Guessgame = guess()