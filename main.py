import random

trocas = {
    'a': '4',
    'b': '8', 
    's': '5',
    'g': '6',
    'z': '2',
    'i': '1',
    'e': '3',
    't': '7',
    'o': '0'
}
letras_trocas = [
    'a', 'b', 's', 'g', 'z', 'i', 'e', 't', 'o'
]
palavras =  [
    'cachorro', 'casa', 'lua', 'mar', 'rio', 'flor', 'livro', 
    'verde', 'feliz', 'pequeno', 'rapido', 'lento', 'forte', 
    'doce', 'carro', 'navio', 'montanha', 'floresta', 'chuva', 
    'neve', 'vento', 'praia', 'ponte', 'cidade', 'vila', 
    'passaro', 'peixe', 'leao', 'macaco', 'cobra', 'cavalo', 
    'vaca', 'porco', 'formiga', 'porta', 'janela', 'parede', 
    'quarto', 'cozinha', 'cama', 'mesa', 'cadeira', 'lampada', 
    'computador', 'radio', 'relogio', 'caneta', 'lapis',
    'papel', 'caderno', 'quadro', 'pintura', 'jogo', 'roupa',
    'chapeu', 'camisa', 'calca', 'vestido', 'meia', 'luva',
    'dinheiro', 'professor', 'livraria', 'mercado', 'loja',
    'festa', 'musica', 'filme', 'canto', 'viagem', 'metro', 
    'motocicleta', 'hospital', 'medico', 'dor', 'raiva', 'medo',
    'coragem', 'paz', 'familia', 'mae', 'filho', 'filha', 'primo', 
    'prima', 'vizinho', 'pessoa', 'homem', 'mulher', 'crianca', 
    'jovem', 'rei', 'rainha', 'principe', 'heroi', 'vilao', 
    'policia', 'ladrao', 'juiz', 'cantor'
]

def testar_lista_palavras():
    global trocas, letras_trocas, palavras
    palavras_copia = palavras.copy()

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
    if len(palavras_proibidas) > 0 or contador_palavras_repetidas > 0:
        print("Erro na lista de palavras!")
        print(f"Palavras proibidas: {palavras_proibidas}")
        print(f"Total de palavras: {contador_palavras}")
        print(f"Total de palavras repetidas: {contador_palavras_repetidas}")

def converter_texto(texto):
    global trocas, letras_trocas, palavras
    contador_caracteres = 0
    resultado = ""
    for letra in texto.lower():
        if contador_caracteres == 0:
            resultado += letra.upper()
            contador_caracteres += 1
        elif letra in trocas:
            resultado += trocas[letra]
        else:
            resultado += letra
    
    return resultado

def gerador_senha_memoravel(num_palavras=4, separador="-"):
    global trocas, letras_trocas, palavras

    palavras_selecionadas = random.sample(palavras, num_palavras)
    
    senha = separador.join(palavras_selecionadas)
    
    return senha

if __name__ == "__main__":
    testar_lista_palavras()
    palavra = gerador_senha_memoravel()
    resultado = converter_texto(palavra)
    print(f"Original: {palavra}")
    print(f"Convertido: {resultado}")