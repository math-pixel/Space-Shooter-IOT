// Step 1: Setup
let shipImg;
let missileImg;
let shipX, shipY;
let missileX, missileY;
let allMissile = []
const missileSpeed = 5;
const shipSpeed = 3;


let ennemies = []
let ennemieSpeed = 2


function preload() {
  shipImg = loadImage('assets/ship.png');
  missileImg = loadImage('assets/ship.png');
}

function setup() {
  createCanvas(1000, 800);
  shipX = width / 2;
  shipY = height / 2;
}

// Step 2: Draw
function draw() {
    background(220);
    
    // Calculate skew values based on movement
    let skewX = 0;
    let skewY = 0;
    if (keyIsDown(LEFT_ARROW)) {
        shipX -= shipSpeed;
        skewX = -0.1;
    }
    if (keyIsDown(RIGHT_ARROW)) {
        shipX += shipSpeed;
        skewX = 0.1;
    }
    if (keyIsDown(UP_ARROW)) {
        shipY -= shipSpeed;
        skewY = -0.1;
    }
    if (keyIsDown(DOWN_ARROW)) {
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
    
    ennemies.forEach((currentEnnemi, index) => {
        image(missileImg, currentEnnemi.x, currentEnnemi.y, 50, 50);
        currentEnnemi.y += currentEnnemi.speed;

        if (currentEnnemi.y > 800){
            ennemies.splice(index, 1);
        }
    })
}

// Step 4: Firing
function keyTyped() {
  if (key === ' ') {
    allMissile.push({x: shipX, y: shipY})
  }
}

function ennemieSpawn(interval){
    setTimeout(() => {
    
        ennemies.push({x: getRandomArbitrary(0, 1000), y: 0, speed: ennemieSpeed})
        ennemieSpawn( getRandomArbitrary(500, 2000) )

    }, interval )
}

ennemieSpawn(1000)


function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}