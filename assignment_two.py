import csv

# Fictional student records (all data is made up for this assignment)
students = [
    {"student_id": "STU001", "department": "Computer Science", "level": 100, "attendance_percentage": 92, "average_exam_score": 84},
    {"student_id": "STU002", "department": "Accounting", "level": 200, "attendance_percentage": 88, "average_exam_score": 76},
    {"student_id": "STU003", "department": "Computer Science", "level": 300, "attendance_percentage": 95, "average_exam_score": 91},
    {"student_id": "STU004", "department": "Business Administration", "level": 100, "attendance_percentage": 79, "average_exam_score": 68},
    {"student_id": "STU005", "department": "Mass Communication", "level": 200, "attendance_percentage": 85, "average_exam_score": 73},
    {"student_id": "STU006", "department": "Computer Science", "level": 400, "attendance_percentage": 97, "average_exam_score": 88},
    {"student_id": "STU007", "department": "Accounting", "level": 300, "attendance_percentage": 90, "average_exam_score": 81},
    {"student_id": "STU008", "department": "Business Administration", "level": 200, "attendance_percentage": 82, "average_exam_score": 79},
    {"student_id": "STU009", "department": "Mass Communication", "level": 100, "attendance_percentage": 76, "average_exam_score": 65},
    {"student_id": "STU010", "department": "Computer Science", "level": 200, "attendance_percentage": 89, "average_exam_score": 86},
]

# Save the dataset as a CSV file that can be opened in Excel
filename = "fictional_student_dataset.csv"
fieldnames = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score",
]

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
        extrasaction="ignore"
    )
    writer.writeheader()

    for student in students:
        writer.writerow({
            "Student ID": student["student_id"],
            "Department": student["department"],
            "Level": student["level"],
            "Attendance Percentage": student["attendance_percentage"],
            "Average Examination Score": student["average_exam_score"],
        })

print(f"Dataset created successfully: {filename}")
print(f"Number of student records: {len(students)}")
