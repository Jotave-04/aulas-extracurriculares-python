"""
Arquivo: extracurricular.py
Descrição: Aulas complementares de Python (29/09 a 08/10/2025)
Autor: João Victor Canavez
Objetivo: Consolidar fundamentos de lógica e programação em Python.
"""


# =====================================================
# DIA 1 (29/09/2025) — Revisão inicial
# =====================================================

# 1. Frase com três formas
# Mostrar a frase:
# "Meu nome é João e tenho 20 anos."
# Usando: concatenação (+), vírgulas, f-string

nome = "João"
idade = 20

print("Meu nome é " + nome + " e tenho " + str(idade) + " anos.")  # concatenação
print("Meu nome é", nome, "e tenho", idade, "anos.")               # vírgulas
print(f"Meu nome é {nome} e tenho {idade} anos.")                  # f-string

# -----------------------------------------------------

# 2. Nome e cidade
# Peça ao usuário o nome e a cidade e mostre:
# "Olá, Maria! Vejo que você mora em São Paulo."

nome = input("Olá, bem-vindo. Me diga seu nome: ")
casa = input("Onde você mora? ")

print(f"Olá, {nome}! Vejo que você mora em {casa}.")

# -----------------------------------------------------

# 3. Calculando idade no futuro
# Peça a idade do usuário e mostre quantos anos terá em 2050.

from datetime import date

idade = int(input("Qual a sua idade? "))
ano_atual = date.today().year
ano_futuro = 2050

print(f"Vejo que em 2050 você terá {idade + (ano_futuro - ano_atual)} anos, correto?")

# =====================================================
# DIA 2 (30/09/2025) — Números e Operações
# =====================================================

# 1. Tipos numéricos
# int  -> números inteiros (10, -5, 2025)
# float -> números decimais (3.14, -0.5, 2.0)

# 2. Conversões de tipos
# int("25")   -> 25
# float("3.14") -> 3.14
# str(25)     -> "25"

# 3. Operadores matemáticos
# +  soma           5 + 2  -> 7
# -  subtração      5 - 2  -> 3
# *  multiplicação  5 * 2  -> 10
# /  divisão        5 / 2  -> 2.5
# // divisão inteira 5 // 2 -> 2
# %  resto          5 % 2  -> 1
# ** potência       5 ** 2 -> 25

# 4. Exemplos práticos
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

# -----------------------------------------------------

# Exercício 1 — Operações básicas
n1 = int(input("Olá, me diga um número: "))
n2 = int(input("Show! Agora me diga outro: "))

print("A soma é:", n1 + n2)
print("A subtração é:", n1 - n2)
print("A multiplicação é:", n1 * n2)
print("A divisão normal é:", n1 / n2)
print("A divisão inteira é:", n1 // n2)
print("O resto da divisão é:", n1 % n2)
print("A potência do primeiro elevado ao segundo é:", n1 ** n2)

# -----------------------------------------------------

# Exercício 2 — Trabalhando com idade
idade = int(input("Bom dia, me diga a sua idade: "))

print("O dobro da sua idade é", idade * 2)
print("A metade da sua idade é", idade / 2)     # divisão float
print("A sua idade ao quadrado é", idade ** 2)

# -----------------------------------------------------

# Exercício 3 — Cálculo de média
nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))
nota3 = float(input("Terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média do aluno é: {media:.2f}")

if media < 6:
    print("REPROVADO!")
else:
    print("APROVADO")

# =====================================================
# DIA 3 (01/10/2025) — Strings e manipulação
# =====================================================

# 1. Strings são textos, definidos entre aspas simples, duplas ou triplas.
nome = "Maria"
frase = 'Python é divertido'
texto_longo = """Este é um texto
com várias linhas."""

# -----------------------------------------------------

# 2. Operações básicas com strings
print("Olá " + nome)     # concatenação
print("Oi! " * 3)        # repetição
print("Linha 1\nLinha 2\nLinha 3")  # nova linha
print("Nome:\tMaria")    # tabulação
print("Idade:\t20")

# -----------------------------------------------------

# 3. Diferença entre vírgula e +
nome = "João"
idade = 20
print("Meu nome é", nome, "e tenho", idade, "anos.")               # vírgulas
print("Meu nome é " + nome + " e tenho " + str(idade) + " anos.")  # concatenação

# -----------------------------------------------------

# 4. Métodos úteis de strings
texto = "  Python é Incrível!  "

print(texto.lower())    # tudo minúsculo
print(texto.upper())    # tudo maiúsculo
print(texto.strip())    # remove espaços extras
print(texto.replace("Incrível", "muito legal"))  # troca palavras
print(len(texto))       # tamanho da string

# =====================================================
# 📝 Exercícios do Dia 3
# =====================================================

# Exercício 1 — Repetição
# Peça ao usuário um nome e mostre ele repetido 5 vezes em linhas diferentes.
# (Dica: pode usar \n ou um loop for)

# 🔹 Solução com FOR:
# - O comando "for" repete automaticamente um bloco de código várias vezes.
# - range(5) -> gera os números 0, 1, 2, 3, 4 (total de 5 repetições).
# - A cada repetição, o valor de "i" muda, mas nesse exercício não precisamos usar "i".
# - Dentro do laço, usamos apenas print(nome).

nome = input("Olá, qual seu nome? ")

for i in range(5):      # repete o bloco 5 vezes
    print(nome)         # mostra o nome em cada repetição


# Exercício 2 — Tabelinha
# Peça nome, idade e email e mostre como se fosse uma tabelinha usando \t:
# Exemplo:
# Nome:   Maria
# Idade:  20
# Email:  maria@email.com

# 🔹 \t representa uma TABULAÇÃO (como se fosse a tecla TAB do teclado).
# Isso ajuda a alinhar o texto em colunas.

# Entrada de dados (input do usuário)
nome = input("Olá, qual seu nome? ")
idade = int(input("Agora me diga sua idade: "))
email = input("Qual seu e-mail? ")

# Saída formatada (com tabulação)
print("Nome:\t", nome)
print("Idade:\t", idade)
print("E-mail:\t", email)

# Exercício 3 — Ficha formatada
# Peça os mesmos dados (nome, idade e email), mas mostre como um formulário:
# _________________________
# Nome: Maria
# Idade: 20
# Email: maria@email.com
# _________________________
# (Dica: pode usar "_" * 25 para a linha)

# Entrada de dados
nome = input("Olá, qual seu nome? ")
idade = int(input("Agora me diga sua idade: "))
email = input("Qual seu e-mail? ")

# Saída formatada
print("_" * 25)            # linha superior
print("Nome:", nome)       # mostra nome
print("Idade:", idade)     # mostra idade
print("E-mail:", email)    # mostra e-mail
print("_" * 25)            # linha inferior

# Desafio Extra 😎
# Peça ao usuário para digitar uma frase.
# Depois mostre:
# - A frase toda em maiúsculas
# - A frase toda em minúsculas
# - Quantos caracteres a frase tem (sem espaços nas pontas)

# Entrada de dados
texto = input("Coloque sua frase aqui: ")

# Saída formatada
print(texto.lower())          # tudo minúsculo
print(texto.upper())          # tudo maiúsculo
print(len(texto.strip()))     # conta caracteres sem espaços nas pontas

# =====================================================
# DIA 4 (02/10/2025) — Misturando tudo
# (print, variáveis, input, números, strings, formatação)
# =====================================================

# 1) Relembrando: três jeitos de imprimir valores
nome = "Ana"
idade = 22

print("Meu nome é " + nome + " e tenho " + str(idade) + " anos.")  # concatenação (+)
print("Meu nome é", nome, "e tenho", idade, "anos.")               # vírgulas no print
print(f"Meu nome é {nome} e tenho {idade} anos.")                  # f-string (recomendado)

# -----------------------------------------------------

# 2) Convertendo tipos ao ler com input()
# input() sempre retorna str -> converta quando precisar de número
altura = float(input("Sua altura (em metros): "))
ano_atual = 2025  # vamos manter explícito aqui
nascimento = int(input("Ano de nascimento: "))

print(f"Você tem aproximadamente {ano_atual - nascimento} anos e mede {altura} m.")

# -----------------------------------------------------

# 3) Formatação de números (duas casas decimais)
preco = 19.9
quant = 3
total = preco * quant

print("Total sem formatação:", total)
print(f"Total com 2 casas: R$ {total:.2f}")  # :.2f -> duas casas decimais

# -----------------------------------------------------

# 4) Montando “layouts” com caracteres repetidos, \n e \t
print("_" * 30)
print("Produto:\tCaderno")
print("Preço:\t\tR$ 12.50")
print("Qtd:\t\t2")
print("_" * 30)

# \n quebra linha; \t é tabulação (como a tecla TAB)

# -----------------------------------------------------

# 5) Strings úteis no dia a dia
frase = "   python é demais!   "
print(frase.strip())                 # remove espaços extras nas pontas
print(frase.strip().title())         # Título: 'Python É Demais!'
print(frase.upper())                 # MAIÚSCULAS
print(len(frase.strip()))            # tamanho sem espaços das pontas

# -----------------------------------------------------

# 6) Observações importantes
# - Divisão por zero causa erro: 10 / 0 (cuidado quando pedir números ao usuário)
# - Use f-strings para misturar texto + variáveis de forma clara
# - Quando quiser alinhar “tabelinhas”, \t ajuda bastante

# =====================================================
# 📝 Exercícios do Dia 4 (não resolver aqui)
# =====================================================

# Exercício 1 — Cartão de visita
# Peça nome, profissão e cidade. Mostre um “cartão” com moldura e \t para alinhar:
# ______________________________
# Nome:       ...
# Profissão:  ...
# Cidade:     ...
# ______________________________

# Entrada de dados (input do usuário)
nome = input("Olá, me diga seu nome: ")
profi = input(f"Olá {nome}, qual sua profissão? ")
cidade = input(f"Perfeito {nome}, agora me fala em qual cidade você vive: ")

# Saída formatada (cartão de visita)
print("_" * 25)
print("Nome:\t", nome)
print("Profissão:\t", profi)
print("Cidade:\t", cidade)
print("_" * 25)

# Exercício 2 — Mini “cupom” de compra
# Peça 3 itens (nome do item, preço unitário, quantidade).
# Calcule o total de cada item (preço * quantidade) e o total geral.
# Mostre tudo formatado com duas casas decimais e uma moldura.

# -----------------------------------------------------
# 🔹 Estrutura escolhida: DICIONÁRIOS
# - Cada item é um dicionário com 3 campos:
#   "Nome", "Preço", "Quantidade"
# - Isso torna o código mais organizado e legível.

# Entrada de dados (input do usuário)
print("Verifique aqui seu item:")
item1 = {
    "Nome": input("Nome: "),
    "Preço": float(input("Preço: ")),
    "Quantidade": int(input("Quantidade: "))
}

print("Agora me diga outro item:")
item2 = {
    "Nome": input("Nome: "),
    "Preço": float(input("Preço: ")),
    "Quantidade": int(input("Quantidade: "))
}

print("Agora outro:")
item3 = {
    "Nome": input("Nome: "),
    "Preço": float(input("Preço: ")),
    "Quantidade": int(input("Quantidade: "))
}

# -----------------------------------------------------
# Cálculo dos totais
total1 = item1["Preço"] * item1["Quantidade"]
total2 = item2["Preço"] * item2["Quantidade"]
total3 = item3["Preço"] * item3["Quantidade"]

# Total geral da compra
total_geral = total1 + total2 + total3

# -----------------------------------------------------
# Saída formatada (resumo da compra)
print("\nResumo da compra:")
print(item1["Nome"], "-", item1["Quantidade"], "x R$", item1["Preço"], "=", total1)
print(item2["Nome"], "-", item2["Quantidade"], "x R$", item2["Preço"], "=", total2)
print(item3["Nome"], "-", item3["Quantidade"], "x R$", item3["Preço"], "=", total3)
print("Total da compra = R$", total_geral)

# -----------------------------------------------------
# 📌 Melhorias possíveis (não obrigatórias agora):
# - Usar f-strings para formatar valores monetários com 2 casas decimais:
#   f"R$ {total1:.2f}"
# - Guardar os 3 dicionários dentro de uma lista e percorrer com for,
#   evitando repetir tanto código (veremos isso nas próximas aulas).


# Exercício 3 — Resumo pessoal
# Peça nome, idade e ano atual (como número).
# Mostre: “Olá, <nome>! Em <ano_atual + 1> você terá <idade + 1> anos.”
# (Use f-strings.)

# 🔹 Esse exercício serve para treinar:
#   - Leitura de dados com input()
#   - Conversão para int (idade e ano)
#   - Uso de f-strings para misturar texto e variáveis
#   - Operações matemáticas simples (+1)

# Entrada de dados
nome = input("Me diga seu nome: ")  # string
idade = int(input(f"Olá {nome}, quantos anos você tem? "))  # int
ano_atual = int(input("Agora me fala, qual o ano atual? "))  # int

# Saída formatada
print(f"Olá, {nome}! Em {ano_atual + 1} você terá {idade + 1} anos.")


# Exercício 4 — Média de 4 notas
# Peça 4 notas (float), calcule a média e mostre com 2 casas.
# Não usar if aqui; foco é prática de leitura, soma e formatação.

# 🔹 Neste exercício usamos um DICIONÁRIO para organizar as notas.
# 🔹 Para acessar os valores, usamos colchetes: notas["nota1"].

# Entrada de dados (input do usuário)
notas = {
    "nota1": float(input("Coloque a primeira nota: ")),
    "nota2": float(input("Coloque a segunda nota: ")),
    "nota3": float(input("Coloque a terceira nota: ")),
    "nota4": float(input("Coloque a quarta nota: "))
}

# Cálculo da média
# Somamos as 4 notas e dividimos por 4
media = (notas["nota1"] + notas["nota2"] + notas["nota3"] + notas["nota4"]) / 4

# Saída formatada
print(f"A sua média é: {media:.2f}")


# Exercício 5 — Texto normalizado
# Peça uma frase qualquer.
# Mostre:
# - A frase sem espaços nas pontas
# - A frase em Título (title)
# - Quantos caracteres a frase tem (sem espaços das pontas)
# - A mesma frase entre molduras (linhas acima e abaixo)

# 🔹 Esse exercício serve para treinar:
#   - Métodos de string: .strip(), .title(), len()
#   - Impressão formatada com caracteres repetidos ("_" * 25)

# Entrada de dados
frase = input("Me diga uma frase engraçada: ")

# Saídas
print(frase.strip())            # 1) Frase sem espaços extras
print(frase.strip().title())    # 2) Frase em formato de Título
print(len(frase.strip()))       # 3) Quantidade de caracteres (sem espaços)
print("_" * 25)                 # 4) Moldura superior
print(frase.strip())            #    Frase limpa dentro da moldura
print("_" * 25)                 #    Moldura inferior


# Desafio Extra 😎 — “Painel informativo”
# Monte um pequeno painel combinando tudo:
# - Uma linha de título com moldura
# - 2 ou 3 linhas de “campo: valor” usando \t para alinhar
# - Um rodapé com o total (se aplicar), formatado com 2 casas
# Dica: escolha um tema (ex.: pedido, perfil, evento) e capriche no layout.

# ---------------------------
# Seu rascunho com observações
# ---------------------------

evento = "One Night Ink"
dados = {
    "nome": input("Nome do cliente: "),
    "tattoo": input("Arte selecionada: "),
    "senha": int(input("Senha de número: "))
}
preço = {
    "tempo": input("Duração do trabalho: "),
    "valor": float(input("Quanto foi a arte: "))
}

print("=" * 25)
print(evento.strip().title())
print("=" * 25)

print(dados)                 # ❌ Isso imprime o dicionário "cru" (ex.: {'nome': '…', ...})
                             #    Correto: mostrar cada campo separadamente (dados["nome"], etc.).

print("_" * 25)

print(preço["tempo"])        # ✅ Ok (acessa a chave "tempo")
print(preço["valor" - "valor"])  # ❌ Não existe subtração de strings.
                                 #    Correto: acessar direto a chave "valor" -> preço["valor"]
print("Total: 0800 PAPAI!")

# ---------------------------
# Versão corrigida e comentada
# ---------------------------

# Dica: é comum evitar acentos em nomes de variáveis (ex.: usar 'preco' em vez de 'preço').
# Aqui manteremos 'preço' porque você já usou assim e funciona no Python 3.

evento = "One Night Ink"
dados = {
    "nome": input("Nome do cliente: "),
    "tattoo": input("Arte selecionada: "),
    "senha": int(input("Senha de número: "))
}
preço = {
    "tempo": input("Duração do trabalho: "),
    "valor": float(input("Quanto foi a arte: "))
}

# Cabeçalho
print("\n" + "=" * 30)
print(evento.strip().upper())       # Deixa o título em CAIXA ALTA para destacar
print("=" * 30)

# Bloco: Dados do cliente (mostrando campos individualmente)
print("Cliente:\t", dados["nome"])
print("Arte:\t\t", dados["tattoo"])
print("Senha:\t\t", dados["senha"])

print("-" * 30)

# Bloco: Dados do serviço
print("Duração:\t", preço["tempo"])
print(f"Valor:\t\t R$ {preço['valor']:.2f}")   # formata com 2 casas decimais

print("=" * 30)
print("TOTAL:\t\t 0800 PAPAI!")               # Mensagem final divertida :)
print("=" * 30)


# =====================================================
# DIA 5 (03/10/2025) — Condições e Mini-Desafios
# =====================================================

# -----------------------------------------------------
# 1. Estruturas condicionais
# -----------------------------------------------------
# O "if" serve para tomar decisões no programa.
# Exemplo simples:
#
# nota = 7
# if nota >= 6:
#     print("Aprovado")
# else:
#     print("Reprovado")
#
# O "elif" permite verificar várias condições:
#
# nota = 8
# if nota < 6:
#     print("Reprovado")
# elif nota < 8:
#     print("Recuperação")
# else:
#     print("Aprovado com sucesso")

# -----------------------------------------------------
# 2. Operadores relacionais
# -----------------------------------------------------
# ==  igual
# !=  diferente
# <   menor
# >   maior
# <=  menor ou igual
# >=  maior ou igual

# -----------------------------------------------------
# 3. Operadores lógicos
# -----------------------------------------------------
# and → todas as condições precisam ser verdadeiras
# or  → pelo menos uma condição precisa ser verdadeira
# not → inverte o valor lógico (True → False, False → True)
#
# Exemplo:
# idade = 20
# tem_carteira = True
#
# if idade >= 18 and tem_carteira:
#     print("Pode dirigir")

# =====================================================
# Exercícios do Dia 5
# =====================================================

# -----------------------------------------------------
# Exercício 1 — Cadastro simples
# -----------------------------------------------------
# Aqui usamos um IF/ELSE básico:
# - Se a idade for >= 18 → maior de idade
# - Caso contrário → menor de idade

nome = input("Me diga seu nome: ")         # pede o nome do usuário
idade = int(input("Qual a sua idade? "))   # pede a idade (convertida em número inteiro)

if idade >= 18:                            # condição: idade maior ou igual a 18
    print(f"{nome}, você é maior de idade!")  # se for verdadeiro
else:                                      # caso contrário
    print(f"{nome}, você ainda é menor de idade.")


# -----------------------------------------------------
# Exercício 2 — Calculadora com escolha
# -----------------------------------------------------
# Passos:
# 1. Ler dois números (float para aceitar decimais)
# 2. Perguntar a operação desejada
# 3. Usar IF/ELIF para decidir qual cálculo fazer
# 4. ELSE para tratar operação inválida

n1 = float(input("Diga um número: "))
n2 = float(input("Agora diga outro número: "))

op = input("Agora me diga que operação você quer executar: ").lower()  # .lower() deixa tudo minúsculo

if op == "soma":
    print(f"A soma é igual a: {n1 + n2}")
elif op == "subtração":
    print(f"A subtração é igual a: {n1 - n2}")
elif op == "multiplicação":
    print(f"A multiplicação é igual a: {n1 * n2}")
elif op == "divisão":
    if n2 != 0:                                     # proteção contra divisão por zero
        print(f"A divisão é igual a: {n1 / n2}")
    else:
        print("Não é possível dividir por zero!")
else:
    print("Operação inválida!")                     # caso o usuário digite algo diferente


# -----------------------------------------------------
# Exercício 3 — Sistema de notas
# -----------------------------------------------------
# Aqui temos 3 situações:
# - média < 6  → Reprovado
# - média entre 6 e 7.9 → Recuperação
# - média >= 8 → Aprovado com sucesso

media = float(input("Qual a média do aluno: "))

if media < 6:
    print("Reprovado!")
elif media < 8:                     # até 7.9
    print("Recuperação!")
else: 
    print("Aprovado com sucesso!")


# -----------------------------------------------------
# Exercício 4 — Login simples
# -----------------------------------------------------
# Objetivo: verificar usuário e senha
# - Usuário deve ser "admin"
# - Senha deve ser "1234"
# OBS: .lower() no usuário permite digitar "ADMIN", "Admin", etc.
#      Já a senha deve ser exatamente igual (sem .lower())

user = input("Digite o nome de usuário: ").lower()
senha = input("Agora digite a senha: ")

if user == "admin" and senha == "1234":   # duas condições ao mesmo tempo (and)
    print("Acesso Permitido!")
else:
    print("Usuário ou senha inválidos!")  # caso qualquer uma esteja errada


# -----------------------------------------------------
# Exercício 5 — Menu interativo
# -----------------------------------------------------
# Aqui usamos um LOOP (while True) para repetir até a opção 3 (sair).
# Estrutura do menu:
# [1] Ver cartão de visita → lê nome, profissão, cidade
# [2] Calcular média → lê 3 notas e mostra a média
# [3] Sair → encerra o programa com "break"

while True:
    print("========== MENU ==========")
    print("[1] Ver cartão de visita")
    print("[2] Calcular média")
    print("[3] Sair")
    print("==========================")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # cartão de visita
        nome = input("Nome: ")
        profi = input("Profissão: ")
        cidade = input("Cidade: ")

        print("_" * 25)
        print(f"Nome: {nome}")
        print(f"Profissão: {profi}")
        print(f"Cidade: {cidade}")
        print("_" * 25)
        print()  # apenas para dar espaço visual

    elif opcao == 2:
        # cálculo da média
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))

        media = (n1 + n2 + n3) / 3
        print(f"\nSua média é: {media:.2f}\n")

    elif opcao == 3:
        # sair do programa
        print("Saindo do programa... Até a próxima!")
        break

    else:
        print("Operação inválida! Tente de novo.\n")  # tratamento de erro
    

# =====================================================
# DIA 6 (05/10/2025) — Tipos de dados, Strings e Estruturas de decisão
# =====================================================
# Nas aulas 3 e 4 do curso, aprendemos:
# - Tipos de dados em Python
# - Entrada e saída de informações (input / print)
# - Manipulação de textos (strings)
# - Estruturas de decisão (if, elif, else)
# - Exercícios práticos com base em situações reais

# =====================================================
# 1) Tipos de dados em Python
# -----------------------------------------------------
# Cada valor em Python tem um tipo (type).
# Os mais comuns são:
#   int   → números inteiros (ex.: 10, -5, 1000)
#   float → números decimais (ex.: 3.14, -0.5, 2.0)
#   str   → textos (strings) (ex.: "Olá", 'Python', "123")
#   bool  → valores lógicos (True ou False)
#
# Você pode verificar o tipo de uma variável com:
#   type(nome_da_variavel)
#
# Exemplo:
#   idade = 25
#   print(type(idade))   # <class 'int'>
#
# Observação:
#   O Python converte tipos automaticamente em alguns casos,
#   mas é comum usarmos funções de conversão:
#   int()  → converte para inteiro
#   float() → converte para decimal
#   str()  → converte para texto

# =====================================================
# Exercício 0 — Tipos de dados
# -----------------------------------------------------
# Peça ao usuário para digitar:
# - Um número inteiro
# - Um número decimal
# - Um texto qualquer
# Em seguida, mostre na tela os valores e seus tipos usando a função type().

nint = int(input("Digite um número inteiro: "))   # converte o input para inteiro (int)
ndec = float(input("Digite um número decimal: ")) # converte o input para decimal (float)
text = input("Digite uma frase qualquer: ")       # entrada padrão (string)

# Exibe o valor e o tipo de cada variável
print(nint)              # mostra o valor inteiro digitado
print(type(nint))        # mostra o tipo <class 'int'>
print(ndec)              # mostra o valor decimal digitado
print(type(ndec))        # mostra o tipo <class 'float'>
print(text)              # mostra o texto digitado
print(type(text))        # mostra o tipo <class 'str'>

# Dica:
# type() → retorna o tipo do valor dentro dos parênteses.
# Isso ajuda muito quando estamos aprendendo conversões em Python.


# =====================================================
# 2) Entradas e saídas (revisão)
# -----------------------------------------------------
# input() → lê dados do usuário sempre como texto (string)
# print() → exibe mensagens e valores
#
# Dica: para usar valores numéricos em contas, converta o input
# para o tipo correto (int ou float).

# =====================================================
# Exercício 1 — Entrevista
# -----------------------------------------------------
# Crie um programa que faça perguntas a uma pessoa (simulando uma entrevista).
# Peça:
#   - Nome
#   - Idade
#   - Profissão
#   - Cidade
# E mostre uma frase final juntando tudo de forma organizada:
#   "Olá, <nome>! Você tem <idade> anos, é <profissão> e mora em <cidade>."

print("Seja Bem-Vindo à Sua Entrevista de Emprego")  # mensagem inicial

# Entradas de dados
nome = input("Comece me dizendo seu nome: ")         # nome (texto)
idade = int(input("Agora me diga sua idade: "))      # idade (convertida para número inteiro)
profi = input("Qual sua profissão? ")                # profissão (texto)
cidade = input("De qual cidade você é? ")            # cidade (texto)

# Saída de dados formatada com f-string
print(f"Olá, {nome}! Você tem {idade} anos, é {profi} e mora em {cidade}.")

# -----------------------------------------------------
# Dica:
# - f-string (f"...") permite inserir variáveis dentro do texto.
# - Você pode usar qualquer expressão dentro das chaves { }.
# Exemplo: print(f"{nome.upper()} tem {idade + 1} anos no próximo aniversário.")

# =====================================================
# 3) Manipulação de Strings
# -----------------------------------------------------
# Strings são textos entre aspas. Podemos manipulá-las de várias formas.
#
# Métodos mais comuns:
#   .upper()   → tudo maiúsculo
#   .lower()   → tudo minúsculo
#   .title()   → primeira letra de cada palavra em maiúsculo
#   .strip()   → remove espaços extras no início e fim
#   .replace("a", "@") → substitui partes do texto
#
# Outras funções úteis:
#   len(texto) → conta quantos caracteres tem o texto
#
# Exemplo:
#   nome = "  joão da silva  "
#   print(nome.strip().title())   # "João Da Silva"

# =====================================================
# Exercício 2 — Trabalhando com Strings
# -----------------------------------------------------
# Peça ao usuário que digite uma frase.
# Depois, mostre:
# - A frase em letras maiúsculas
# - A frase em letras minúsculas
# - A frase com apenas as iniciais maiúsculas
# - Quantos caracteres a frase tem (sem contar espaços extras)
# - Uma versão da frase sem espaços no início e no fim

frase = input("Me diga uma frase: ")  # entrada de texto do usuário

# Exibe diferentes transformações da frase
print("Sua frase com letras maiúsculas é:", frase.upper())   # tudo MAIÚSCULO
print("Sua frase com letras minúsculas é:", frase.lower())   # tudo minúsculo
print("Sua frase com iniciais maiúsculas é:", frase.title()) # primeira letra de cada palavra em maiúsculo
print("Essa é a quantidade de caracteres na sua frase:", len(frase))  # conta caracteres totais
print("Sua frase sem espaços no início e no fim é:", frase.strip())   # remove espaços extras

# -----------------------------------------------------
# Dica:
# - upper()  → transforma tudo em maiúsculo
# - lower()  → transforma tudo em minúsculo
# - title()  → inicial de cada palavra em maiúsculo
# - strip()  → remove espaços no início e no fim
# - len()    → conta quantos caracteres tem o texto


# =====================================================
# 4) Estruturas de decisão (if / elif / else)
# -----------------------------------------------------
# Com o if, o programa pode "escolher" o que fazer dependendo de uma condição.
#
# Exemplo:
#   nota = 8
#   if nota >= 7:
#       print("Aprovado!")
#   else:
#       print("Reprovado!")
#
# Também podemos usar elif (senão se):
#   if nota < 6:
#       print("Reprovado")
#   elif nota < 8:
#       print("Recuperação")
#   else:
#       print("Aprovado com sucesso")

# =====================================================
# Exercício 3 — Estrutura de decisão
# -----------------------------------------------------
# Peça ao usuário para digitar um número.
# Se for positivo, mostre "Número positivo".
# Se for negativo, mostre "Número negativo".
# Se for zero, mostre "O número é zero."

numero = int(input("Digite um número: "))  # lê um número inteiro

if numero >= 1:                             # se for maior ou igual a 1
    print("Este número é positivo")         # mensagem para números positivos
elif numero < 0:                            # se for menor que zero
    print("Este número é negativo")         # mensagem para negativos
else:                                       # caso contrário (é zero)
    print("O número é zero")                # mensagem para zero

# -----------------------------------------------------
# Dica:
# - 'if' é usado para a primeira condição.
# - 'elif' significa "senão se" → verifica outras possibilidades.
# - 'else' é executado quando nenhuma condição anterior é verdadeira.



# =====================================================
# DIA 7 (06/10/2025) — Continuação Aulas 3 e 4
# (strings + decisões + validações simples)
# =====================================================
# Hoje vamos reforçar:
# - Manipulação de strings em situações reais
# - Decisões com if/elif/else
# - Primeiras validações de entrada (sem complicar)
# - Programas curtos, bem “mão na massa”
#
# Lembrete:
#  - input() sempre retorna str → converta quando precisar (int/float)
#  - .strip() remove espaços das pontas
#  - .lower() / .upper() / .title() para normalizar textos
#  - len() conta caracteres

# =====================================================
# 1) Normalização de texto (revisão rápida)
# -----------------------------------------------------
# Exemplos úteis (rode para ver se quiser revisar, depois apague):
# nome = "  aNa cláuDia  "
# print(nome.strip().title())  # "Ana Cláudia"
# email = "  EXEMPLO@MAIL.COM "
# print(email.strip().lower()) # "exemplo@mail.com"

# =====================================================
# Exercício 1 — Cadastro com normalização
# -----------------------------------------------------
# Objetivo:
#   Ler nome completo, e-mail e cidade.
#   Mostrar um “resumo” com:
#     - Nome em Título (title)
#     - E-mail todo minúsculo e sem espaços nas pontas
#     - Cidade em Título
#   Dica: use .strip(), .title(), .lower()
#
# Passos sugeridos:
#   1) Ler nome, email, cidade
#   2) Normalizar (ex.: nome_fmt = nome.strip().title())
#   3) Imprimir um bloco formatado com os valores normalizados

# Conceitos usados:
#   .title() → deixa a primeira letra de cada palavra em maiúsculo
#   .lower() → transforma todas as letras em minúsculas
#   .strip() → remove espaços extras no início e fim do texto

nome = input("Digite seu nome: ")       # lê o nome completo
email = input("Digite seu e-mail: ")    # lê o e-mail do usuário
cidade = input("Digite a cidade: ")     # lê a cidade

# Saída formatada
print(f"Seu nome é: {nome.title()}")        # formata nome com iniciais maiúsculas
print(f"Seu e-mail é: {email.lower().strip()}")  # minúsculas e sem espaços extras
print(f"Sua cidade é: {cidade.title()}")    # cidade com iniciais maiúsculas
    

# =====================================================
# 2) Decisões com faixas e limites
# -----------------------------------------------------
# Relembrando padrão de faixas:
# if valor < A:
#     ...
# elif valor < B:   # aqui já sabemos que A <= valor < B
#     ...
# else:
#     ...           # valor >= B

# =====================================================
# Exercício 2 — Classificador de senha simples
# -----------------------------------------------------
# Objetivo:
#   Pedir uma senha (texto) e classificar por “força”:
#     - < 6 caracteres  -> "Fraca"
#     - 6 a 9           -> "Média"
#     - >= 10           -> "Forte"
#   Mostrar também a versão “oculta” da senha (mesmo número de * que o tamanho).
#   Dica: use len(senha) e "*" * len(senha)

# Conceitos usados:
#   len() → conta quantos caracteres há em uma string

senha = input("Digite sua senha: ")    # lê a senha digitada
caracteres = len(senha)                # conta o número de caracteres

# Estrutura condicional para classificar a senha
if caracteres < 6:
    print("Senha fraca")               # se for menor que 6
elif caracteres < 10:                  # entre 6 e 9
    print("Senha média")
else:                                  # 10 ou mais
    print("Senha forte")

# -----------------------------------------------------
# Dica:
# - len() sempre retorna um número inteiro.
# - Você também pode exibir a senha "oculta" com asteriscos:
#   print("*" * len(senha))
#   Isso mostra algo como: ********



# =====================================================
# 3) Pequenas validações de entrada (sem try/except)
# -----------------------------------------------------
# Estratégia inicial:
#   - Ler como texto
#   - Verificar com .isdigit() se é numérico inteiro
#   - Se não for, avisar que é inválido
#
# Exemplo:
# txt = input("Digite um número inteiro: ")
# if txt.isdigit():
#     n = int(txt)
#     print("ok:", n)
# else:
#     print("valor inválido!")

# =====================================================
# Exercício 3 — Idade válida
# -----------------------------------------------------
# Objetivo:
#   Perguntar a idade como string.
#   - Se não for composta apenas por dígitos → "Idade inválida"
#   - Caso contrário, converter para int e:
#       * < 12  → "Criança"
#       * 12-17 → "Adolescente"
#       * 18-64 → "Adulto"
#       * >= 65 → "Idoso"
#   Dicas:
#     - idade_txt.isdigit()
#     - Depois de converter, use faixas com if/elif/else

# Conceitos usados:
#   .isdigit() → retorna True se a string contiver apenas números.
#   int()      → converte o texto em número inteiro.

idade = input("Digite sua idade: ")     # lê a idade como texto

if idade.isdigit():                     # verifica se é composta apenas por números
    n = int(idade)                      # converte para inteiro
    print("Ok:", n)                     # exibe valor validado

    # Classificação por faixa etária
    if n < 12:
        print("Criança")
    elif n < 18:
        print("Adolescente")
    elif n < 65:
        print("Adulto")
    else:
        print("Idoso")

else:
    print("Valor inválido!")            # caso tenha letras ou caracteres especiais

# -----------------------------------------------------
# Dica:
# - .isdigit() ignora sinais (+, -) e pontos, então “12.5” ou “-3” não são válidos.
# - Para aceitar decimais ou negativos, precisaríamos usar try/except (em aulas futuras).


# =====================================================
# 4) Strings + decisões na prática (extensão de arquivo)
# -----------------------------------------------------
# Relembrando:
# arq = "foto.perfil.jpg"
# partes = arq.split(".")
# última extensão: partes[-1].lower()

# =====================================================
# Exercício 4 — Detector de extensão
# -----------------------------------------------------
# Objetivo:
#   Pedir o nome de um arquivo (ex.: "documento.PDF", "foto.png", "planilha.xls").
#   Mostrar:
#     - Nome base (sem a extensão)
#     - Extensão em minúsculas
#   Depois, decidir pelo tipo:
#     - "Imagem" se for jpg/jpeg/png/gif
#     - "Documento" se for pdf/doc/docx/txt
#     - "Planilha" se for xls/xlsx/csv
#     - Caso contrário: "Tipo desconhecido"
#   Dicas:
#     - Use .split(".") e pegue a última parte como extensão
#     - Use .lower() na extensão
#     - Base do nome: junte o que veio antes da última extensão (ou use rsplit(".", 1))

# Conceitos usados:
#   .split(".")  → separa o texto nas partes divididas por ponto
#   partes[-1]   → pega o último item da lista (a extensão)
#   .lower()     → transforma o texto em minúsculas
#   ".".join(...) → junta as partes da lista com ponto
#   in [lista]   → verifica se o valor está dentro de uma lista

arquivo = input("Digite o nome do arquivo: ")          # lê o nome completo do arquivo
partes = arquivo.split(".")                            # divide o nome em partes separadas pelo ponto
extensao = partes[-1].lower()                          # pega a última parte (extensão) e deixa minúscula
nome_base = ".".join(partes[:-1])                      # junta todas as partes antes da extensão

# Mostra as informações
print("Nome do arquivo:", nome_base)
print("Extensão:", extensao)

# Classificação do tipo de arquivo
if extensao in ["jpg", "jpeg", "png", "gif"]:
    print("Tipo: Imagem")
elif extensao in ["pdf", "doc", "docx", "txt"]:
    print("Tipo: Documento")
elif extensao in ["xls", "xlsx", "csv"]:
    print("Tipo: Planilha")
else:
    print("Tipo: Desconhecido!")

# -----------------------------------------------------
# Dica:
# - split() divide a string e retorna uma lista.
# - join() faz o inverso: junta os elementos da lista em uma string.
# - [-1] acessa o último item da lista, e [:-1] pega todos menos o último.
# - lower() evita erros com letras maiúsculas (como “JPG” ou “PDF”).



# =====================================================
# 5) Mini-programa com menu (versão simples)
# -----------------------------------------------------
# Estrutura típica:
# while True:
#     mostrar opções
#     ler opção
#     if ... elif ... elif ... else ...
#     break para sair

# =====================================================
# Exercício 5 — Menu utilitário de strings
# -----------------------------------------------------
# Objetivo:
#   Montar um menu em loop com as opções:
#     [1] Contar caracteres de uma frase
#     [2] Colocar frase em MAIÚSCULAS
#     [3] Colocar frase em minúsculas
#     [4] Voltar/Sair
#   Regras:
#     - Em [1], peça a frase e mostre len(frase)
#     - Em [2] e [3], peça a frase e mostre transformada
#     - Em [4], encerrar o loop
#     - Se a opção não for 1,2,3,4 → mensagem "Opção inválida"
#   Dica:
#     - Você pode ler a opção como string (sem converter) para simplificar as comparações

# Conceitos usados:
#   while True     → cria um loop infinito até que o break seja acionado
#   len(texto)     → retorna o número de caracteres na string
#   .upper()       → transforma todas as letras em maiúsculas
#   .lower()       → transforma todas as letras em minúsculas
#   break          → encerra o loop imediatamente

while True:
    # Exibição do menu
    print("========== MENU ==========")
    print("[1] Contar caracteres")
    print("[2] Colocar a frase em MAIÚSCULAS")
    print("[3] Colocar a frase em minúsculas")
    print("[4] Voltar/Sair")
    print("==========================")

    opcao = int(input("Escolha uma opção: "))  # lê a escolha do usuário

    # Opção 1 → contar caracteres
    if opcao == 1:
        carac = input("Digite sua frase: ")
        print("A sua frase tem", len(carac), "caracteres")  # len() conta os caracteres da frase

    # Opção 2 → transformar em MAIÚSCULAS
    elif opcao == 2:
        fraseM = input("Digite a frase: ")
        print("A frase fica:", fraseM.upper())  # .upper() transforma tudo em maiúsculas

    # Opção 3 → transformar em minúsculas
    elif opcao == 3:
        frasem = input("Digite sua frase: ")
        print("Sua frase fica:", frasem.lower())  # .lower() transforma tudo em minúsculas

    # Opção 4 → sair do menu
    elif opcao == 4:
        print("Saindo do menu... Até logo!")
        break

    # Qualquer outra opção → inválida
    else:
        print("Opção inválida! Tente novamente.\n")

# -----------------------------------------------------
# Dica:
# - Se quiser deixar o menu mais bonito, pode usar "\n" para quebrar linhas.
# - Também dá pra ler a opção como string (ex.: opcao = input(...)),
#   assim o programa não dá erro se o usuário digitar texto por engano.
    

# =====================================================
# 6) Bônus (opcional): formatação de nome e e-mail
# -----------------------------------------------------
# Objetivo:
#   Ler nome completo e email.
#   - nome_fmt = .strip().title()
#   - email_fmt = .strip().lower()
#   Mostrar:
#     "Usuário: <primeiro_nome>  Email: <email_fmt>"
#   Dicas:
#     - Para pegar o primeiro nome: nome_fmt.split()[0]
#     - Trate casos com espaços a mais usando .strip()

# Dicas:
#   - .strip() remove espaços no começo/fim.
#   - .title() capitaliza cada palavra (cuidado com nomes como "da", "dos" — serve para este nível).
#   - .lower() padroniza o e-mail.

# Entrada de dados
nome = input("Nome completo: ")
email = input("E-mail: ")

# Normalização / padronização
nome_fmt = nome.strip().title()       # Ex.: "  joão da silva  " -> "João Da Silva"
email_fmt = email.strip().lower()     # Ex.: "  EXEMPLO@MAIL.COM " -> "exemplo@mail.com"

# Primeiro nome (se houver palavras após o strip)
partes_nome = nome_fmt.split()        # divide por espaços
if len(partes_nome) > 0:
    primeiro_nome = partes_nome[0]
else:
    primeiro_nome = ""                # vazio se o usuário não digitou nada

# Saída
print("_" * 32)
print(f"Usuário: {primeiro_nome}")
print(f"Nome completo: {nome_fmt}")
print(f"E-mail: {email_fmt}")
print("_" * 32)

# -----------------------------------------------------
# Extras (opcionais):
# - Você pode validar se o e-mail contém "@" e "."
#   if "@" in email_fmt and "." in email_fmt: print("E-mail parece válido")
#   else: print("Atenção: e-mail pode estar incorreto")


# =====================================================
# DIA 8 (07/10/2025) — Introdução a Laços de Repetição
# =====================================================
# Hoje começamos a usar repetições (loops), que permitem
# executar blocos de código várias vezes sem precisar copiar.
#
# Vamos entender o uso de:
#   - while → repete enquanto uma condição for verdadeira
#   - for   → repete um número conhecido de vezes (ou percorre listas, textos, etc.)
#
# Também veremos:
#   - range() → gera uma sequência de números
#   - break  → interrompe o loop
#   - continue → pula para a próxima repetição

# =====================================================
# 1) Estrutura WHILE — repetição condicional
# -----------------------------------------------------
# while <condição>:
#     bloco a repetir enquanto a condição for verdadeira
#
# Exemplo:
# contador = 1
# while contador <= 5:
#     print("Contando:", contador)
#     contador += 1
#
# print("Fim!")

# =====================================================
# Exercício 1 — Contagem simples
# -----------------------------------------------------
# Objetivo:
#   Mostrar na tela uma contagem de 1 a 10.
# Dica:
#   Use uma variável contador e incremente com += 1
#   até chegar em 10.

contador = 1                          # início da contagem

while contador <= 10:                  # enquanto o contador for menor ou igual a 10
    print("Número:", contador)         # mostra o número atual
    contador += 1                      # incrementa o contador (soma +1 a cada volta)

print("Contagem finalizada!")          # mensagem final fora do loop

# =====================================================
# 2) Estrutura FOR — repetição com contador
# -----------------------------------------------------
# for <variável> in range(início, fim, passo):
#     bloco de código
#
# Exemplo:
# for i in range(1, 6):
#     print("Número:", i)
#
# range(1, 6) → gera [1, 2, 3, 4, 5]
#
# Observação:
# - O número final (fim) não é incluído.
# - Você pode usar range(10) para ir de 0 até 9.

# =====================================================
# Exercício 2 — Tabuada
# -----------------------------------------------------
# Objetivo:
#   Ler um número do usuário e mostrar a tabuada dele (1 a 10).
# Dica:
#   Use o for com range(1, 11)
#   Exemplo de saída:
#     5 x 1 = 5
#     5 x 2 = 10
#     ...
#     5 x 10 = 50

num = int(input("Digite um número para ver a tabuada: ")) # lê o número
print(f"Tabuada do {num}:")                               # título da tabuada
for i in range(1, 11):                                    # de 1 a 10
    print(f"{num} x {i} = {num * i}")                     # mostra a multiplicação
print("Tabuada finalizada!")                              # mensagem final
# Dica:
# - f-string (f"...") facilita a formatação da saída.
# - range(1, 11) gera números de 1 a 10 (11 não incluso).

# =====================================================
# 3) Controle de loops com BREAK e CONTINUE
# -----------------------------------------------------
# break → encerra o loop imediatamente.
# continue → pula a repetição atual e vai pra próxima.
#
# Exemplo:
# for i in range(1, 6):
#     if i == 3:
#         continue    # pula o número 3
#     print(i)
#
# Resultado: 1, 2, 4, 5

# =====================================================
# Exercício 3 — Contagem com pausa
# -----------------------------------------------------
# Objetivo:
#   Faça um loop que peça ao usuário para digitar números.
#   O programa deve continuar até que o usuário digite 0.
#   Quando digitar 0, o loop termina e mostra:
#       "Fim! Você digitou X números."
# Dica:
#   Use while True e break quando o número for 0.
#   Use um contador para contar quantos foram digitados.

contador = 0                          # contador de números digitados
while True:                           # loop infinito
    num = int(input("Digite um número (0 para sair): "))  # lê o número
    if num == 0:                      # se for 0, sai do loop
        break
    contador += 1                     # incrementa o contador
print(f"Fim! Você digitou {contador} números.")  # mostra quantos foram digitados
# Dica:
# - while True cria um loop que só termina com break.
# - Use um contador para rastrear quantas vezes o usuário entrou com um número diferente de 0.

# =====================================================
# 4) Trabalhando com Strings em loops
# -----------------------------------------------------
# Você pode percorrer cada letra de uma string usando:
# for letra in texto:
#     print(letra)
#
# Ou contar vogais, espaços, etc.

# =====================================================
# Exercício 4 — Contador de vogais
# -----------------------------------------------------
# Objetivo:
#   Ler uma frase do usuário e contar quantas vogais (a, e, i, o, u)
#   existem no texto, desconsiderando maiúsculas/minúsculas.
# Dica:
#   Use .lower() e um contador.
#   Para verificar se a letra é vogal:
#       if letra in "aeiou":

frase = input("Digite sua frase: ")        # pede a frase do usuário
frase = frase.lower().strip()              # normaliza o texto (minúsculas e sem espaços)
vogais = 0                                 # contador começa em zero

for letra in frase:                        # percorre cada letra da frase
    if letra in "aeiou":                   # se for vogal
        vogais += 1                        # soma 1 ao contador

print("Sua frase é:", frase)               # mostra a frase padronizada
print(f"Sua frase tem {vogais} vogais.")   # mostra quantas vogais foram encontradas

# -----------------------------------------------------
# Dica:
# - Você pode adicionar .count() em alternativa rápida:
#     total = sum(frase.count(v) for v in "aeiou")
# - Mas o método com o for é melhor pra entender a lógica de loops.



# =====================================================
# 5) Laços + Condições (combinação prática)
# -----------------------------------------------------
# Podemos combinar loops com if/else dentro deles para criar
# pequenas simulações e menus interativos.

# =====================================================
# Exercício 5 — Sistema de login com tentativas
# -----------------------------------------------------
# Objetivo:
#   Criar um sistema simples de login com até 3 tentativas.
#
# Regras:
#   - Usuário e senha corretos: "admin" e "1234"
#   - Se acertar → "Acesso permitido"
#   - Se errar 3 vezes → "Acesso bloqueado"
#
# Dica:
#   Use um contador dentro de um while e o comando break
#   quando o login for bem-sucedido.

# Conceitos usados:
#   - while tentativas > 0  → repete enquanto ainda há tentativas
#   - break → encerra o loop imediatamente
#   - -= 1 → subtrai 1 da variável

usuario_correto = "admin"      # usuário autorizado
senha_correta = "1234"         # senha autorizada

tentativas = 3                 # número máximo de tentativas

while tentativas > 0:          # repete enquanto ainda há tentativas
    user = input("Usuário: ")  # pede usuário
    senha = input("Senha: ")   # pede senha

    if user == usuario_correto and senha == senha_correta:
        print("Acesso permitido!")
        break                  # sai do loop se estiver correto
    else:
        tentativas -= 1        # reduz uma tentativa
        print("Acesso negado! Tente novamente.")
        print(f"Tentativas restantes: {tentativas}\n")

        if tentativas == 0:    # se acabar as tentativas
            print("Acesso bloqueado! Tente novamente mais tarde.")
        

# =====================================================
# 6) Bônus — Soma de múltiplos de 3
# -----------------------------------------------------
# Objetivo:
#   Some todos os números de 1 a 50 que sejam múltiplos de 3.
# Dica:
#   Use for com range(1, 51) e o operador % (módulo).
#   if número % 3 == 0 → é múltiplo de 3.

total = 0                          # acumulador para a soma
for num in range(1, 51):           # de 1 a 50
    if num % 3 == 0:               # verifica se é múltiplo de 3
        total += num               # soma ao total
print("A soma dos múltiplos de 3 entre 1 e 50 é:", total)  # mostra o resultado
# Dica:
# - O operador % retorna o resto da divisão.
# - Se o resto for 0, significa que é múltiplo (ex.: 9 % 3 == 0).
# - Você pode mudar o range para outros intervalos conforme desejar.


# =====================================================
# DIA 9 (08/10/2025) — Homework: Revisão Aulas 3 e 4
# =====================================================
# Objetivo:
#   Revisar os principais conceitos das aulas 3 e 4:
#   - Tipos de dados, strings, condicionais, loops e formatação
# =====================================================

# =====================================================
# Exercício 1 — Conversor de Temperatura
# =====================================================
# Fórmula:
#   F = (C × 9/5) + 32

celsius = float(input("Temperatura em °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.1f}°C equivalem a {fahrenheit:.1f}°F")

# -----------------------------------------------------
# Dica:
# - float() permite entrada com decimais
# - f-string com :.1f mostra uma casa decimal
# - Fórmula inversa seria: C = (F - 32) * 5/9
# =====================================================


# =====================================================
# Exercício 2 — Contador de Palavras
# =====================================================

frase = input("Digite uma frase: ")
frase_limpa = frase.strip().lower()          # remove espaços e padroniza
palavras = frase_limpa.split()               # separa as palavras em lista
total_palavras = len(palavras)               # conta as palavras
caracteres = len(frase_limpa.replace(" ", ""))  # remove espaços e conta letras
letras_a = frase_limpa.count("a")            # conta quantos 'a' aparecem

print(f"A frase tem {total_palavras} palavras, {caracteres} caracteres e {letras_a} letras 'a'.")

# -----------------------------------------------------
# Dica:
# - .split() separa por espaços
# - .replace(" ", "") tira os espaços
# - .count("a") conta todas as letras “a”
# =====================================================


# =====================================================
# Exercício 3 — Verificador de Número Par ou Ímpar
# =====================================================

num = int(input("Digite um número: "))
if num % 2 == 0:
    print("Este número é PAR.")
else:
    print("Este número é ÍMPAR.")

# -----------------------------------------------------
# Dica:
# - Operador % (módulo) mostra o resto da divisão.
# - Se o resto for 0 → é par.
# =====================================================


# =====================================================
# Exercício 4 — Média com Situação Final
# =====================================================

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media:.2f} — Situação: {situacao}")

# -----------------------------------------------------
# Dica:
# - Estrutura em faixas: >= 7 / >= 5 / else.
# - :.2f → duas casas decimais.
# =====================================================


# =====================================================
# Exercício 5 — Analisador de Idade
# =====================================================

nomes = []
idades = []

for i in range(5):
    nome = input(f"Nome da {i+1}ª pessoa: ")
    idade = int(input(f"Idade da {i+1}ª pessoa: "))
    nomes.append(nome)
    idades.append(idade)
    print("-" * 25)

media_idades = sum(idades) / len(idades)
mais_velho = nomes[idades.index(max(idades))]
mais_novo = nomes[idades.index(min(idades))]

print(f"Média das idades: {media_idades:.1f}")
print(f"Mais velho: {mais_velho} ({max(idades)} anos)")
print(f"Mais novo: {mais_novo} ({min(idades)} anos)")

# -----------------------------------------------------
# Dica:
# - .append() adiciona valores em listas.
# - sum(lista) soma os elementos numéricos.
# - max() e min() retornam o maior e o menor valor.
# =====================================================


# =====================================================
# Exercício 6 — Gerador de Cupom Fiscal
# =====================================================

cliente = input("Nome do cliente: ")
produto = input("Produto: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço unitário: "))

total = quantidade * preco

print("=" * 30)
print(f"CLIENTE: {cliente}")
print(f"PRODUTO: {produto}")
print(f"QUANTIDADE: {quantidade}")
print(f"TOTAL: R${total:.2f}")
print("=" * 30)

# -----------------------------------------------------
# Dica:
# - Use multiplicação para o total.
# - f-string com :.2f formata em reais (2 casas decimais).
# =====================================================


# =====================================================
# DESAFIO FINAL — Simulador de Caixa de Loja
# =====================================================

nomes = []
valores = []
quantidades = []

while True:
    nome = input("Nome do produto (ou 'fim' para encerrar): ").strip().title()
    if nome.lower() == "fim":
        break
    preco = float(input("Preço unitário: R$"))
    qtd = int(input("Quantidade: "))

    nomes.append(nome)
    valores.append(preco * qtd)
    quantidades.append(qtd)
    print("-" * 30)

# Resumo final
print("\n===== RESUMO DA COMPRA =====")
print(f"Itens comprados: {len(nomes)}")
print(f"Total de produtos: {sum(quantidades)}")
print(f"Valor total: R${sum(valores):.2f}")
print(f"Produto mais caro: {nomes[valores.index(max(valores))]}")
print("=" * 30)

# -----------------------------------------------------
# Dica:
# - while True + break cria o loop infinito controlado.
# - .append() adiciona os dados nas listas.
# - .index(max(valores)) encontra o produto mais caro.
# =====================================================
