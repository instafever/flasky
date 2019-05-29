"""
通用函数
"""


def to_json_list(objs):
    """
    将多个实体对象转为json列表格式
    :return:
        [
            {
                "attr": value
            }
        ]
    """
    list = []
    for obj in objs:
        list.append(obj.to_dict())
    return list
