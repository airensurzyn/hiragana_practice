#!/usr/bin/python

import random



hiragana_list = {'a':u'\u3042','i':u'\u3044','e':u'\u3048','o':u'\u304A','u':u'\u3046',
                'ka':u'\u304B','ke':u'\u3051','ko':u'\u3053','ku':u'\u304F','ki':u'\u304D',
                'sa':u'\u3055','shi':u'\u3057','se':u'\u305B','su':u'\u3059','so':u'\u305D',
                'ta':u'\u305F','chi':u'\u3061','tsu':u'\u3064','te':u'\u3066','to':u'\u3068',
                'na':u'\u306A','ni':u'\u306B','nu':u'\u306C','ne':u'\u306D','no':u'\u306E',
                'ha':u'\u306F','hi':u'\u3072','fu':u'\u3075','he':u'\u3078','ho':u'\u307B',
                'ma':u'\u307E','mi':u'\u307F','mu':u'\u3080','me':u'\u3081','mo':u'\u3082',
                'ya':u'\u3084','yu':u'\u3086','yo':u'\u3088',
                'ra':u'\u3089','ri':u'\u308A','ru':u'\u308B','re':u'\u308C','ro':u'\u308D',
                'wa':u'\u308F','wo':u'\u3092','n':u'\u3093'}

while(true):
    question_list = []
    answer_list = []
    question_string = ''
    answer_string = ''
    length = random.randint(4,8)
    print "========================================\n========================================"
    for i in range(length):
        index = random.choice(hiragana_list.keys())
        question_list.append(index)
        answer_list.append(hiragana_list[index])
    for k in range(len(question_list)):
        question_string = question_string + question_list[k] + "-"
    print question_string
    raw_input('')
    for m in range(len(answer_list)):
        answer_string = answer_string + answer_list[m]
    print answer_string
