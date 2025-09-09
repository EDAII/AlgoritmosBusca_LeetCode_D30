class Solution:
    def mergeKLists(self, listas: list) -> 'ListNode':
        if not listas or len(listas) == 0:
            return None

        while len(listas) > 1:
            listas_mescladas = []  # vetor auxiliar

            for indice in range(0, len(listas), 2):  # passo 2 em 2
                lista_a = listas[indice]
                lista_b = listas[indice + 1] if (indice + 1) < len(listas) else None
                listas_mescladas.append(self.mesclarListas(lista_a, lista_b))  # adiciona a lista mesclada ao vetor auxiliar
            listas = listas_mescladas  # atualiza a lista original com o vetor auxiliar
        return listas[0]

    def mesclarListas(self, no_a, no_b):
        sentinela = ListNode()  # nó fictício
        ponteiro = sentinela    # ponteiro para o final da lista mesclada

        while no_a and no_b:  # enquanto ambos não forem nulos
            if no_a.val < no_b.val:
                ponteiro.next = no_a
                no_a = no_a.next
            else:
                ponteiro.next = no_b
                no_b = no_b.next
            ponteiro = ponteiro.next
        if no_a:
            ponteiro.next = no_a
        if no_b:
            ponteiro.next = no_b
        return sentinela.next