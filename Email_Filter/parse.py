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
STORE_PATH4 = "demo-model-exp4.txt"
STORE_PATH5 = "demo-model-exp5.txt"
OUTPUT_PATH1='baseline-result.txt'
OUTPUT_PATH2='stopword-result.txt'
OUTPUT_PATH3='wordlength-result.txt'
OUTPUT_PATH4 = "demo-result-exp4.txt"
OUTPUT_PATH5 = "demo-result-exp5.txt"



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
              +str(overrall_ham).strip()+'  '+str(overrall_spam).strip()+'  '+str(file_type).strip()+'  '+str(right_or_not).strip(),
              file=open(path2, 'a'))
        count+=1
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
        if overrall_ham>overrall_spam:
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
        # print(str(count).strip() + '  ' + str(item).strip() + '  '+str(label).strip()+'  ' \
        #       +str(overrall_ham).strip()+'  '+str(overrall_spam).strip()+'  '+str(file_type).strip()+'  '+str(right_or_not).strip(),
        #       file=open(path2, 'a'))
        count += 1
    accuracy=(ham_right+spam_right)/(spam_right+ham_right+wrong_count)
    precision = (spam_right)/(test_spam_count)
    recall = (spam_right)/(spam_count)
    F_score = (2*precision*recall)/(precision+recall)
    return accuracy,recall,precision,F_score
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
              +str(value[1]).strip()+'  '+str(value[2]).strip()+'  '+str(value[3]).strip(),
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
    count=1
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
    test_file(TEST_PATH, output_path, nChoose)

def drop_item_run(nChoose,path1,path2):
    accuracy_list=[]
    vocabulary=[]
    recall_list=[]
    precision_list=[]
    fscore_list = []
    ham_file, spam_file = readfile(TRAIN_PATH)
    get_vocabulary(ham_file, spam_file, nChoose)
    for item in fakevocabulary:
        vocabulary.append(item)
    for i in range(1,6):
        newvocabulary,new_dict_frequency_ham,new_dict_frequency_spam = change_vocabulary(vocabulary,dict_frequency_ham,dict_frequency_spam,i)
        training2(newvocabulary,new_dict_frequency_ham, new_dict_frequency_spam, SMOOTH)
        accuracy,recall,precision,f_score= test_file2(TEST_PATH, nChoose,path2)
        accuracy_list.append(accuracy)
        recall_list.append(recall)
        precision_list.append(precision)
        fscore_list.append(f_score)
    return set(newvocabulary),new_dict_frequency_ham,new_dict_frequency_spam,accuracy_list,recall_list,precision_list,fscore_list

def drop_item_run2(nChoose,vocabulary2,last_dict_frequency_ham,last_dict_frequency_spam,accuracy_list,recall_list,precision_list,fscore_list, path1,path2):
    remove_tem=[1,2,3,4,5,6,7,8,9,10]
    for i in range(1,6):
        newvocabulary, new_dict_frequency_ham, new_dict_frequency_spam = change_vocabulary2(vocabulary2,last_dict_frequency_ham,last_dict_frequency_spam, i)
        training2(newvocabulary, new_dict_frequency_ham, new_dict_frequency_spam, SMOOTH)
        accuracy,recall,precision,f_score= test_file2(TEST_PATH, nChoose,path2)
        accuracy_list.append(accuracy)
        recall_list.append(recall)
        precision_list.append(precision)
        fscore_list.append(f_score)
    plt.figure(1)
    plt.title('Test Results')
    plt.plot(remove_tem,accuracy_list)
    plt.ylabel('Accuracy')
    plt.xlabel('Word Filtering Situation')
    plt.savefig("Accuracy.png")

    plt.figure(2)
    plt.title('Test Results')
    plt.plot(remove_tem,recall_list)
    plt.ylabel('Recall')
    plt.xlabel('Word Filtering Situation')
    plt.savefig("Recall.png")

    plt.figure(3)
    plt.title('Test Results')
    plt.plot(remove_tem,precision_list)
    plt.ylabel('Precision')
    plt.xlabel('Word Filtering Situation')
    plt.savefig("Precision.png")

    plt.figure(4)
    plt.title('Test Results')
    plt.plot(remove_tem,fscore_list)
    plt.ylabel('F-measure')
    plt.xlabel('Word Filtering Situation')
    plt.savefig("F-measure.png")
    plt.show()

def change_smooth(nChoose,path1,path2):
    smooth_list=[]
    for i in np.arange(0,1.1,0.1):
        smooth_list.append(i)
    accuracy_list=[]
    recall_list=[]
    precision_list=[]
    fscore_list= []
    ham_file, spam_file = readfile(TRAIN_PATH)
    get_vocabulary(ham_file, spam_file, nChoose)
    for i in range(len(smooth_list)):
        training2(fakevocabulary,dict_frequency_ham, dict_frequency_spam, smooth_list[i])
        accuracy,recall,precision,f_score = test_file2(TEST_PATH, nChoose,path2)
        accuracy_list.append(accuracy)
        recall_list.append(recall)
        precision_list.append(precision)
        fscore_list.append(f_score)
    plt.figure(1)
    plt.title('Test Results')
    plt.plot(smooth_list,accuracy_list)
    plt.ylabel('Accuracy')
    plt.xlabel('Smooth Value')
    plt.savefig("Accuracy.png")

    plt.figure(2)
    plt.title('Test Results')
    plt.plot(smooth_list,recall_list)
    plt.ylabel('Recall')
    plt.xlabel('Smooth Value')
    plt.savefig("Recall.png")

    plt.figure(3)
    plt.title('Test Results')
    plt.plot(smooth_list,precision_list)
    plt.ylabel('Precision')
    plt.xlabel('Smooth Value')
    plt.savefig("Precision.png")

    plt.figure(4)
    plt.title('Test Results')
    plt.plot(smooth_list,fscore_list)
    plt.ylabel('F-measure')
    plt.xlabel('Smooth Value')
    plt.savefig("F-measure.png")
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

        vocabulary,new_dict_frequency_ham,new_dict_frequency_spam,accuracy_list,recall_list,precision_list,fscore_list = drop_item_run(nChoose,STORE_PATH4,OUTPUT_PATH4)
        drop_item_run2(nChoose,vocabulary,new_dict_frequency_ham,new_dict_frequency_spam,accuracy_list,recall_list,precision_list,fscore_list,STORE_PATH4,OUTPUT_PATH4)

    if nChoose == "5":
        change_smooth(nChoose,STORE_PATH5,OUTPUT_PATH5)

if __name__ == "__main__":
    main()