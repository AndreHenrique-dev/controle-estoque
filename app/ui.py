def title(txt = '',line = '='): #Estilização de texto.
    """
        -> Escreve um titulo centralizado entre duas linhas.
    Parâmetros:
        txt (string, opicional): Define o conteudo do titulo. Definido por padrão como: ''
        line (string, opicional): Define o conteudo(simbolo) da linha. Definido por padrão como '='.
    """
    print(line*(len(txt)+6))
    print(txt.center(len(txt)+6).upper())
    print(line*(len(txt)+6))