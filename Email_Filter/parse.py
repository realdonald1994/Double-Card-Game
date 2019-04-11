import re
from os import listdir
import math
import matplotlib.pyplot as plt
import numpy as np
import sys

computing_pham = 0
computing_pspam = 0
fakevocabulary = set()
except_stopword_voca = set()
dict_frequency_ham = {}
dict_frequency_spam = {}
over_dic = {}
TRAIN_PATH='train'
TEST_PATH = 'test'
STOP_WORD =  'English_StopWords.txt'
STORE_PATH1='baseline-model.txt'
STORE_PATH2='stopword-model.txt'
STORE_PATH3='wordlength-model.txt'
STORE_PATH4 = "demo-model-exp4.txt"
STORE_PATH5 = "demo-model-exp5.txt"
STORE_PATH6 = 'Infrequent Word Filtering1_model.txt'
STORE_PATH7 = 'Infrequent Word Filtering2_model.txt'
STORE_PATH8 = 'Smoothing_model.txt'
OUTPUT_PATH1='baseline-result.txt'
OUTPUT_PATH2='stopword-result.txt'
OUTPUT_PATH3='wordlength-result.txt'
OUTPUT_PATH4 = "demo-result-exp4.txt"
OUTPUT_PATH5 = "demo-result-exp5.txt"
OUTPUT_PATH6 = 'Infrequent Word Filtering1_result.txt'
OUTPUT_PATH7 = 'Infrequent Word Filtering2_result.txt'
OUTPUT_PATH8 = 'Smoothing_result.txt'



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

def demo(vocabulary,diction1,diction2,value):
    if not '.' in value:
        value = int(value)
        demo_vocabulary=[]
        for item in vocabulary:
            demo_vocabulary.append(item)
        if value==1:
            for i in range(len(demo_vocabulary) - 1, -1, -1):
                if diction1.get(demo_vocabulary[i], 0) + diction2.get(demo_vocabulary[i], 0) == value:
                    del demo_vocabulary[i]
            new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in demo_vocabulary}
            new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in demo_vocabulary}
            return demo_vocabulary, new_dict_frequency_ham, new_dict_frequency_spam
        else:
            for i in range(len(demo_vocabulary) - 1, -1, -1):
                if diction1.get(demo_vocabulary[i],0) + diction2.get(demo_vocabulary[i],0) < value:
                    del demo_vocabulary[i]
            new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in demo_vocabulary}
            new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in demo_vocabulary}
            return demo_vocabulary,new_dict_frequency_ham,new_dict_frequency_spam
    else:
        value = float(value)
        dictdata = set()
        top = math.ceil(value * len(vocabulary))
        finaldition = {x: diction1.get(x, 0) + diction2.get(x, 0) for x in set(diction1).union(diction2)}
        new_diction = sorted(finaldition.items(), key=lambda e: e[1], reverse=True)[:top]
        for l in new_diction:
            dictdata.add(l[0])
        vocabulary2 = vocabulary-dictdata
        new_dict_frequency_ham = {k: v for k, v in diction1.items() if k in vocabulary2}
        new_dict_frequency_spam = {k: v for k, v in diction2.items() if k in vocabulary2}
        return vocabulary2, new_dict_frequency_ham, new_dict_frequency_spam
def test_file2(path,nchoose,path2):
    datasetList = listdir(path)
    wrong_count=0
    test_ham_count= 0
    test_spam_count=0
    ham_right=0
    spam_right=0
    ham_count =0
    spam_count=0
    count=1
    for item in datasetList:
        file_type = item.split('-')[1]
        if file_type=='ham':
            ham_count+=1
        else:
            spam_count+=1
        overrall_ham,overrall_spam = testing(path+'/'+item,nchoose)
        if overrall_ham>=overrall_spam:
            label='ham'
            test_ham_count+=1
        else:
            label='spam'
            test_spam_count+=1
        if label=='ham' and label==file_type:
            right_or_not = 'right'
            ham_right+=1
        elif label=='spam' and label==file_type:
            right_or_not = 'right'
            spam_right+=1
        else:
            right_or_not = 'wrong'
            wrong_count+=1
        print(str(count).strip() + '  ' + str(item).strip() + '  '+str(label).strip()+'  ' \
              +str(overrall_ham).strip()+'  '+str(overrall_spam).strip()+'  '+str(file_type).strip()+'  '+str(right_or_not).strip(),
              file=open(path2, 'a'))
        count += 1
    accuracy=(ham_right+spam_right)/(spam_right+ham_right+wrong_count)
    precision_spam = (spam_right)/(test_spam_count)
    recall_spam = (spam_right)/(spam_count)
    F_score_spam = (2*precision_spam*recall_spam)/(precision_spam+recall_spam)
    precision_ham = (ham_right)/(test_ham_count)
    recall_ham = (ham_right)/(ham_count)
    F_score_ham = (2*precision_ham*recall_ham)/(precision_ham+recall_ham)
    # accuracy = 0
    # precision_spam=0
    # recall_spam=0
    # F_score_spam=0
    # precision_ham=0
    # recall_ham=0
    # F_score_ham=0
    print('accuracy: '+str(accuracy)+' '+'recall_ham: '+str(recall_ham)+' '+'precision_ham: '+str(precision_ham)+' '\
          +'fscore_ham: '+str(F_score_ham)+' '+'recall_spam: '+str(recall_spam)+' '+'precision_spam: '+str(precision_spam)+' '\
          +'fscore_spam: '+str(F_score_spam)+' '+'ham right: '+str(ham_right)+' '+'ham wrong: '+str((test_ham_count-ham_right))+' '+'spam right: '\
          +str(spam_right)+' '+'spam_wrong '+str((test_spam_count-spam_right))+'\n')
    return accuracy,recall_ham,precision_ham,F_score_ham,recall_spam,precision_spam,F_score_spam
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
        print(str(count).strip() + '  ' + str(key).strip() + '  '+str(round(value[0]-smooth)).strip()+'  ' \
              +str(value[1]).strip()+'  '+str(round(value[2]-smooth)).strip()+'  '+str(value[3]).strip(),
              file=open(path, 'a'))
        count+=1

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
            probility_ham=-float('inf')
            probility_spam = -float('inf')
        elif over_dic.get(item)[1]==0 and over_dic.get(item)[3]!=0:
            probility_ham = -float('inf')
            probility_spam = math.log10(over_dic.get(item)[3])
        elif over_dic.get(item)[1]!=0 and over_dic.get(item)[3]==0:
            probility_spam = -float('inf')
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

    top1= math.ceil(0.05*len(vocabulary))
    top2= math.ceil(0.1*len(vocabulary))
    top3= math.ceil(0.15*len(vocabulary))
    top4= math.ceil(0.2*len(vocabulary))
    top5= math.ceil(0.25*len(vocabulary))
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
    test_file2(TEST_PATH, nChoose,output_path)

def drop_item_run(nChoose,path1,path2):
    accuracy_list=[]
    vocabulary=[]
    recall_list_ham=[]
    precision_list_ham=[]
    fscore_list_ham = []
    recall_list_spam=[]
    precision_list_spam=[]
    fscore_list_spam= []
    remove_tem=[1,5,10,15,20]
    ham_file, spam_file = readfile(TRAIN_PATH)
    get_vocabulary(ham_file, spam_file, nChoose)
    for item in fakevocabulary:
        vocabulary.append(item)
    for i in range(1,6):
        newvocabulary,new_dict_frequency_ham,new_dict_frequency_spam = change_vocabulary(vocabulary,dict_frequency_ham,dict_frequency_spam,i)
        training(newvocabulary,new_dict_frequency_ham, new_dict_frequency_spam, SMOOTH,path1)
        accuracy,recall_ham,precision_ham,f_score_ham,recall_spam,precision_spam,f_score_spam= test_file2(TEST_PATH, nChoose,path2)
        accuracy_list.append(accuracy)
        recall_list_ham.append(recall_ham)
        precision_list_ham.append(precision_ham)
        fscore_list_ham.append(f_score_ham)
        recall_list_spam.append(recall_spam)
        precision_list_spam.append(precision_spam)
        fscore_list_spam.append(f_score_spam)
    plt.figure(1)
    plt.title('Test Results')
    plt.plot(remove_tem, accuracy_list)
    plt.ylabel('Accuracy')
    plt.xlabel('Frequency Item Will Be Removed')
    plt.savefig("Accuracy1.png")

    plt.figure(2)
    plt.title('Test Results')
    plt.plot(remove_tem, recall_list_ham)
    plt.ylabel('Recall_Ham')
    plt.xlabel('Frequency Item Will Be Removed')
    plt.savefig("Recall_Ham1.png")

    plt.figure(3)
    plt.title('Test Results')
    plt.plot(remove_tem, precision_list_ham)
    plt.ylabel('Precision_Ham')
    plt.xlabel('Frequency Item Will Be Removed')
    plt.savefig("Precision_Ham1.png")

    plt.figure(4)
    plt.title('Test Results')
    plt.plot(remove_tem, fscore_list_ham)
    plt.ylabel('F-measure_Ham')
    plt.xlabel('Frequency Item Will Be Removed')
    plt.savefig("F-measure_Ham1.png")

    plt.figure(5)
    plt.title('Test Results')
    plt.plot(remove_tem,recall_list_spam)
    plt.ylabel('Recall_Spam')
    plt.xlabel('Frequency Item Will Be Removed')
    plt.savefig("Recall_Spam1.png")

    plt.figure(6)
    plt.title('Test Results')
    plt.plot(remove_tem,precision_list_spam)
    plt.ylabel('Precision_Spam')
    plt.xlabel('Frequency Item Will Be Removed')
    plt.savefig("Precision_Spam1.png")

    plt.figure(7)
    plt.title('Test Results')
    plt.plot(remove_tem,fscore_list_spam)
    plt.ylabel('F-measure_Spam')
    plt.xlabel('Frequency Item Will Be Removed')
    plt.savefig("F-measure_Spam1.png")
    plt.show()


def drop_item_run2(nChoose, path1,path2):
    accuracy_list=[]
    recall_list_ham=[]
    precision_list_ham=[]
    fscore_list_ham = []
    recall_list_spam=[]
    precision_list_spam=[]
    fscore_list_spam= []
    remove_pro_tem= [0.05,0.10,0.15,0.20,0.25]
    ham_file, spam_file = readfile(TRAIN_PATH)
    get_vocabulary(ham_file, spam_file, nChoose)
    for i in range(1,6):
        newvocabulary, new_dict_frequency_ham, new_dict_frequency_spam = change_vocabulary2(fakevocabulary,dict_frequency_ham,dict_frequency_spam, i)
        training(newvocabulary, new_dict_frequency_ham, new_dict_frequency_spam, SMOOTH,path1)
        accuracy,recall_ham,precision_ham,f_score_ham,recall_spam,precision_spam,f_score_spam= test_file2(TEST_PATH, nChoose,path2)
        accuracy_list.append(accuracy)
        recall_list_ham.append(recall_ham)
        precision_list_ham.append(precision_ham)
        fscore_list_ham.append(f_score_ham)
        recall_list_spam.append(recall_spam)
        precision_list_spam.append(precision_spam)
        fscore_list_spam.append(f_score_spam)
    plt.figure(1)
    plt.title('Test Results')
    plt.plot(remove_pro_tem, accuracy_list)
    plt.ylabel('Accuracy')
    plt.xlabel('Frequency Top Precentage Will Be Removed')
    plt.savefig("Accuracy2.png")

    plt.figure(2)
    plt.title('Test Results')
    plt.plot(remove_pro_tem, recall_list_ham)
    plt.ylabel('Recall_Ham')
    plt.xlabel('Frequency Top Precentage Will Be Removed')
    plt.savefig("Recall_Ham2.png")

    plt.figure(3)
    plt.title('Test Results')
    plt.plot(remove_pro_tem, precision_list_ham)
    plt.ylabel('Precision_Ham')
    plt.xlabel('Frequency Top Precentage Will Be Removed')
    plt.savefig("Precision_Ham2.png")

    plt.figure(4)
    plt.title('Test Results')
    plt.plot(remove_pro_tem, fscore_list_ham)
    plt.ylabel('F-measure_Ham')
    plt.xlabel('Frequency Top Precentage Will Be Removed')
    plt.savefig("F-measure_Ham2.png")

    plt.figure(5)
    plt.title('Test Results')
    plt.plot(remove_pro_tem, recall_list_spam)
    plt.ylabel('Recall_Spam')
    plt.xlabel('Frequency Top Precentage Will Be Removed')
    plt.savefig("Recall_Spam2.png")

    plt.figure(6)
    plt.title('Test Results')
    plt.plot(remove_pro_tem, precision_list_spam)
    plt.ylabel('Precision_Spam')
    plt.xlabel('Frequency Top Precentage Will Be Removed')
    plt.savefig("Precision_Spam2.png")

    plt.figure(7)
    plt.title('Test Results')
    plt.plot(remove_pro_tem, fscore_list_spam)
    plt.ylabel('F-measure_Spam')
    plt.xlabel('Frequency Top Precentage Will Be Removed')
    plt.savefig("F-measure_Spam2.png")
    plt.show()

def change_smooth(nChoose,path1,path2):
    smooth_list=[]
    for i in np.arange(0,1.1,0.1):
        smooth_list.append(i)
    accuracy_list=[]
    recall_list_ham=[]
    precision_list_ham=[]
    fscore_list_ham= []
    recall_list_spam=[]
    precision_list_spam=[]
    fscore_list_spam= []
    ham_file, spam_file = readfile(TRAIN_PATH)
    get_vocabulary(ham_file, spam_file, nChoose)
    for i in range(len(smooth_list)):
        training(fakevocabulary,dict_frequency_ham, dict_frequency_spam, smooth_list[i],path1)
        accuracy,recall_ham,precision_ham,f_score_ham,recall_spam,precision_spam,f_score_spam = test_file2(TEST_PATH, nChoose,path2)
        accuracy_list.append(accuracy)
        recall_list_ham.append(recall_ham)
        precision_list_ham.append(precision_ham)
        fscore_list_ham.append(f_score_ham)
        recall_list_spam.append(recall_spam)
        precision_list_spam.append(precision_spam)
        fscore_list_spam.append(f_score_spam)
    plt.figure(1)
    plt.title('Test Results')
    plt.plot(smooth_list,accuracy_list)
    plt.ylabel('Accuracy')
    plt.xlabel('Smooth Value')
    plt.savefig("Accuracy2.png")

    plt.figure(2)
    plt.title('Test Results')
    plt.plot(smooth_list,recall_list_ham)
    plt.ylabel('Recall_Ham')
    plt.xlabel('Smooth Value')
    plt.savefig("Recall_Ham2.png")

    plt.figure(3)
    plt.title('Test Results')
    plt.plot(smooth_list,precision_list_ham)
    plt.ylabel('Precision_Ham')
    plt.xlabel('Smooth Value')
    plt.savefig("Precision_Ham2.png")

    plt.figure(4)
    plt.title('Test Results')
    plt.plot(smooth_list,fscore_list_ham)
    plt.ylabel('F-measure_Ham')
    plt.xlabel('Smooth Value')
    plt.savefig("F-measure_Ham2.png")

    plt.figure(5)
    plt.title('Test Results')
    plt.plot(smooth_list,recall_list_spam)
    plt.ylabel('Recall_Spam')
    plt.xlabel('Smooth Value')
    plt.savefig("Recall_Spam2.png")

    plt.figure(6)
    plt.title('Test Results')
    plt.plot(smooth_list,precision_list_spam)
    plt.ylabel('Precision_Spam')
    plt.xlabel('Smooth Value')
    plt.savefig("Precision_Spam2.png")

    plt.figure(7)
    plt.title('Test Results')
    plt.plot(smooth_list,fscore_list_spam)
    plt.ylabel('F-measure_Spam')
    plt.xlabel('Smooth Value')
    plt.savefig("F-measure_Spam2.png")
    plt.show()


def main():

    print("1> Normal email-filter")
    print("2> Stop-word Filtering")
    print("3> Word Length Filtering")
    print("4> Infrequent Word Filtering1")
    print("5> Infrequent Word Filtering2")
    print("6> Smoothing")
    print("7> Exit")

    nChoose = input("please enter your choice:")
    if nChoose == "1":
        run(nChoose,STORE_PATH1,OUTPUT_PATH1)
    if nChoose == "2":
        run(nChoose,STORE_PATH2,OUTPUT_PATH2)
    if nChoose == "3":
        run(nChoose,STORE_PATH3,OUTPUT_PATH3)
    if nChoose == "4":
        userinput = input("modo 1 or modo2?")
        if userinput == '1':
            value = input("input your frequency value:")
            ham_file, spam_file = readfile(TRAIN_PATH)
            get_vocabulary(ham_file, spam_file, nChoose)
            newvocabulary,new_dict_frequency_ham,new_dict_frequency_spam = demo(fakevocabulary,dict_frequency_ham,dict_frequency_spam,value)
            training(newvocabulary, new_dict_frequency_ham, new_dict_frequency_spam, SMOOTH, STORE_PATH4)
            test_file2(TEST_PATH, nChoose, OUTPUT_PATH4)
        else:
            drop_item_run(nChoose,STORE_PATH6,OUTPUT_PATH6)
    if nChoose == "5":
        userinput = input("modo 1 or modo2?")
        if userinput == '1':
            value = input("input your frequency value:")
            ham_file, spam_file = readfile(TRAIN_PATH)
            get_vocabulary(ham_file, spam_file, nChoose)
            newvocabulary,new_dict_frequency_ham,new_dict_frequency_spam = demo(fakevocabulary,dict_frequency_ham,dict_frequency_spam,value)
            training(newvocabulary, new_dict_frequency_ham, new_dict_frequency_spam, SMOOTH, STORE_PATH4)
            test_file2(TEST_PATH, nChoose, OUTPUT_PATH4)
        else:
            drop_item_run2(nChoose,STORE_PATH7,OUTPUT_PATH7)
    if nChoose == "6":
        userinput= input("modo 1 or modo2?")
        if userinput=='1':
            smooth = input("input your smooth value:")
            ham_file, spam_file = readfile(TRAIN_PATH)
            get_stopword(STOP_WORD)
            get_vocabulary(ham_file, spam_file, nChoose)
            training(fakevocabulary, dict_frequency_ham, dict_frequency_spam, float(smooth.strip()), STORE_PATH5)
            test_file2(TEST_PATH, nChoose, OUTPUT_PATH5)
        else:
            change_smooth(nChoose,STORE_PATH8,OUTPUT_PATH8)
    if nChoose == "7":
        print("Good Bye")
        sys.exit()

if __name__ == "__main__":
    main()