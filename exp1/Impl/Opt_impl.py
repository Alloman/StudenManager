# !/usr/bin/python
# -*- coding: UTF-8 -*-
from exp1.Interface.Opt import Opt_DB
from exp1.utils.utils_mysql import Stu_DB

class Opt_impl(Opt_DB):
    def __init__(self, db):
        super(Opt_impl, self).__init__()
        self.__db = db
        self.__cursor =  db.cursor()

    def insert_stu(self, sid, id, name, phone):
        stu = (sid, id, name, phone)
        sql = "INSERT INTO student (std_ID, id, name, phone) VALUE %s" % str(stu)
        self.__cursor.execute(sql)
        self.__db.commit()

        print("insert data: ", stu, "to table student")
        return

    def del_stu(self, sid):
        sql = "DELETE FROM student WHERE std_ID = '%s'" % sid
        self.__cursor.execute(sql)
        self.__db.commit()

        print("delete data: ", sid, "to table student")
        return

    def alter_stu(self, sid, name):
        sql = "UPDATE student SET name = '%s'" % str(name) +"WHERE std_ID = '%s'" % sid
        self.__cursor.execute(sql)
        self.__db.commit()

        print("alter data: ", sid, " name to", name)
        return

    def find_stu(self, sid):
        sql = "SELECT * FROM student WHERE std_ID = '%s'" % sid
        data = self.__cursor.execute(sql)

        print("find data: ", data, "to table student")
        return



if __name__ == '__main__':
    db = Stu_DB("localhost", "root", "1234", "studentmanager").connect()

    opt = Opt_impl(db)


    opt.insert_stu("1", "321", "狗蛋", "1314")
    opt.alter_stu("1", "王狗蛋")
    opt.find_stu("1")
    opt.del_stu("1")

    db.close()
