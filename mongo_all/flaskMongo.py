# flask app connected to a MongoDB Standalone instance ( Not a Cluster)
# https://cloud.mongodb.com


# Method getcwd() - (from the os library) gets the current working directory for classes. Class
# conn is then imported.
# os.getcwd() returns the absolute path of the working directory where Python is currently running as a string str.

"""
Source - https://docs.python.org/3/library/csv.html#csv.DictReader
    #The fieldnames parameter is a sequence. 
    If fieldnames is omitted, the values in the first
     row of file f will be used as the fieldnames.
      Regardless of how the fieldnames are determined, 
      the dictionary preserves their original ordering.
"""

"""
Source -- https://docs.python.org/3/library/json.html
Note - 
JSON is a subset of YAML 1.2. The JSON produced by this module’s default settings (in particular, the default separators value) is also a subset of YAML 1.0 and 1.1. This module can thus also be used as a YAML serializer.
Note - 
This module’s encoders and decoders preserve input and output order by default. Order is only lost if the underlying containers are unordered.
Prior to Python 3.7, dict was not guaranteed to be ordered, so inputs and outputs were typically scrambled unless collections.OrderedDict was specifically requested. Starting with Python 3.7, the regular dict became order preserving, so it is no longer necessary to specify collections.OrderedDict for JSON generation and parsing.

"""

"""
SOURCE -- https://stackoverflow.com/questions/36059194/what-is-the-difference-between-json-dump-and-json-dumps-in-python
## FOOBAR -- Read Further seems dumps - is Faster though eats more memory 

If you want to dump the JSON into a file/socket or whatever, then you should go with dump(). 
If you only need it as a string (for printing, parsing or whatever) then use dumps() (dump string)
"""
    
import json, csv, sys, os , time
#sys.path.append(os.getcwd()+'/classes')
#import conn

""" Source - https://api.mongodb.com/python/current/tutorial.html """
from pymongo import MongoClient
client = MongoClient('localhost', port=27017) 
#print(type(client)) #<class 'pymongo.mongo_client.MongoClient'>
""" Alternative -URI Format -MongoClient('mongodb://localhost:27017/')"""
#flask_test.coll_1.insert({name: "Rohit Dhankar", alias: 'rd'})

db = client['flask_test'] #access databases using attribute style access on MongoClient instances
collection = db.coll_1
#print(collection)
#Collection(Database(MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True), 'flask_test'), 'coll_1')
insert_dict = {'name': "Rohit Dhankar_1", 'alias': 'rd_1'}
result = collection.insert_one(insert_dict)
# Above - exact same Record will get inserted Multiple Times with a DIFF = _id = '_id': ObjectId(
"""
{'_id': ObjectId('5f7752b8fafb9872d45dab6a'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
{'_id': ObjectId('5f7753eb4cf20aa6747190e0'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
{'_id': ObjectId('5f7754151e2fdb708aec17fd'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
{'_id': ObjectId('5f77545efadd4c73f2a00fdf'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
{'_id': ObjectId('5f77551b07b3516a62e85e1c'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
"""
print('Record Inserted : {0}'.format(result.inserted_id))
#Record Inserted : 5f7752b8fafb9872d45dab6a
print(collection.find_one())
#{'_id': ObjectId('5f774e4b94c9da14793d06a7'), 'name': 'Rohit Dhankar', 'alias': 'rd'}
for doc_test in collection.find():
    print(doc_test)
"""
{'_id': ObjectId('5f7752b8fafb9872d45dab6a'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
{'_id': ObjectId('5f7753eb4cf20aa6747190e0'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
{'_id': ObjectId('5f7754151e2fdb708aec17fd'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
{'_id': ObjectId('5f77545efadd4c73f2a00fdf'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
{'_id': ObjectId('5f77551b07b3516a62e85e1c'), 'name': 'Rohit Dhankar_1', 'alias': 'rd_1'}
"""





def read_dict(f):#, h):
    input_file = csv.DictReader(open(f))#, fieldnames=h)
    #print(type(input_file)) #<class 'csv.DictReader'>
    return (input_file)

def conv_reg_dict(ls_order_dict_input):
    """
    #Function conv_reg_dict() converts a -- list of OrderedDict elements -- to a list of
    #regular dictionary elements (for easier processing).
    #
    # dict_ls == Its a LIST of DICTS - the DICT at Element 0 (for the mtcars.csv) is as seen below 
    Its the FIRST DATA ROW of the mtcars.csv File , the Column Labels are now DICT KEYS 
    and the FIRST DATA ROW is VALUES
     
    # {'model': 'Mazda RX4', 'mpg': '21', 'cyl': '6', 
    'disp': '160', 'hp': '110', 'drat': '3.9', 
    'wt': '2.62', 'qsec': '16.46', 'vs': '0', 'am': '1', 'gear': '4', 'carb': '4'}
    """
    #print(ls_order_dict_input) #<csv.DictReader object at 0x7ff20c538e20>
    #print(type(order_dict_in)) #<class 'csv.DictReader'>
    #print(order_dict_in.item()[0])
    return [dict(x) for x in ls_order_dict_input]
    
def dump_json(file_json, dict_input):
    """ writes JSON data to disk"""
    with open(file_json, 'w') as file_json:
        start_time = time.process_time()# DEPRECATED - time.clock()
        json.dump(dict_input, file_json)
        end_time = time.process_time()# DEPRECATED - time.clock()
        #
        time_diff = end_time - start_time
        print("-----time_diff------",time_diff)
        #-----time_diff------ 12.416963380000002 (699 MB CSV File)
        #-----time_diff------ 0.662583566 (8 MB CSV File)
        #-----time_diff------ 0.00028367600000000007 ( mtcars)
        # FOOBAR - Use -- json.dumps(dict_input, file_json) 
        # Faster - Need to Timeit

def read_json(f):
    """ reads JSON data from disk"""
    with open(f) as f:
        return json.load(f)

if __name__ == '__main__':
    #csv_file_in = '/home/dhankar/temp/flask/1/learn-flask/mysql/csvData/mtcars.csv' # FoobarABS path -- change t relative
    csv_file_in = '/home/dhankar/temp/flask/1/learn-flask/mongo_testData/train.csv' # 8 MB File Size
    #csv_file_in = '/home/dhankar/temp/flask/1/learn-flask/mongo_testData/a_z_handwritten_data.csv' # 699 MB File Size
    
    #headers = ['first', 'last'] # this is Read from File FIRST ROW if - fieldnames- left as None
    # Above line - headers == fieldnames of the == class 'csv.DictReader' -- FOOBAR See comment above 
    r_dict = read_dict(csv_file_in)#, headers)
    #print("--type(r_dict)---",type(r_dict)) #<class 'csv.DictReader'>
    #
    dict_ls = conv_reg_dict(r_dict)
    print("---type(dict_ls)---",type(dict_ls)) #<class 'list'>
    print("---type(dict_ls)---",dict_ls[0]) #
    
    json_file = '/home/dhankar/temp/flask/1/learn-flask/mongo_testData/test.json'
    dump_json(json_file, dict_ls) #def dump_json(file_json, dict_input):
    data = read_json(json_file)
    #print(type(data)) # <class 'list'>
    print("          "*10)
    #print(data)


    # obj = conn.conn('test')
    # db = obj.getDB()
    # names = db.names
    # names.drop()
    # for i, row in enumerate(data):
    #     row['_id'] = i
    #     names.insert_one(row)
    # n = 3
    # print('1st', n, 'names:')
    # people = names.find()
    # for i, row in enumerate(people):
    #     if i < n:
    #         print (row)
    # people.rewind()
    # print('\n1st', n, 'names with rewind:')    
    # for i, row in enumerate(people):
    #     #
    #     if i < n:
    #         print (row)
    # print ('\nquery 1st', n, 'names')
    # first_n = names.find().limit(n)
    # for row in first_n:
    #     print (row)
    # print ('\nquery last', n, 'names')
    # length = names.find().count()
    # last_n = names.find().skip(length - n)
    # for row in last_n:
    #     print (row)
    # fnames = ['Ella', 'Lou']
    # lnames = ['Vader', 'Pole']    
    # print ('\nquery Ella:')
    # query_1st_in_list = names.find( {'first':{'$in':[fnames[0]]}})
    # for row in query_1st_in_list:
    #     print (row)
    # print ('\nquery Ella or Lou:')
    # query_1st = names.find( {'first':{'$in':fnames}} )
    # for row in query_1st:
    #     print (row)



