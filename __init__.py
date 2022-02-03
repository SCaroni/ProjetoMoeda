def aumenta(n=0.0, q=0, formatar=False):
    """
    -→ Acrescenta uma determinada porcentagem ao valor.
    :param n: valor informado.
    :param q: porcentagem a ser acrescentada.
    :param formatar: formata ou não em moeda.
    :return: retorna o valor somado a porcentagem.
    """
    n = n + ((n*q)/100)
    return n if formatar is False else formate(n)


def reduz(n=0.0, q=0, formatar=False):
    """
    -→ Diminui uma determinada porcentagem ao valor.
    :param n: valor informado
    :param q: porcentagem a ser diminuida.
    :param formatar: formata ou não em moeda.
    :return: retorna o valor menos a porcentagem.
    """
    n = n - ((n*q)/100)
    return n if formatar is False else formate(n)


def metade(n=0.0, formatar=False):
    """
    -→ Divide um valor por 2.
    :param n: valor informado.
    :param formatar: formata ou não em moeda.
    :return: retorna a metade do valor.
    """
    n = n/2
    return n if formatar is False else formate(n)


def dobro(n=0.0, formatar=False):
    """
    -→ Multiplica um valor por 2.
    :param n: valor informado.
    :param formatar: formata ou não em moeda.
    :return: retorna o dobro do valor
    """
    n = n*2
    return n if formatar is False else formate(n)


def formate(n=0.0, din='R$'):
    """
    -→ Formata o valor em moeda.
    :param n: valor informado.
    :param din: formata em moeda no padrão informado.
    :return: retorna um valor em formato de moeda.
    """
    return f'{din}{n:.2f}'.replace('.', ',')


def resumo(n=0, taxaA=10, taxaR=5):
    """
    -→ Mostra uma análize de um valor em forma de tabela.
    :param n: valor informado.
    :param taxaA: taxa de acréscimo.
    :param taxaR: taxa de redução.
    :return: retorna o dobro, metade, aumento, e redução de um valor.
    """
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('='*30)
    print(f'Preço analizado: \t{formate(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{taxaA}% de aumento: \t{aumenta(n, taxaA, True)}')
    print(f'{taxaR}% de redução: \t{reduz(n, taxaR, True)}')
    print('='*30)


def leiaDinheiro(msg):
    """
    -→ Lê valores em formato de moeda (somente Dinheiro).
    :param msg: mensagem de entrada inválida ou 'NÃO DINHEIRO'
    :return: retorna o valor formatado em moeda.
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print('\033[31m<ERRO> Preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
