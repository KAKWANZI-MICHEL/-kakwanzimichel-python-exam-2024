
def calculate_operations(num1, num2):
    # Calculating sum
    sum_result = num1 + num2
    
    # Calculating difference
    difference_result = num1 - num2
    
    # Calculating product
    product_result = num1 * num2
    
    # Calculating quotient 
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "undefined" 
    
    return {
        'sum': sum_result,
        'difference': difference_result,
        'product': product_result,
        'quotient': quotient_result
    }

