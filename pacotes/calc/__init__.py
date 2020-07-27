from pacote2.modulo1 import sub
from pacote1.modulo1 import soma

print(f'importado do modulo {__name__}, de {__package__}')


__all__ = ['soma', 'sub']
