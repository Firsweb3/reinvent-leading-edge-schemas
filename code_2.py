
def generate_random_data():
    random_string = 'Picture should life card.'
    random_number = 31

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Picture should life card.")
        print(f"Random Number: 31")

if __name__ == "__main__":
    main()
