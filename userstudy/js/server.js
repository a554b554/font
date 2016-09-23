const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;
var qs = require('querystring');
var fs = require('fs');

const server = http.createServer((req, res) => {
  // res.statusCode = 200;
  // res.setHeader('Content-Type', 'text/plain');
  // res.end('Hello World\n');
  if (req.method == 'POST') {
        var body = '';

        req.on('data', function (data) {
            body += data;

            // Too much POST data, kill the connection!
            // 1e6 === 1 * Math.pow(10, 6) === 1 * 1000000 ~~~ 1MB
            // if (body.length > 1e6)
                // request.connection.destroy();
        });

        req.on('end', function () {
            var post = qs.parse(body);
            post.toString();
            // use post['blah'], etc.
            // console.log('pst')
            console.log(post)
            fs.appendFile('./record/record.txt', JSON.stringify(post)+'\n', function(err){
              if(err) throw err;
              console.log('saved!')
            })
        });
        // console.log('body')
        // console.log(body)
    }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
