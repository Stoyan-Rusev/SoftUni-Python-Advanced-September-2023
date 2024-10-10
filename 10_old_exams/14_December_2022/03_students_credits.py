def students_credits(*courses_info):
    credits_needed = 240
    total_credits = 0
    passed_courses = []
    result = ''

    for current_course_info in courses_info:
        course_name, course_credits, max_test_points, student_points = current_course_info.split('-')
        course_credits = int(course_credits)
        max_test_points = int(max_test_points)
        student_points = int(student_points)
        percents = student_points / max_test_points
        credits_gained = percents * course_credits
        total_credits += credits_gained
        passed_courses.append((course_name, credits_gained))

    if total_credits >= credits_needed:
        result += f'Diyan gets a diploma with {total_credits:.1f} credits.\n'

    else:
        result += f'Diyan needs {float(credits_needed - total_credits):.1f} credits more for a diploma.\n'

    sorted_courses = sorted(passed_courses, key=lambda kvp: -kvp[1])
    for course, credits_ in sorted_courses:
        result += f'{course} - {credits_:.1f}\n'
    result = result.strip()
    return result


print(students_credits("Computer Science-1000-200-100"))
print()

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )
# print()
# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
# print()
# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
