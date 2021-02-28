

import random
from langdetect import detect
import os
import os.path


def add_word():
    user_finished = ''

    # validation - check txt bucket exists
    file_name = 'english_bucket.txt'
    cur_dir = os.getcwd()
    file_list = os.listdir(cur_dir)
    if file_name not in file_list:
        file = open("english_bucket.txt", "w")
        file2 = open("grades_bucket.txt", "w")
        file1 = open("hebrew_bucket.txt", "w", encoding="utf-8")
    else:
        file = open("english_bucket.txt", "a")
        file2 = open("grades_bucket.txt", "a")
        file1 = open("hebrew_bucket.txt", "a", encoding="utf-8")

    while user_finished != 'done':
        english_word = str(input('Enter your English word: '))
        english_check = detect(english_word)
        while english_check == 'he':
            print('-------------\nChoose your English word!\n-------------')
            english_word = str(input('Please enter your English word: '))
            english_check = detect(english_word)

        hebreww_word = str(input("Enter its meaning: "))
        hebrew_check = detect(hebreww_word)
        while hebrew_check != 'he':
            print('-------------\nChoose your Hebrew word!\n-------------')
            hebrew_word = str(input('Please enter your Hebrew word: '))
            hebrew_check = detect(hebrew_word)
        grade = 1
        file.write("{e},".format(e=english_word))
        file2.write("{g},".format(g=grade))
        file1.write("{h},".format(h=hebreww_word))
        his_choose = str(input("finished? write yes , more words? write go: "))
        if his_choose == 'yes':
            file.close()
            file2.close()
            file1.close()
            user_finished = "done"
        else:
            user_finished = 'go'
    return 'q'


def practice_words():
    english_bucket = []
    english_bucket1 = []

    # validation - check txt bucket exists
    file_name = 'english_bucket.txt'
    cur_dir = os.getcwd()
    file_list = os.listdir(cur_dir)
    if file_name not in file_list:
        print('---------------\nFirst you need to create vocabulary for practice\n-----------------------')
        return

    # validation - check if bucket empty
    e = open('english_bucket.txt', 'r')
    english_bucket = e.readlines()
    if len(english_bucket[0].split(',')) < 5:
        print(f"-------------\nYour English bucket contains only {len(english_bucket[0].split(','))-1} words.\nPlease"
              " add at least 5 words in it before practice.\n----------------")
        return

    # english_bucket = e.readlines()
    for words in english_bucket:
        word = words.split(',')
        for i in word:
            if i == '':
                pass
            else:
                english_bucket1.append(i)

    grades_bucket = []
    grades_bucket1 = []
    g = open('grades_bucket.txt', 'rt')
    grades_bucket = g.readlines()
    for words in grades_bucket:
        word = words.split(',')
        for i in word:
            if i == '':
                int_grades = []

                for i in range(len(grades_bucket1)):
                    item = int(grades_bucket1[i])
                    int_grades.append(item)
                pass
            else:
                grades_bucket1.append(i)

    dic = {1: 5, 2: 4, 4: 2, 5: 1}
    int_grades = [dic.get(n, n) for n in int_grades]


    hebrew_bucket = []
    hebrew_bucket1 = []
    h = open('hebrew_bucket.txt', 'r', encoding="utf-8")
    hebrew_bucket = h.readlines()
    for words in hebrew_bucket:
        word = words.split(',')
        for i in word:
            if i == '':
                pass
            else:
                hebrew_bucket1.append(i)

    done_for_now = 'keep'
    while done_for_now != 'f':
        the_word = random.choices(english_bucket1, int_grades, k=1)
        the_word = the_word[0]
        print(f'{the_word}: ')
        index_word = english_bucket1.index(the_word)
        answer_array = []
        the_word_meaning = hebrew_bucket1[index_word]
        answer_array.append(the_word_meaning)

        while len(answer_array) < 5:
            hebrew_word = random.choice(hebrew_bucket1)
            if hebrew_word in answer_array:
                pass
            else:
                answer_array.append(hebrew_word)

        counter = 1
        for i in range(len(answer_array)):
            h_word = random.choice(answer_array)
            if h_word == hebrew_bucket1[index_word]:
                answer_right_number = i
            h_clear_word = answer_array.index(h_word)
            print(f'{counter}. {answer_array[h_clear_word]}')
            del answer_array[h_clear_word]
            counter = counter + 1

        num_ans = str(input('press answer number: '))
        grade_word_change = str(grades_bucket1[index_word])
        if num_ans == str(int(answer_right_number) + 1):
            print('--------------------------')
            print('you are GOOD!')
            print('--------------------------')
            if grade_word_change == '5':
                grade_word_change = '5'
            else:
                grade_word_change = str(int(grade_word_change) + 1)
                grades_bucket1[index_word] = grade_word_change
            done_for_now = input('\nstop press (f) practice press (k)\n')
        else:
            print('--------------------------')
            print(f'The answer is: {hebrew_bucket1[index_word]}')
            print('--------------------------')
            if grade_word_change == '1':
                grade_word_change = '1'
            else:
                grade_word_change = str(int(grade_word_change) - 1)
                grades_bucket1[index_word] = grade_word_change

    last_rates_arr = []
    for i in range(len(grades_bucket1)):
        if i == 0:
            num_degree = f"{grades_bucket1[i]},"
        else:
            num_degree = num_degree + f"{grades_bucket1[i]},"

    g = open('grades_bucket.txt', 'w')
    g.write(num_degree)
    e.close()
    g.close()
    h.close()
    return 'q'


def finish():
    print('GOOD BYE!')


what_your_needs = 'q'
while what_your_needs != 'bye':
    user_choosed = str(input('For edit english words (w) for practice (p) for quit (q): '))
    if user_choosed == 'w':
        add_word()
    elif user_choosed == 'p':
        practice_words()
    elif user_choosed == 'q':
        finish()
        what_your_needs = 'bye'
