# REDIS --- WIP 
from flask import Flask , render_template , url_for , request , redirect
import redis 
from rq import Queue
import time

app = Flask(__name__)

r = redis.Redis()
print(type(r))
q = Queue(connection=r)
print(type(q))

my_ls = [1,2,2,3,3,4,4,5,5]
def someTask(my_ls):
    delay = 2 
    print("delay ==2 ")
    time.sleep(delay)
    print(len(my_ls))
    print("All Done - thanks")
    return len(my_ls)

#someTask(my_ls)

@app.route("/root_url")
def taskQueue():
    if request.args.get("my_ls"): # Why Double Quotes here ? 
        job = q.enqueue(someTask,request.args.get("my_ls")) # Why Double Quotes here ? 
        # This - job - created above , will be Heard and Picked up by the - rq - worker 
        print(my_ls)
        q_len = len(q)
        print("--tasks in q -- length of - q == ",q_len)

        return print(q_len)
    return "nothing in Q"

if __name__ == "__main__":
    app.run("my_ls")    































