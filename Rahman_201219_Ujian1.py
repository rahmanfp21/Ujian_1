### Rahman Fitra Perdana

# Soal 1 
def Hashtag(string):
    list_string = string.split()
    # print(list_string)
    list_new = []
    for i in list_string:
        list_new.append(i.capitalize())
    list_char = list(string)
    count_string = len(list_char)
    # print(count_string)
    # z = "#"
    z = "#"

    if count_string > 0:
        for i in list_new:
            if i != " ":
                z += i
    else:
        return print("False")
    list2 = list(z)
    # print(list2)
    print(len(list2))
    if len(list2) > 140:
        return print("False")
    else:
        return print(z)

Hashtag(" Hello there how are you doing")
Hashtag(" Hello World " )
Hashtag("")
Hashtag("            opq    uvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")

# Soal 2
def create_phone_number(number):
    phone = ""
    zip = ""
    first_line = ""
    last_line = ""
    for i in number:
        if len(number) != 10:
            return print("Jumlah angka harus 10")
        elif i < 0 or i > 9:
            return print("Angka tidak boleh kurang dari 0 atau lebih dari 9")
    for i in number:
        phone += str(i)
    for i in range(0,3):
        zip += str(number[i])
    for i in range(3,6):
        first_line += str(number[i])
    for i in range(6,10):
        last_line += str(number[i])
    join = '"({}) {}-{}"'.format(zip,first_line,last_line)
    print(join)

create_phone_number([0,2,1,8,6,5,0,2,1,7])
create_phone_number([0,2,1,8,6,5,0,2,1,11])
create_phone_number([0,2,1,8,6,5,0,2,1])
create_phone_number([0,2,1,8,6,5,0,2,1,-7])

# Soal 3
def sort_odd_even(num):
    new_list = num
    # print(new_list)
    list_even = [i for i in num if i % 2 == 0 ]
    list_odd = [i for i in num if i % 2 != 0 ]
    # print(num)
    for i in range(len(list_odd)-1):
        for j in range(len(list_odd)-1):
            if list_odd[j] > list_odd[j+1]:
                a = list_odd[j]
                list_odd[j] = list_odd[j+1]
                list_odd[j+1] = a
    for i in range(len(list_even)-1):
        for j in range(len(list_even)-1):
            if list_even[j] < list_even[j+1]:
                a = list_even[j]
                list_even[j] = list_even[j+1]
                list_even[j+1] = a
    # print(list_even)
    # print(list_odd)
    join_list = []
    a = 0
    b = 0
    for i in range(len(num)):
        if num[i] % 2 != 0:
            join_list.append(list_odd[a])
            a += 1
        else:
            join_list.append(list_even[b])
            b += 1
    print(join_list)

sort_odd_even([5,3,2,8,1,4])
sort_odd_even([1,4,2,5,3,7])
sort_odd_even([6,7,2,5,3,8])

# Soal 4
def hollowTriangle(n):
    z = ""
    x = n-1
    for i in range(n):
        if i == n-1:
            z += "#" * (2*n-1)
        else:
            for j in range(2*n-1):
                if j == x+i or j == x-i:
                    z += "#"
                else:
                    z += "_"
            z += "\n"
    print(z)

hollowTriangle(6)
