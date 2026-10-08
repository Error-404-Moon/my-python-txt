#stings 1
def count_words (sentens):
    dic_words ={}
    for word in sentens.split(' '):
        if word in dic_words.keys():
            dic_words[word]+= 1
        else:
            dic_words[word] = 1
    print(dic_words)
    
#count_words('hi hi world')
#strings 2
def title (sentens):
    words=[]
    for word in sentens.split(' '):
        words.append(word.capitalize())
    print(" ".join(words))
    
#title("hi hi world")

#strings 3

import string as st
'''
def num(sentens):
    for i in st.punctuation :
        sentens = sentens.replace(i, "")
    print(sentens)

num("udhei, he, 9l ,,!@$")
'''
def num(sentens):
    words =[]
    pu =[]
    okey_char = st.punctuation
    for word in sentens:
        if word in st.punctuation:
            pu.append(word)
        else:
            words.append(word)       
    print(''.join(words))
#num("udhei, he, 9l ,,!@$")

#list 1
def list_sum(liist) :
    summ = 0
    for num in liist:
        summ += num
    print(summ)
list_sum([2, 6, 3])

#list 2
def not_in_list(liist):
    new_list = []
    for i in liist:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

not_in_list([8, 9 ,9 ,672,'dbr','dbr'])

#list 3

def join_list(lisst):
    return','.join(str(indrxx) for indrxx in lisst)

print(join_list([2, 4, 6]))

#set 1
def in_set (set1, set2):
    return set1 & set2
    
print(in_set({1, 2, 3}, {2, 3, 8})) 

#set 2
def difrents(set1, set2):
    itemes = set({})
    print(set1.symmetric_difference(set2))
    print( (set1 | set2) - (set1 & set2))
    

difrents({1, 2, 3}, {2, 3, 8})
#set 3
def sets(set1, set2):
    if set2.issubset(set1) or set1.issubset(set2):
      print('okey')
    else:
        print("no")  
sets({1, 3, 2, 4},{1,4})
#tuple 1
def list_to_tuple(list1):
    new_tuple = []
    for x in list1:
        new_tuple.append( tuple(x))
    print(tuple(new_tuple))

list_to_tuple([[2,3],[8] ,[99, 88]])
'''
#tuple 2
list1=[[2,3],[8] ,[99, 88]]
list2=[]
for x in list1:
    list3 =[]
    for i in x:
        list3.append(i)
        list2.append(tuple(list3))
    
o = tuple(list2)
print(o)
'''
'''
#tuple 2
def count_tuple(tp):

'''
            
#dict 1
def dictt(dict1):
    new_dict ={}
    for i in dict1.values():
        for ch in dict1.keys():
            new_dict[ch] = i
    return new_dict
print(dictt({'a':1, 'b':2}))

#dict 2
def dicct(dict1, dict2):
    new_dict ={}
    char1 = 0
    char2 = 0
    n_char = 0
    for ch in dict1.keys():
        if ch in dict2.keys():
            char1 += dict1.get(ch)
            char2 += dict2.get(ch)
            dict1[ch] = char1 + char2
    print(dict1)
dicct({'a':2, 'n':3, 'k': 9}, {'s':0, 'a':3})