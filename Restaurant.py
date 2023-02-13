reask = True
while reask == True:
    Vegetarian = False
    Vegan = False
    GlutenFree = False
    Vegetarian = input("Is anyone in your party vegetarian?: ")
    VegetarianAnswer = Vegetarian.lower()
    if VegetarianAnswer == 'yes':
        Vegetarian = True
    elif VegetarianAnswer == 'no':
        Vegetarian = False
    else:
        print("Please enter yes or no")

    Vegan = input("Is anyone in your party vegan?: ")
    VeganAnswer = Vegan.lower()
    if VeganAnswer == 'yes':
        Vegan = True
    elif VeganAnswer == 'no':
            Vegan = False
    else:
        print("Please enter yes or no")

    GlutenFree = input("Is anyone in your party gluten free?: ")
    GlutenAnswer = GlutenFree.lower()
    if GlutenFree == 'yes':
        GlutenFree = True
    elif GlutenFree == 'no':
            GlutenFree = False
    else:
        print("Please enter yes or no")

    print("Here are your restaurant choices:\n")
    if not Vegetarian and not Vegan and not GlutenFree:
        print("Joe's Gourmet Burgers")
    if not Vegan and not GlutenFree:
            print("Mama's Fine Italian")
    if not Vegan:
        print("Main Street Pizza")
    print("CornerCafe")
    print("Chef's Kitchen")


    input = input("\nWould you like to go again? ")
    inputAnswer = input.lower()
    if inputAnswer == "yes":
        reask = True
    elif inputAnswer == "no":
        reask = False
        print("\nHave a nice day!")


