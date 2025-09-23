def converter_texto(texto):
    trocas = {
        'A': '4',
        'B': '8', 
        'S': '5',
        'G': '6',
        'Z': '2',
        'I': '1',
        'E': '3',
        'T': '7',
        'O': '0'
    }
    
    resultado = ""
    for letra in texto.upper():
        if letra in trocas:
            resultado += trocas[letra]
        else:
            resultado += letra
    
    return resultado

if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    resultado = converter_texto(palavra)
    
    print(f"Original: {palavra}")
    print(f"Convertido: {resultado}")