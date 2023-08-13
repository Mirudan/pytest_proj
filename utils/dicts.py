def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение по-умолчанию.
    :param collection: словарь
    :param key: ключ для поиска
    :param default: значение по-умолчанию
    :return: значение по ключу или значение по-умолчанию
    """
    if key not in collection.keys():
        return default
    else:
        return collection[key]
