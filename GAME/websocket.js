

const socket = io("localhost");

socket.on("connect", () => {
    console.log(socket.connected); // true
});

socket.on("disconnect", () => {
    console.log(socket.connected); // false
});

socket.on("data", () => { /* ... */ });