<<<<<<< HEAD
even_list= []

def filter_even(user_provided_num):
    for num in range(1, user_provided_num+1):
        [even_list.append(num) if num%2 ==0 else even_list.append(num)]

any_num =int(input("provide any number:-->"))
filter_even(any_num)

print(f"now the even_list is:{even_list}")
=======
odd_list = []


def filter_odd(user_provided_num):
    for num in range(1, user_provided_num+1):
        [odd_list.append(num)if num %2 ==0 else odd_list.append(num)]

any_num = int(input("please provide any number :-->"))
filter_odd(any_num)

print(f"the odd_list is:{odd_list}")

>>>>>>> 59866076c89279270aebd779b0dc4447b8a3f578
