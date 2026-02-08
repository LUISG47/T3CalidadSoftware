# pylint: disable=invalid-name
"""
Módulo para calcular estadísticas descriptivas.
"""

import sys
import time
import os


# pylint: disable=too-many-locals
def calculate_stats(valid_data):
    """Calculo de estadisticas"""
    n_valid = len(valid_data)
    if n_valid == 0:
        return None

    # MEAN
    total_sum = 0
    for value in valid_data:
        total_sum += value
    mean = total_sum / n_valid

    # MEDIAN
    sorted_data = sorted(valid_data)
    if n_valid % 2 == 0:
        median = (sorted_data[n_valid // 2 - 1] + sorted_data[n_valid // 2]) / 2
    else:
        median = sorted_data[n_valid // 2]

    # MODE
    counts = {}
    for value in valid_data:
        counts[value] = counts.get(value, 0) + 1

    max_count = 0
    mode = "#N/A"
    for val, count_val in counts.items():
        if count_val > max_count:
            max_count = count_val
            mode = val

    if max_count <= 1:
        mode = "#N/A"

    # VARIANCE and SD
    sum_sq_diff = 0
    for value in valid_data:
        sum_sq_diff += (value - mean) ** 2

    variance_sample = sum_sq_diff / (n_valid - 1) if n_valid > 1 else 0
    variance_pop = sum_sq_diff / n_valid
    sd_pop = variance_pop ** 0.5

    return mean, median, mode, sd_pop, variance_sample


def main():
    """Ejecución principal con conteo total de ítems."""
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        return

    input_file = sys.argv[1]
    base_name = os.path.basename(input_file).split('.')[0]
    output_filename = f"StatisticsResults{base_name}.txt"

    valid_data = []
    total_count = 0
    try:
        with open(input_file, 'r', encoding='utf-8') as file_input:
            for line in file_input:
                item = line.strip()
                if item:
                    total_count += 1
                    try:
                        valid_data.append(float(item))
                    except ValueError:
                        print(f"Error: Invalid data detected '{item}'")
    except FileNotFoundError:
        print("Error: File not found.")
        return

    results = calculate_stats(valid_data)
    elapsed_time = time.time() - start_time

    if results:
        output = (
            f"COUNT: {total_count}\n"
            f"MEAN: {results[0]}\n"
            f"MEDIAN: {results[1]}\n"
            f"MODE: {results[2]}\n"
            f"SD: {results[3]}\n"
            f"VARIANCE: {results[4]}\n"
            f"Execution Time: {elapsed_time:.6f}s\n"
        )
        print(output)
        with open(output_filename, "w", encoding='utf-8') as file_res:
            file_res.write(output)


if __name__ == "__main__":
    main()
