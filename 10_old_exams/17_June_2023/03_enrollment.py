def gather_credits(credits_needed, *args):
    collected_credits = 0
    passed_courses = []

    for current_pair in args:
        if collected_credits >= credits_needed:
            break
        course_name = current_pair[0]
        course_credits = current_pair[1]

        if course_name in passed_courses:
            continue
        collected_credits += course_credits
        passed_courses.append(course_name)

    if collected_credits >= credits_needed:
        return f'Enrollment finished! Maximum credits: {collected_credits}.\nCourses: {", ".join(sorted(passed_courses))}'
    return f'You need to enroll in more courses! You have to gather {credits_needed - collected_credits} credits more.'


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Fundamentals", 100),
    ("Advanced", 10),
    ("Web", 30)
))

# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
# print()
#
# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
# print()
#
# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))
