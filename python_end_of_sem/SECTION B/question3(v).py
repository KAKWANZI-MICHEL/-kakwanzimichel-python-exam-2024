def grade_student(marks):  
    if not isinstance(marks, (int, float)):  
        return "Invalid input"  
    
    if marks >= 90:  
        return 'A - Excellent'  
    elif marks >= 80:  
        return 'B - Excellent'  
    elif marks >= 70:  
        return 'C - Good'  
    elif marks >= 60:  
        return 'D - Satisfactory'  
    else:  
        return 'F - Needs Improvement'  
result = grade_student(85)  
print(result)  

invalid_result = grade_student("eighty")  
print(invalid_result)  