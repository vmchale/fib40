from flask import Flask, request
app = Flask(__name__)

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1) + fib(n-2)

@app.route('/', methods=['GET'])
def fib_bench():
    return '{n}'.format(n=fib(40))

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
