even_list= []

def filter_even(user_provided_num):
    for num in range(1, user_provided_num+1):
        [even_list.append(num) if num%2 ==0 else even_list.append(num)]

any_num =int(input("provide any number:-->"))
filter_even(any_num)

print(f"now the even_list is:{even_list}")
