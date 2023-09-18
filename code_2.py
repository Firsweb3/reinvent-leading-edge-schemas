
def generate_random_data():
    random_string = 'Recognize itself fund too.'
    random_number = 26

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Recognize itself fund too.")
        print(f"Random Number: 26")

if __name__ == "__main__":
    main()
