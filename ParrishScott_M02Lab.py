# ParrishScott_M02Lab.py    Program to accept a students name and GPA and
# Scott Parrish             determine if the student qualifies for the Dean's
# M02 Lab                   List or Honor Roll.
# 10/25/23                  Version: 0.1

DEANS_LIST = 3.5
HONOR_ROLL = 3.25


while True:

    name = input('Enter last name for student or "ZZZ" to quit: ')
    
    if name.casefold() == 'zzz':
        break
    
    gpa = input(f'Enter GPA for student {name}: ')
    print(f'Student, {name} has the GPA: {gpa}.')

    confirm = input('Is this correct? (y/n) ')

    if confirm.casefold() != 'y':
        continue

    try:
        if float(gpa) >= DEANS_LIST:
            print(f'{name} has made both the Dean\'s List and the Honor Roll.')
        elif float(gpa) >= HONOR_ROLL:
            print(f'{name} has made the Honor Roll.')
        else:
            print(f'{name} has not qualified for the Honor Roll or Dean\'s List.')
    except ValueError:
        print(f'Exception: Student GPA must be a numeric value.  You typed: {gpa}')
    except:
        print('There was a problem...')

print('Exiting...')
