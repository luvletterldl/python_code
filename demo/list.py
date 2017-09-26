a=['1','fe','32','1efw']
list=list(a)
print(a)
# a.append("5")
a[len(a):]=[5]
print(a)
print(a[3])
print(a.__len__())
print()
print()

s=['a','b','c','d','e',]
d=['q','w','e','r']
print(s)
print(d)
# s[len(s):]=d
s.extend(d)
print(s)

print()
print()
print()

s.insert(3,'666')
print(s)

z=s.pop(5)
print(z)

s.insert(0,"你")
s.append('$%#')
s.sort()
print(s)
print(s.count('666'))
cs=s[:]
css=s.copy()
print(css)
print(cs)

print()
print()
print()
print()

# f=[1,2,3]
v=[x+'5'for x in s]
print(v)
v=[[x,x+'5'] for x in s]
print(v)
print()
print()
print()
print()
print()
print()


for ri in map(lambda x : x*x, [1,2,3,4,5]):
    print(ri)

print()
print()

qw=1
we=2
er=3
yz=qw,we,er
print(type(yz))

print()
print()
print()

questions=['name','quest','favorite color']
answers=['qinshihuang','the holy','blue']
aaaa=['qwer','abcde','wasd']
for q,a,l in zip(questions,answers,aaaa):
    print('what is your %s? it is %s qqqq %s' %(q,a,l))
    print('what is your {0}? it is {1}'.format(q,a))
print('\n' * 3)

k={"a":"1", "b":"2", "c":"3"}
for x,y in k.items():
    print(x,y)
print(k)
print(k.keys())
print(k.values())
print(k.items())

print(repr(s))

print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))


class Test:
    def prt(ldl):
        print(ldl)
        print(ldl.__class__)
t = Test()
t.prt()

class people:
    name=''
    age=0
    _wight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._wight=w
    def speak(self):
        print("%s say: I'm %s kg and I'm %s ages." %(self.name,self._wight,self.age))
p=people("ldl",67,21)
p.speak()


class divcal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return 'ldl (%d,%d)' % (self.a,self.b)
    def __add__(self, other):
        return (self.a+other.a,self.b+other.b)
vv=divcal(3,4)
vv1=divcal(5,6)
print(vv+vv1)
