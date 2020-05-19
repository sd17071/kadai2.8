import argparse
#お決まり
parser = argparse.ArgumentParser(description='このプログラムの説明を書けるよ')
#必須の引数の指定
parser.add_argument('texts',help='データセットの説明を書けるよ')
parser.add_argument('texts2',help='')
#引数の解析
args = parser.parse_args()

path = './' + args.texts
text2 = str(args.texts2)
with open(path, 'r', encoding = 'UTF-8') as file:
    contents = file.read()
    with open(text2,'w',encoding ='UTF-8') as file2:
        file2.write(contents)