import io, json
import sys
import os
from datetime import datetime
import codecs

def add():
    note = ""
    tags = []
    ''' filters = { filter1:[] } '''
    filters = {}
    for arg in sys.argv[2:]:
        if '+' in arg:
            tags.append(arg)
        elif ':' in arg:
            filter_key, value = arg.split(':')
            if filter_key not in filters:
                filters[filter_key] = []
            filters[filter_key].append(value)
        else:
            note += arg
    data = {'note':note, 'timestamp': str(datetime.now()), 'filters': filters,
    'tags': tags}

    home = os.path.expanduser('~')
    with open(home+'/data.txt', 'a+') as f:
        json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)

subcommand = sys.argv[1]
if subcommand == 'add':
    add()
