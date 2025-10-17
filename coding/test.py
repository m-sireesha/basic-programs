# check_key
# first three chars
# count vowels consonents
# leap year
# multiplication
# find_peak
# fibonnacci
# remove vowels
# diamond
# second second_largest
# amstrong
# remove duplicate
# missing and repeated numbers
# bubble sort
# replace vowels with *
# re arrange negatives first
 
def check_key(d,key):
    if key in d:
        print(d[key])
    else:
        print("key not found")
data={"name":"alice","age":"30"}
check_key(data,"name")

def first_three_char(s):
    print(s[:3])
first_three_char("python")

def count_vowels_consonents(s):
    vowels="aeiouAEIOU"
    v_count=0
    c_count=0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count+=1
            else:
                c_count+=1
    return v_count,c_count
v,c=count_vowels_consonents("hello world")
print("vowels :",v,"consonents :",c)

def leap_year(year):
    if (year % 400 ==0) and (year%4==0 and year % 100 !=0):
        return True
    return False
print(leap_year(2023))

def multiplication(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
multiplication(5)

def find_peak(arr):
    n=len(arr)
    if n ==1:
        return arr[0]
    if arr[0]>arr[1]:
        return arr[0]
    if arr[n-1]>arr[n-2]:
        return arr[n-1]
    
    for i in range(1,n-1):
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
            return arr[i]
    return None
# Example
print(find_peak([1, 3, 20, 4, 1, 0]))  # 20
print(find_peak([10, 20, 15]))         # 20
print(find_peak([5]))                  # 5 (edge case single element)
print(find_peak([10, 5, 2])) 

def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end="")
        a,b=b,a+b
fibonacci(6)

def remove_vowels(s):
    vowels="aeiouAEIOU"
    result=""
    for ch in s:
        if ch not in vowels:
            result+=ch
    return result
print()
print(remove_vowels("python"))

def diamond(rows):
    for i in range(rows):
        print(" "*(rows-i-1)+"*"*(2*i-1))
    for i in range(rows-2,-1,-1):
          print(" "*(rows-i-1)+"*"*(2*i-1))
diamond(5)
        
def second_largest(nums):
    if len(nums)<2:
        return None
    largest=nums[0]
    second=None
    for x in nums[1:]:
        if x>largest:
            second=largest
            largest=x
        elif x!=largest and (second is None or x>second):
            second=x
    return second
print(second_largest([1,5,4,3,2]))

def amstrong(num):
   s=str(num)
   n=len(s)
   total=0
   for ch in s:
        digit=int(ch)
        total+=digit**n
   return total==num
print(amstrong(153))

def remove_duplicates(lst):
    result=[]
    for ch in lst:
        if ch not in result:
            result.append(ch)
    return result
lst=[1,1,2,2,2,3,4,5,5,5,6]
print(remove_duplicates(lst))


arr = [1, 2, 3, 4, 4, 5, 6, 6, 8, 10]
n=len(arr)
count=[0]*(n+1)

for num in arr:
    count[num]+=1
    
missing=[]
repeated=[]

for i in range(1,n+1):
    if count[i]==0:
        missing.append(i)
    elif count[i]>0:
        repeated.append(i)
        
print("missing number :",missing)
print("repeated number :", repeated)

def bubble_sort(lst):
    n=len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
print(bubble_sort([5, 3, 8, 6, 2]))

def replace(str):
    vowels="aeiouAEIOU"
    result=""
    for ch in s:
        if ch in vowels:
            result+='*'
        else:
            result+=ch
    return result
s=input("enter string")
print(replace(s))

def negatives_first(nums):
    negatives=[]
    positives=[]
    for num in nums:
        if num<0:
            negatives.append(num)
        else:
            positives.append(num)
    return negatives+positives
arr = [12, -11, -13, -5, 6, -7, 5, -3, -6]
print(negatives_first(arr))