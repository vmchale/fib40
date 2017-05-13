from flask import Flask, request
app = Flask(__name__)

def fib_memo(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fib_memo(n-1) + fib_memo(n-2))
    return 1

def fib(n):
    x = [1,1]
    for i in range(n):    
        x.append(x[-1] + x[-2])
    return x[n]

def fib_naive(n):
    if n == 0: return 1
    elif n == 1: return 1
    else: return fib_naive(n-1) + fib_naive(n-2)

@app.route('/', methods=['GET'])
def fib_bench():
    return '{n}\n'.format(n=fib_naive(40))

if __name__ == '__main__':
    app.run(host='localhost', port=3000)
