### **README: Explicação dos Blocos de Código em Python**

Este documento fornece uma explicação detalhada de três blocos de código em Python, cada um com funcionalidades diferentes, mas fundamentais para o aprendizado da linguagem. Vamos analisar cada bloco, explicando como ele funciona e quais conceitos são abordados.

---

## **Bloco de Código 1: Concatenando Nome e Sobrenome**

### **Código:**
```python
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = nome + " " + sobrenome

print(nome_completo)
```

### **Explicação:**

1. **Entrada de Dados:**
   - `nome = input("Digite seu nome: ")` e `sobrenome = input("Digite seu sobrenome: ")` solicitam ao usuário que insira seu nome e sobrenome. Os valores digitados são armazenados nas variáveis `nome` e `sobrenome`, respectivamente.

2. **Concatenação:**
   - `nome_completo = nome + " " + sobrenome` concatena as strings `nome` e `sobrenome`, adicionando um espaço `" "` entre elas. O resultado é armazenado na variável `nome_completo`.

3. **Saída:**
   - `print(nome_completo)` exibe o nome completo do usuário, com o espaço entre o nome e o sobrenome.

---

## **Bloco de Código 2: Repetindo uma String**

### **Código:**
```python
# Solicitar uma string
texto = input("Digite uma palavra ou frase: ")

# Solicitar um número inteiro
numero = int(input("Digite um número inteiro: "))

print((texto + " ") * numero)
```

### **Explicação:**

1. **Entrada de Dados:**
   - `texto = input("Digite uma palavra ou frase: ")` solicita ao usuário que insira uma palavra ou frase, armazenando o valor na variável `texto`.
   - `numero = int(input("Digite um número inteiro: "))` solicita ao usuário que insira um número inteiro, que é armazenado na variável `numero` após ser convertido para o tipo `int`.

2. **Concatenação e Repetição:**
   - `print((texto + " ") * numero)` concatena a string `texto` com um espaço `" "` e multiplica essa concatenação pelo valor de `numero`. Isso resulta em `numero` repetições da string `texto`, separadas por espaços.

3. **Saída:**
   - O resultado da operação é impresso na tela, repetindo a string digitada pelo usuário o número de vezes especificado.

---

## **Bloco de Código 3: Calculadora Simples**

### **Código:**
```python
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
operacao = input("Qual operação deseja fazer(+, -, *, /) : ")

if operacao == "+":
    print(num1 + num2)

elif operacao == "-":
    print(abs(num1 - num2))

elif operacao == "*":
    print(num1 * num2)

elif operacao == "/":
    print(num1 / num2)

else:
    print("Operação digitada inválida")
```

### **Explicação:**

1. **Entrada de Dados:**
   - `num1 = int(input("Digite um numero: "))` e `num2 = int(input("Digite outro numero: "))` solicitam ao usuário que insira dois números inteiros. Esses valores são armazenados nas variáveis `num1` e `num2`.
   - `operacao = input("Qual operação deseja fazer(+, -, *, /) : ")` solicita ao usuário que escolha uma operação matemática (adição, subtração, multiplicação ou divisão) e armazena o valor na variável `operacao`.

2. **Estrutura Condicional (if-elif-else):**
   - O bloco `if-elif-else` avalia a operação escolhida:
     - Se `operacao` for `"+"`, realiza a adição (`print(num1 + num2)`).
     - Se `operacao` for `"-"`, realiza a subtração e imprime o valor absoluto do resultado (`print(abs(num1 - num2))`).
     - Se `operacao` for `"*"`, realiza a multiplicação (`print(num1 * num2)`).
     - Se `operacao` for `"/"`, realiza a divisão (`print(num1 / num2)`).
     - Se o usuário digitar uma operação inválida, imprime uma mensagem de erro (`print("Operação digitada inválida")`).

3. **Saída:**
   - Dependendo da operação escolhida pelo usuário, o resultado correspondente é exibido. Se a operação for inválida, o código informa ao usuário que a operação digitada não é reconhecida.
