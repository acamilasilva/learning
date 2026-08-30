print("~~SEJA BEM VINDO(A) AO QUIZ~~")
answer_user = input ("Deseja começar? (S/N)")
print(answer_user)

if answer_user != "S":
    quit()

score = 0 

print("Começando...")
print("Qual jogo originou o gênero Battle Royale moderno? \n (A) Fortnite  \n (B) Apex Legends \n (C) PUBG  \n")
answer_1 = input("RESPOSTA: ")

if answer_1 == "C":
    print("CORRETO =D")
    score = score + 1
else:
    print("INCORRETO =C O PUBG que popularizou e estabeleceu as bases do gênero Battle Royale moderno na indústria.")

print("Em qual ano foi lançado o primeiro console Playstation? \n (A) 1991  \n (B) 1994 \n (C) 2002 \n")
answer_2 = input("RESPOSTA: ")

if answer_2 == "B":
    print("CORRETO =D")
    score = score + 1
else:
    print("INCORRETO =C O primeiro console PlayStation foi lançado no Japão em Dezembro de 1994.")

print("Qual empresa criou  famosa franquia de jogos Zelda? \n (A) SEGA \n (B) CAPCOM \n (C) NINTENDO \n")
answer_3 = input("RESPOSTA:")

if answer_3 == "C":
    print("CORRETO =D")
    score = score + 1 
else:
    print("INCORRETO =C The Legend Of Zelda é uma das principais franquias desenvolvidas pela Nintendo.")

print("Qual é o nome do protagonista de God Of War \n (A) Kratos (B) Ares (C) Perseu \n")
answer_4 = input("RESPOSTA:")

if answer_4 == "A":
    print("CORRETO =D VOCÊ TA INDO MUITO BEM!!")
    score = score + 1 
else:
    print("INCORRETO =C MAS NÃO DESANIMA! Kratos é o protagonista do God Of War.")

print("No universo Pokémon , qual é o Pokémon número 001 da Pokédex Nacional? \n (A) Caterpie \n (B) Squirtle \n (C) Bulbasaur \n")
answer_5 = input("RESPOSTA:")

if answer_5 == "C":
    print("CORRETO =D MANDOU BEM!!! >_<")
    score = score + 1 
else:
    print("INCORRETO =C Não foi dessa vez :/ O Pokémon número 001 na Pokédex Nacional é o Bulbasaur")

print("FINAL DO QUIZ :D Isso é tudo até aqui \n Deseja ver sua pontuação final? (S/N) \n")
answer_6 = input("RESPOSTA:")

if answer_6 == "S":
    print(f"OBA =D SUA PONTUAÇÃO FINAL FOI DE {score}/5 MANDOU MUITO BEM!! ATÉ A PRÓXIMA JOGADOR ;D")
else:
    print("TUDO BEM ENTÃO! ATÉ A PRÓXIMA JOGADOR =D")
    
