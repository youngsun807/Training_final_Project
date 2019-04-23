from django.shortcuts import render
import json
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.
from myapp.models import *
import re
from collections import Counter


def intro(request):
    print('--------------intro----------------')
    return render(request, 'intro.html')


def index(request):
    # latest_user_list = User.objects.all()
    print("======")
    print(request.method)
    if request.method =='GET':
        return render(request, 'index.html', {'my_name': request.session['user']})
    elif request.method =='POST':
        request.session['user'] = request.POST['user']
        return render(request, 'index.html', {'my_name': request.session['user']})

def personal(request):
    print("***")
    queryset = User.objects.values('id').filter(name=request.session['user'])
    print(queryset[0]['id'])
    user_id = queryset[0]['id']
    word_list = Word.objects.values_list('id', 'word', 'count').filter(no_id=user_id, datetime__icontains='2019').order_by('-count')[:10]
    print(word_list)
    noun = Word.objects.values('word', 'count').order_by('-count').filter(no_id=user_id, datetime__icontains='2019', word_part='nng')
    adverb = Word.objects.values('word', 'count').order_by('-count').filter(no_id=user_id, datetime__icontains='2019', word_part='mag')
    return render(request, 'myapp/personal.html', {'user_info' : word_list, 'noun_list' : noun, 'adverb_list' : adverb})
    # 명사(MAG, NNP, 부사)


def age(request):
    print('----------------------')
    queryset = User.objects.values('id', 'age').filter(name=request.session['user'])
    print(queryset[0]['id'], queryset[0]['age'])

    user_id = queryset[0]['id']
    user_word_list = Word.objects.values_list('word', 'count').filter(no_id=user_id, datetime__icontains='2019').order_by('-count')[:50]
    print(user_word_list)
    compare_list = []
    for user_word in user_word_list:
        print(user_word[0])
        compare_list.append(user_word[0])

    user_age = queryset[0]['id']

    ten_id = User.objects.values_list('id').filter(age__startswith=1)
    ten_word_list = []
    ten_count_list= []
    for ten in ten_id:
        print(ten[0])
        word_list = Word.objects.values_list('word', 'count').filter(no_id=ten[0]).order_by('-count')[:10]
        if word_list:
            for word in word_list:
                ten_word_list.append(word[0])
                ten_count_list.append(word[1])

    ten_compare = []
    for compare in compare_list:
        for ten in ten_word_list:
            if compare==ten:
                ten_compare.append(ten)
    result = Counter(ten_compare)
    print (result)

    ten_key = ''
    ten_key_count = []
    if len(result)!=0:
        for key in result:
            ten_key = ten_key + ',' + key
            ten_key_count.append(result[key])
    else:
        ten_key = 'no'
        ten_key_count.append(0)

    ten_key = ten_key.strip().lstrip(',')

    print("--------------------10대단어리스트-----------------------", "\n", ten_word_list, '\n', ten_count_list, '\n', ten_key, '\n', ten_key_count)
        


    twenty_id = User.objects.values_list('id').filter(age__startswith=2)
    twenty_word_list = []
    twenty_count_list= []
    for twenty in twenty_id:
        print(twenty[0])
        word_list = Word.objects.values_list('word', 'count').filter(no_id=twenty[0]).order_by('-count')[:10]
        if word_list:
            for word in word_list:
                twenty_word_list.append(word[0])
                twenty_count_list.append(word[1])
    twenty_compare = []
    for compare in compare_list:
        for twenty in twenty_word_list:
            if compare==twenty:
                twenty_compare.append(twenty)

    result = Counter(twenty_compare)
    print (result)
    

    twenty_key = ''
    twenty_key_count = []
    if len(result)!=0:
        for key in result:
            twenty_key = twenty_key + ',' + key
            twenty_key_count.append(result[key])
    else:
        twenty_key = 'no'
        twenty_key_count.append(0)

    twenty_key = twenty_key.strip().lstrip(',')
    
    print("--------------------20대단어리스트-----------------------", "\n", twenty_word_list, '\n', twenty_count_list, '\n', twenty_key, '\n', twenty_key_count)

    thirty_id = User.objects.values_list('id').filter(age__startswith=3)
    thirty_word_list = []
    thirty_count_list= []
    for thirty in thirty_id:
        print(thirty[0])
        word_list = Word.objects.values_list('word', 'count').filter(no_id=thirty[0]).order_by('-count')[:10]
        if word_list:
            for word in word_list:
                thirty_word_list.append(word[0])
                thirty_count_list.append(word[1])

    thirty_compare = []
    for compare in compare_list:
        for thirty in thirty_word_list:
            if compare==ten:
                thirty_compare.append(thirty)
    result = Counter(thirty_compare)
    print (result)

    thirty_key = ''
    thirty_key_count = []
    if len(result)!=0:
        for key in result:
            thirty_key = thirty_key + ',' + key
            thirty_key_count.append(result[key])
    else:
        thirty_key = 'no'
        thirty_key_count.append(0)
    
    thirty_key = thirty_key.strip().lstrip(',')
    
    print("--------------------30대단어리스트-----------------------", "\n", thirty_word_list, '\n', thirty_count_list, '\n', thirty_key, '\n', thirty_key_count)
    

    forty_id = User.objects.values_list('id').filter(age__startswith=4)
    forty_word_list = []
    forty_count_list= []
    for forty in forty_id:
        print(forty[0])
        word_list = Word.objects.values_list('word', 'count').filter(no_id=forty[0]).order_by('-count')[:10]
        if word_list:
            for word in word_list:
                forty_word_list.append(word[0])
                forty_count_list.append(word[1])
    
    forty_compare = []
    for compare in compare_list:
        for forty in forty_word_list:
            if compare==ten:
                forty_compare.append(forty)
    result = Counter(forty_compare)
    print (result)

    forty_key = ''
    forty_key_count = []
    if len(result)!=0:
        for key in result:
            forty_key = forty_key + ',' + key
            forty_key_count.append(result[key])
    else:
        forty_key = 'no'
        forty_key_count.append(0)

    forty_key = forty_key.strip().lstrip(',')

    print("--------------------40대단어리스트-----------------------", "\n", forty_word_list, '\n', forty_count_list, '\n', forty_key, '\n', forty_key_count)
    
    sumALL = sum(ten_key_count)+sum(twenty_key_count)+sum(thirty_key_count)+sum(forty_key_count)
    age_word_list = {'ten' : ten_word_list, 'twenty': twenty_word_list, 'thirty' : thirty_word_list, 'forty' : forty_word_list}
    age_count_list = {'ten' : ten_count_list, 'twenty': twenty_count_list, 'thirty' : thirty_count_list, 'forty' : forty_count_list}
    age_compare_key = {'ten' : ten_key, 'twenty' : twenty_key, 'thirty' : thirty_key, 'forty' : forty_key}
    age_compare_count = {'ten' : ten_key_count, 'twenty' : twenty_key_count, 'thirty' : thirty_key_count, 'forty' : forty_key_count}
    return render(request, 'myapp/age.html', {'sumALL' : sumALL, 'user_word_list' : user_word_list, 'age_word_list' : age_word_list, 'age_count_list': age_count_list, 'age_compare_key':age_compare_key, 'age_compare_count' : age_compare_count})
    

def habit(request):
    print('*/*/*/*/*/*/*/*/*/*/')
    queryset = User.objects.values('id').filter(name=request.session['user'])
    print(queryset[0]['id'])
    user_id = queryset[0]['id']
    sentence_list = Emotion.objects.values_list('sentence', 'negative', 'neutral', 'positive').filter( datetime__icontains='2019')
    print(len(sentence_list))
    
    positive_dict = {}
    negative_dict = {}
    positive_count = 0
    negative_count = 0

    positive_list = ''
    negative_list = ''
    positive_count_list = []
    negative_count_list = []
    if sentence_list:
        for sentence in sentence_list:
            # print(sentence)
            result = max(sentence[1], sentence[2], sentence[3])
            # print(result)

            if result==sentence[1]:
                sentence_split = sentence[0].split()
                negative_count += 1
                for one in sentence_split:
                    count_q = Word.objects.values('count').filter(no_id=user_id, word_part='nng', word=one)
                    if count_q:
                        negative_dict[one] = count_q[0]['count']
                   

            elif result==sentence[3]:
                sentence_split = sentence[0].split()
                positive_count += 1
                for one in sentence_split:
                    count_q = Word.objects.values('count').filter(no_id=user_id, word_part='nng', word=one)
                    if count_q:
                        positive_dict[one] = count_q[0]['count']
    
    print(len(positive_dict), len(negative_dict))
    print(negative_dict, '\n', positive_dict, '\n')
    
    
    for k,v in dict(negative_dict).items():
        negative_list = negative_list + ' ' + k
        negative_count_list.append(v)

    negative_list = negative_list.strip()

    for k,v in dict(positive_dict).items():
        positive_list = positive_list + ' ' + k
        positive_count_list.append(v)

    positive_list = positive_list.strip()

    print('부정:', negative_list, '\n', negative_count_list)
    print('------------------------------------------------')

    neutral_count = len(sentence_list) - (positive_count + negative_count)
    print(neutral_count)
    positive_sentence = Emotion.objects.values_list('sentence').filter(no_id=user_id).order_by('-positive')[:1]
    negative_sentence = Emotion.objects.values_list('sentence').filter(no_id=user_id).order_by('-negative')[:1]
    
    return render(request, 'myapp/habit.html', {'positive_dict':positive_dict, 'negative_dict':dict(negative_dict), 'positive_sentence_count' : positive_count, 'negative_sentence_count' : negative_count, 'neutral_sentence_count' : neutral_count, 'positive_word_list' : positive_list, 'negative_word_list' : negative_list, 'positive_count_list' : positive_count_list, 'negative_count_list':negative_count_list, 'positive_sentence' : positive_sentence, 'negative_sentence':negative_sentence})





'''
<Wordclouding code>
- the following codes are implemented in Jupyter Notebook.
- But In this file, I didn't apply it. Need more time to study and implement
- Just note the following only.


import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image

# negative_dict = sorted(negative_dict.items(), key=lambda n:n[1], reverse=True)
# positive_dict = sorted(positive_dict.items(), key=lambda p:p[1], reverse=True)


    <version 1>
    # wc = WordCloud(font_path='./NanumGothicBold.ttf', background_color='white', width=500, height=440, colormap=plt.cm.Reds)
    # cloud = wc.generate_from_frequencies(dict(negative_dict))
    # plt.figure(figsize=(8, 6))
    # plt.axis('off')
    # plt.imshow(cloud, cmap=plt.cm.Reds, interpolation="bilinear")
    # plt.savefig('myapp\static\images\\negative.png', dpi=100, facecolor='w', edgecolor='w', relative_scaling=0.5, orientation='portrait', pad_inches=0.1,frameon=None)

    <version2>
    # wc = WordCloud(font_path='./NanumGothicBold.ttf', background_color='white', width=500, height=440)
    # cloud = wc.generate_from_frequencies(dict(positive_dict))
    # plt.figure(figsize=(8, 6))
    # plt.axis('off')
    # s = plt.imshow(cloud, interpolation="bilinear")
    # plt.savefig('myapp\static\images\\positive.png', dpi=100, facecolor='w', edgecolor='w', relative_scaling=0.5, orientation='portrait', pad_inches=0.1,frameon=None)
'''