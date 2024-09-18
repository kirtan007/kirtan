# Define a Car class
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"

# Define a main function
def main():
    # Ask the user for input
    print("Enter the car brand (if available, otherwise press Enter):")
    brand = input().strip().capitalize()
    if brand:
        print("Brand is available")
    else:
        brand = "Not available"

    print("Enter the car model name (if available, otherwise press Enter):")
    model = input().strip().capitalize()
    if model:
        print("Model is available")
    else:
        model = "Not available"

    print("Enter the car color (if available, otherwise press Enter):")
    color = input().strip().capitalize()
    if color:
        print("Color is available")
    else:
        color = "Not available"

    # Create a Car object
    my_car = Car(brand, model, color)

    # Print the car details
    print("My car is a:", my_car)

# Call the main function
if __name__ == "__main__":
    main()