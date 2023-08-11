# -*- coding:UTF-8 -*-
from no import No

class ListaLigada:
    """
    Implementação de Lista Ligada Ordenada com Capacidade
    A lista a ser implementada deverá ser em ordem crescente
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Lista Ligada com capacidade: {capacidade}")


    # retorna True se a lista ligada está vazia, False caso contrário
    def is_empty(self) -> bool:
        if (self.__qtdItens == 0):
            return True
        else: 
            return False

    
    # retorna True se a lista ligada está cheia, False caso contrário
    def is_full(self) -> bool:
        if (self.__qtdItens == self.__capacidade):
            return True
        else:
            return False


    # insere um elemento na lista ligada em ordem crescente em seguida retorna True
    # se a lista ligada estiver cheia, lança uma exceção: raise Exception("mensagem de erro")
    def add(self, valor) -> bool:
        if self.is_full():
            raise Exception("A lista ligada está cheia.")

        novo_no = No(valor)

        if self.is_empty():
            self.__inicio = novo_no
            self.__fim = novo_no
        else:
            if novo_no.dado < self.__inicio.dado:
                novo_no.prox = self.__inicio
                self.__inicio = novo_no
            else:
                noAtual = self.__inicio
                while noAtual.prox and noAtual.prox.dado < novo_no.dado:
                    noAtual = noAtual.prox
                novo_no.prox = noAtual.prox
                noAtual.prox = novo_no

        self.__qtdItens += 1
        return True

    # remove um elemento da lista ligada retornando True caso ele seja removido
    # se o elemento não estiver na lista ligada, retorne False
    # se a lista ligada estiver vazia, lança uma exceção: raise Exception("mensagem de erro")
    def remove(self, valor) -> bool:
        if self.is_empty() == True:
            raise Exception("A lista ligada está vazia.")

        if self.__inicio.dado == valor:
            self.__inicio = self.__inicio.prox
            self.__qtdItens -= 1
            return True

        noAtual = self.__inicio
        while noAtual.prox:
            if noAtual.prox.dado == valor:
                noAtual.prox = noAtual.prox.prox
                self.__qtdItens -= 1
                return True
            noAtual = noAtual.prox

        return False


        
    # retornar True caso o elemento esteja presente na lista ligada
    # ou False caso contrário
    def contains(self, valor) -> No:
        # implementação do método
        if self.is_empty():
            return False

        atual = self.__inicio
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.prox

        return False


    # retorna uma lista de string com valores dos elementos da lista ligada
    # imprima os elementos da lista ligada do primeiro para o último
    # caso a lista ligada esteja vazia, imprime uma mensagem informando
    # que a lista ligada está vazia e retorna uma lista vazia
    def display(self) -> list[int]:
        if self.is_empty() == True:
            print("A lista ligada está vazia.")
            return []

        lista = []
        atual = self.__inicio
        while atual is not None:
            lista.append(atual.dado)
            atual = atual.prox

        
        return lista

    # retorna a quantidade de elementos na lista ligada
    # se a lista ligada estiver vazia, retorna ZERO
    def size(self) -> int:
        if (self.__qtdItens == 0):
            return 0
        else:
            return self.__qtdItens
