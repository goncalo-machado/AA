from collections import Counter
import project_utils
import time
import json

if __name__ == '__main__':

    stats = open("results/times/exact_counter_time.txt", "w", encoding="utf-8")
    stats.write(f'{"Language":<20} {"Time":<20}\n')

    books = project_utils.process_books()
    for language in books.keys():

        start_time = time.time()

        exact_counter = Counter(books[language])

        exact_counter_time = time.time() - start_time

        stats.write(f'{language:<20} {exact_counter_time:<20}\n')

        with open("results/counters/exact_counter/odyssey_" + language + ".txt", "w", encoding="utf-8") as file:
            file.write(json.dumps(exact_counter, ensure_ascii=False))

    stats.close()