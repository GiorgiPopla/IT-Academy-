from random import randint

def list_generator(length):
    generated_list = []
    for _ in range(0,length):
        generated_list.append(randint(1,111))
    return generated_list


#shell sort მეთოდი რომელიც აჯგუფებს გარკვეულ რიცხვებს სიაში გარკვეული მანძილით ერთმანეთისგან და შედარების მერე ანაცვლებს მათ პოზიციას სიაში
a = list_generator(10)
def shell_sort(arr):
    gap = len(arr)//2 #მანძილი/დაშორება ელემენტების რომლითაც იწყებს ფუნქცია და შემდგომ ამცირებს 2ით
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i] #რიცხვი რომელსაც შედარებისთვის გამოვიყენებთ
            j = i
            while j >= gap and arr[j-gap] > temp: #აწყობს ელემენტებს რომლებიც უფრო დიდებია temp-ზე მარჯვნივ
                arr[j] = arr[j-gap]
                j = j-gap
            arr[j] = temp#მოცემული ელემენტის სიაში თავისი ადგილის მინიჭება
        gap = gap//2#შემდეგ ირეტაციაზე გადასვლა შემცირებული მანძილით
    return arr
arr = shell_sort(a)
print(arr)       



#used only for sorted list search
# a = [1,15,22,10,24,15]

# def binary_search(arr,element):
#     begin_index = 0
#     end_index = len(arr)-1
#     while begin_index <= end_index:
#         middle_point = begin_index + (end_index-begin_index)//2
#         middle_point_value = arr[middle_point]
#         if middle_point_value == element:
#             return middle_point
#         elif  element < middle_point_value:
#             end_index = middle_point - 1
#         else:
#             begin_index = middle_point + 1
#     return None
# print(a)
# print(binary_search(a,10))
#linear sort
# a = [1,5,12,3,6]
# def linear_search(arr,x):
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i
#     return -1
# print(linear_search(a,10))
#bubble sort
# def insertion_sort():
#     arr = list_generator(100)
#     indexing_lenght = range(1,len(arr))
#     for i in indexing_lenght:
#         value_to_sort = arr[i]
#         while arr[i-1] > value_to_sort and i >0:
#             arr[i],arr[i-1] = arr[i-1],arr[i]
#             i = i-1
#     print(insertion_sort)
#     return arr
# print(insertion_sort())

#
# my_list = list_generator(10)
# def quick_sort(arr):
#     length = len(arr)
#     if length <= 1:
#         return arr
#     else:
#         pivot = arr.pop()
#     items_greater = []
#     items_lower = []
#     for item in arr:
#         if item > pivot:
#             items_greater.append(item)
#         else:
#             items_lower.append(item)
#     return quick_sort(items_lower) + [pivot] +quick_sort(items_greater)
# print(my_list)
# print(quick_sort(my_list))


