import argparse
#お決まり
parser = argparse.ArgumentParser(description='このプログラムの説明を書けるよ')
#必須の引数の指定
parser.add_argument('dataset',help='データセットの説明を書けるよ')
#引数の解析
args = parser.parse_args()

text = str(args.dataset)

with open(text,'r', encoding = "Windows-1252") as f:
    txt = f.read()

word1 = txt.replace(',', '')
word2 = word1.replace('.', '')

words = word2.split()
word_list = set(words)
#上記で重複が無い辞書word_listが出来た


#単語の数と単語の辞書を作る
counter = {}


#wordsの単語を仕分ける
for i in words:
    if i in counter:#counterに既に単語があるならば
        counter[i] += 1
    else:#単語が無ければ登録する
        counter[i] =1

#出力調整
word_dict = sorted(counter.items(), key = lambda x:x[1], reverse =True) #数字でsortする

print(word_dict)

for i in range(0,10):
    print(word_dict[i][0],":", word_dict[i][1])
