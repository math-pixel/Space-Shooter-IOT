const express = require("express");
const { createServer } = require("http");
const { join } = require("path");
const { Server } = require("socket.io");

const app = express();
app.use(express.static('GAME'))
const httpServer = createServer(app);
const io = new Server(httpServer, { /* options */ });

io.on("connection", (socket) => {

  console.log("new connection websocket")

  socket.on("setSpeed", (data) => {
    console.log("set new speed")
    io.emit("setSpeed", data)
  })
  
  socket.on("fire", (data) => {
    console.log("fireeeeeeeeeeeeeeeee")
    io.emit("fire", data)
  })
  
  socket.on("mouvement", (data) => {
    console.log("new mouvement")
    io.emit("mouvement", data)
  })

});

// socket.emit("setSpeed", 1)
// socket.emit("fire")
// socket.emit("mouvement" , 
// {
//   x: "idle",
//   y: "idle"
// })

app.get("/", (req, res) => {
  res.sendFile(join(__dirname, "/GAME/index.html"))
})

httpServer.listen(8000);