# BMR CALCULATOR IN PYTHON

run = True
while run:
    print("-------------------------------------------------------------------------------------------------")
    print("TYPE THE INFORMATION REQUIRED IN ORDER TO CALCULATE YOUR BMR AS WELL AS YOUR MAINTENANCE CALORIES")
    print("-------------------------------------------------------------------------------------------------")

    # could add try catch blocks for possible user errors
    weight = int(input("Type your weight in kg: "))
    height = int(input("Type your height in cm: "))
    age = int(input("Type your age in years: "))
    sex = input("Sex, (type man/ male or woman/ female): ")

    def calculator(num1, num2, num3, num4):

        bmr = num1 + (num2 * weight) + (num3 * height) - (num4 * age)

        print("\nYour BMR is: " + str(round(bmr, 0)) + " calories")
        print("\nNow let's calculate the calories required to maintain your current weight")
        print("\n1)  Little to no exercise")
        print("2)  Light exercise (1-3 days per week)")
        print("3)  Moderate exercise (3-5 days per week)")
        print("4)  Heavy exercise (6-7 days per week)")
        print("5)  Very heavy exercise (twice per day etc.)")

        exercise_type = int(input("\nPlease type the number of your exercise type: "))

        if exercise_type == 1:
            maintain_calories = bmr * 1.2
        elif exercise_type == 2:
            maintain_calories = bmr * 1.375
        elif exercise_type == 3:
            maintain_calories = bmr * 1.55
        elif exercise_type == 4:
            maintain_calories = bmr * 1.725
        elif exercise_type == 5:
            maintain_calories = bmr * 1.9

        print("\nMaintenance calories: " + str(round(maintain_calories, 0)))

    if sex == "man" or sex == "MAN" or sex == "male" or sex == "MALE":
        calculator(88.362, 13.397, 4.799, 5.677)
    elif sex == "woman" or sex == "WOMAN" or sex == "female" or sex == "FEMALE":
        calculator(447.593, 9.247, 3.0987, 4.330)

    question = str(input("Do you want to calculate again? (type 'yes' or 'no'): "))
    if question == "no":
        run = False
