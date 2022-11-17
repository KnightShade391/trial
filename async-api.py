from flask import Flask, jsonify
import asyncio
import time
from threading import Thread

app = Flask(__name__)

async def speak_async():
    time.sleep(3)
    print('OMG asynchronicity!')

def threaded_task(duration):
    for i in range(duration):
        print("Working... {}/{}".format(i + 1, duration))
        time.sleep(1)

@app.route('/')
def hello():
    thread = Thread(target=threaded_task, args=(10,))
    thread.daemon = True
    thread.start()
    return jsonify({'thread_name': str(thread.name),'started': True})

if __name__ == '__main__':
    app.run()
