# -*- coding: utf-8 -*-
"""
Created on Sun May 26 20:45:52 2024

@author: rahul
"""

import os
import datetime


def startTime():
    INIT =  open(os.path.join(os.getcwd(), 'logs/init.csv'), "a+")
    x = f"'{datetime.datetime.now()}', '{os.getenv('USERNAME')}', '{os.getenv('PROCESSOR_IDENTIFIER')}' \n"
    INIT.write(x)
    INIT.close()

def SaveSettings(SETTINGS, VARIABLES):
    SAVE = open(os.path.join(os.getcwd(), 'logs/save.csv'), "a+")
    x = f"{SETTINGS['model_directory']}, {SETTINGS['nltk_directory']}, {SETTINGS['img_shape']}, {SETTINGS['model_publisher']}, {SETTINGS['model_name']}, {SETTINGS['temperature']}, {SETTINGS['offset']}, {SETTINGS['grad_scale']}, {SETTINGS['working_dic']}\n"
    SAVE.write(x)
    SAVE.close()

def reportFailure(x):
    FAIL = open(os.path.join(os.getcwd(), 'logs/faillogs.csv'), "a+")
    x = "'Time', 'StudentID', 'StudentName', 'Branch', 'Score'\n"
    FAIL.write(x)
    FAIL.close()

def reportScore(x):
    STUDENT = open(os.path.join(os.getcwd(), 'logs/scorelogs.csv'), "a+")
    x = "'Time', 'StudentID', 'StudentName', 'Branch', 'Score'\n"
    STUDENT.write(x)
    STUDENT.close()
    
def setlogFiles():
    if not os.path.exists('logs'):
        os.system('mkdir logs')
    PATH = os.getcwd()
    FAIL = open(os.path.join(PATH, 'logs/faillogs.csv'), "a+")
    FAIL.write("'Time', 'cause'\n")
    FAIL.close()
    STUDENT =  open(os.path.join(PATH, 'logs/scorelogs.csv'), "a+")
    STUDENT.write("'Time', 'StudentID', 'StudentName', 'Branch', 'Score'\n")
    STUDENT.close()
    INIT =  open(os.path.join(PATH, 'logs/init.csv'), "a+")
    INIT.write("'Time&Day', 'SystemUSerName', 'PROCESSOR_IDENTIFIER'\n")
    INIT.close()
    SAVE = open(os.path.join(PATH, 'logs/save.csv'), "a+")
    SAVE.write("'max_length','model_directory','nltk_directory', img_shape', 'model_publisher', 'model_name', 'temperature', 'offset', 'grad_scale', 'model', 'working_dic', 'setlogFiles'\n")
    SAVE.close()    