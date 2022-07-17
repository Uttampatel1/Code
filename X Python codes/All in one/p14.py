def game():
    return 100
    
score = game()

with open ("hiscore.tet") as op:
    hiscore=f.read()
    
if hiscore<score :
    with open ("hiscore.txt") as f:
        f.write(str(score))