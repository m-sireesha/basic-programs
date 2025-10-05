


def count_upto(n):
    i=0
    while i<=n:
        yield i
        i+=1
    


for num in count_upto(5):
    print(num)