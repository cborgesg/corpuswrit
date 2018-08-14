"""

Esse script abre um prompt no qual pede os parâmetros:
    Identificador:
            - Autor
            - Título
            - Numeração
    Passagem:
            - Passagem
            - Glosa
            - Tradução
    Atração
    Informação morfológica:
            - Verbo principal:
                    - Diátese
                    - Transitividade
                    - Pessoal / Impessoal
                        - Sujeito explícito? se pessoal = True
            - Verbo infinitivo:
                    - É cópula?
                    - Diátese
                    - Transitividade
            - Beneficiário / Alvo:
                    - Número
                    - Caso
                    - Gênero
                    - É pronominal ou nominal?
            - Adjunto:
                    - Número
                    - Caso
                    - Gênero
                    - Participial, substantivo ou adjetival?
            - Distância Ben-Adj

O script armazena as informações e por append adiciona elas ao arquivo corpus.tex em formato LaTeX

"""


def get_boll(mensagem='Sim ou não?'):
    while True:
        try:
            return {"sim": True, "não": False}[input(mensagem + '\n').lower()]
        except KeyError:
            print("Resposta inválida, digite Sim ou Não!")


def autor_init(autor=None,
               trabalho=None,
               numeracao=0):

    # Inicializa lista com as possibilidades de autor:

    autor_plat = ['Platão', 'Plato', 'Plat', 'Plat.', 'PLAT', 'plat.', 'plat']
    autor_xen = ['Xenofonte', 'Xenophon', 'Xen.', 'Xe.', 'XEN', 'Xen', 'xen.', 'xen']
    autor_hdt = ['Heródoto', 'Herodotus', 'Hdt', 'Hdt.', 'HDT', 'hdt', 'hdt.']
    autores = autor_hdt + autor_plat + autor_xen

    # Prompt autor

    while autor not in autores:
        print('Autor não identificado\n')
        autor = input("Autor?\n")

    if autor in autor_hdt:
            autor = 'Hdt.'
            trabalho = 'Hist.'

    if autor in autor_xen:
        autor = 'Xen.'
        trabalhos = ['Cyrop.']
        while trabalho not in trabalhos:
            print('Trabalho não identificado\n')
            trabalho = input("Trabalho?\n" + str(trabalhos) + '\n')

    if autor in autor_plat:
        autor = 'Plat.'
        trabalhos = ['Apol.']
        while trabalho not in trabalhos:
            print('Trabalho não identificado\n')
            trabalho = input("Trabalho?\n" + str(trabalhos) + '\n')

    if numeracao == 0:
        numeracao = input("Número da passagem?\n")

    return autor, trabalho, numeracao


def infoverbo(verbo=None,
                   diatese=None,
                   transitividade=None,
                   copula=None,
                   pessoal=None):
    """
    Recebe as informações sobre o verbo principal, checa a validade delas e as retorna

    """
    diateses = ['atv', 'mp', 'pass']

    while diatese not in diateses:
        print('Diátese não identificada.')
        diatese = input('Defina a diátese:\n' + str(diateses) + '\n')

    transitividades = ['mono', 'bi', 'tri']

    while transitividade not in transitividades:
        print('Transitividade não identificada.')
        transitividade = input('Defina a transitividade:\n' + str(transitividades) + '\n')

    if copula is None:
        copula = get_boll("O verbo é copular?")

    if pessoal is None:
        pessoal = get_boll("O verbo é pessoal?")


    return verbo, diatese, transitividade, copula, pessoal

def main(autor=False, trabalho=False, numeracao=False,
         atracao=None,
         verboprincipal=False, diateseprin=False, transitividadeprin=False, copulaprim=False, pessoalprim=None,
         verboinf=None, diateseinf=None, transitividadeinf=None, copulainf=None, pessoalinf=None,
         benalvo=None,
         adjunto=None,
         distanciabenadj=0):

    # Inicializa o documento corpus.tex

    corpus = open("corpus.tex", "a")

    # Inicializa prompt de de autor, trabalho e parágrafo
    if not autor and not trabalho and not numeracao:
        autor, trabalho, numeracao = autor_init(autor=input("Autor?\n"), trabalho=input("Trabalho?\n"))
    else:
        print("Entrada: " + autor + trabalho + numeracao + '\n')
        autor, trabalho, numeracao = autor_init(autor, trabalho, numeracao)

    corpus.write("\\textbf{" + autor + trabalho + numeracao + '}\n')
    corpus.write('\n\n')

    # Inicializa prompt de passagem e tradução

    passagem = input("Passagem em grego:\n")
    traducao = input("Tradução\n")

    corpus.write(passagem + '\n\n' + traducao + '\n\n')

    if atracao is None:
        atracao = get_boll('Há atração de caso?')

    if atracao:
        corpus.write('\\textbf{' + 'Atração}: ' + 'Sim' + '\n\n')
    else:
        corpus.write('\\textbf{' + 'Atração}: ' + 'Sim' + '\n\n')



    ### Inicializa as informações morfológicas

    # Verbo principal

    if not verboprincipal and not diateseprin and not transitividadeprin and pessoalprim is None:
        verboprincipal, \
        diateseprin, \
        transitividadeprin, \
        copulaprim, \
        pessoalprim = infoverbo(verbo=input("Verbo:\n"),
                                diatese=input("Diátese:\n"),
                                transitividade=input('Transitividade:\n'),
                                copula=copulaprim)

    else:
        verboprincipal, diateseprin, transitividadeprin, copulaprim, pessoalprim = infoverbo(verbo=verboprincipal,
                                                                                             diatese=diateseprin,
                                                                                             transitividade=transitividadeprin,
                                                                                             copula=copulaprim,
                                                                                             pessoal=pessoalprim)



    # Imprime resumo das informações recolhidas

    print(autor + trabalho + numeracao)
    print(atracao)
    print('Verbo principal:')
    print(verboprincipal + 'Diátese: ' + diateseprin + ' Transitividade: ' + transitividadeprin + ' Pessoal: ' + str(pessoalprim))

    # Finaliza o documento corpus.tex
    corpus.close()


main()
