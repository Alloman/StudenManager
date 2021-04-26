# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
    class Student:
        def __init__(self, sid, name, id, phone):
            self.__sid = sid
            self.__name = name
            self.__id = id
            self.__phone = phone

        def get_sid(self):
            return self.__sid

        def get_name(self):
            return self.__name

        def get_id(self):
            return self.__id

        def get_phone(self):
            return self.__phone

        def set_name(self, new_name):
            self.__name = new_name
            return

        def set_id(self, new_sid):
            self.__id = new_sid
            return

        def set_phone(self, new_phone):
            self.__phone = new_phone
            return