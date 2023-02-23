# CS 175L
# Raul Cortinas
# 2/23/2023

def letter_grade(test_score):
    if test_score >= 90:
        return "A"
    elif test_score >= 80:
        return "B"
    elif test_score >= 70:
        return "C"
    elif test_score >= 60:
        return "D"
    else:
        return "F"

def print_scores(test_scores):
    test_number = 0
    for test_score in test_scores:
        test_number += 1
        grade = letter_grade(test_score)
        print("Score", test_number, f'{test_score:>26}', f'{grade:>23}')


def main():
    ask = True
    while ask:

        number_of_scores = (int(input('\nEnter the number of scores you will like to input: ')))
        print()

        test_scores = []
        for x in range(number_of_scores):
            test_score = int(input("Enter a test score: ",))
            test_scores.append(test_score)

        print()
        print("Score", f'{"Numeric Score:":>25}', f'{"Letter Grade: ":>25} ')
        print("-----------------------------------------------------------")

        print_scores(test_scores)
        average_score = sum(test_scores) / len(test_scores)
        print('\nAverage is: ', f'{average_score:>23}', f'{letter_grade(average_score):>21}')

        ask_more = str(input("\nWould you like another calculation? "))

        if ask_more.lower() == 'yes' or ask_more.lower() == 'y':
            ask = True
        elif ask_more.lower() == 'no' or ask_more.lower() == 'n':
            ask = False
            print("Have a nice day!")
        else:
            print("Please enter yes / y or no / n")
            ask = input("Would you like another calculation?")

if __name__ == '__main__':
    main()
