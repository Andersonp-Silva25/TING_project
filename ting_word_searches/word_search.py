import re


def exists_word(word, instance):
    for index in range(len(instance)):
        file = instance.search(index)
        line = file["linhas_do_arquivo"]
        file_name = file["nome_do_arquivo"]

        data = {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": [],
        }
        
        for i in range(len(line)):
            if re.search(word, line[i], re.I):
                data["ocorrencias"].append({"linha": i + 1})

        result = [data] if len(data["ocorrencias"]) != 0 else []

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
