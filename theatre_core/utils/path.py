from os import path
from django.db.models.base import ModelBase


def replace_upper_underscore(cls_name):
    if isinstance(cls_name, str):
        tmp = []
        for s in cls_name:
            if s.isupper():
                if cls_name.index(s) is not 0:
                    tmp.append('_')
                    tmp.append(s.lower())
                else:
                    tmp.append(s.lower())
            else:
                tmp.append(s)
        return ''.join(tmp)
    else:
        return ''


def template_path(cls, view, prefix):
    """
    Return template patch
    cls = class
    view = 'backend' or 'frontend'
    prefix = prefix string eg list or create_form
    """
    if isinstance(cls, ModelBase) and isinstance(view, str):

        cls_name = replace_upper_underscore(cls._meta.object_name)
        app_name = cls._meta.app_label
        file_name = '{0}_{1}.html'.format(cls_name, prefix)
        return path.join(app_name, view, file_name)
    else:
        raise ValueError
