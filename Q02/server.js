const https = require('https')
const express = require('express')
const fs = require('fs')
const path = require('path')
const app = express()
const port = 8080

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, '/index.html'))
})

https.createServer({
    key: fs.readFileSync('key.pem'),
    cert: fs.readFileSync('cert.pem')
}, app).listen(port)
console.log('Servidor iniciado em https://localhost:' + port)