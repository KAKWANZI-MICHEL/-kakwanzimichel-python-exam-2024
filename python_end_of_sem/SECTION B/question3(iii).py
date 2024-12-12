
def grade_student(marks):  
    if marks >= 90:  
        return 'A'  
    elif marks >= 80:  
        return 'B'  
    elif marks >= 70:  
        return 'C'  
    elif marks >= 60:  
        return 'D'  
    else:  
        return 'F'  
grade = grade_student(85)  
print(grade)  

def test_function(marks):  
    grade = grade_student(marks)  
    print(f'Grade: {grade}')  

test_function(85)