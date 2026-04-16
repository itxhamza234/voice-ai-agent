students = [
    {"name": "Hamza", "math": 99, "english": 88, "science": 80},
    {"name": "Ali", "math": 99, "english": 87, "science": 88}
]

for student in students:
    total = student["math"] + student["english"] + student["science"]
    average = total / 3
    
    if average >= 50:
        result = "PASS ✅" 
    else:
        result = "FAIL ❌"
    
    # Print statement loop ke andar hona chahiye taake har student ka result dikhe
    print(f"Name: {student['name']} | Average: {average:.2f} | Result: {result}")