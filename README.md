[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/dGj0D1-K)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11269145&assignment_repo_type=AssignmentRepo)
# 1. Propósito
---
Esta tarefa tem os seguintes propósitos:
- Desenvolver as habilidades de criação e manipulação de estruturas de dados do tipo lista ligada ordenada (Ordered Linked List);
- Implementar e validar os conceitos relacionados ao métodos de estruturas de dados lista ligada ordenada.

# 2. Orientações
---

As subsessões a seguir orientam sobre o uso de soluções as quais poderão auxiliar na realização dessa tarefa, bem como os aspectos gerais relativos à implementação (código fonte) da sua solução.

## 2.1. Instalação do framework pytest
---
A estrutura do código fonte está montada para ser validada com a framework pytest, o qual poderá ser instalado com o comando:

```console
$ pip install pytest
```

Você não está obrigado a instalar o pytest e rodar os testes de validação antes do envio da tarefa, entretanto pode ser bastante útil para que você consiga identificar onde estão os pontos de falhas no seu projeto.

Para realizar um teste de validação da sua implementação, basta executar o seguinte comando:

```console
$ pytest test/test_lista_ligada.py -v
```

O pytest permite que você realize o teste sobre métodos específicos da sua estrutura de dados lista ligada. Portanto, também é válido o comando:

```console
$ pytest test/test_lista_ligada.py -k is_empty -v --no-header
```

Para mais detalhes e informações sobre o framework consultar no [link](https://docs.pytest.org/en/7.3.x/contents.html).

## 2.2. Implementação da solução
---

Você deverá implementar os **métodos da classe ListaLigada** no arquivo **lista_ligada.py**, os quais ainda não foram implementados. Esteja atento ao tipo de retorno de cada método, pois isso irá impactar diretamente na avaliação da sua solução após você enviar o commit com as suas implementações para o repositório remoto.

Após concluir a tarefa, você deverá realizar um **git push** para entregar a sua atividade. Você poderá realizar tantos envios ao repositório remoto quanto desejar. Entretanto, esteja atento ao prazo de entreda da atividade para não realizar a entrega com atraso, pois isso irá impactar sobre a nota da atividade. 

Os testes de validação da pontuação realizados pelo GitHub-Classroom não ocorrem imediatamente após o envio do push para o servidor. Normalmente, o GitHub levará o tempo de alguns segundos para realizar o teste sobre a solução enviada por você. Você deverá atualizar a página no GitHub-Classroom a cada 10s, caso não perceba a mudança no resultado da pontuação, até que o GitHub faça o computo dos seus pontos a partir da execução dos testes sobre a sua entrega.

Esteja atento aos tipos de retorno de cada método, os quais se encontram descritos com _type hint_ no próprio método.

## 2.3. Prazo de entrega
---

O prazo de entrega encontra-se descrito no ambiente do Google Sala de Aula da turma e também do GitHub Classroom.


# 3. Tarefas
---

Segue a relação de tarefas a serem observadas na implementação de cada método e a respectiva pontuação do método destacada em parênteses. Toda a tarefa valerá **20pts**, o que corresponde a **20%** da nota da segunda etapa.

- [x] Estudar e analizar os conceitos e técnicas para implementação da estrutura de dados do tipo lista ligada ordenada
- [ ] **(1pts)** Implementar o método **is_empty()**
  - [ ] Deve retornar um boolean True se não houver itens (Nó) na lista ligada ordenada ou False, caso contrário
- [ ] **(1pts)** Implementar o método **is_full()**
  - [ ] Deve retornar um boolean True se houver itens (Nó) na lista ligada ordenada ou False, caso contrário
- [ ] **(6pts)** Implementar o método **add()**, o qual deve receber como entrada um valor para criar um nó que deverá ser inserido no início da lista ligada ordenada
  - [ ] Criar um objeto Nó a partir do valor recebido pelo método
  - [ ] Deve retornar um boolean True se conseguir inserir um item (Nó) em ordem crescente na lista ligada ordenada
  - [ ] Caso a lista ligada ordenada tenha alcançado a sua capacidade máxima deverá lançar uma Exception com uma mensagem de erro relativo ao ocorrido, senão o item (Nó) deve ser inserido em ordem crescente na lista ligada ordenada e método deverá retornar um boolean True
- [ ] **(6pts)** Implementar o método **remove()**, o qual deve receber como entrada um valor para ser buscado na lista ligada ordenada e remover esse item da lista, caso esteja presente 
  - [ ] Caso a lista ligada ordenada esteja vazia deverá lançar uma Exception com uma mensagem de erro
  - [ ] Caso o item a ser removido esteja presente na lista ligada ordenada o item (Nó) da lista ligada ordenada deverá ser removido e em seguida o método deverá retornar o valor True
  - [ ] Caso o item a ser removido não esteja presente na lista ligada ordenada o método deverá retornar o valor False
- [ ] **(4pts)** Implementar o método **contains()**, o qual deverá receber como entrar um valor a ser buscado e retornar o valor True ou False como resultado da busca
  - [ ] Caso o valor a ser encontrado esteja presente na lista ligada ordenada, o método deverá retornar o valor True
  - [ ] Caso o valor a ser encontrado não esteja presente na lista ligada ordenada, o método deverá retornar o valor False
- [ ] **(1pts)** Implementar o método **display()**, o qual deve retornar uma lista com os valores (atributo dado) dos itens (Nó) inseridos na lista ligada ordenada
  - [ ] Caso a lista ligada ordenada esteja vazia deverá retornar uma lista vazia []
  - [ ] Caso a lista ligada ordenada possua um ou mais itens, o primeiro elemento da lista deve ser o valor do dado do primeiro item (Nó) na lista ligada ordenada, seguido das demais valores que compõem a lista ligada ordenada (do primeiro ao último), nessa ordem
- [ ] **(1pts)** Implementar o método **size()**, o qual deve retornar um int
  - [ ] O método deverá retornar ZERO, caso a lista ligada ordenada esteja vazia, ou, caso possua algum item na lista ligada ordenada, o valor relativo à quantidade de itens presentes na lista ligada ordenada