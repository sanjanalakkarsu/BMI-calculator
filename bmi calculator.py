import math

def bmi_calculator(height,weight):
    bmi = weight/(math.pow(height,2))
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal"
    elif 25 <= bmi < 30:
        return "overweight"
    else:
        return "obese"
    
def main():
    height = float(input("Enter your height in meters:"))
    weight = float(input("Enter your weight in kilograms:"))

    bmi = bmi_calculator(height,weight)
    category = bmi_category(bmi)

    if bmi:
        print(f"Your bmi is {bmi:.2f}, which comes under the category of {category}")
    else:
        print("Unable to calculate bmi")

if __name__ == "__main__":
    main()