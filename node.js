// const { spawn } = require('child_process');

// const child = spawn('wc');

// process.stdin.pipe(child.stdin)

// child.stdout.on('data', (data) => {
//   console.log(`child stdout:\n${data}`);
// });


// var http = require('http');
// http.createServer(function (req, res) {
//   res.writeHead(200, {'Content-Type': 'text/plain'});
//   res.end('Hello World!');
// }).listen(8000);



let http = require('http');
let fs = require('fs');
 
let handleRequest = (request, response) => {
    response.writeHead(200, {
        'Content-Type': 'text/html'
    });
    fs.readFile('./ManycoreOS-demo/index.html', null, function (error, data) {
        if (error) {
            response.writeHead(404);
            respone.write('Whoops! File not found!');
        } else {
            response.write(data);
        }
        response.end();
    });
};
 
http.createServer(handleRequest).listen(8000);

//var spawn = require('child_process').spawn,
//    ls    = spawn('ls', ['-lh', '/usr']);
//
//ls.stdout.on('data', function (data) {
//  console.log('stdout: ' + data.toString());
//});
//
//ls.stderr.on('data', function (data) {
//  console.log('stderr: ' + data.toString());
//});
//
//ls.on('exit', function (code) {
//  console.log('child process exited with code ' + code.toString());
//});

const { exec } = require('child_process');

var ssa = exec('./bin/ssa -olblc -c glove.42B.300d_normalized', (err, stdout, stderr) => {
  if (err) {
    console.error(`exec error: ${err}`);
    return;
  }

  console.log(`Number of files ${stdout}`);
});

ssa.stdout.on('data', function(data) {
    console.log(data); 
});
