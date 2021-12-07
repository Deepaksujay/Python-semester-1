# myarray=[0,2,3,1,5,6]
# def length(arrayss):
#     for j in arrayss:
#         j=j+1
#     return j-1
# def check_array(arrays):
#     l=0
#     for i in range(0,length(arrays)-1):
#         if (arrays[i]<=arrays[i+1]):
#             l=l+1
#         else:
#             l=0
#             break

#     if (l==0):
#         print("not in ascending order")
#     else:
#         print("in  ascending order")

# check_array(myarray)

string='chegg'
for c in string[::-1]:
    print(c, end="")
    string=string.upper()


