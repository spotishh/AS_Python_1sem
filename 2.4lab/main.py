if __name__ == "__main__":
    pass
# а) Объединение строк
def join_strings(strings, delimiter=','):
    result = ''
    for i in range(len(strings)):
        if i != 0:
            result += delimiter
        result += strings[i]
    return result

# б) Объединение списков
def combine_lists(list1, list2, join_str=''):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + join_str + list2[i])
    return new_list

# в) Уникальные значения
def unique_values(*args):
    result = []
    for item in args:
        if item not in result:
            result.append(item)
    return result

# г) Обратная конкатенация
def reverse_concatenate(*strings):
    result = ''
    for i in range(len(strings)-1, -1, -1):
        if i != len(strings)-1:
            result += ' '
        result += strings[i]
    return result

# Проверка всех функций
print("а) join_strings:")
print(join_strings(['один', 'два', 'три']))
print(join_strings(['sun', 'moon', 'stars'], delimiter=' | '))

print("\nб) combine_lists:")
print(combine_lists(['a', 'b'], ['1', '2']))
print(combine_lists(['x', 'y'], ['10', '20'], join_str='-'))

print("\nв) unique_values:")
print(unique_values(1, 2, 2, 3, 3, 3))
print(unique_values('a', 'b', 'a', 'c', 'b'))

print("\nг) reverse_concatenate:")
print(reverse_concatenate('one', 'two', 'three'))
print(reverse_concatenate('hello', 'world'))
