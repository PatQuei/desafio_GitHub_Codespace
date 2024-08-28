# **Explicação Educativa: String, Variável e Concatenação**

Este projeto simples em Python visa demonstrar conceitos básicos de programação, incluindo **variáveis**, **strings**, e **concatenação**. O código interativo solicita ao usuário que insira seu nome e sobrenome e, em seguida, combina essas informações para exibir o nome completo do usuário.

## **Código**

```python
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = nome + " " + sobrenome

print(nome_completo)
```

## **Conceitos Importantes**

### **1. Variável**
Uma **variável** é um espaço na memória do computador onde podemos armazenar dados. Pense em uma variável como uma "caixinha" onde você guarda alguma informação que será usada mais tarde. 

No código, temos três variáveis:
- `nome`: armazena o valor digitado pelo usuário como nome.
- `sobrenome`: armazena o valor digitado pelo usuário como sobrenome.
- `nome_completo`: armazena o resultado da combinação (concatenação) das variáveis `nome` e `sobrenome`, separadas por um espaço.

### **2. String**
Uma **string** é um tipo de dado que armazena texto. Em outras palavras, é uma sequência de caracteres, como letras, números e símbolos.

Exemplos de strings:
- `"Patricia"`
- `"Queiroz"`
- `"123"`

No nosso código, as variáveis `nome` e `sobrenome` são strings porque armazenam texto.

### **3. Concatenação**
**Concatenação** é o processo de unir duas ou mais strings. Usamos o operador `+` em Python para fazer isso.

No código, fazemos a concatenação das strings `nome`, `" "` (um espaço em branco) e `sobrenome`:
```python
nome_completo = nome + " " + sobrenome
```
Se o usuário digitar `"Patricia"` como nome e `"Queiroz"` como sobrenome, a variável `nome_completo` armazenará `"Patricia Queiroz"`, com um espaço entre o nome e o sobrenome.

### **4. Interação com o Usuário**
O código começa solicitando ao usuário que insira seu nome e sobrenome, utilizando a função `input()`:
```python
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
```
Essa função permite que o programa receba dados diretamente do usuário.

### **5. Impressão do Resultado**
Por fim, o código exibe o valor de `nome_completo` usando a função `print()`:
```python
print(nome_completo)
```
Isso mostra na tela o nome completo do usuário, com um espaço entre o nome e o sobrenome.

## **Exemplo de Execução**

```bash
Digite seu nome: Patricia
Digite seu sobrenome: Queiroz
Patricia Queiroz
```

Neste exemplo, o usuário digitou "Patricia" como nome e "Queiroz" como sobrenome. O código, então, exibiu "Patricia Queiroz" como resultado, separando o nome e o sobrenome com um espaço.

