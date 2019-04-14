import time
import datetime
import pandas as pd
from konlpy.tag import Kkma, Okt, Komoran
from konlpy.tag import Okt
from collections import Counter
from konlpy.tag import Kkma, Okt, Komoran
import csv

pos_taggers = [('kkma', Kkma()), ('twitter', Okt()), ('Komoran', Komoran())]
results = []

now = datetime.datetime.
nowDatetime = now.strftime('%Y%m%d')
texts = pd.read_csv('/home/ubuntu/sentence_{}.csv'.format(nowDatetime-datetime.timedelta(1)), header=None)
texts.columns=['문장']
for name, tagger in pos_taggers:
    if name=='Komoran':
        tokens = []
        process_time = time.time()
        for text in texts['문장']:
            tokens.append(tagger.pos(text))
        process_time = time.time() - process_time
        print('tagger name = %10s, %.3f secs' % (name, process_time))
        results.append(tokens)


delist=[]
for i in range(len(results[0])-1):

    a=len(results[0][i])-1

    for j in range(a):
        if (
            results[0][i][j][1] == 'NNG' or results[0][i][j][1] == 'NNP'
            ):
            a=results[0][i][j]
            delist.append(a)


list_up=pd.DataFrame(delist)

list_up.to_csv("{}.txt".format(nowDatetime-datetime.timedelta(1)))

def get_tags(text, ntags=50):
    spliter = Okt()

    nouns = spliter.pos(text)

    count = Counter(nouns)
    return_list = []  # Noun-frequency list

    # from max frequency word to min frequency word
    # Descending order list
    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)

    return return_list


def main():
    # files for analyze
    text_file_name = "{}.txt".format(nowDatetime-datetime.timedelta(1))
    noun_count = 100
    # Making files about top 'n' words
    output_file_name = "wordcount_{}.txt".format(nowDatetime-datetime.timedelta(1)) 

    open_text_file = open(text_file_name, 'r',-1,"utf-8")
    text = open_text_file.read() 
    tags = get_tags(text, noun_count) 
    open_text_file.close()
    open_output_file = open(output_file_name, 'w',-1,"utf-8")
    
    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        open_output_file.write('{} {}\n'.format(noun, count))

    open_output_file.close()

if __name__ == '__main__':
    main()
