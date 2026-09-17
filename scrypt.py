lista = [
    (3, 'Anna'), (10, 'Bruno'), (15, 'Carlos'), (18, 'Daniela'), (19, 'Eduardo'),
    (28, 'Fernanda'), (33, 'Gustavo'), (35, 'Helena'), (43, 'Igor'), (48, 'Juliana'),
    (58, 'Kleber'), (83, 'Larissa'), (84, 'Marcos'), (86, 'Natália'), (97, 'Otávio'),
    (104, 'Patrícia'), (106, 'Rafael'), (115, 'Sabrina'), (120, 'Thiago'), (122, 'Vanesa'),
    (127, 'Amanda'), (143, 'Breno'), (147, 'Camila'), (149, 'Diego'), (151, 'Eliane'),
    (175, 'Fabiano'), (179, 'Gabriela'), (184, 'Henrique'), (187, 'Isabella'), (194, 'João'),
    (199, 'Karen'), (201, 'Leonardo'), (211, 'Mirella'), (213, 'Nicolas'), (232, 'Olívia'),
    (241, 'Pedro'), (244, 'Queila'), (246, 'Rodrigo'), (256, 'Simone'), (258, 'Túlio'),
    (259, 'Ursula'), (261, 'Victor'), (269, 'Wesley'), (273, 'Xênia'), (278, 'Yasmin'),
    (280, 'Zeca'), (288, 'Alana'), (291, 'Caio'), (292, 'Diana'), (294, 'Fábio')
]

def pesquisa_binaria(lista, numero):
    baixo = 0
    alto = len(lista) - 1
    tentativas = 0

    while baixo <= alto:
        meio = (baixo + alto) // 2
        tentativas += 1

        if lista[meio][0] == numero:
            return lista[meio][1], tentativas

        elif lista[meio][0] < numero:
            baixo = meio + 1

        else:
            alto = meio - 1

    return None, tentativas

nome, tentativas = pesquisa_binaria(lista, 256)

print("O nome associado ao número 256 é:", nome)
print("Foram feitas", tentativas, "tentativas na pesquisa binária.")
