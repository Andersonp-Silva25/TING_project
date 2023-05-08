import sys


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file, "r") as file:
                return [line.strip("\n") for line in file.readlines()]
        print("Formato inválido", file=sys.stderr)
    except FileNotFoundError:
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
