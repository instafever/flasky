from sqlalchemy.orm import class_mapper

from app import db


class Base():
    """
    基础类
    """

    def to_dict(self):
        """
        将实体对象转为字典格式
        :return:
            {
                attr: value
            }
        """
        return dict((col.name, getattr(self, col.name)) for col in class_mapper(self.__class__).mapped_table.c)


class Model(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
