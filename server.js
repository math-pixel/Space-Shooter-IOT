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

app.get("/dataGyro", (req, res) => {
  const x = req.query.x; // x: left | right | idle,
  const y = req.query.y; // y: up | down | idle
  console.log("new data position : ", x, y)
  io.emit("mouvement", {x: x, y:y})
  res.send("data receive")
})

httpServer.listen(8000);