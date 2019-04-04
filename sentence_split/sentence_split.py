import pandas as pd
import numpy as np
import csv
import re
import time
import datetime

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y%m%d')
end_list = ['다$', '나$', '라$', '자$', '네$', '오$', '게$', '세$', '까$', '요$',
            '마$', '니$', '아$', '어$', '지$', '돼$', '야$', '해$', '군$', '걸$',
            '래$', '대$', '며$', '냐$', '줘$', '구먼$', '구려$', '시오$', '시다$', '면서$']

output = pd.read_csv("./{}_YS.csv".format(nowDatetime-datetime.timedelta(1)), header=None)
compare_df = pd.read_csv('./word_end_unique_0212.csv')

output.columns=['문장']
compare_df.drop(['Unnamed: 0'], axis=1, inplace=True)
compare_list = []
for i in compare_df['term']:
    compare_list.append(i)

count = 0
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y%m%d')
f = open('sentence_{}.txt'.format(nowDatetime-datetime.timedelta(1)), 'w', encoding='utf-8', newline='')
for line in output['문장']:
    s=''
    new_line = line.split()
    print(new_line)
    for n in range(len(new_line)):
        print(new_line[n])
        for e in end_list:
            if e =='해$' or e=='돼$' or e=='줘$':
                result=''
                result = re.search(e, new_line[n])
    #             print(result)
                if result!=None:
                    if new_line[n] in compare_list:
                        pass
                    else:
                        new_line[n] = new_line[n]+'/'
                        print('***********')
                else:
                    pass
            else:
                result=''
                result = re.search(e, new_line[n])
                if result!=None and len(new_line[n])>1:
                    if new_line[n] in compare_list:
                        pass
                    else:
                        new_line[n] = new_line[n]+'/'
                        print('--------------')
                else:
                    pass

    #     print(new_line[n])
    for n in range(len(new_line)-1):
        if '/' in new_line[n] and '/' in new_line[n+1]:
            new_line[n] = re.sub('/', '', new_line[n])
        else:
            pass
    for n in new_line:
        s = s+' '+n
    # print(s)
    print('*******************')
    s = s.strip()
    # print(s)
    line_complete = s.split('/ ')
    # print(line_complete)

    for one in line_complete:
        if '/' in one:
            one = re.sub('/', '', one)
        wr = csv.writer(f)
        wr.writerow([one])
            # STTfile.append(line[0])
f.close()
