
def count_common_elements():

    list1=[1,2,3,4,5,6,7,8,9]
    list2=[1,1,2,23,43,45,5,56,8]

    len1=len(list1)
    len2=len(list2)
    k=0
    n=max(len1,len2)


    for i in range(n):
        for j in range(n):
            if(list1[i]==list2[j]):
                k=k+1


    print(f"no of common elements are:{k} ")


def main():
    count_common_elements()

if __name__ == "__main__":
    main()