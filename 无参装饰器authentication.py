# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:23:21 2022

@author: pioglola
"""


def authentication(func):
     
    def wrapper(*args,**kwargs):
        print('Please input your account info')
        while True:
            inp_name=input('your username===>').strip()
            inp_pwd=input('your password===>').strip()
            
            with open('user_info.txt',mode='rt',encoding='utf-8') as f:
                for line in f:
                    username,password= line.strip().split(":")
                    if inp_name == username and inp_pwd == password:
                        print('Logged in ')
                        func(*args,**kwargs)
                        break
                else:
                    print('Please re-enter your name and password.')
        
    return wrapper
        
    
@authentication    
def cutie(x):
    print('%s,You are a cutie, you are always right.' %(x))

x=input('Tell me your nickname plz>>>')
cutie(x)
