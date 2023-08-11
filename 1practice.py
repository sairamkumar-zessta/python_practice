def process_grade(grade):
    match grade:
        case 'A':
            print("Excellent")
        case 'B':
            print("Good")
        case 'C':
            print("Fair")
        case 'D':
            print("Needs Improvement")
        case _:
            print("Unknown Grade")

grade = 'e'
process_grade(grade)