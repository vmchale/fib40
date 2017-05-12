var http = require('http');

function fibonacci(n) {
    if (n < 2)
        return 1;
    else
        return fibonacci(n-2) + fibonacci(n-1);
}

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type' : 'text/plain'});
    res.end(fibonacci(40) + '');
}).listen(3000);
