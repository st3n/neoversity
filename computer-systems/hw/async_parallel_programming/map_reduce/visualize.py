import matplotlib.pyplot as plt


def visualize_top_words(word_counts, top_n=10):
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[
        :top_n
    ]

    words, counts = zip(*sorted_word_counts)

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color="skyblue")
    plt.xlabel("Words")
    plt.ylabel("Counts")
    plt.title("Top Words by Frequency")
    plt.xticks(rotation=45)
    plt.show()
