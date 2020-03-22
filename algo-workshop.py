def get_even_numbers(x, stop, z):
    """
    Returns a list containing first 'x' even elements lower than 'stop'.
    Those elements must be divisible by 'z'. 
    """
    raw_list = []
    for i in range(1,(stop//2)):
        raw_list.append(2*i)
    # print(raw_list)

    list_sorted = []
    for element in raw_list:
        if element%z != 0:
            list_sorted.append(element)
    # print(list_sorted)

    for i in range(x):
        print(list_sorted[i])



def get_sum_of_greatest_elements(my_list, x):
    """
    Returns a single integer, which is a sum of 'x' biggest elements from 'my_list'
    i.e. Returns a sum of 3 biggest elements from [2, 18, 5, -11, 7, 6, 9]
    """
    pass

get_even_numbers(2, 15, 10)