import random
word=random.choice(["absence","abuse drugs","bank account","fatal accident","beneath","bend","benefit from","biology class","bitter","candidate","campaign","broken camera","capacity","capture","deaf","daughter","deal","decorate","dialogue","economy","finance","educate","very efficient","very supportive","elderly","flight","folk","flame","frustration","garbage","gather information","gentle","global hunger","hilarious","intelligence","jazz","sharp knife","longevity","beautiful momument","nonsense","nobody","turmeric","utilize batteries","sashimi","reconfigure","wheat","yellowish","zone"])
lives=8
print(word)
word=list(word)
def blank(n):
    if n!=" ":
        return "_"
    else:
        return " "

hiddenword=list(map(blank,word))
print(hiddenword)


def hangman():
    used_words=[]
    while hiddenword!=word:
        guess = input("letter: ")



