
import corpus


def main():
    bancodedados = open('frases.txt', 'r')

    contador = 0

    for line in bancodedados.readlines():
        if line != '\n':
            contador += 1
            if line.startswith('Hdt.'):
                autor = 'Hdt.'
                line = line[5:]
                line = line.split(' ', 1)
                numeracao = line[0]
                passagem = line[1]
                corpus.main(autor=autor, numeracao=numeracao, passagem=passagem, trabalho='Hist.')
            elif line.startswith('Xen.'):
                autor = 'Xen.'
                line = line[5:]
                line = line.split(' ', 2)
                trabalho = line[0]
                numeracao = line[1]
                passagem = line[2]
                corpus.main(autor=autor, numeracao=numeracao, passagem=passagem, trabalho=trabalho)
            elif line.startswith('Plat.'):
                autor = 'Plat.'
                line = line[6:]
                line = line.split(' ', 2)
                trabalho = line[0]
                numeracao = line[1]
                passagem = line[2]
                corpus.main(autor=autor, numeracao=numeracao, passagem=passagem, trabalho=trabalho)

    print(contador)

    bancodedados.close()


main()
