var http = require("http");

http.createServer(function(request, response) {
  response.writeHead(200, {"Content-Type": "text/html"});
  response.write("<!DOCTYPE html><html><head><title>Jarvis</title></head><body><h1>Jarvis Test Dashboard</h1></body></html>");
  response.end();
}).listen(8891);