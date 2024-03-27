

const socket = io();

socket.on("connect", () => {
    console.log(socket.connected); // true
});

socket.on("disconnect", () => {
    // console.log(socket.connected); // false
});

/*
{
    x: left | right | idle,
    y: up | down | idle
}
*/
socket.on("mouvement", (data) => { 
    print(data)
    if (data.x == "left") {
        stateMouvement.left = true
        stateMouvement.right = false
    }else if (data.x == "right") {
        stateMouvement.left = false
        stateMouvement.right = true
    }else if (data.x == "idle") {
        stateMouvement.left = false
        stateMouvement.right = false
    }

    if (data.y == "up") {
        stateMouvement.up = true
        stateMouvement.down = false
    }else if (data.y == "down") {
        stateMouvement.up = false
        stateMouvement.down = true
    }else if (data.y == "idle") {
        stateMouvement.up = false
        stateMouvement.down = false
    }
});

socket.on("fire", () => {
    fireBullet()
})

socket.on("setSpeed", (speed) => {
    shipSpeed = speed
})