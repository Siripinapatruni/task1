def calculate_bmi(weight_kg, height_m):
    """Calculate BMI (Body Mass Index)"""
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    """Return the BMI category based on predefined WHO categories"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI calculator!")
    print("Please enter your weight (in kilograms) and height (in meters).")

    # Input weight from user
    while True:
        try:
            weight_kg = float(input("Enter your weight in kilograms: "))
            if weight_kg <= 0:
                print("Please enter a valid weight (greater than zero).")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for weight.")

    # Input height from user
    while True:
        try:
            height_m = float(input("Enter your height in meters: "))
            if height_m <= 0:
                print("Please enter a valid height (greater than zero).")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for height.")

    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)

    # Determine BMI category
    bmi_category = get_bmi_category(bmi)

    # Display BMI and category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"This is considered: {bmi_category}")

if __name__ == "__main__":
    main()
