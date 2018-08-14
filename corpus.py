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


def autor_init(autor=None, trabalho=None, numeracao=0):

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


def infoverbo(verbo=None, diatese=None, transitividade=None, copula=None, pessoal=None):
    """
    Recebe as informações sobre o verbo principal, checa a validade delas e as retorna

    """
    diateses = ['atv', 'mp', 'pass']

    while diatese not in diateses:
        print('Diátese não identificada.')
        diatese = input('Defina a diátese:\n' + str(diateses) + '\n')

    transitividades = ['intr', 'trans', 'bi']

    while transitividade not in transitividades:
        print('Transitividade não identificada.')
        transitividade = input('Defina a transitividade:\n' + str(transitividades) + '\n')

    if copula is None:
        copula = get_boll("O verbo é copular?")

    if pessoal is None:
        pessoal = get_boll("O verbo é pessoal?")

    return verbo, diatese, transitividade, copula, pessoal


def main(autor=None, trabalho=None, numeracao=None,
         atracao=None,
         verboprincipal=None, diateseprin=None, transitividadeprin=None, copulaprim=None, pessoalprim=None,
         verboinf=None, diateseinf=None, transitividadeinf=None, copulainf=None, pessoalinf=None,
         benalvo=None,
         adjunto=None,
         distanciabenadj=None):

    # Inicializa o documento corpus.tex

    corpus = open("corpus.tex", "a")

    # Inicializa prompt de de autor, trabalho e parágrafo
    if autor is None and trabalho is None and numeracao is None:
        autor, trabalho, numeracao = autor_init(autor=input("Autor?\n"), trabalho=input("Trabalho?\n"))
    else:
        print("Entrada: " + autor + trabalho + numeracao + '\n')
        autor, trabalho, numeracao = autor_init(autor, trabalho, numeracao)


    # Inicializa prompt de passagem e tradução

    passagem = input("Passagem em grego:\n")
    traducao = input("Tradução\n")

    # Inicializa prompt de atração

    if atracao is None:
        atracao = get_boll('Há atração de caso?')


    # Inicializa as informações morfológicas

    # Verbo principal
    print("Verbo principal:")
    if verboprincipal is None and\
            diateseprin is None and \
            transitividadeprin is None and \
            pessoalprim is None and \
            copulaprim is None:
        verboprincipal, \
            diateseprin, \
            transitividadeprin, \
            copulaprim, \
            pessoalprim = infoverbo(verbo=input("Verbo:\n"),
                                    diatese=input("Diátese:\n"),
                                    transitividade=input('Transitividade:\n'),
                                    copula=copulaprim)

    else:
        print(verboprincipal, diateseprin, transitividadeprin, str(copulaprim), str(pessoalprim))
        verboprincipal, \
            diateseprin, \
            transitividadeprin,\
            copulaprim,\
            pessoalprim = infoverbo(verbo=verboprincipal,
                                    diatese=diateseprin,
                                    transitividade=transitividadeprin,
                                    copula=copulaprim,
                                    pessoal=pessoalprim)

    # Verbo infinitivo
    print("Verbo infinitivo")
    if verboinf is None and\
            diateseinf is None and\
            transitividadeinf is None and\
            pessoalinf is None and\
            copulainf is None:
        verboinf, \
            diateseinf, \
            transitividadeinf, \
            copulainf, \
            pessoalinf = infoverbo(verbo=input("Verbo:\n"),
                                   diatese=input("Diátese:\n"),
                                   transitividade=input('Transitividade:\n'),
                                   copula=copulainf,
                                   pessoal=pessoalinf)
    else:
        print(verboinf, diateseinf, transitividadeinf, str(copulainf), str(pessoalinf))
        verboinf,\
            diateseinf, \
            transitividadeinf, \
            copulainf, \
            pessoalinf = infoverbo(verbo=verboinf,
                                   diatese=diateseinf,
                                   transitividade=transitividadeinf,
                                   copula=copulainf,
                                   pessoal=pessoalinf)

    generos = ["masc.", "neutr.", "fem."]
    numeros = ["sg.", "pl.", "du."]
    benalvovalido = ['pronominal', 'adjetivo', 'substantivo']
    if benalvo is None:
        benalvo = dict()
        benalvo.update({'forma': None, 'tipo': None, 'gênero': None, 'número': None})
        benalvo['forma'] = input("Qual é o beneficiário?\n")
        while benalvo['tipo'] not in benalvovalido:
            benalvo['tipo'] = input("Qual é o tipo do beneficiário/alvo?\n" + str(benalvovalido) + "\n")
        while benalvo['gênero'] not in generos:
            benalvo['gênero'] = input("Qual é o gênero do beneficiário/alvo?\n" + str(generos) + "\n")
        while benalvo['número'] not in numeros:
            benalvo['número'] = input("Qual é o número do beneficiário/alvo?\n" + str(numeros) + '\n')

    adjuntovalido = ['adjetivo', 'substantivo', 'particípio']
    if adjunto is None:
        adjunto = dict()
        adjunto.update({'forma': None, 'tipo': None, 'gênero': None, 'número': None})
        adjunto['forma'] = input("Qual é a forma do adjunto?\n")
        while adjunto['tipo'] not in adjuntovalido:
            adjunto['tipo'] = input("Qual é o tipo do adjunto?\n" + str(adjuntovalido) + "\n")
        while adjunto['gênero'] not in generos:
            adjunto['gênero'] = input("Qual é o gênero do adjunto?\n" + str(generos) + "\n")
        while adjunto['número'] not in numeros:
            adjunto['número'] = input("Qual é o número do adjunto?\n" + str(numeros) + '\n')

    if distanciabenadj is None:
        distanciabenadj = float(input("Qual a distância entre o ben-adj e o adjunto?\n"))

    # Edita as informações abreviadas para maior clareza:

    if diateseprin == 'atv':
        diateseprin = 'Ativo'
    elif diateseprin == 'mp':
        diateseprin = 'Médio-passivo'
    elif diateseprin == 'pass':
        diateseprin = 'Passivo'

    if transitividadeprin == 'intr':
        transitividadeprin = 'Intransitivo'
    elif transitividadeprin == 'trans':
        transitividadeprin = 'Transitivo'
    elif transitividadeprin == 'bi':
        transitividadeprin = 'Bitransitivo'

    if diateseinf == 'atv':
        diateseinf = 'Ativo'
    elif diateseinf == 'mp':
        diateseinf = 'Médio-passivo'
    elif diateseinf == 'pass':
        diateseinf = 'Passivo'

    if transitividadeinf == 'intr':
        transitividadeinf = 'Intransitivo'
    elif transitividadeinf == 'trans':
        transitividadeinf = 'Transitivo'
    elif transitividadeinf == 'bi':
        transitividadeinf = 'Bitransitivo'



    # Imprime resumo das informações recolhidas

    print(autor + trabalho + numeracao)
    print('Atração: ' + str(atracao))
    print('Verbo principal:')
    print(verboprincipal + ' Diátese: ' + diateseprin + ' Transitividade: ' + transitividadeprin +
          ' Pessoal: ' + str(pessoalprim))
    print('Verbo infinitivo:')
    print(verboinf + ' Diátese: ' + diateseinf + ' Transitividade: ' + transitividadeinf +
          ' Pessoal: ' + str(pessoalprim))
    print('Ben-alvo: ' + str(benalvo))
    print('Adjunto:' + str(adjunto))
    print('A distância entre ben-adj e adjunto é: ' + str(distanciabenadj) + ' palavras.')

    # Escreve as informações no arquivo devidamente formatadas

    # Identificação do texto

    corpus.write("\\textbf{" + autor + trabalho + numeracao + '}\n\n')

    # Passagem e tradução

    corpus.write(passagem + '\n\n' + traducao + '\n\n')

    # Atração:

    if atracao:
        corpus.write('\\textbf{' + 'Atração}: ' + 'Sim' + '\n\n')
    else:
        corpus.write('\\textbf{' + 'Atração}: ' + 'Sim' + '\n\n')

    # Informações sobre o verbo principal

    corpus.write("\\textbf{Verbo principal}:" + verboprincipal + " (" + diateseprin + ' ' + transitividadeprin + ")\n\n" )
    corpus.write("\\textbf{Verbo infinitivo}:" + verboinf + " (" + diateseinf + ' ' + transitividadeinf + ")\n\n" )

    # Finaliza o documento corpus.tex
    corpus.close()


# main()
main(autor='xen', trabalho='Cyrop.', numeracao='1.1.1',
     verboprincipal='exesti', diateseprin="atv", transitividadeprin='intr', copulaprim=True, pessoalprim=False,
     verboinf='gignomai', diateseinf='mp', transitividadeinf='intr', copulainf=True, pessoalinf=True,
     benalvo={'forma': 'soi', 'gênero': 'masc.', 'número': 'sg.', 'tipo': 'pronominal'},
     adjunto={'forma': 'andri', 'gênero': 'masc.', 'número': 'sg.', 'tipo': 'substantivo'},
     atracao=True)

