const express = require("express");
const { createServer } = require("http");
const { join } = require("path");
const { Server } = require("socket.io");

const app = express();
app.use(express.static('GAME'))
const httpServer = createServer(app);
const io = new Server(httpServer, { /* options */ });

io.on("connection", (socket) => {
  // ...
});

app.get("/", (req, res) => {
  res.sendFile(join(__dirname, "/GAME/index.html"))
})

httpServer.listen(3000);