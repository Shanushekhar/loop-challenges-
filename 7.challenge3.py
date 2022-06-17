#!/usr/bin/env python
# coding: utf-8

# In[48]:


#q1
s='ineuron'
for i in range(3):
    for j in range(i+1):
        print(s,end=' ')
    print()
for i in range(3,4):
    print(s,s,s,end=' ')
    
    
    


# In[51]:


#q2
s='ineuron'
n=3
for i in range(3):
    for j in range(i,n-1):
        print(' ',end=' ')
    for j in range(i+1):
        print(s,end=" ")
    print()
for i in range(3,4):
    for j in range(i-2):
        print(' ',end=' ')    
    for j in range(i-1):
            print(s,end=' ')
    print()       
for i in range(4,5):
    print('   ',s,end=' ')
      
    


# In[35]:


l=(1,4,2)
for k in l:
    print(k)


# In[13]:


len(s)


# In[40]:


for i in range(0,3):
    print(i)


# In[42]:


s='ineuron'
for i in range(3):
    for j in range(i,2):
        print(s,end=' ')
    


# In[59]:


#q3
#try to extract all the list entity
l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,5]),{'k1':'sudh', 'k2':'ineuron', 'k3':'kumar', 3:6, 7:8},['ineuron','datascience']]
for i in l:
    if type(i)==list:
        print(i)
        for j in i:
            print(j)


# In[55]:


ll=[1,2,3,4]
type(ll)


# In[64]:


#q4 extract all dict entities
for i in l:
    if type(i)==dict:
        print(i)
        for k,v in i.items():
            print(k,':',v)


# In[65]:


#q5 extract all tuple entities
for i in l:
    if type(i)==tuple:
        print(i)
        for j in i:
            print(j)


# In[71]:


#q6 extract all the numerical value for dict(keys and values)
for i in l:
    if type(i)==dict:
        for k,v in i.items():
            if type(k)==int:
                print(k)
            if type(v)==int:
                print(v)


# In[66]:


s={1,2,5,8,3,4}


# In[67]:


s


# In[68]:


s[0]


# In[72]:


#q7 extract all odd numeric values from lists of list(l)
for i in l:
    if type(i)==list:
        print(i)
        for j in i:
            if type(j)==int:
                print(j)


# In[79]:


#extra question-extract all the numeriical data from the list
for i in l:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==int:
                print(j)
    if type(i)==set:
        ll=list(i)
        for j in ll:
            if type(j)==int:
                print(j)
    if type(i)==dict:
        for k,v in i.items():
            if type(k)==int:
                print(k)
            if type(v)==int:
                print(v)


# In[80]:


#q8-all the odd value numeric numbers
for i in l:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==int:
                if j%2==0:
                    print(j)
    if type(i)==set:
        ll=list(i)
        for j in ll:
            if type(j)==int:
                if j%2==0:
                    print(j)
    if type(i)==dict:
        for k,v in i.items():
            if type(k)==int:
                if j%2==0:
                    print(k)
            if type(v)==int:
                if j%2==0:
                    print(v)


# In[124]:


#q9 summation of all the numeric values
s6=0
s7=0
s8=0
s9=0
for i in l:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==int:
                s6+=j
        print(s6)
    if type(i)==set:
        ll=list(i)
        for j in ll:
            if type(j)==int:
                s7+=j
        print(s7)       
    if type(i)==dict:
        for k,v in i.items():
            if type(k)==int:
                s8+=k
                print(s8)
            if type(v)==int:
                s9+=v
                print(s9)
                        
s6+s7+s8+s9


# In[98]:


i=0
for i in range(10):
    k+=i
print(k)


# In[112]:


s2=0
for i in l:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==int:
                s2+=j
        print(s2)


# In[107]:


for j in i:


# In[152]:


#q10 extract ineuron out of this data
l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,5]),{'k1':'sudh', 'k2':'ineuron', 'k3':'kumar', 3:6, 7:8},['ineuron','datascience']]
for i in l:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if j=='ineuron':
                print(j)
    if type(i)==set:
        ll=list(i)
        for j in ll:
            if j=='ineuron':
                print(j)
    if type(i)==dict:
        for k,v in i.items():
            if k=='ineuron':
                print(k)
            if v=='ineuron':
                print(v)


# In[144]:


if type(i)==dict:
        for k,v in i.items():
            print(k,v)


# In[150]:


for i in l:
    if type(i)==dict:
        for k,v in i.items():
            if k=='ineuron':
                print(k)
            if v=='ineuron':
                print(v)


# In[149]:


li=[1,3,4,'shanu',5,6,'shanu']
for i in li:
    if i=='shanu':
        print(i)
    
        


# In[166]:


##q11 find out the occurances of all the data
l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,5]),{'k1':'sudh', 'k2':'ineuron', 'k3':'kumar', 3:6, 7:8},['ineuron','datascience']]
for i in l:
    if type(i)==list:
        for j in set(i):
            print(j,':',i.count(j))


# In[163]:


a='ggghllaaa'
for i in set(a):
    print(i,':',a.count(i))


# In[170]:


l=[[1,2,3,4,2,2,1,1],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,5]),{'k1':'sudh', 'k2':'ineuron', 'k3':'kumar', 3:6, 7:8},['ineuron','datascience']]
for i in l:
    if type(i)=list:
        


# In[174]:


x=[1,4,4,2,3,3,5,5,6]
y=[4,4,5,5,5,9,8]
x+y


# In[199]:


for i in l:
    if type(i)==tuple:
        l1=list(i)
        print(l1)
    if type(i)==set:
        l2=list(i)
        print(l2)
    if type(i)==list:
        l3=i
        print(l3)  
  
g=print(l1+l2+l3)        
    


# In[191]:


print(l1)


# In[198]:


l1
l1


# In[187]:


l2


# In[188]:


l3


# In[196]:


q=l1+l2+l3


# In[197]:


for i in q:
    print(i,':',q.count(i))


# In[217]:


#q12 find out number of keys in dict element
g=[]
for i in l:
    if type(i)==dict:
        for j in i:
            print(j)
            g.append(j)
g
len(g)


# In[220]:


#q13 filter out all the string data
l=[[1,2,3,4,2,2,1,1],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,5]),{'k1':'sudh', 'k2':'ineuron', 'k3':'kumar', 3:6, 7:8},['ineuron','datascience']]
for i in l:
    if type(i)==set:
        ll=list(i)
        for j in ll:
            if type(j)==str:
                print(j)
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==str:
                print(j)        
    if type(i)==dict:
        for k,v in i.items():
            if type(k)==str:
                print(k)
            if type(v)==str:
                print(v)


# In[238]:


##q14 try to extract alphanumeric from list
for i in l:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==str:
                j.isalnum()

j.isalnum()


# In[243]:


k='hhjjh 988'
k.isalnum()


# In[75]:


#q15 try to find out multiplication of all numeric value in individual collection
l=[[1,2,3,4,2,2,1,1],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,5]),{'k1':'sudh', 'k2':'ineuron', 'k3':'kumar', 3:6, 7:8},['ineuron','datascience']]
mul=1
pro=1
product=1
multiplication=1
for i in l:
    if type(i)==list:
        for j in i:
            if type(j)==int:
                mul=mul*j
        print(mul)
for i in l:
    if type(i)==tuple:
        print(i)
        for j in i:
            if type(j)==int:           
                pro=pro*j
                print(pro)
for i in l:
    if type(i)==set:
        print(i)
        for j in i:
            if type(j)==int:
                product=product*j
                print(product)
for i in l:
    if type(i)==dict:
        print(i)
        for k,v in i.items():
            if type(k)==int and type(v)==int:
                multiplication=multiplication*(k*v)
        print(multiplication)        
                
        
                
                
        
        
    



# In[45]:


k=787
type(k)
    


# In[67]:


pro=1
k=[[1,12,5,6],['shanu','shekhar'],(22,33,44)]
for i in k:
    if type(i)==list:
        for j in i:
            if type(j)==int:
                pro=pro*j
                print(pro)    
        


# In[82]:


#q16 unwrap all items
new_l=[]
for i in l:
    if type(i)==list or type(i)==tuple or type(i)==set:
        for j in i:
            new_l.append(j)
new_l
for i in l:
    if type(i)==dict:
        for k,v in i.items():
            new_l.append(k)
            new_l.append(v)

new_l    


# In[ ]:





# In[ ]:




