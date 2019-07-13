# To do list app
import sys
import re

"""
    Args:
        --add (add a new task)
        --remove (remove a task)
        --update (update details of task)
"""

tasks = []

def add(task):
    # Urgency, Time duration, Subtasks
    while True:
        isUrgent = input('Is urgent (yes/no): ')
        timeDuration = input('Time duration: 45sec|5min|2hour: ')
        if isUrgent != 'yes' and isUrgent != 'no':
            continue
        else:
            break

    pattern = re.compile(r'\d?\d(sec|min|hour)')
    time = pattern.search(timeDuration).group()
    task = {'name': task,
            'urgent': isUrgent,
            'time': time,
            'completed': False
            }
    tasks.append(task)
    return task



def handleArgs():
    # Maximum number of args to be passed
    # First arg will always be program name
    acceptedArgs = ['--add', '--remove', '--update']
    for arg in sys.argv[1:]:
        if arg not in acceptedArgs:
            print(arg + ' Not found')
            sys.exit(1)
        else:
            if arg == acceptedArgs[0]:
                print(add('Cleaning'))

    # if len(sys.argv[1:]) > 3:
    #     print('Exceeded args')
    #     sys.exit(1)

handleArgs()
