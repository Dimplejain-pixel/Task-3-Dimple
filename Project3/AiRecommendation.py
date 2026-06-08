print("=" * 60)
print("         AI RECOMMENDATION SYSTEM")
print("=" * 60)

name = input("Enter Your Name: ")

recommendations = {
    "technology": [
        "Python Programming",
        "Machine Learning",
        "Web Development",
        "Data Science"
    ],
    "sports": [
        "Cricket",
        "Football",
        "Badminton",
        "Basketball"
    ],
    "music": [
        "Classical Music",
        "Pop Music",
        "Rock Music",
        "Instrumental Music"
    ],
    "movies": [
        "Interstellar",
        "3 Idiots",
        "Inception",
        "The Dark Knight"
    ],
    "books": [
        "Atomic Habits",
        "Rich Dad Poor Dad",
        "The Alchemist",
        "Think and Grow Rich"
    ]
}

print(f"\nWelcome {name}!")

while True:

    print("\nAvailable Categories:")
    for category in recommendations:
        print("-", category.capitalize())

    user_interest = input(
        "\nEnter your interest (or type 'exit' to quit): "
    ).lower().strip()

    if user_interest == "exit":
        print("\nThank You For Using AI Recommendation System!")
        break

    if user_interest in recommendations:

        print("\nAnalyzing Preferences...")
        print("\nRecommended Items:\n")

        for i, item in enumerate(
            recommendations[user_interest],
            start=1
        ):
            print(f"{i}. {item}")

        print("\nAI Confidence Score: 95%")
        print("Recommendation Generated Successfully!")

        rating = input(
            "\nDid you like these recommendations? (yes/no): "
        ).lower()

        if rating == "yes":
            print("Great! Glad you liked them.")
        else:
            print("Thank you for your feedback.")

    else:
        print(
            "\nSorry! No recommendations available for this category."
        )

print("\nHave a Nice Day!")