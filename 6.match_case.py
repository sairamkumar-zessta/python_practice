def find_perfomance(grade):
    match grade:
        case 'O':
            print("Out standing")
        case 'A':
            print("Exellent")
        case 'B':
            print("Good")
        case 'C':
            print("Average")
        case _:
            print("Unknown")
find_perfomance("A")

    