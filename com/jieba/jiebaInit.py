import jieba


def lcut(txt):
    jieba.add_word('刘玄德')
    jieba.del_word('玄德曰')
    jieba.del_word('三人')
    jieba.del_word('商议')
    words=jieba.lcut(txt)
    counts={}
    for word in words:
        if len(word)==1:
            continue
        else:
            counts[word]=counts.get(word,0)+1

    items = list(counts.items())  # 将键值对转换成列表
    items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
    return items

if __name__ == '__main__':
    txt = open("D:\\三国演义.txt", "r", encoding='utf-8').read()
    items = lcut(txt)
    for i in range(15):
        word, count = items[i]
        print("{0:<5}{1:>5}".format(word, count))


