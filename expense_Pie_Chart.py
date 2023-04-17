import matplotlib.pyplot as plt
import numpy as np

def main():

    number_list = []
            
    bills = open('/Users/rcurt17/Downloads/expenses.txt', 'r')

    lines = bills.readlines()

    for x in lines:
        try:
            m = x.split('\t')
            num = m[1]
            num = num.strip('\n')
            num = int(num)
            number_list.append(num)
        except ValueError:
            break

    array_list = np.array(number_list)

    bills_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']


    plt.pie(array_list, labels=bills_labels)


    plt.title('Monthly Expenses')
            

    plt.show()


if __name__ == '__main__':
    main()
