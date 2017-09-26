#Python中的容器是内置数据结构(Built-in Data Structure)
# fruit = ['p','pe']
# fruit[1:2]=['O']
# print(fruit)
# # del fruit[0:2]
# # print(fruit)
# letters=['a','b','c','d','e','f','g']
# for num,letter in enumerate(letters):
#     print(letter,'is',num+1)
#
# g={i:j.upper() for i,j in zip(range(1,6),'abcde')}
# print(g)
# 查找出文本中所有的字符串的出现次数并降序排列
import string
path='F:/Walden.txt'
with open(path,'r') as text:
    words=[raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index=set(words)
    counts_dict={index:words.count(index) for index in words_index}
    for word in sorted(counts_dict,key=lambda x:counts_dict[x],reverse=True):
        print('{} -- {} times'.format(word,counts_dict[word]))
#证实分片在取出字典所有key
s={1:'3',2:'4',3:'5'}
for w in sorted(s,key=lambda x:s[x],reverse=True):
    print('{} -- {} times'.format(w,s[w]))