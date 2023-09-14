import random

# Load Wu-Tang name components from a text file
def load_name_components(filename):
    with open(filename, 'r') as file:
        components = [line.strip() for line in file]
    return components

# Generate a Wu-Tang name
def generate_wu_tang_name(name, components):
    random_component = random.choice(components)
    wu_tang_name = name + " " + random_component
    return wu_tang_name

def main():
    # Load Wu-Tang name components from a text file
    components = load_name_components("wu_tang_name_components.txt")

    # Ask for the user's name
    user_name = input("Enter your name: ")

    # Generate and print the Wu-Tang name
    wu_tang_name = generate_wu_tang_name(user_name, components)
    print("Your Wu-Tang name is:", wu_tang_name)

if __name__ == "__main__":
    main()
