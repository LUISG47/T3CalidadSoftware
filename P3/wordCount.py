# pylint: disable=invalid-name
# pylint: disable=too-many-locals
"""
Módulo para contar frecuencia de palabras.
Actividad 4.2 - Ejercicio 3.
"""

import sys
import time
import os


def main():
    """Cuenta palabras, ordena resultados y genera archivo dinámico."""
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return

    file_path = sys.argv[1]
    # Extraer nombre base (ej. TC1)
    base_filename = os.path.basename(file_path).split('.')[0]
    # Concatenación corregida: WordCountResults + TC1 + .txt
    output_name = f"WordCountResults{base_filename}.txt"

    word_freq = {}
    blank_count = 0
    total_words = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file_ptr:
            for line in file_ptr:
                if not line.strip():
                    blank_count += 1
                    continue
                for word in line.split():
                    clean_word = word.strip().lower()
                    if clean_word:
                        word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
                        total_words += 1
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # Ordenar resultados de mayor a menor frecuencia
    sorted_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)

    elapsed_time = time.time() - start_time
    header = f"Row Labels\tCount of {base_filename}"

    # Escritura en el archivo con el nombre dinámico corregido
    with open(output_name, "w", encoding='utf-8') as f_out:
        print(header)
        f_out.write(header + "\n")

        for word, freq in sorted_freq:
            line = f"{word}\t{freq}"
            print(line)
            f_out.write(line + "\n")

        blank_line = f"(blank)\t{blank_count if blank_count > 0 else ''}"
        total_line = f"Grand Total\t{total_words}"
        time_msg = f"Execution Time: {elapsed_time:.6f}s"

        for msg in [blank_line, total_line, time_msg]:
            print(msg)
            f_out.write(msg + "\n")


if __name__ == "__main__":
    main()
