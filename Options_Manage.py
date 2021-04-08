#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author   : lisztomania
# @Date     : 2021/1/23
# @Software : Pycharm
# @Version  : Python 3.8.5
# @File     : Options_Manage.py
# @Function : 选项管理
from inside.Config.Path import PATH
from inside.Baidu_AI.Baidu_AI_Manage import BAIDU_AI_MANAGE
from inside.Options.Options import OPTIONS

from inside.Template.Meta_Singleton import SINGLETON
from inside.Tools import Quit

__all__ = ['OPTIONS_MANAGE']


class OPTIONS_MANAGE(metaclass=SINGLETON):
    """选项管理类"""

    @classmethod
    def __Auto(cls) -> None:
        """
        __Auto() -> None
        禁音选项(默认: True)

        :return: True
        """
        OPTIONS().Mute_Audio = True

    @classmethod
    def __Headless(cls) -> None:
        """
        __Headless() -> None
        显示过程选项(默认: False)

        :return: None
        """
        OPTIONS().Headless = True

    @classmethod
    def __Token(cls) -> None:
        """
        __Token() -> None
        持久化选项(默认：True)

        :return: None
        """
        OPTIONS().Token = True

    @classmethod
    def __Baidu_AI(cls) -> None:
        """
        __Baidu_AI() -> None
        百度AI选项(默认：False)

        Returns: None

        """
        OPTIONS().Baidu_AI = True



    @classmethod
    def Init_Options(cls) -> None:
        """
        Options() -> None
        选项初始化

        :return: None
        """
        cls.__Auto()
        cls.__Headless()
        cls.__Token()
        cls.__Baidu_AI()

    @classmethod
    def Task_Options(cls, hint: str = None) -> None:
        """
        Task_Options() -> None
        任务选项初始化

        :return: None
        """
        OPTIONS().Task_Option_Set_Off_All()
        print("可选任务:")
        print("0、全选\t", end='')
        for key, value in OPTIONS().Task_Options.items():
            print(f"{key}、{value}\t", end='')
        print(hint if hint else '')
        OPTIONS().Task_Option_Set_On_All()
        return None

_inst = OPTIONS_MANAGE
Init_Options = _inst.Init_Options
