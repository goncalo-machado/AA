from collections import Counter
import project_utils
import time
import json

def frequent_counter(stream, k):
    counters = Counter()
    for item in stream:
        ## case 1: item already has counter or there are empty counters
        if item in counters or len(counters) < k-1:
            counters[item] += 1
        ## case 2: item doesn't have counter and there are no empty counters
        else:
            for key in list(counters.keys()):
                counters[key] -= 1
                if counters[key] == 0:
                    del counters[key]
    return counters

if __name__ == '__main__':

    possible_k = [3,5,10]

    stats = open("results/times/frequent_counter_time.txt", "w", encoding="utf-8")
    stats.write(f'{"Language":<20} {"Average Time":<20} {"k":<20}\n')

    books = project_utils.process_books()
    for language in books.keys():

        for k in possible_k:
        
            start_time = time.time()

            counter = frequent_counter(books[language], k)

            frequent_counter_time = time.time() - start_time

            with open("results/counters/frequent_counter/odyssey_" + language + "_" + str(k) + ".txt", "w", encoding="utf-8") as file:
                file.write(json.dumps(counter, ensure_ascii=False) + "\n")

            stats.write(f'{language:<20} {frequent_counter_time:<20} {k:<20}\n')

    stats.close()