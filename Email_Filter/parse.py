import re
from os import listdir
import timeit
import math

computing_pham = 0
computing_pspam = 0
fakevocabulary = set()
dict_frequency_ham = {}
dict_frequency_spam = {}
over_dic = {}
TRAIN_PATH='train'
TEST_PATH = 'test'
SMOOTH=0.5

def test_file(path):
    datasetList = listdir(path)
    count=1
    for item in datasetList:
        file_type = item.split('-')[1]
        overrall_ham,overrall_spam = testing(path+'/'+item)
        if overrall_ham>overrall_spam:
            label='ham'
        else:
            label='spam'
        if label==file_type:
            right_or_not='right'
        else:
            right_or_not='wrong'
        print(str(count).strip() + '  ' + str(item).strip() + '  '+str(label).strip()+'  ' \
              +str(overrall_ham).strip()+'  '+str(overrall_spam).strip()+'  '+str(right_or_not).strip()+'\n',
              file=open('baseline-result.txt', 'a'))
        count+=1

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

def get_vocabulary(ham_file,spam_file):
    for i in range(len(ham_file)):
        with open(ham_file[i], encoding='latin-1') as df:
            for line in df:
                for item in re.split('[^a-zA-Z]',line):
                    if item!=''and item!=' ':
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
                        fakevocabulary.add(item.lower())
                        if item.lower() in dict_frequency_spam:
                            dict_frequency_spam[item.lower()] += 1
                        else:
                            dict_frequency_spam[item.lower()]=1
                    else:
                        continue

def training(dic_ham,dic_spam,smooth):
    path='model.txt'
    length = smooth*len(fakevocabulary)
    count_ham=0
    count_spam = 0
    for value in dic_ham.values():
        count_ham+=value
    for value in dic_spam.values():
        count_spam+=value
    count=1
    for item in sorted(fakevocabulary):
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
def testing(path):
    overrall_ham=computing_pham
    overrall_spam=computing_pspam
    with open(path, encoding='latin-1') as df:
        for line in df:
            for item in re.split('[^a-zA-Z]', line):
                if item != '' and item != ' ':
                    probility_ham,probility_spam= math_compute(item)
                    overrall_ham+=probility_ham
                    overrall_spam+=probility_spam
    return overrall_ham,overrall_spam
def math_compute(item):
    probility_ham=0
    probility_spam=0
    if item in over_dic:
        probility_ham=math.log10(over_dic.get(item)[1])
        probility_spam=math.log10(over_dic.get(item)[3])
    return probility_ham,probility_spam
def main():
    while True:
        print("1> Normal email-filter")
        print("2> Stop-word Filtering")
        print("3> Word Length Filtering")
        print("4> Infrequent Word Filtering")
        print("5> Smoothing")
        print("6> Exit")

        nChoose = input("please enter your choice:")
        if nChoose == "1":
            start = timeit.default_timer()
            ham_file, spam_file = readfile(TRAIN_PATH)
            get_vocabulary(ham_file, spam_file)
            training(dict_frequency_ham, dict_frequency_spam, SMOOTH)
            test_file(TEST_PATH)
            stop = timeit.default_timer()
            print('Time: ', stop - start, 'S')
        if nChoose == "2":
            pass
        if nChoose == "3":
            pass
        if nChoose == "4":
            pass
        if nChoose == "5":
            pass
        if nChoose == "6":
            pass
if __name__ == "__main__":
    main()