'''
def the_function():
    get all 3 digit numbers between 900 and 999, store those numbers
    for numbers in range
        start with highest number and multiply by each number less than that number
            test if product is palindrome
            if palindrome store in something
        compare all palindromes stored to find largest palindrome
'''

def is_palindrome(num):
    reverse_num = str(num)[::-1]
    if num == int(reverse_num):
        return True
    else:
        return False 


def get_max_palindrome():
    products = []

    for num1 in range(999, 900, -1):
        for num2 in range(num1, 900, -1):
            product = num1 * num2
            if is_palindrome(product) is True:
                products.append(product)
    return max(products)

            
        

        
        