import jieba


words=jieba.cut("他来到了网易杭研大厦")
print( "/".join(words))
