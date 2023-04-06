print()
world_series = open('/Users/rcurt17/Desktop/CS175Work/WorldSeriesWinners.txt', 'r')

world_series_winners = []
for g in world_series:
    g = g.rstrip('\n')
    world_series_winners.append(g)

x = True
while x:
    count = 0

    phrase = str(input("Enter the name of a team: "))
    once = []
    broad_search = [line for line in world_series_winners if phrase.lower() in line.lower()]

    for g in broad_search:
        if g not in once:
            once.append(g)

    for line in once:
        print()
        print(line)
        count += 1

    count_specific = 0

    phrase_specific = str(input("\nEnter the name of the team you would like to focus on: "))

    with open('WorldSeriesWinners.txt', 'r') as file:

        for line in file:

            line = line.rstrip('\n')

            if phrase_specific.upper() in line.upper():
                count_specific += 1

    print(f"\nThe team '{phrase_specific}' appears {count_specific} times in the file '{'WorldSeries.txt'}'.")

    y = True
    while y:
        ask = input("\nWould you like to continue? (y or n) ")
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
