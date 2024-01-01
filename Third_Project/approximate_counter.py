from collections import Counter
import project_utils
import time
import json
import random

def approximate_counter(text):

    counter = {}

    for letter in text:

        if letter not in counter:
            counter[letter] = 0

        k = counter[letter]

        prob = 1 / 4

        if  random.uniform(0,1) <= prob:
            counter[letter] += 1

    return counter

if __name__ == '__main__':

    random.seed(98359)

    n_trials = 20000

    stats = open("results/times/approximate_counter/approximate_counter_time.txt", "w", encoding="utf-8")
    stats.write(f'{"Language":<20} {"Average Time":<20}\n')

    books = project_utils.process_books()
    for language in books.keys():

        total_time = 0

        with open("results/counters/approximate_counter/odyssey_" + language + ".txt", "w", encoding="utf-8") as file:

            for trial in range(n_trials):
            
                start_time = time.time()

                counter = approximate_counter(books[language])

                total_time += time.time() - start_time

                file.write(json.dumps(counter, ensure_ascii=False) + "\n")

        stats.write(f'{language + ":":<20} {total_time/n_trials:<20}\n')

    stats.close()