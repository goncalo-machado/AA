import json

def get_exact_counter(language):
    
    dir = "results/counters/exact_counter/odyssey_" + language + ".txt"

    with open(dir,"r", encoding="utf-8") as file:
        line = file.readline()
        counter = dict(json.loads(line))

        sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

        return sorted_counter

def compare_approximate_counter(language, exact_counter):
    pass 

def compare_frequent_counter(language, exact_counter):

    possible_k = [3,5,10]

    for k in possible_k:
        with open("results/counters/frequent_counter/odyssey_" + language + "_" + str(k) + ".txt", "r", encoding="utf-8") as file:
            line = file.readline()
            frequent_counter = dict(json.loads(line))

        top_k_letters = sorted(exact_counter.items(), key=lambda item: item[1], reverse=True)[0:k-1]

        with open("results/comparisons/frequent_counter/odyssey_" + language + "_" + str(k) + ".txt", "w", encoding="utf-8") as results:

            results.write(f"Top {k-1} letters (Exact Counter):\n")
            for letter, counter in top_k_letters:
                results.write(f"{letter}: {counter}\n")

            results.write("\n")

            results.write(f"Top {k-1} letters (Frequent Counter):\n")
            for letter, counter in frequent_counter.items():
                results.write(f"{letter}: {counter}\n")

            results.write("\n")

            accurate_letters = len([letter for letter, _ in top_k_letters if letter in frequent_counter])

            accuracy = accurate_letters/(k-1)

            accuracy_str = "{0:.2f}".format(accuracy*100)

            results.write(f"Accurate letters: {accurate_letters}/{k-1}\n")
            results.write(f"Accuracy: {accuracy_str}%\n")

if __name__ == "__main__":
    
    languages = ["english","spanish","french"]

    for language in languages:

        exact_counter = get_exact_counter(language)

        compare_approximate_counter(language, exact_counter)

        compare_frequent_counter(language, exact_counter)