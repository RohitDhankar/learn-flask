# flask app connected to a MongoDB Standalone instance ( Not a Cluster)
# https://cloud.mongodb.com


# Method getcwd() - (from the os library) gets the current working directory for classes. Class
# conn is then imported.
# os.getcwd() returns the absolute path of the working directory where Python is currently running as a string str.


import json, csv, sys, os
sys.path.append(os.getcwd()+'/classes')
import conn

def read_dict(f, h):
    input_file = csv.DictReader(open(f), fieldnames=h)
    return (input_file)

def conv_reg_dict(d):
    return [dict(x) for x in d]

def dump_json(f, d):
    """ writes JSON data to disk"""
    with open(f, 'w') as f:
        json.dump(d, f)

def read_json(f):
    """ reads JSON data from disk"""
    with open(f) as f:
        return json.load(f)

if __name__ == '__main__':
    f = 'data/names.csv'
    headers = ['first', 'last']
    r_dict = read_dict(f, headers)
    dict_ls = conv_reg_dict(r_dict)
    json_file = 'data/names.json'
    dump_json(json_file, dict_ls)
    data = read_json(json_file)
    obj = conn.conn('test')
    db = obj.getDB()
    names = db.names
    names.drop()
    for i, row in enumerate(data):
        row['_id'] = i
        names.insert_one(row)
    n = 3
    print('1st', n, 'names:')
    people = names.find()
    for i, row in enumerate(people):
        if i < n:
            print (row)
    people.rewind()
    print('\n1st', n, 'names with rewind:')    
    for i, row in enumerate(people):
        #
        if i < n:
            print (row)
    print ('\nquery 1st', n, 'names')
    first_n = names.find().limit(n)
    for row in first_n:
        print (row)
    print ('\nquery last', n, 'names')
    length = names.find().count()
    last_n = names.find().skip(length - n)
    for row in last_n:
        print (row)
    fnames = ['Ella', 'Lou']
    lnames = ['Vader', 'Pole']    
    print ('\nquery Ella:')
    query_1st_in_list = names.find( {'first':{'$in':[fnames[0]]}})
    for row in query_1st_in_list:
        print (row)
    print ('\nquery Ella or Lou:')
    query_1st = names.find( {'first':{'$in':fnames}} )
    for row in query_1st:
        print (row)
