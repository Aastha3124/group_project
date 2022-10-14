odd_list = []


def filter_odd(user_provided_num):
    for num in range(1, user_provided_num+1):
        [odd_list.append(num)if num %2 ==0 else odd_list.append(num)]

any_num = int(input("please provide any number :-->"))
filter_odd(any_num)

print(f"the odd_list is:{odd_list}")

