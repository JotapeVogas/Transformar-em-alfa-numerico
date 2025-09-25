palavras = [
    'cachorro', 'casa', 'lua', 'mar', 'rio', 'flor', 'livro', 
    'verde', 'feliz', 'pequeno', 'rapido', 'lento', 'forte', 
    'doce', 'carro', 'navio', 'montanha', 'floresta', 'chuva', 
    'neve', 'vento', 'praia', 'ponte', 'cidade', 'vila', 
    'passaro', 'peixe', 'leao', 'macaco', 'cobra', 'cavalo', 
    'vaca', 'porco', 'formiga', 'porta', 'janela', 'parede', 
    'quarto', 'cozinha', 'cama', 'mesa', 'cadeira', 'lampada', 
    'computador', 'radio', 'relogio', 'caneta', 'lapis', 'papel', 
    'caderno', 'quadro', 'pintura', 'jogo', 'roupa', 'chapeu', 
    'camisa', 'calca', 'vestido', 'meia', 'luva', 'dinheiro', 
    'professor', 'livraria', 'mercado', 'loja', 'festa', 'musica', 
    'filme', 'canto', 'viagem', 'metro', 
    'motocicleta', 'hospital', 'medico', 'dor', 'raiva', 'medo',
    'coragem', 'paz', 'familia', 'mae', 'filho', 'filha', 'primo', 
    'prima', 'vizinho', 'pessoa', 'homem', 'mulher', 'crianca', 
    'jovem', 'rei', 'rainha', 'principe', 'heroi', 'vilao', 
    'policia', 'ladrao', 'juiz', 'cantor'
]
palavras_copia = [
    'cachorro', 'casa', 'lua', 'mar', 'rio', 'flor', 'livro', 
    'verde', 'feliz', 'pequeno', 'rapido', 'lento', 'forte', 
    'doce', 'carro', 'navio', 'montanha', 'floresta', 'chuva', 
    'neve', 'vento', 'praia', 'ponte', 'cidade', 'vila', 
    'passaro', 'peixe', 'leao', 'macaco', 'cobra', 'cavalo', 
    'vaca', 'porco', 'formiga', 'porta', 'janela', 'parede', 
    'quarto', 'cozinha', 'cama', 'mesa', 'cadeira', 'lampada', 
    'computador', 'radio', 'relogio', 'caneta', 'lapis', 'papel', 
    'caderno', 'quadro', 'pintura', 'jogo', 'roupa', 'chapeu', 
    'camisa', 'calca', 'vestido', 'meia', 'luva', 'dinheiro', 
    'professor', 'livraria', 'mercado', 'loja', 'festa', 'musica', 
    'filme', 'canto', 'viagem', 'metro', 
    'motocicleta', 'hospital', 'medico', 'dor', 'raiva', 'medo',
    'coragem', 'paz', 'familia', 'mae', 'filho', 'filha', 'primo', 
    'prima', 'vizinho', 'pessoa', 'homem', 'mulher', 'crianca', 
    'jovem', 'rei', 'rainha', 'principe', 'heroi', 'vilao', 
    'policia', 'ladrao', 'juiz', 'cantor'
]

letras_trocas = ['a', 'b', 's', 'g', 'z', 'i', 'e', 't', 'o']

palavras_proibidas = []
contador_palavras = 0
contador_palavras_repetidas = 0
for palavra in palavras:
    palavras_copia.remove(palavra)
    if palavra in palavras_copia:
        contador_palavras_repetidas += 1
    if palavra[0] not in letras_trocas:
        contador_palavras += 1
        continue
    else:
        palavras_proibidas.append(palavra)
print(f"Palavras que tem em lista palavras mas não na lista palavras_copia: {palavras_copia}")
print(f"Palavras proibidas: {palavras_proibidas}")
print(f"Total de palavras: {contador_palavras}")
print(f"Total de palavras repetidas: {contador_palavras_repetidas}")