
def generate_random_data():
    random_string = 'Their power field TV.'
    random_number = 89

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Their power field TV.")
        print(f"Random Number: 89")

if __name__ == "__main__":
    main()
