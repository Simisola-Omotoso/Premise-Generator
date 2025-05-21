def main():
    genre = get_genre()
    keywords = get_keywords()
    premise = generate_premise(genre, keywords)

    print("Ideas: ")
    print(premise)

    save_to_file(premise)

if __name__ == "__main__":
    main()