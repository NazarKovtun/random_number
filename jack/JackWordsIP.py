from collections import Counter


class JackWordsIP:
    """
    Practical use of the IP
    """
    @staticmethod
    def print() -> None:
        print("-" * 20)
        print("JackWordsIP.print()")

        with open("jack.txt", "r") as lines:
            letters_counts = Counter()
            unique_words = set()
            for line in lines:
                words = line.split()
                for word in words:
                    word = word.lower().strip(".")
                    if word not in unique_words:
                        unique_words.add(word)
                        letters_counts[word[0]] += 1
            first_letters = sorted(letters_counts.items(), key=lambda x: -x[1])
            print(first_letters)

        letter = first_letters[1][0]

        with open("jack.txt", "r") as lines:
            word_counts = Counter()
            for line in lines:
                words = line.split()
                for word in words:
                    word = word.lower().strip(".")
                    if word.startswith(letter):
                        word_counts[word] += 1
            words = sorted(word_counts.items(), key=lambda x: -x[1])
            print(words)