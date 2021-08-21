print("helloworld")
print("its me arif")
#okkk
# problem 3Given a string, display only those characters which are present at an even index number.
def even_numre(str):

    size=len(str)
    for i in range(0,size-1,2):
        print(f"{str[i]}")


num=input("please type here")
even_numre(num)

#Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
def removechar(str,num):
    size=len(str)
    if num<size:

        print(f"{str[num:]}")
    else:
        print("out of index")

String=input("enter something")
number=int(input("enter numbr  "))
removechar(String,number)

#Exercise 5: Given a list of numbers, return True if first and last number of a list is same
def first_andlast(list):
    first=list[0]
    last=list[-1]
    if (first == last):
        return True
    else:
        return False

list=[19,2,45,44,3,7,8,77,19,7]

print(f"result is :{first_andlast(list)}")


#Exercise 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
def divideby5(list):
    size=len(list)
    for i in range(size):
        if (list[i]%5==0):
            print(list[i])


list=[10,5,60,44,33,50,40]
divideby5(list)

# Return the count of sub-string “Emma” appears in the given string
def count(str):
    return str.count("Emma")

string=input("enter something")
print(count(string))


#type pyramid
for i in range(10):
    for x in range(i):
        print(i,end=" ")
    print("\n\n")
    #new problem