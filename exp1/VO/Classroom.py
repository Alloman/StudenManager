# !/usr/bin/python
# -*- coding: UTF-8 -*-

from .Student import Student

class Classroom:
    def __init__(self):
        self.__cid = ''
        self.__classname = ""
        self.__leader_sid = ""
        self.__students = []

    def set_classname(self, classname):
        self.__classname = classname

        return

    def get_classname(self):
        return self.__classname

    def set_leader(self, leader_sid):
        self.__leader_sid = leader_sid

        return

    def get_leader(self):

        return self.__leader_sid

    def set_students(self, stu_list):
        """
        :param stu_list: (sid, id, name, phone)
        :return:
        """
        for (sid, id, name, phone) in stu_list:
            self.__students.append(Student(sid, id, name, phone))

        return

    def get_students(self):
        assert len(self.__students) > 0 , "students are not initialized"
        return self.__students