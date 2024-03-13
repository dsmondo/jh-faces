const http = require('http');
const { exec } = require('child_process');

const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      try {
        const data = JSON.parse(body);
        if (data && data.ref === 'refs/heads/master') {
          // Pull the latest changes from GitHub
          exec('git pull origin master', (error, stdout, stderr) => {
            if (error) {
              console.error(`exec error: ${error}`);
              return;
            }
            console.log(`stdout: ${stdout}`);
            console.error(`stderr: ${stderr}`);
            // Restart Docker Compose
            exec('docker-compose stop && docker-compose up -d', (error, stdout, stderr) => {
              if (error) {
                console.error(`exec error: ${error}`);
                return;
              }
              console.log(`stdout: ${stdout}`);
              console.error(`stderr: ${stderr}`);
            });
          });
        }
      } catch (error) {
        console.error('Error parsing payload:', error);
      }
    });
    res.end('Received WebHook');
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

const PORT = 3003;
server.listen(PORT, () => {
  console.log(`Server running at port ${PORT}`);
});
