# **Explicações Educativas de Blocos de Código em Python**

Este documento fornece explicações detalhadas de três diferentes blocos de código em Python, com foco nos conceitos de variáveis, strings, números inteiros, concatenação, repetição, e operações matemáticas. Cada bloco de código aborda um exercício específico, facilitando o entendimento de conceitos fundamentais na programação em Python.

## **Bloco de Código 1: Concatenando Nome e Sobrenome**

### **Código:**
```python
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = nome + " " + sobrenome

print(nome_completo)
```

### **Explicação:**
Este bloco de código solicita ao usuário que insira seu nome e sobrenome, e em seguida concatena esses dois valores com um espaço entre eles para formar o nome completo.

- **nome** e **sobrenome**: Variáveis que armazenam as strings fornecidas pelo usuário.
- **nome_completo**: Variável que armazena a concatenação de `nome`, um espaço `" "`, e `sobrenome`.
- **print(nome_completo)**: Exibe o nome completo na tela.

### **Exemplo de Execução:**
```bash
Digite seu nome: Patricia
Digite seu sobrenome: Queiroz
Patricia Queiroz
```

## **Bloco de Código 2: Repetição de Texto com Multiplicação**

### **Código:**
```python
# Solicitar uma string
texto = input("Digite uma palavra ou frase: ")

# Solicitar um número inteiro
numero = int(input("Digite um número inteiro: "))

print((texto + " ") * numero)
```

### **Explicação:**
Este bloco de código solicita ao usuário uma string e um número inteiro, e então repete a string o número de vezes especificado.

- **texto**: Variável que armazena a string fornecida pelo usuário.
- **numero**: Variável que armazena o número inteiro fornecido pelo usuário.
- **print((texto + " ") * numero)**: Exibe a string `texto` repetida `numero` vezes, com um espaço adicionado após cada repetição.

### **Exemplo de Execução:**
```bash
Digite uma palavra ou frase: Python
Digite um número inteiro: 3
Python Python Python 
```

## **Bloco de Código 3: Calculadora Simples**

### **Código:**
```python
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
operacao = input("Qual operação deseja fazer(+, -, *, /) : ")

if operacao == "+":
    print(num1 + num2)

elif operacao == "-":
    print(num1 - num2)

elif operacao == "*":
    print(num1 * num2)

elif operacao == "/":
    print(num1 / num2)

else:
    print("Operação digitada inválida")
```

### **Explicação:**
Este bloco de código implementa uma calculadora simples que realiza adição, subtração, multiplicação ou divisão, dependendo da operação escolhida pelo usuário.

- **num1** e **num2**: Variáveis que armazenam os números inteiros fornecidos pelo usuário.
- **operacao**: Variável que armazena o símbolo da operação escolhida (`+, -, *, /`).
- **if/elif/else**: Estruturas de controle que determinam qual operação será realizada com base na escolha do usuário. O código realiza a operação correspondente e exibe o resultado. Se a operação for inválida, uma mensagem de erro é exibida.

### **Exemplo de Execução:**
```bash
Digite um numero: 10
Digite outro numero: 5
Qual operação deseja fazer(+, -, *, /) : *
50
```

## **Resumo**

Esses três blocos de código são exemplos práticos de como trabalhar com entradas do usuário, manipulação de strings, repetição de operações, e cálculos matemáticos em Python. Eles ilustram conceitos importantes de programação, que são essenciais para qualquer desenvolvedor iniciante.

