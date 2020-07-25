def log(function):
    def decorator(*args, **kwargs):
        print(f'nome da função{function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma_2(x, y):
    return x + y


if __name__ == "__main__":
    soma_2(4, 4)
