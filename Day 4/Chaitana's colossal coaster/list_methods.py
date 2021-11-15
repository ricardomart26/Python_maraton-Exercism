"""
To Add a new item to the list, you can use the append method Ex. list.append(item), vai adicionar o item no ultimo indice da lista
To Add a new item to the list in the specific index, you can use the insert method Ex. list.insert(index, item), vai adicionar o item no indice (index) da lista
To concatenate lists with other iterables (tupples, sets, strings, other lists), you can use the extend method Ex. list.extend(another list), vai adicionar o iteravel que passas a variavel em que usares o metodo
To Remove a item of the list, you can use the remove method Ex. list.remove(item), vai remover o item da lista, enquanto para remover e receber o index que retiraste da lista, podemos usar o metodo pop Ex. list.pop(index), e retorna o index
O list.clear vai limpar a lista
O list.reverse vai reverter a lista
O list.sort() vai organizar a lista, e para organizarmos ao contrario podemos passar "reverse=True" como argumento, Ex. list.sort(reverse=True)

Por vezes alterar a propria lista nao e o desejado, e para isso existe uma built in function para organizar sem alterar os valores, O sorted(iterable)
O list.count(value) vai contar quantos values existem na lista

Para encontrar os index de um item na lista, usamos a funcao list.index(value), que vai retornar a primeira ocurrencia da lista Ex. list.index(value). E podemos especificar um start e end Ex. (list.index(value, 2, 5))
"""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """
    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue:  list - names in the normal queue.
    :param ticket_type:  int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    normal_queue.append(person_name)
    return normal_queue


def find_my_friend(queue, friend_name):
    """

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)
    

def add_me_with_my_friends(queue, index, person_name):
    """

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    return queue.insert(index, person_name)


def remove_the_mean_person(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return:  list - queue update with the mean persons name removed.
    """
    return queue.remove(person_name)

def how_many_namefellows(queue, person_name):
    """

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return:  int - the number of times the name appears in the queue.
    """
    return queue.count(person_name)


def remove_the_last_person(queue):
    """
    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop(-1)

def sorted_names(queue):
    """
    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    return sorted(queue)
