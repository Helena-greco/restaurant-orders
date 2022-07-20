import csv


def analyze_log(path_to_file):
    if '.csv' not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, encoding='utf-8') as csv_file:
            file = csv.reader(csv_file, delimiter=",", quotechar='"')
            header, *data = file

        print(data)

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
