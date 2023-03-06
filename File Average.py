#CS 175L
#Raul Cortinas
#3/2/2023


def main():

    try:
        numbers_file = open('/Users/rcurt17/Downloads/numbers.txt', 'r')

        counter = 0

        total = 0

        for nums in numbers_file:
    
            counter += 1

            print('I read in ', str(counter), end='')
            print('number(s) Current number is:' , float(nums), end='')
            print(' Total is: ', end='')
            total += float(nums)
            print(total)

        avg = total / counter
        print('Average is: ',  avg)

    except IOError:
        print("Could not find file, please make sure correct file name is being opened")

    except ValueError:
        print("\nCheck file for any strings or non integer characters")


if __name__=='__main__':
    main()
