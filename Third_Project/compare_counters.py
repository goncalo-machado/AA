import json
import numpy as np


def obtain_exact_counters(language):

    with open("results/counters/exact_counter/odyssey_" + language + ".txt", "r", encoding="utf8") as file:
        line = file.readline()
        counters = dict(json.loads(line))

        return dict(sorted(counters.items(), key=lambda item: item[1], reverse=True))


def compare_approximate_counters(language, exact_counters):

    total_letters = []
    letters = {}
    total_orders = {}
    top_3_letters_order = {}
    most_frequent_letters = {}

    with open("results/counters/approximate_counter/odyssey_" + language + ".txt", "r", encoding="utf8") as file:

        lines = file.readlines()

        line_counter = 0

        for line in lines:

            counters = dict(json.loads(line))
            counters = dict(sorted(counters.items(), key=lambda item: item[1], reverse=True))

            total = sum(counters.values())
            total_letters.append(total)

            for letter, count in counters.items():

                if letter not in letters:
                    letters[letter] = []

                letters[letter].append(count)

            order = "".join(counters)
            if order not in total_orders:
                total_orders[order] = 0

            total_orders[order] += 1

            order = order[:3]

            if order not in top_3_letters_order:
                top_3_letters_order[order] = 0

            top_3_letters_order[order] += 1

            most_frequent_letter = order[0]

            if most_frequent_letter not in most_frequent_letters:
                most_frequent_letters[most_frequent_letter] = 0

            most_frequent_letters[most_frequent_letter] += 1

    avg_counts = {letter: sum(count)/len(count) for letter, count in letters.items()}
    avg_counts = dict(sorted(avg_counts.items(), key=lambda item: item[1], reverse=True))

    real_order = "".join(exact_counters.keys())

    expected_value_dict = {letter: count/4
                           for letter, count in exact_counters.items()}

    expected_value = sum(expected_value_dict.values())

    real_value = sum(exact_counters.values())

    real_variance, real_standard_deviation, mean_absolute_error, mean_relative_error, mean_accuracy_ratio, \
        smallest_value, largest_value, mean, mean_absolute_deviation, standard_deviation, maximum_deviation, \
        variance = calculate_results(real_value, total_letters, expected_value)

    total_orders = {letter: counter for letter, counter in sorted(total_orders.items(), key=lambda item: item[1], reverse=True)}

    expected_value_dict = {letter: counter for letter, counter in sorted(expected_value_dict.items(), key=lambda item: item[1], reverse=True)}

    top_3_letters_order = {letter: counter for letter, counter in sorted(top_3_letters_order.items(), key=lambda item: item[1], reverse=True)}

    most_frequent_letters = {letter: counter for letter, counter in sorted(most_frequent_letters.items(), key=lambda item: item[1], reverse=True)}

    order_accuracy = total_orders[real_order] / sum(total_orders.values()) if real_order in total_orders else 0

    first_3_letters_accuracy = top_3_letters_order[real_order[:3]] / sum(top_3_letters_order.values()) if real_order[:3] in top_3_letters_order else 0

    with open("results/comparisons/approximate_counter/odyssey_" + language + ".txt", "w", encoding="utf8") as results:

        results.write(f"Expected value: {expected_value}\n")
        results.write(f"Variance: {real_variance}\n")
        results.write(f"Standard deviation: {real_standard_deviation}\n\n")

        results.write(f"Mean absolute error: {mean_absolute_error}\n")
        results.write(f"Mean relative error: {mean_relative_error}%\n")
        results.write(f"Mean accuracy ratio: {mean_accuracy_ratio * 100}%\n\n")

        results.write(f"Smallest counter value: {smallest_value}\n")
        results.write(f"Largest counter value: {largest_value}\n\n")

        results.write(f"Mean counter value: {mean}\n")
        results.write(f"Mean absolute deviation: {mean_absolute_deviation}\n")
        results.write(f"Standard deviation: {standard_deviation}\n")
        results.write(f"Maximum deviation: {maximum_deviation}\n")
        results.write(f"Variance: {variance}\n\n")

        results.write(f"Real Char Frequency Order: {real_order}\n")
        results.write(f"Letter Order Accuracy: {order_accuracy * 100}%\n")
        results.write("10 Most Common Orders:\n")

        for i, order in enumerate(total_orders):
            if i >= 10:
                break
            results.write(f'{order}: {total_orders[order]}\n')

        results.write("\n")

        results.write(f'Top 3 Char Order Accuracy: {first_3_letters_accuracy * 100}%\n')
        results.write('10 Most Common Orders:\n')
        for i, order in enumerate(top_3_letters_order):
            if i >= 10:
                break
            results.write(f'{order}: {top_3_letters_order[order]}\n')

        results.write("\n")

        results.write('Mean Counter Values per letter:\n')
        results.write(f'Letter : Counter Value : Expected Value\n')
        for letter, counter in avg_counts.items():
            results.write(f'{letter:<6} : {counter:<13} : {expected_value_dict[letter]}\n')

        results.write("\n")

        results.write(f"Most Frequent Letter: {real_order[0]}\n")
        results.write(f"Letter Accuracy: {most_frequent_letters[real_order[0]]/sum(most_frequent_letters.values()) * 100}%\n")
        results.write("10 Most Common Letters:\n")

        for i, letter in enumerate(most_frequent_letters):
            if i >= 10:
                break
            results.write(f'{letter} ')

        results.write("\n\n")

        print(most_frequent_letters)

        for i, letter in enumerate(most_frequent_letters):
            if i >= 3:
                break

            real_variance, real_standard_deviation, mean_absolute_error, mean_relative_error, mean_accuracy_ratio, \
                smallest_value, largest_value, mean, mean_absolute_deviation, standard_deviation, maximum_deviation, \
                variance = calculate_results(exact_counters[letter], letters[letter], expected_value_dict[letter])

            results.write(f"--------- Letter {letter}\n")
            results.write(f"Expected value: {expected_value_dict[letter]}\n")
            results.write(f"Variance: {real_variance}\n")
            results.write(f"Standard deviation: {real_standard_deviation}\n\n")

            results.write(f"Mean absolute error: {mean_absolute_error}\n")
            results.write(f"Mean relative error: {mean_relative_error}%\n")
            results.write(f"Mean accuracy ratio: {mean_accuracy_ratio * 100}%\n\n")

            results.write(f"Smallest counter value: {smallest_value}\n")
            results.write(f"Largest counter value: {largest_value}\n\n")

            results.write(f"Mean counter value: {mean}\n")
            results.write(f"Mean absolute deviation: {mean_absolute_deviation}\n")
            results.write(f"Standard deviation: {standard_deviation}\n")
            results.write(f"Maximum deviation: {maximum_deviation}\n")
            results.write(f"Variance: {variance}\n\n")


def calculate_results(real_value, counters, expected_value):

    real_variance = expected_value / 2

    real_standard_deviation = np.sqrt(real_variance)

    n = len(counters)
    mean = sum(counters) / n

    maximum_deviation = max([abs(total - mean) for total in counters])

    mean_absolute_deviation = sum([abs(total - mean) for total in counters]) / n

    variance = sum([(count - mean) ** 2 for count in counters]) / n

    standard_deviation = np.sqrt(sum([(count - mean) ** 2 for count in counters]) / n)

    mean_absolute_error = sum([abs(count - expected_value) for count in counters]) / n

    mean_relative_error = sum([abs(count - expected_value) / expected_value for count in counters]) / n * 100

    mean_accuracy_ratio = mean / expected_value

    smallest_value = min(counters)

    largest_value = max(counters)

    return real_variance, real_standard_deviation, mean_absolute_error, mean_relative_error, mean_accuracy_ratio, \
        smallest_value, largest_value, mean, mean_absolute_deviation, standard_deviation, maximum_deviation, variance


def compare_frequent_counter(language, exact_counter):

    exact_counter = sorted(exact_counter.items(), key=lambda item: item[1], reverse=True)

    possible_k = [3,5,10]

    for k in possible_k:
        with open("results/counters/frequent_counter/odyssey_" + language + "_" + str(k) + ".txt", "r", encoding="utf-8") as file:
            line = file.readline()
            frequent_counter = dict(json.loads(line))

        top_k_letters = exact_counter[0:k-1]

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

    # All books
    languages = ["english","spanish","french"]

    for language in languages:

        exact_counters = obtain_exact_counters(language)

        # Compare approximate counters
        compare_approximate_counters(language, exact_counters)

        # Compare data stream counters
        compare_frequent_counter(language, exact_counters)