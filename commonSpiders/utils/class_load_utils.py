#!/user/bin/env python
# -*- coding: utf-8 -*-
'''
 @Time    : 2018/4/17 21:26
 @File    : class_load_utils.py
 @desc    :
'''
import os
from importlib import import_module


def get_file_path_by_super_path(path, prefix):
    '''
    根据包路径名递归查找该包下所有的文件路径
    :param path:
    :param prefix:
    :return:
    '''

    file_path_list = []
    if os.path.isdir(path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                children_file_path_list = get_file_path_by_super_path(file_path, prefix)
                file_path_list += children_file_path_list
            else:
                file_path_list.append(file_path.replace(prefix, ''))
    else:
        file_path_list = [path.replace(prefix, '')]
    return file_path_list


def get_module_by_path(package_or_module):
    '''
    通过包或模块路径查找所有的模块路径
    :param package_or_module:
    :return:
    '''
    array = []
    is_module = False
    if package_or_module:
        try:
            module = import_module(package_or_module)
            if module and module.__path__:
                real_path = module.__path__[0]
                array = get_file_path_by_super_path(real_path, real_path)
            else:
                is_module = True
        except Exception as e:
            print(e)
    module_children_list = [path.replace('\\', '.').replace('py', '').strip('.') for path in array if path]
    module_list = ['.'.join([package_or_module, module_children]) for module_children in module_children_list if module_children]
    if is_module:
        module_list.append(package_or_module)
    return module_list


def get_class_obj_by_modules(modules_list, super_class):

    class_list = []
    if modules_list and super_class and isinstance(super_class, type):
        for module in modules_list:
            if not module.endswith('__init__'):
                module_obj = import_module(module)
                module_keys = dir(module_obj)
                for key in module_keys:
                    obj = getattr(module_obj, key)
                    if isinstance(obj, super_class):
                        class_list.append(obj)
    return class_list


def get_class_obj_by_package_or_module(package_or_module, super_class):

    modules_list = get_module_by_path(package_or_module)
    class_list = get_class_obj_by_modules(modules_list, super_class)
    return class_list


def get_class_obj_by_pm_list(package_or_module_list, super_class):

    class_list = []
    if isinstance(package_or_module_list, list):
        for package_or_module in package_or_module_list:
            class_children_list = get_class_obj_by_package_or_module(package_or_module, super_class)
            class_list += class_children_list
    return class_list



