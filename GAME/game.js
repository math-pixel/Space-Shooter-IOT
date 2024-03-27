// Step 1: Setup
let shipImg;
let missileImg;
let ennemieImg;
let backgroundImage;
let lifeImage;
let shipX, shipY;
let missileX, missileY;
let allMissile = []
const missileSpeed = 5;
let shipSpeed = 3;

let ptLife = 4

let stateGame = "inGame" // home , inGame, end
let stateMouvement = {
    up: false,
    right: false,
    down: false,
    left: false
}

let ennemies = []
let ennemieSpeed = 2


function preload() {
  shipImg = loadImage('assets/ship.png');
  missileImg = loadImage('assets/laser.png');
  ennemieImg = loadImage('assets/ship2.png');
  backgroundImage = loadImage('assets/bg.jpg')
    backgroundImage.play()

    lifeImage = [loadImage('assets/lifes/1.png'), loadImage('assets/lifes/2.png'), loadImage('assets/lifes/3.png'),loadImage('assets/lifes/4.png'),loadImage('assets/lifes/5.png')]
}

function setup() {
  createCanvas(1000, 800);
  shipX = width / 2;
  shipY = height / 2;
}

// Step 2: Draw
function draw() {
    image(backgroundImage, 0, 0, 1000, 800)

    switch(stateGame){
        case "home":
            textSize(32);
            fill(255);
            stroke(0);
            strokeWeight(4);
            text('Waiting to connection', 350, 390);
            break
            
        case "inGame":
            drawGame()
            break

        case "end":
            textSize(32);
            fill(255);
            stroke(0);
            strokeWeight(4);
            text('END GAME', 400, 390);
            break
        
    }

}

function drawGame(){
    
    
    // Calculate skew values based on movement
    let skewX = 0;
    let skewY = 0;
    if (stateMouvement.left) {
        shipX -= shipSpeed;
        skewX = -0.1;
    }
    if (stateMouvement.right) {
        shipX += shipSpeed;
        skewX = 0.1;
    }
    if (stateMouvement.up) {
        shipY -= shipSpeed;
        skewY = -0.1;
    }
    if (stateMouvement.down) {
        shipY += shipSpeed;
        skewY = 0.1;
    }
    
    // Draw ship with skew
    push();
    translate(shipX, shipY);
    shearX(skewX);
    shearY(skewY);
    imageMode(CENTER);
    image(shipImg, 0, 0, 100, 100);

    pop();
  
    // Draw missile
    allMissile.forEach((currentMissile, index) => {
        image(missileImg, currentMissile.x, currentMissile.y, 50, 50);
        currentMissile.y -= missileSpeed;

        if (currentMissile.y < -10){
            allMissile.splice(index, 1);
        }
    })
    
    // draw ennemie
    ennemies.forEach((currentEnnemi, index) => {
        image(ennemieImg, currentEnnemi.x, currentEnnemi.y, 50, 50);


        rectCurrentEnnemi = [currentEnnemi.x, currentEnnemi.y, 50, 50]
        
        
        if (currentEnnemi.y > 800){
            ennemies.splice(index, 1);
            ptLife -= 1
            if (ptLife == 0) {
                stateGame = "end"
            }
        }else{
            allMissile.forEach((cMissile, indexMissile) => {
                rectMissile = [cMissile.x, cMissile.y, 50, 50]
                if (rectIsInRect(rectCurrentEnnemi, rectMissile)) {
                    allMissile.splice(indexMissile,1)
                    ennemies.splice(index, 1);
                }
            })
        }
        
        
        currentEnnemi.y += currentEnnemi.speed;
    })
    image(lifeImage[ptLife], 0, 0)
}

// Step 4: Firing
function keyTyped() {
  if (key === ' ') {
    fireBullet()
  }
}

function fireBullet(){
    allMissile.push({x: shipX, y: shipY})
}

function ennemieSpawn(interval){
    setTimeout(() => {
    
        ennemies.push({x: getRandomArbitrary(50, 950), y: 0, speed: ennemieSpeed})
        ennemieSpawn( getRandomArbitrary(500, 2000) )

    }, interval )
}

ennemieSpawn(1000)


function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

function keyPressed(){
    if (keyCode === LEFT_ARROW) {
        stateMouvement.left = true
    }
    if (keyCode == RIGHT_ARROW) {
        stateMouvement.right = true

    }
    if (keyCode == DOWN_ARROW) {
        stateMouvement.down = true

    }
    if (keyCode == UP_ARROW) {
        stateMouvement.up = true

    }
}

function keyReleased() {
    if (keyCode === LEFT_ARROW) {
        stateMouvement.left = false
    }
    if (keyCode == RIGHT_ARROW) {
        stateMouvement.right = false
    }
    if (keyCode == DOWN_ARROW) {
        stateMouvement.down = false
    }
    if (keyCode == UP_ARROW) {
        stateMouvement.up = false
    }
  }