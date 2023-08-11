# ATENÇÃO: Não altere o código de arquivo
import os.path
import sys
from pytest import mark, raises
from no import No
from lista_ligada import ListaLigada

# ---- INÍCIO: teste método is_empty()

def test_is_empty_true():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    result = lista_ligada.is_empty()
    expected = True

    assert result == expected and lista_ligada.size() == 0


def test_is_empty_false():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada(3)
    lista_ligada.add(1)
    lista_ligada.add(2)

    result = lista_ligada.is_empty()
    expected = False

    assert result == expected and lista_ligada.size() == 2

# ---- FIM: teste método is_empty()


# ---- INÍCIO: teste método is_full()

def test_is_full_true():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada(1)
    lista_ligada.add(1)

    result = lista_ligada.is_full()
    expected = True

    assert result == expected and lista_ligada.size() == 1


def test_is_full_false():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada(3)
    lista_ligada.add(1)
    lista_ligada.add(2)

    result = lista_ligada.is_full()
    expected = False

    assert result == expected and lista_ligada.size() == 2

# ---- FIM: teste método is_full()


# ---- INÍCIO: teste método add()

def test_add_em_pilha_cheia():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada(1)

    lista_ligada.add(1)

    result = lista_ligada.contains(1)
    expected = True

    assert result == expected
    with raises(Exception):
        lista_ligada.add(2) # deve gerar erro


def test_add_em_lista_ligada_vazia():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    result = lista_ligada.add(1)
    result = lista_ligada.add(2)
    expected = True

    assert result == expected and lista_ligada.size() == 2


def test_add_em_lista_ligada_para_verificar_ordem_aleatoria():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada(10)

    lista_ligada.add(1)
    lista_ligada.add(4)
    lista_ligada.add(2)
    lista_ligada.add(3)
    lista_ligada.add(5)

    result = lista_ligada.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected


def test_add_em_lista_ligada_para_verificar_ordem_crescente():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada(10)

    lista_ligada.add(1)
    lista_ligada.add(2)
    lista_ligada.add(3)
    lista_ligada.add(4)
    lista_ligada.add(5)

    result = lista_ligada.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected


def test_add_em_lista_ligada_para_verificar_ordem_decrescente():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada(10)

    lista_ligada.add(5)
    lista_ligada.add(4)
    lista_ligada.add(3)
    lista_ligada.add(2)
    lista_ligada.add(1)

    result = lista_ligada.display()
    expected = [
        1,
        2,
        3,
        4,
        5
    ]

    assert result == expected

# ---- FIM: teste método add()


# ---- INÍCIO: teste método remove()

def test_remove_em_lista_ligada_vazia():

    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    with raises(Exception):
        lista_ligada.remove() # deve gerar erro


def test_remove_em_lista_ligada_com_item_presente_no_meio():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_ligada.add(item[:-1])

    result = lista_ligada.remove('3')
    expected = True

    assert expected == result

    result = lista_ligada.display()
    expected = [
        '1',
        '2',
        '4',
        '5'
    ]

    assert expected == result


def test_remove_em_lista_ligada_com_item_presente_no_inicio():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_ligada.add(item[:-1])

    result = lista_ligada.remove('1')
    expected = True

    assert expected == result

    result = lista_ligada.display()
    expected = [
        '2',
        '3',
        '4',
        '5'
    ]

    assert expected == result


def test_remove_em_lista_ligada_com_item_presente_no_fim():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_ligada.add(item[:-1])

    result = lista_ligada.remove('5')
    expected = True

    assert expected == result

    result = lista_ligada.display()
    expected = [
        '1',
        '2',
        '3',
        '4'
    ]

    assert expected == result


def test_remove_em_lista_ligada_sem_item_presente():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_ligada.add(item[:-1])

    result = lista_ligada.remove('9')
    expected = False

    assert expected == result


def test_remove_em_lista_ligada_com_itens_ate_esvaziar():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_ligada.add(item[:-1])

    for x in range(5):
      lista_ligada.remove(str(x+1))

    with raises(Exception):
        lista_ligada.remove(1) # deve gerar erro

# ---- FIM: teste método remove()


# ---- INÍCIO: teste método contains()

def test_contains_em_lista_ligada_vazia():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    result = lista_ligada.contains(1)
    expected = False

    assert expected == result


def test_contains_em_lista_ligada_com_item_presente():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()
    lista_ligada.add(1)

    result = lista_ligada.contains(1)
    expected = True

    assert expected == result


def test_contains_em_lista_ligada_sem_item_presente():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()
    lista_ligada.add(1)

    result = lista_ligada.contains(2)
    expected = False

    assert expected == result

# ---- FIM: teste método contains()


# ---- INÍCIO: teste método display()

def test_display_em_lista_ligada_com_elementos_string():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            lista_ligada.add(item[:-1])

    result = lista_ligada.display()
    expected = [
        "1",
        "2",
        "3",
        "4",
        "5",
    ]

    assert result == expected


def test_display_em_lista_ligada_com_elementos_int():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    lista_ligada.add(1)
    lista_ligada.add(2)
    lista_ligada.add(3)

    result = lista_ligada.display()
    expected = [
        1,
        2,
        3,
    ]

    assert result == expected


def test_display_em_lista_ligada_sem_elementos_ao_criar_lista_ligada():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    result = lista_ligada.display()
    expected = []
    
    assert result == expected


def test_display_em_lista_ligada_sem_elementos_ao_esvaziar_lista_ligada():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    lista_ligada.add(1)
    lista_ligada.add(2)
    lista_ligada.remove(2)
    lista_ligada.remove(1)

    result = lista_ligada.display()
    expected = []
    
    assert result == expected

# ---- FIM: teste método display()


# ---- INÍCIO: teste método size()

def test_size_em_lista_ligada_ao_criar_lista():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    result = lista_ligada.size()
    expected = 0
    
    assert result == expected


def test_size_em_lista_ligada_ao_inserir_itens():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    lista_ligada.add(1)
    expected = 1
    assert lista_ligada.size() == expected

    lista_ligada.add(1)
    expected = 2
    assert lista_ligada.size() == expected

    lista_ligada.add(1)
    expected = 3
    assert lista_ligada.size() == expected


def test_size_ao_remover_itens():
    try:
        exists = os.path.exists("lista_ligada.py")
        assert exists == True
    except:
        sys.exit()

    lista_ligada = ListaLigada()

    lista_ligada.add(1)
    lista_ligada.add(1)
    lista_ligada.add(1)

    lista_ligada.remove(1)
    result = lista_ligada.size()
    expected = 2
    assert result == expected

    lista_ligada.remove(1)
    result = lista_ligada.size()
    expected = 1
    assert result == expected

    lista_ligada.remove(1)
    result = lista_ligada.size()
    expected = 0
    assert result == expected

# ---- FIM: teste método size()