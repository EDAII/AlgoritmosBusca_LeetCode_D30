class Solution:
    def findSubstring(self, texto: str, lista_palavras: List[str]) -> List[int]:
        # Verifica se a string 'texto' ou a lista 'lista_palavras' está vazia
        if not texto or not lista_palavras:
            return []
       
        tam_palavra = len(lista_palavras[0])
        qtd_palavras = len(lista_palavras)
        tam_total = tam_palavra * qtd_palavras
        tam_texto = len(texto)

        # Verifica se a string 'texto' é menor que o comprimento total necessário.
        if tam_texto < tam_total:
            return []

        # 'necessario' é um dicionário que conta quantas vezes cada palavra aparece na lista 'lista_palavras'.
        necessario = {}
        for palavra in lista_palavras:
            necessario[palavra] = necessario.get(palavra, 0) + 1

        # 'indices_resultado' é a lista que armazenará os índices iniciais das substrings concatenadas encontradas.
        indices_resultado: List[int] = []

        for desloc in range(tam_palavra):
            inicio = desloc
            fim = desloc
            vistos = {}
            palavras_vistas = 0

            # Desliza a janela pela string 'texto' em incrementos do tamanho da palavra 'tam_palavra'.
            while fim + tam_palavra <= tam_texto:
                palavra_atual = texto[fim:fim + tam_palavra]
                fim += tam_palavra

                if palavra_atual in necessario:
                    vistos[palavra_atual] = vistos.get(palavra_atual, 0) + 1
                    palavras_vistas += 1

                    # Se a palavra foi vista mais vezes do que o necessário, move a janela para a direita.
                    while vistos[palavra_atual] > necessario[palavra_atual]:
                        palavra_inicio = texto[inicio:inicio + tam_palavra]
                        vistos[palavra_inicio] -= 1
                        if vistos[palavra_inicio] == 0:
                            del vistos[palavra_inicio]
                        inicio += tam_palavra
                        palavras_vistas -= 1

# Se o número de palavras vistas é igual ao número total de palavras, adiciona o índice inicial à lista de resultados.
                    if palavras_vistas == qtd_palavras:
                        indices_resultado.append(inicio)

                        palavra_inicio = texto[inicio:inicio + tam_palavra]
                        vistos[palavra_inicio] -= 1
                        if vistos[palavra_inicio] == 0:
                            del vistos[palavra_inicio]
                        inicio += tam_palavra
                        palavras_vistas -= 1
                else:
                    # Se a palavra não está na lista 'lista_palavras', reseta a janela.
                    vistos.clear()
                    palavras_vistas = 0
                    inicio = fim

        return indices_resultado