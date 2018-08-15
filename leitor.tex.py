
import corpus


def main():
    bancodedados = open('frases.txt', 'r')

    contador = 0

    for line in bancodedados.readlines():
        if line != '\n':
            contador += 1
            line = line.split(' ', 3)
            autor = line[0]
            trabalho = line[1]
            numeracao = line[2]
            passagem = line[3]
            # corpus.main(autor=autor, numeracao=numeracao, passagem=passagem, trabalho=trabalho)
    print(contador)

    bancodedados.close()


main()
