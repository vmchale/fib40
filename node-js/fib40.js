var http = require('http');

function fib_naive(n) {
    if (n < 2)
        return 1;
    else
        return fib_naive(n-2) + fib_naive(n-1);
}

function fib(n) {
    for(var fibArray = [0,1], i=0,j=1,k=0; k < n;i=j,j=x,k++ ){
        x=i+j;
        fibArray.push(x);
    }
    return fibArray[n];
}

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type' : 'text/plain'});
    res.end(fib_naive(40) + '');
}).listen(3000);
