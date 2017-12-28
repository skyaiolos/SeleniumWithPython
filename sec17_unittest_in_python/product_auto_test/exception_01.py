#!/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/10/25

__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

"""
    Description:
        错误与异常处理
    try:
        #
    except ValueError:
        # 问题处理语句
    except TypeError:
        #
    except:
        #
    except:
        # 没有异常

"""
while True:
    try:
        n = int(input('请输入一个数字：'))
        m = int(input("请在输入一个数字："))

        result = n / m
        print(result)

    except TypeError as err:
        print("值类型有问题", err)

    except ValueError as err:
        print("输入的值有问题", err)

    except ZeroDivisionError:
        print("除数不能为0")

    except:
        print("其他错误")

    else:
        print(result)
        break

    finally:
        pass
