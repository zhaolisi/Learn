#coding=utf-8
#二分查找法(有序列表)
from Sort import QuickSort
def BinaryChop(mylist,data):
    first=0
    last=len(mylist)-1
    while first<=last:
        mid=(first+last)/2
        if mylist[mid]>data:
            last=mid-1
        elif mylist[mid]<data:
            first=mid+1
        else:
            return True
    return False
if __name__ == "__main__":
    mylist=[49,38,65,97,76,3,27,49]
    QuickSort(mylist, 0, len(mylist) - 1)
    if BinaryChop(mylist,15):
        print("The data was found")
    else:
        print ("No such data in the list")

