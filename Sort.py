#coding=utf-8

#冒泡排序
def bubble_sort(Mylist):
    n=len(Mylist)-1
    for i in range(0,n):
        for j in range(0,n-i):
            if Mylist[j]>=Mylist[j+1]:
                Mylist[j],Mylist[j+1]=Mylist[j+1],Mylist[j]
#快速排序

def QuickSort(Mylist,start,end):
    if start<end:
        i,j=start,end
        base=Mylist[i]
        while i<j:
            while (i<j and Mylist[j]>=base):
                j -= 1
            Mylist[i]=Mylist[j]
            while (i<j and Mylist[i]<=base):
                i += 1
            Mylist[j] = Mylist[i]
        Mylist[i]=base
        QuickSort(Mylist,start,i-1)
        QuickSort(Mylist,j+1,end)

#给指定列表中的奇数偶数调换位置，偶数在前，奇数在后
def OddEvenSort(MyList):
    i=0
    j=len(MyList)-1
    while i<j:
        while i<j and MyList[i]%2 == 0:
            i+=1
        Mylist[i],Mylist[j]=Mylist[j],Mylist[i]
        while i<j and MyList[j]%2 != 0:
            j-=1
        Mylist[i], Mylist[j] = Mylist[j], Mylist[i]

if __name__ == "__main__":
    Mylist=[49,38,65,97,76,3,27,49]
    bubble_sort(Mylist)
    print Mylist
    QuickSort(Mylist,0,len(Mylist)-1)
    print Mylist
    OddEvenSort(Mylist)
    print Mylist