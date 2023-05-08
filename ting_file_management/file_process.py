from ting_file_management.file_management import txt_importer as file
import sys


def process(path_file, instance):
    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file(path_file)),
        "linhas_do_arquivo": file(path_file),
    }
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(file_data)
    print(file_data, file=sys.stdout)


def remove(instance):
    if len(instance) > 0:
        delete = instance.dequeue()
        file = delete["nome_do_arquivo"]
        print(f"Arquivo {file} removido com sucesso")
    print("Não há elementos")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except  IndexError:
        print("Posição inválida", file=sys.stderr)
