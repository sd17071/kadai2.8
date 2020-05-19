import argparse
#お決まり
parser = argparse.ArgumentParser(description='このプログラムの説明を書けるよ')
#必須の引数の指定
parser.add_argument('texts',help='データセットの説明を書けるよ')
#オプションの指定
parser.add_argument('-n', action = 'store_true')
#引数の解析
args = parser.parse_args()

path = './' + args.texts

if args.n == False:
    with open(path, 'r', encoding = 'UTF-8') as file:
        contents = file.read()
        print(contents)

else:
    with open(path, 'r', encoding = 'UTF-8') as file:
        count = 0
        for line in file:
            count += 1
            print(count, line)