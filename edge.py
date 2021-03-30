#!/usr/bin/python


# The dictionary key represent the script functions and the values are the arguments needed to be passed
Scripts = {
    'add customer': ['add', 'customer', 'TARIFF', 'IP'],
    'add tariff': ['add', 'tariff', 'TARIFF','UP','DOWN'],
    'add suspend': ['add', 'suspend', 'IP'],
    'delete customer': ['delete', 'customer', 'TARIFF', 'IP'],
    'delete tariff': ['delete', 'tariff', 'TARIFF'],
    'delete suspend': ['delete', 'suspend', 'IP']
}

# Those are dynamic arguments (IP, Tariff plan name) that are imported by the user
Dynamic_Arguments = {
    'add customer': ['TARIFF','IP'],
    'add tariff': ['TARIFF','UP','DOWN'],
    'add suspend': ['IP'],
    'delete customer': ['TARIFF', 'IP'],
    'delete tariff': ['TARIFF'],
    'delete suspend': ['IP']
}
# put comments on each of the script after being executed
comments = {
    'add customer': 'Adding a customer to the tariff plan',
    'add tariff': 'Creating a brand new Tariff plan',
    'add suspend': 'Suspending the customer',
    'delete customer': 'Deleting customer from a tariff plan',
    'delete tariff': 'Deleting Tariff plan',
    'delete suspend': 'Removing customer from suspend list'
}
# import Checking functions

from check import *
import sys

Results={Checker(sys.argv,Scripts[key],Dynamic_Arguments[key]):key for key in Scripts.keys()}

try:
    script=Results[True]
except:
    print("Invalid Input")
    exit(1)

try:
    print(comments[script])
except:    pass

Dynamic_Argument={key:key for key in Dynamic_Arguments[script]}
Dynamic_Argument['WAN']='WAN'
for Some in zip(sys.argv[1:],Scripts[script]):
    if(Some[1] in Dynamic_Argument.keys()):
        Dynamic_Argument[Some[1]]=Some[0]

Dynamic_Argument=[Sample[0]+"="+Sample[1]+'\n' for Sample in zip(Dynamic_Argument.keys(),Dynamic_Argument.values())]
Dynamic_Argument=str().join(Dynamic_Argument)


with open("./configure/prefix.vbash",'r') as prefix:
 with open("./configure/"+script+".vbash",'r') as SCRIPT:
  with open('Script.vbash','w+') as file:
   file.write(prefix.read())
   file.write('\n')
   file.write(Dynamic_Argument)
   file.write('\n')
   file.write(SCRIPT.read())

import os
os.system('vbash Script.vbash')