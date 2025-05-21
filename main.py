def get_user_input():
    genre = input("Enter genre: ")
    keywords = input("Enter keywords (separate by commas): ")
    return genre, keywords

def main():
    print("Premise Generator")
    genre, keywords = get_user_input()
    print("Generating... ")
    premise = generate_premise(genre, keywords)
    print("Story idea: ")
    print(premise)

    save_to_file(premise)

if __name__ == "__main__":
    main()