"""
    Create a xml to make transitioning wallpaper
    Specify time for each image
"""

from bs4 import BeautifulSoup

start_time = {
    'year': 2011,
    'month': 6,
    'day': 20,
    'hour': 7, # Default starttime set to 7 AM
    'minute': 00,
    'second': 00,
    'names': {
        'name1': {
            'name11': 'Alice'
        }
    }
}

pictures_dir = ''

# Duration in which to change in seconds
#           7 - 8    8 - 1    1 - 6    7 - 12   12 - 5   5 - 7
time_sets = [3600.0, 18000.0, 18000.0, 21600.0, 18000.0, 7200.0]

def writeChanges():
    result_file = open('result.xml', 'r')

    


writeChanges()
items = start_time.values()

print(items)