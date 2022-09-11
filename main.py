import wordcloud
from matplotlib import pyplot as plt


file1 = open("text/1.txt", encoding="utf-8")
textfile = file1.read()
file1.close()
textfile = textfile.lower()


def calculate_frequencies():
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = ["!", "-", ";", ":", "\'", "\"", ".", ",", "?", "&", "(", ")"]
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just", "like", "jaise", "dekh", "mere",
                           "mein", "main", "one", "ke", "ye", "tere", "nahi", "na", "haan", "bhi", "tu", "up", "mai", "pe",
                           "jo", "kare", "aur", "on", "hai", "ka", "never", "mujhe", "tujhe", "mera", "mene", "tune", "jab",
                           "ko", "ki", "inki", "don't", "i'm", "got", "ain't", "inke", "yeh", "yahan", "nhi", "aur", "saare",
                           "hoon", "maine", "rap", "hi", "woh"]

    word_array = {}
    arr = textfile.split()
    print(arr)
    for word in arr:
        if word in uninteresting_words or len(word) < 4:
            pass
        else:
            for letter in word:
                if letter in punctuations:
                    letter.replace(letter, "")
            if word not in word_array:
                word_array[word] = 0
            else:
                word_array[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud(max_font_size=50, max_words=100, background_color="white")
    cloud.generate_from_frequencies(word_array)
    return cloud.to_array()


myimage = calculate_frequencies()
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
