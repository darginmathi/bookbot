def main():
    with open("books/frankenstein.txt") as f:
        print("--- Begin report of books/frankenstein.txt ---")
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"{word_count} words found in the document")

        letters = {}
        words_lower = file_contents.lower()
        for i in words_lower:
            if i.isalpha():
                if i not in letters:
                    letters[i] = 1
                else:
                    letters[i] += 1
        letter_list = []
        for i, j in letters.items():
            letter_list.append({"char": i,"num": j})
        letter_list.sort(reverse=True, key=lambda x: x["num"])
        for i in letter_list:
            print(f"The '{i['char']}' character was found {i['num']} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()