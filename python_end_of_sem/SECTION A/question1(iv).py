
student_info = {'name':'Aice', 'age':20,'grade':'A'} 
student_info['age'] = 26 
student_info['city'] = 'Kampala'  
student_info['grade'] = 'A'
print(student_info)  

original_dict = {'city': 'kampala'}  
new_dict = {key: value for key, value in original_dict.items()}  
print(new_dict)  



