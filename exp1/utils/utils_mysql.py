# !/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

class Stu_DB:
    """初始化一个学生表db指针"""
    def __init__(self, host, user, psd, db_name, charset="utf8"):
        self.__host = host
        self.__user = user
        self.__psd = psd
        self.__db_name = db_name
        self.__charset = charset

    def connect(self):
        db = pymysql.connect(host=self.__host, user=self.__user, password=self.__psd,
                                    database=self.__db_name, charset=self.__charset)
        print("--------------Dataset", self.__db_name ,"has connected----------------")
        return db