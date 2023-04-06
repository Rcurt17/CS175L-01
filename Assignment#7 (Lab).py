print()
world_series = open('/Users/rcurt17/Desktop/CS175Work/WorldSeriesWinners.txt', 'r')

x = True
while x:
    count = 0

    phrase = str(input("Enter the name of a team: "))

    with open('WorldSeriesWinners.txt', 'r') as file:

        for line in file:
            line = line.rstrip('\n')
            if phrase.upper() in line.upper():
                print(line)
                count += 1

    count_specific = 0

    phrase_specific = str(input("Enter the name of the team you would like to focus on: "))

    with open('WorldSeriesWinners.txt', 'r') as file:

        for line in file:
            line = line.rstrip('\n')
            if phrase_specific.upper() in line.upper():
                count_specific += 1

    print(f"The team '{phrase_specific}' appears {count_specific} times in the file '{'WorldSeries.txt'}'.")

    y = True
    while y:
        ask = input("Would you like to continue? (y or n) ")
        if ask.lower() == 'y' or ask.lower() == 'yes':
            x = True
            y = False
        elif ask.lower() == 'n' or ask.lower() == 'no':
            x = False
            y = False
            print('Goodbye!')
        else:
            print("Enter y or n")
            y = True
