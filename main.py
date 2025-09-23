def converter_texto(texto):
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
    contador_upper = 0
    resultado = ""
    for letra in texto.lower():
        if letra.isalpha() and contador_upper == 0:
            letra = letra.upper()
            contador_upper += 1
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