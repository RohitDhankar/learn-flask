# REDIS --- WIP 
from flask import Flask , render_template , url_for , request , redirect
import redis 
from rq import Queue
import time

app = Flask(__name__)

r = redis.Redis()
print(type(r)) #<class 'redis.client.Redis'>
q = Queue(connection=r)
print(type(q)) #<class 'rq.queue.Queue'>

#my_ls = [1,2,2,3,3,4,4,5,5]
def someTask(n):
    delay = 2 
    print("delay ==2 ")
    time.sleep(delay)
    print(len(n))
    print("All Done - thanks")
    return len(n)

#someTask(my_ls)

@app.route("/root_url")
def taskQueue():
    if request.args.get("n"): # Why Double Quotes here ? 
        job = q.enqueue(someTask,request.args.get("n")) # Why Double Quotes here ? 
        # This - job - created above , will be Heard and Picked up by the - rq - worker 
        print("---job.get_id()----",job.get_id())
        print(n)
        q_len = len(q)
        print("--tasks in q -- length of - q == ",q_len)

        return print(q_len)
    return "nothing in Q"

if __name__ == "__main__":
    app.run()    































