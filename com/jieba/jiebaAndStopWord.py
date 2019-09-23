
import jieba
import jieba.analyse

def lcut(txt):
    jieba.add_word('刘玄德')
    jieba.del_word('玄德曰')
    jieba.del_word('三人')
    jieba.del_word('商议')
    jieba.analyse.set_stop_words("stopwords.txt")
    tags = jieba.analyse.extract_tags(txt, topK=10, withWeight=True)
    for tag in tags:
        print("tag:%s\t\t weight:%f" % (tag[0], tag[1]))


if __name__ == '__main__':
    txt = open("D:\\三国演义.txt", "r", encoding='utf-8').read()
    lcut(txt)
