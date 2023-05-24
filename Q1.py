# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 21:23:46 2022

@author      :  Avinash Mahala
@Student ID  :  1002079433
"""

#All imports goes below
import random
import timeit
import copy
import matplotlib.pyplot as plt
#All imports ends here


"""Input Number List Generator
(List Elements To be generated using Random Function)
Input  :  number of elements "N" to be generated & Returned.
Output :  list returning a list of "N" random numbers 
"""

def randomNumListGen(rStart,rEnd,numOfElem):
    ranNumList=random.sample(range(rStart,rEnd), numOfElem)
    
    """
    Uncomment This block if you want to print the ramdomListGenerated
    ranNumListInString=' '.join(str(s) for s in ranNumList)
    print("Random List Generated--> "+ranNumListInString)
    """
    return ranNumList


#Insertion Sort Function starts
def insertionSort(toSort):
    for i in toSort:
        #print(i)
        j=toSort.index(i)
        while j>0:
            if toSort[j-1]>toSort[j]:
                'toSort[j-1],toSort[j]=toSort[j],toSort[j-1]'
            else:
                break
            j=j-1
            
#Insertion Sort Function ends


#Merge Sort Starts Here
def merge(listToSort, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
 
    leftList = [0] * (n1)
    rightList = [0] * (n2)

    for i in range(0, n1):
        leftList[i] = listToSort[left + i]
 
    for j in range(0, n2):
        rightList[j] = listToSort[mid + 1 + j]
 
    i = 0
    j = 0
    k = left
 
    while i < n1 and j < n2:
        if leftList[i] <= rightList[j]:
            listToSort[k] = leftList[i]
            i += 1
        else:
            listToSort[k] = rightList[j]
            j += 1
        k += 1

    while i < n1:
        listToSort[k] = leftList[i]
        i += 1
        k += 1

    while j < n2:
        listToSort[k] = rightList[j]
        j += 1
        k += 1
 
def mergeSort(listToSort, left, right):
    if left < right:
        mid = left+(right-left)//2
 
        mergeSort(listToSort, left, mid)
        mergeSort(listToSort, mid+1, right)
        merge(listToSort, left, mid, right)




def mergeMain(l):
    mergeSort(l, 0, len(l)-1)

    
#Merge Sort ends Here


#Main Function starts here
def main():
    dataSize=range(10,100,20)
    time_list_ins=[]
    time_list_merge=[]
    
    count=[]
    
    for ds in dataSize:
        r=randomNumListGen(1,500,ds)
        s=copy.deepcopy(r)
        start = timeit.default_timer()
        insertionSort(r)
        stop = timeit.default_timer()
        total_time_ins = (stop - start)
        time_list_ins.append(total_time_ins)
        
        
        start = timeit.default_timer()
        mergeMain(s)
        stop = timeit.default_timer()
        total_time_merge = (stop - start)
        time_list_merge.append(total_time_merge)
        count.append(ds)
        if total_time_merge<total_time_ins:
            break
        
    
    print("----For Insertion Sort List of Time of Execution in Seconds----")
    print(time_list_ins)
    print("\n")
    print("----For Merge Sort List of Time of Execution in Seconds----")
    print(time_list_merge)

    x1 = count
    y1 = time_list_ins
    plt.plot(x1, y1, label = "Insertion Sort")
  
    x2 = count
    y2 = time_list_merge
    plt.plot(x2, y2, label = "Merge Sort")
    plt.xlabel('Input List Size')
    plt.ylabel('Execution Time [ In Seconds ]')
    plt.title('Insertion Sort Vs Merge Sort')
    
    plt.legend()
    plt.show()
#Main Function ends here



if __name__ == "__main__":
    main()





