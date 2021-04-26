# !/usr/bin/python
# -*- coding: UTF-8 -*-

from exp1.Impl.Opt_impl import Opt_impl

class factory():
    def __init__(self, db):
        self.__db = db
    def get_student_instance(self):
        return Opt_impl(self.__db)