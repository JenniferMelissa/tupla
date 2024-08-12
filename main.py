#tupla
#é uma lista imutavel
#consegue exibir a lista normalmente, consegue fazer join nela, pesquisar nela
#nao consegue: alterar nenhuma informacao e indice, nao consegue adicionar item na tupla, nao consegue excluir item na tupla e ordenar os itens na tupla
#usa pra quando voce quer manter a integridade da lista se for uma tupla
#tupla tem parenteses
#lista tem cochetes

#tupla
paises = ('Brasíl','Paraguai','Romênia','França','Espanha','Portugal','Argentina','China','Japão','Tailândia','Itália')

#exibir a tupla
for pais in paises:
    print(pais)

print('\n')

#exibe o tipo de colecao 
print(type(paises))

paises_lista = sorted(paises)
#pega a tupla e cria uma copia dela para a lista, e assim conseguimos ordenar a lista

#exibe a lista
for pais in paises_lista:
    print(pais)

