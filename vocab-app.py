import json
import os
import random

DATA_FILE = 'vocab-data.json'


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def add_word(data):
    word = input("Enter word: ").strip()
    category = input("Enter category: ").strip()
    example = input("Enter example sentence: ").strip()

    data.append({
        "word": word,
        "category": category,
        "example": example
    })
    save_data(data)
    print(f"\n✅ '{word}' added successfully!\n")


def start_quiz(data):
    if not data:
        print("No words found. Please add words first.")
        return

    random.shuffle(data)
    for item in data:
        print(f"\nWORD: {item['word']}")
        guess = input("Which category does this word belong to? > ").strip()
        if guess.lower() == 'exit':
            print("Exiting quiz.")
            break
        if guess.lower() == item['category'].lower():
            print("✅ Correct!")
        else:
            print(f"❌ Wrong. Correct category: {item['category']}")
        print(f"Example: {item['example']}")

def show_random_words(data, count=5):
    if not data:
        print("No words found.")
        return

    print(f"\n--- {count} Random Words ---")
    random_words = random.sample(data, min(count, len(data)))
    for item in random_words:
        print(f"\nWORD: {item['word']}")
        input("Press Enter to see the category and example...")
        print(f"Category: {item['category']}")
        print(f"Example: {item['example']}")
        print("---------------------------")


def show_all_words(data):
    if not data:
        print("No words found.")
        return

    print("\n--- All Words ---")
    for i, item in enumerate(data, 1):
        print(f"{i}. {item['word']} | {item['category']} | {item['example']}")
    print("-----------------")


def main():
    data = load_data()

    while True:
        print("\n📘 IELTS Vocabulary Trainer")
        print("1. Add word")
        print("2. Start quiz")
        print("3. Show all words")
        print("4. Show random words")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_word(data)
        elif choice == '2':
            start_quiz(data)
        elif choice == '3':
            show_all_words(data)
        elif choice == '5':
            print("Good luck with your IELTS practice! 👋")
            break
        elif choice == '4':
            count = input("How many random words would you like to see? (default is 5): ").strip()
            if count.isdigit():
                show_random_words(data, int(count))
            else:
                print("Invalid input. Showing default 5 random words.")
                show_random_words(data)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()
