import pickle

from abc import ABC


class Dao(ABC):
    def __init__(self, datasource=''):
        self.__datasource = 'pkl/' + datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def remove(self, key):
        self.__cache.pop(key)
        self.__dump()

    def update(self, key, obj):
        if self.__cache[key] is not None:
            self.__cache[key] = obj
            self.__dump()

    def get(self, key):
        return self.__cache[key]

    def get_all(self):
        return self.__cache.values()