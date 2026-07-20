def verifica_string(func):
    def wrapper(*args, **kwargs):
        string = args[0]
        if not isinstance(string, str):
            raise ValueError("É necessário passar uma string")
        return func(string)
    return wrapper

@verifica_string
def inverte_string(string):
    return string[::-1]

print(inverte_string(123))
