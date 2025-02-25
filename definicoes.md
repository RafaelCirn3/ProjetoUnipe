# Instâncias, Classes, Parâmetros e Argumentos

## Instância e Classe

- Uma **instância** é um objeto de uma classe.
- **Instanciar um objeto** significa criar um objeto de uma classe.

### Exemplo em Python:
```python
class Copo():
    def __init__(self, cor):
        self.cor = cor

objeto = Copo("azul")
```
- `objeto` é uma instância da classe `Copo`.
- `Copo` é a classe que foi instanciada.

## Parâmetros e Argumentos

- **Parâmetros** são os valores que uma função recebe para executar.
- **Argumentos** são os valores passados para a função no momento da chamada.

### Exemplo em Python:
```python
def soma(a, b):
    return a + b

print(soma(1, 2))
```
- `a` e `b` são **parâmetros** da função `soma`.
- `1` e `2` são **argumentos** passados para a função quando ela é chamada.

Essa distinção é importante para entender como as funções trabalham com valores recebidos e utilizados no seu escopo.