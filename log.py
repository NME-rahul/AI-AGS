# -*- coding: utf-8 -*-
"""
Created on Sun May 26 20:45:52 2024

@author: rahul
"""

import os

def reportFailure(x):
    FAIL = open(os.path.join(PATH, 'logs/faillogs.csv'), "a+")
    x = "'Time', 'StudentID', 'StudentName', 'Branch', 'Score'\n"
    FAIL.write(x)
    FAIL.close()

def reportScore(x):
    STUDENT = open(os.path.join(PATH, 'logs/scorelogs.csv'), "a+")
    x = "'Time', 'StudentID', 'StudentName', 'Branch', 'Score'\n"
    STUDENT.write(x)
    STUDENT.close()
    
if __name__ == "__main__":
    if not os.path.exist('logs'):
        os.system('mkdir logs')
    PATH = os.getcwd() 
    globalFAIL = open(os.path.join(PATH, 'logs/faillogs.csv'), "a+")
    FAIL.write("'Time', 'cause'\n")
    FAIL.close()
    STUDENT =  open(os.path.join(PATH, 'logs/scorelogs.csv'), "a+")
    STUDENT.write("'Time', 'StudentID', 'StudentName', 'Branch', 'Score'\n")
    STUDENT.close()
    
    
    