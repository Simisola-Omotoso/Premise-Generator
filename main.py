def get_user_input():
    """
    Gathers user input

    Parameters:
        genre (str): selected genre
        keywords (str): comma-separated string of keywords or phrases

    Returns:
        str: story premise using the inputs
    """

    # Asks for genre input
    genre = input("Enter genre: ")

    # Asks for keyword input
    keywords = input("Enter keywords (separate by commas): ")

    # Returns genre & keywords
    return genre, keywords

def main():
    """
    Prints way to premise

    Parameters:
        genre (str), keywords (str): genre & keywords pair
        premise (str): generated story idea
    """

    # Prints title of project
    print("Premise Generator")

    # Defines genre & keywords as their inputs
    genre, keywords = get_user_input()

    # Indicates application generating premise
    print("Generating... ")

    # Calls 
    premise = generate_premise(genre, keywords)
    print("Story idea: ")
    print(premise)

    save_to_file(premise)

if __name__ == "__main__":
    main()