import re
from os import listdir
import math
import matplotlib.pyplot as plt
import numpy as np

computing_pham = 0
computing_pspam = 0
fakevocabulary = set()
except_stopword_voca = set()
dict_frequency_ham = {}
dict_frequency_spam = {}
over_dic = {}
TRAIN_PATH='train'
TEST_PATH = 'test'
STOP_WORD =  'Stop_word.txt'
STORE_PATH1='model.txt'
STORE_PATH2='stopword-model.txt'
STORE_PATH3='wordlength-model.txt'
OUTPUT_PATH1='baseline-result.txt'
OUTPUT_PATH2='stopword-result.txt'
OUTPUT_PATH3='wordlength-result.txt'
SMOOTH=0.5
MINI_LENGTH=2
MAX_LENGTH=9

def word_check(item):
    if len(item)<=MINI_LENGTH or len(item)>=MAX_LENGTH:
        return False
    return True
def get_stopword(path):
    with open(path,'r') as df:
        for line in df:
            except_stopword_voca.add(line.strip().lower())

def test_file(path,path2,nchoose):
    datasetList = listdir(path)
    count=1
    for item in datasetList:
        file_type = item.split('-')[1]
        overrall_ham,overrall_spam = testing(path+'/'+item,nchoose)
        if overrall_ham>overrall_spam:
            label='ham'
        else:
            label='spam'
        if label==file_type:
            right_or_not='right'
        else:
            right_or_not='wrong'
        print(str(count).strip() + '  ' + str(item).strip() + '  '+str(label).strip()+'  ' \
              +str(overrall_ham).strip()+'  '+str(overrall_spam).strip()+'  '+str(file_type).strip()+'  '+str(right_or_not).strip()+'\n',
              file=open(path2, 'a'))
        count+=1
def test_file2(path,nchoose):
    datasetList = listdir(path)
    right_count=0
    wrong_count=0
    for item in datasetList:
        file_type = item.split('-')[1]
        overrall_ham,overrall_spam = testing(path+'/'+item,nchoose)
        if overrall_ham>overrall_spam:
            label='ham'
        else:
            label='spam'
        if label==file_type:
            right_count+=1
        else:
            wrong_count+=1
    accuracy=right_count/(right_count+wrong_count)
    return accuracy
def readfile(path):
    global  computing_pham
    global  computing_pspam
    datasetList = listdir(path)
    ham_file=[]
    spam_file=[]
    ham_count=0
    spam_count=0
    for item in datasetList:
        if 'ham' in item:
            ham_file.append(path+'/'+item)
            ham_count+=1
        elif 'spam' in item:
            spam_file.append(path+'/'+item)
            spam_count+=1
    computing_pham= ham_count/(ham_count+spam_count)
    computing_pham = math.log10(computing_pham)
    computing_pspam=spam_count/(ham_count+spam_count)
    computing_pspam =math.log10(computing_pspam)
    return ham_file,spam_file

def get_vocabulary(ham_file,spam_file,nchoose):
    for i in range(len(ham_file)):
        with open(ham_file[i], encoding='latin-1') as df:
            for line in df:
                for item in re.split('[^a-zA-Z]',line):
                    if item!=''and item!=' ':
                        if nchoose=='2' and item.lower() in except_stopword_voca:
                            continue
                        elif nchoose=='3' and word_check(item.lower())==False:
                            continue
                        else:
                            fakevocabulary.add(item.lower())
                            if item.lower() in dict_frequency_ham:
                                dict_frequency_ham[item.lower()] += 1
                            else:
                                dict_frequency_ham[item.lower()] = 1
                    else:
                        continue

    for i in range(len(spam_file)):
        with open(spam_file[i],encoding='latin-1') as df:
            for line in df:
                for item in re.split('[^a-zA-Z]', line):
                    if item!='' and item!=' ':
                        if nchoose=='2' and item.lower() in except_stopword_voca:
                            continue
                        elif nchoose=='3' and word_check(item.lower())==False:
                            continue
                        else:
                            fakevocabulary.add(item.lower())
                            if item.lower() in dict_frequency_spam:
                                dict_frequency_spam[item.lower()] += 1
                            else:
                                dict_frequency_spam[item.lower()]=1
                    else:
                        continue

def training(vocabulary,dic_ham,dic_spam,smooth,path):
    length = smooth*len(vocabulary)
    count_ham=0
    count_spam = 0
    for value in dic_ham.values():
        count_ham+=value
    for value in dic_spam.values():
        count_spam+=value
    count=1
    for item in sorted(vocabulary):
        over_dic[item]=[]
        over_dic[item].append(dic_ham.get(item,0)+smooth)
        over_dic[item].append((dic_ham.get(item,0)+smooth)/(count_ham+length))
        over_dic[item].append(dic_spam.get(item,0)+smooth)
        over_dic[item].append((dic_spam.get(item,0)+smooth)/(count_spam+length))
    for key,value in over_dic.items():

        print(str(count).strip() + '  ' + str(key).strip() + '  '+str(value[0]).strip()+'  ' \
              +str(value[1]).strip()+'  '+str(value[2]).strip()+'  '+str(value[3]).strip()+'\n',
              file=open(path, 'a'))
        count+=1
def training2(vocabulary,dic_ham,dic_spam,smooth):
    length = smooth*len(vocabulary)
    count_ham=0
    count_spam = 0
    for value in dic_ham.values():
        count_ham+=value
    for value in dic_spam.values():
        count_spam+=value
    for item in sorted(vocabulary):
        over_dic[item]=[]
        over_dic[item].append(dic_ham.get(item,0)+smooth)
        over_dic[item].append((dic_ham.get(item,0)+smooth)/(count_ham+length))
        over_dic[item].append(dic_spam.get(item,0)+smooth)
        over_dic[item].append((dic_spam.get(item,0)+smooth)/(count_spam+length))

def testing(path,nchoose):
    overrall_ham=computing_pham
    overrall_spam=computing_pspam
    with open(path, encoding='latin-1') as df:
        for line in df:
            for item in re.split('[^a-zA-Z]', line):
                if item != '' and item != ' ':
                    if nchoose=='2' and item.lower() in except_stopword_voca:
                        continue
                    elif nchoose == '3' and word_check(item.lower()) == False:
                        continue
                    else:
                        probility_ham,probility_spam= math_compute(item.lower())
                        overrall_ham+=probility_ham
                        overrall_spam+=probility_spam
    return overrall_ham,overrall_spam
def math_compute(item):
    probility_ham=0.0
    probility_spam=0.0
    if item in over_dic:
        if over_dic.get(item)[1]==0 and over_dic.get(item)[3]==0:
            probility_ham=-9999999999999
            probility_spam = -9999999999999
        elif over_dic.get(item)[1]==0 and over_dic.get(item)[3]!=0:
            probility_ham = -9999999999999
            probility_spam = math.log10(over_dic.get(item)[3])
        elif over_dic.get(item)[1]!=0 and over_dic.get(item)[3]==0:
            probility_spam = -9999999999999
            probility_ham = math.log10(over_dic.get(item)[1])
        else:
            probility_ham=math.log10(over_dic.get(item)[1])
            probility_spam=math.log10(over_dic.get(item)[3])
    return probility_ham,probility_spam
def change_vocabulary(vocabulary,diction1,diction2,mode):
    if mode == 1:
        for i in range(len(vocabulary) - 1, -1, -1):
            if diction1.get(vocabulary[i],0) + diction2.get(vocabulary[i],0) == 1:
                del vocabulary[i]
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary}

    elif mode == 2:
        for i in range(len(vocabulary) - 1, -1, -1):
            if diction1.get(vocabulary[i],0) + diction2.get(vocabulary[i],0) <= 5:
                del vocabulary[i]
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary}
    elif mode == 3:
        for i in range(len(vocabulary) - 1, -1, -1):
            if diction1.get(vocabulary[i],0) + diction2.get(vocabulary[i],0) <= 10:
                del vocabulary[i]
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary}
    elif mode == 4:

        for i in range(len(vocabulary) - 1, -1, -1):
            if diction1.get(vocabulary[i],0) + diction2.get(vocabulary[i],0) <= 15:
                del vocabulary[i]
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary}
    elif mode == 5:

        for i in range(len(vocabulary) - 1, -1, -1):
            if diction1.get(vocabulary[i],0) + diction2.get(vocabulary[i],0) <= 20:
                del vocabulary[i]
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary}
    return vocabulary,new_dict_frequency_ham,new_dict_frequency_spam
def change_vocabulary2(vocabulary,diction1,diction2,mode):
    dictdata = set()

    top1= math.ceil(0.05*len(fakevocabulary))
    top2= math.ceil(0.1*len(fakevocabulary))
    top3= math.ceil(0.15*len(fakevocabulary))
    top4= math.ceil(0.2*len(fakevocabulary))
    top5= math.ceil(0.25*len(fakevocabulary))
    if mode == 1:
        finaldition = {x: diction1.get(x, 0) + diction2.get(x, 0) for x in set(diction1).union(diction2)}
        new_diction = sorted(finaldition.items(), key=lambda e: e[1], reverse=True)[:top1]
        for l in new_diction:
            dictdata.add(l[0])
        vocabulary2 = vocabulary-dictdata
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary2}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary2}
    elif mode == 2:
        finaldition = {x: diction1.get(x, 0) + diction2.get(x, 0) for x in set(diction1).union(diction2)}
        new_diction = sorted(finaldition.items(), key=lambda e: e[1], reverse=True)[:top2]
        for l in new_diction:
            dictdata.add(l[0])
        vocabulary2 = vocabulary-dictdata
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary2}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary2}
    elif mode == 3:
        finaldition = {x: diction1.get(x, 0) + diction2.get(x, 0) for x in set(diction1).union(diction2)}
        new_diction = sorted(finaldition.items(), key=lambda e: e[1], reverse=True)[:top3]
        for l in new_diction:
            dictdata.add(l[0])
        vocabulary2 = vocabulary-dictdata
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary2}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary2}
    elif mode == 4:
        finaldition = {x: diction1.get(x, 0) + diction2.get(x, 0) for x in set(diction1).union(diction2)}
        new_diction = sorted(finaldition.items(), key=lambda e: e[1], reverse=True)[:top4]
        for l in new_diction:
            dictdata.add(l[0])
        vocabulary2 = vocabulary-dictdata
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary2}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary2}
    elif mode == 5:
        finaldition = {x: diction1.get(x, 0) + diction2.get(x, 0) for x in set(diction1).union(diction2)}
        new_diction = sorted(finaldition.items(), key=lambda e: e[1], reverse=True)[:top5]
        for l in new_diction:
            dictdata.add(l[0])
        vocabulary2 = vocabulary-dictdata
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary2}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary2}
    return vocabulary2,new_dict_frequency_ham,new_dict_frequency_spam

def run(nChoose,store_path,output_path):
    ham_file, spam_file = readfile(TRAIN_PATH)
    get_stopword(STOP_WORD)
    get_vocabulary(ham_file, spam_file, nChoose)
    training(fakevocabulary,dict_frequency_ham, dict_frequency_spam, SMOOTH,store_path)
    test_file(TEST_PATH, output_path, nChoose)

def drop_item_run(nChoose):
    accuracy_list=[]
    vocabulary=[]
    ham_file, spam_file = readfile(TRAIN_PATH)
    get_vocabulary(ham_file, spam_file, nChoose)
    for item in fakevocabulary:
        vocabulary.append(item)
    new_dict_frequency_ham= dict_frequency_ham
    new_dict_frequency_spam=dict_frequency_spam
    for i in range(1,6):
        vocabulary,new_dict_frequency_ham,new_dict_frequency_spam = change_vocabulary(vocabulary,new_dict_frequency_ham,new_dict_frequency_spam,i)
        training2(vocabulary,new_dict_frequency_ham, new_dict_frequency_spam, SMOOTH)
        accuracy = test_file2(TEST_PATH, nChoose)
        accuracy_list.append(accuracy)
    return set(vocabulary),new_dict_frequency_ham,new_dict_frequency_spam,accuracy_list

def drop_item_run2(nChoose,vocabulary2,new_dict_frequency_ham,new_dict_frequency_spam,accuracy_list):
    remove_tem=[1,2,3,4,5,6,7,8,9,10]
    for i in range(1,6):
        vocabulary2, new_dict_frequency_ham, new_dict_frequency_spam = change_vocabulary2(vocabulary2,new_dict_frequency_ham,new_dict_frequency_spam, i)
        training2(vocabulary2, new_dict_frequency_ham, new_dict_frequency_spam, SMOOTH)
        accuracy = test_file2(TEST_PATH, nChoose)
        accuracy_list.append(accuracy)
    plt.figure(1)
    plt.title('Test Results')
    plt.plot(remove_tem,accuracy_list)
    plt.ylabel('Accuracy')
    plt.xlabel('Remove Frequency Word')
    plt.show()

def change_smooth(nChoose):
    smooth_list=[]
    for i in np.arange(0,1.1,0.1):
        smooth_list.append(i)
    accuracy_list=[]

    ham_file, spam_file = readfile(TRAIN_PATH)
    get_vocabulary(ham_file, spam_file, nChoose)
    for i in range(len(smooth_list)):
        training2(fakevocabulary,dict_frequency_ham, dict_frequency_spam, smooth_list[i])
        accuracy = test_file2(TEST_PATH, nChoose)
        accuracy_list.append(accuracy)

    plt.figure(3)
    plt.title('Test Results')
    plt.plot(smooth_list,accuracy_list)
    plt.ylabel('Accuracy')
    plt.xlabel('Smooth Value')
    plt.show()


def main():

    print("1> Normal email-filter")
    print("2> Stop-word Filtering")
    print("3> Word Length Filtering")
    print("4> Infrequent Word Filtering")
    print("5> Smoothing")
    print("6> Exit")

    nChoose = input("please enter your choice:")
    if nChoose == "1":
        run(nChoose,STORE_PATH1,OUTPUT_PATH1)
    if nChoose == "2":
        run(nChoose,STORE_PATH2,OUTPUT_PATH2)
    if nChoose == "3":
        run(nChoose,STORE_PATH3,OUTPUT_PATH3)
    if nChoose == "4":

        vocabulary,new_dict_frequency_ham,new_dict_frequency_spam,accuracy_list = drop_item_run(nChoose)
        drop_item_run2(nChoose,vocabulary,new_dict_frequency_ham,new_dict_frequency_spam,accuracy_list)

    if nChoose == "5":
        change_smooth(nChoose)

if __name__ == "__main__":
    main()