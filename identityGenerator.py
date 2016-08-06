# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 14:15:11 2016

@author: goalves
"""

import argparse
import random
from datetime import datetime
import string

def parser():
    parser=argparse.ArgumentParser(description='Generates a Random Identity')
    parser.add_argument('--min-age', help='Minimum age', dest='minAge', default=18)    
    parser.add_argument('--max-age', help='Maximum age', dest='maxAge', default=60)    
    parser.add_argument('-v', help='Verbose', dest='verbose', action='store_true', default=False)
    parser.add_argument('-g', '--gender', dest='gender', default=None)
    parser.add_argument('-l', '--length', dest='length', default=10)
    return parser.parse_args()
    
def generateDateOfBirth(minAge, maxAge):
    age=random.randint(minAge, maxAge)
    now=datetime.now()
    currentYear=now.year
    yearBorn=currentYear - age
    monthBorn=random.randint(1,12)
    dayBorn=random.randint(1,28)
    
    if monthBorn==now.month:
        if dayBorn>now.day:
            yearBorn-=1
    elif monthBorn>now.month:
        yearBorn-=1
        
    return yearBorn, monthBorn, dayBorn, age

def getName(file):
    selected=random.random()*90
    with open(file) as nameFile:
        for line in nameFile:
            name, zeros, cumulative, id = line.split()
            if float(cumulative)>selected:                        
                return name.capitalize()

def getFirstName(gender):
    genderList=('male', 'female')
    if gender not in genderList:
        gender=random.choice(genderList)
    return getName(gender+'FirstNames.txt')
    
def getLastName():
    return getName('lastNames.txt')
    
def getFullName(gender):
    firstName=getFirstName(gender)
    lastName=getLastName()
    return firstName, lastName
###Refactor
def generateUserName(firstName, lastName, year, month, day):
    userName=''    
    #includeSeparator=False    
    #separator=random.choice(('.','_'))
    #if random.randint(0,1):
    #    includeSeparator=True
    lst=[firstName, lastName, year, month, day]    
    nIterations=random.randint(3, len(lst))
    for i in range(0, nIterations):
        element=random.choice(lst)
        userName+=str(element)
    #    if includeSeparator:
    #        userName+=separator
        lst.remove(element)
    #userName=firstName +lastName + str(year) + str(month) + str(day)
    return userName.lower()

def generatePassword(length):
    password=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits+ ' _#$&=') for _ in range(length))
    return password

def main():
    args=parser()
    firstName, lastName=getFullName(args.gender)
    
    yearBorn, monthBorn, dayBorn, age = generateDateOfBirth(args.minAge, args.maxAge)
    userName=generateUserName(firstName, lastName, yearBorn, monthBorn, dayBorn)        
    password=generatePassword(args.length)
    if args.verbose:
        print('First Name: {}'.format(firstName))
        print('Last Name: {}'.format(lastName))
        print('Year of Birth: {}'.format(yearBorn))
        print('Month of Birth: {}'.format(monthBorn))
        print('Day of Birth: {}'.format(dayBorn))
        print('Age: {}'.format(age))
    else:
        print('Full Name: {} {}'.format(firstName, lastName))
        print('Date of Birth: {}-{:02d}-{:02d}\tAge: {}'.format(yearBorn, monthBorn, dayBorn, age))
        print('User Name: {}'.format(userName))
        print('Password: {}'.format(password))
    
if __name__ == '__main__':
    main()