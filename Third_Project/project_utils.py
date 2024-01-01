import string

def load_stopwords():

    languages = ["english","spanish","french"]
    stop_words = {}

    for language in languages:
        with open("./stopwords/stop_words_" + language + ".txt", encoding="utf8") as file:
            stop_words[language] = file.read().split("\n")
    
    return stop_words
    
def process_books():
    stop_words = load_stopwords()

    languages = ["english","spanish","french"]

    processed_books = {}

    books_start = {}
    books_end = {}

    books_start["english"] = "Tell me, O Muse"
    books_end["english"] = "between the two contending parties."

    books_start["spanish"] = "Háblame, Musa"
    books_end["spanish"] = "FIN"

    books_start["french"] = "Dis-moi, Muse"
    books_end["french"] = "entre les deux partis."

    stats = open("results/book_processing_length.txt", "w", encoding="utf-8")
    stats.write(f'{"Language":<20} {"Starting Length":<20} {"Ending Length":<20}\n')

    for language in languages:
        with open("books/odyssey_" + language + ".txt", encoding="utf-8") as book:
            text = book.read()

            # print(f"Book Language: {language}")

            starting_length = len(text)

            book_start = text.find(books_start[language])

            # print(f"Book Start: {book_start}")
            # print(f"Text Start: {text[book_start:book_start+20]}")

            if language == "spanish":
                book_end = text.find(books_end[language]) - len(books_end["spanish"])
                # print(f"Book End: {book_end}")
                # print(f"Text End: {text[book_end-20:book_end]}")
            else:
                book_end = text.find(books_end[language])
                # print(f"Book End: {book_end}")
                # print(f"Text End: {text[book_end:book_end+20]}")
            
            text = text[book_start:book_end]

            text = text.replace("[Illustration]", "")

            punctuation = string.punctuation
            for char in punctuation:
                text = text.replace(char, "")

            text = "".join([word for word in text.split() if word.lower() not in stop_words[language]])

            text = "".join([char for char in text if char.isalpha()])

            text = text.upper()

            ending_length = len(text)

            processed_books[language] = text
        
        stats.write(f'{language:<20} {starting_length:<20} {ending_length:<20}\n')

    stats.close()

    return processed_books