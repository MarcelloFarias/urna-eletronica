def iniciaVotacao():
    candidato1 = ['Domingos', 90]
    candidato2 = ['Quiabinho', 41]
    candidato3 = ['Marinalvinha', 60]
    contagemCandidato1 = 0
    contagemCandidato2 = 0
    contagemCandidato3 = 0
    votosValidos = 0
    votosBrancos = 0
    votosNulos = 0
    eleitores = 0
    while True:
        numero = int(input('Digite o número do seu candidato a prefeito, ou digite "0" para votar em branco: '))
        
        eleitores += 1
        if numero == candidato1[1]:
            votosValidos += 1
            contagemCandidato1 += 1
        elif numero == candidato2[1]:
            votosValidos += 1
            contagemCandidato2 += 1
        elif numero == candidato3[1]:
            votosValidos += 1
            contagemCandidato3 += 1
        elif numero == 0:
            votosBrancos += 1
        else:
            votosNulos += 1
        
        if numero == 2002:
            eleitores -= 1
            votosNulos -= 1
            maisVotado = contagemCandidato1
            if contagemCandidato2 > maisVotado:
                maisVotado = contagemCandidato2
            elif contagemCandidato3 > maisVotado:
                maisVotado = contagemCandidato3
            
            if maisVotado == contagemCandidato1:
                maisVotado = candidato1[0]
            elif maisVotado == contagemCandidato2:
                maisVotado = candidato2[0]
            else:
                maisVotado = candidato3[0]

            return print(f'\n--------------RESULTADO------------\nEleitores que compareceram: {eleitores}\nVotos válidos: {votosValidos}\nVotos nulos: {votosNulos}\nVotos em branco: {votosBrancos}\nNúmero de votos do candidato {candidato1[0]}: {contagemCandidato1}\nNúmero de votos do candidato {candidato2[0]}: {contagemCandidato2}\nNúmero de votos do candidato {candidato3[0]}: {contagemCandidato3}\nO candidato eleito foi: {maisVotado}')

iniciaVotacao()