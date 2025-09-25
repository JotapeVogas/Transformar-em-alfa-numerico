import random

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
    resultado = ""
    for letra in texto.lower():

        if letra in trocas:
            resultado += trocas[letra]
        else:
            resultado += letra
    
    return resultado

def gerador_senha_memoravel(num_palavras=4, separador="-"):

    palavras = [
    "gato", "cachorro", "casa", "sol", "lua", "mar", "rio", "flor",
    "livro", "tempo", "amigo", "verde", "azul", "bom", "feliz", "grande",
    "pequeno", "rapido", "lento", "forte", "doce", "sal", "fogo", "agua",
    "carro", "aviao", "barco", "montanha", "arvore", "floresta", "chuva", "neve",
    "vento", "areia", "praia", "ilha", "estrada", "ponte", "cidade", "vila",
    "passaro", "peixe", "leao", "tigre", "elefante", "macaco", "cobra", "cavalo",
    "galinha", "boi", "vaca", "porco", "abelha", "borboleta", "formiga", "aranha",
    "porta", "janela", "parede", "telhado", "escada", "quarto", "sala", "cozinha",
    "banheiro", "cama", "mesa", "cadeira", "sofa", "tapete", "espelho", "lampada",
    "computador", "telefone", "televisao", "radio", "relogio", "caneta", "lapis", "papel",
    "caderno", "quadro", "pintura", "bola", "brinquedo", "jogo", "roupa", "sapato",
    "chapeu", "bolsa", "camisa", "calca", "saia", "vestido", "meia", "luva",
    "dinheiro", "trabalho", "escola", "professor", "aluno", "livraria", "mercado", "loja",
    "festa", "musica", "danca", "filme", "teatro", "arte", "canto", "poesia",
    "viagem", "onibus", "metro", "trem", "bicicleta", "motocicleta", "taxi", "hospital",
    "medico", "enfermeiro", "remedio", "farmacia", "saude", "doenca", "dor", "alegria",
    "tristeza", "raiva", "medo", "coragem", "esperanca", "paz", "guerra", "amor",
    "odio", "beijo", "abraco", "familia", "pai", "mae", "filho", "filha",
    "irmao", "irma", "avo", "tia", "tio", "primo", "prima", "sobrinho",
    "sobrinha", "vizinho", "pessoa", "homem", "mulher", "crianca", "bebe", "jovem",
    "adulto", "idoso", "rei", "rainha", "principe", "princesa", "heroi", "vilao",
    "soldado", "policia", "ladrao", "juiz", "advogado", "engenheiro", "arquiteto", "cantor",
    "ator", "atriz", "pintor", "escritor", "poeta", "cozinheiro", "motorista", "jardineiro",
    "profissao", "trabalhador", "chefe", "lider", "estudante", "universidade", "faculdade", "ciencia",
    "matematica", "historia", "geografia", "fisica", "quimica", "biologia", "astronomia", "planeta",
    "estrela", "galaxia", "universo", "terra", "marte", "jupiter", "saturno", "urano",
    "netuno", "plutao", "cometa", "meteoro", "astro", "ceu", "horizonte", "nuvem",
    "clima", "tempestade", "trovao", "raio", "relampago", "furacao", "terremoto", "vulcao",
    "lava", "deserto", "oasis", "campo", "fazenda", "horta", "colheita", "semente",
    "fruto", "legume", "verdura", "maca", "banana", "laranja", "uva", "melancia",
    "abacaxi", "limao", "manga", "morango", "pera", "pessego", "coco", "tomate",
    "batata", "cenoura", "abobora", "milho", "arroz", "feijao", "trigo", "pao",
    "bolo", "sorvete", "chocolate", "mel", "cafe", "cha", "suco", "leite",
    "queijo", "carne", "ovo", "azeite", "oleo", "acucar", "salada", "sopa",
    "pizza", "macarrao", "hamburguer", "lanche", "sobremesa", "garfo", "faca", "colher",
    "prato", "copo", "garrafa", "panela", "frigideira", "forno", "fogao", "geladeira",
    "microondas", "dicionario", "revista", "jornal", "mapa", "globo", "atlas", "tela",
    "projetor", "cadeado", "chave", "fechadura", "corrente", "cadeia", "prisao", "cela",
    "tribunal", "palacio", "castelo", "igreja", "templo", "mesquita", "sinagoga", "catedral",
    "monasterio", "mosteiro", "capela", "altar", "parque", "jardim", "praia", "ilha",
    "grama", "rocha", "pedra", "areia", "mineral", "ferro", "aco", "ouro",
    "prata", "bronze", "cobre", "diamante", "cristal", "vidro", "plastico", "papelao",
    "madeira", "tijolo", "cimento", "argila", "barro", "poeira", "gelo", "neblina",
    "fumaça", "polen", "seiva", "folha", "raiz", "tronco", "galho", "fruta",
    "rosa", "margarida", "girassol", "lirio", "tulipa", "orquidea", "violeta", "hortensia",
    "alecrim", "salsa", "cebola", "alho", "pimenta", "coentro", "ervilha", "soja",
    "trator", "navio", "canoa", "remo", "vela", "motor", "tanque", "aviao",
    "helice", "asa", "roda", "pneu", "freio", "volante", "buzina", "porta",
    "janela", "vidro", "teto", "asfalto", "poste", "fios", "cabo", "rede",
    "internet", "site", "pagina", "blog", "email", "senha", "conta", "perfil",
    "foto", "video", "filme", "seriado", "serie", "drama", "humor", "comedia",
    "terror", "acao", "aventura", "romance", "ficcao", "jornalista", "reporter", "editor",
    "pintura", "escultura", "quadro", "arte", "tecido", "linha", "agulha", "botao",
    "tesoura", "fio", "barroco", "moda", "estilo", "cor", "forma", "tamanho",
    "peso", "altura", "largura", "profundidade", "volume", "area", "tempo", "espaco",
    "segundo", "minuto", "hora", "dia", "semana", "mes", "ano", "seculo",
    "milhar", "numero", "soma", "conta", "subtracao", "divisao", "multiplicacao", "potencia",
    "raiz", "equacao", "formula", "grafo", "mapa", "linha", "ponto", "circulo",
    "quadrado", "retangulo", "triangulo", "poligono", "cubo", "esfera", "cilindro", "cone",
    "piramide", "prisma", "energia", "luz", "sombra", "calor", "som", "eco",
    "onda", "particula", "atomo", "molecula", "celula", "tecido", "orgao", "sistema",
    "corpo", "mente", "alma", "espirito", "coracao", "sangue", "osso", "pele",
    "cabelo", "unha", "dente", "olho", "nariz", "orelha", "boca", "lingua",
    "mao", "braco", "perna", "pe", "dedo", "cabeca", "ombro", "joelho",
    "costa", "peito", "barriga", "estomago", "pulmao", "figado", "rim", "musculo",
    "nervo", "cerebro", "memoria", "ideia", "pensamento", "sonho", "realidade", "verdade",
    "mentira", "justica", "direito", "lei", "governo", "estado", "pais", "nacao",
    "cidade", "bairro", "rua", "praca", "avenida", "mercado", "loja", "supermercado",
    "padaria", "farmacia", "banco", "igreja", "esquina", "predio", "cobertura", "apartamento",
    "quarto", "sala", "cozinha", "garagem", "varanda", "quintal", "chamine", "telhado"
    ]
    
    palavras_selecionadas = random.sample(palavras, num_palavras)
    
    senha = separador.join(palavras_selecionadas)
    
    return senha.capitalize()

if __name__ == "__main__":
    palavra = gerador_senha_memoravel()
    resultado = converter_texto(palavra)
    print(f"Original: {palavra}")
    print(f"Convertido: {resultado}")