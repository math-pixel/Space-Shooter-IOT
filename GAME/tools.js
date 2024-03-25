// Point is in rect
// Prend un point et un rect et renvoie true ou false
function pointIsInRect(point, rect) {
    if (point[0] > rect[0] && point[0] < (rect[0] + rect[2]) && point[1] > rect[1] && point[1] < (rect[1] + rect[3])) {
        return true
    }
    return false
}

// rect is in rect
// prend deux rect et renvoie un tableau avec les points qui sont en contact avec le deuxième rectangle
function rectIsInRect(rect1, rect2) {

    if (pointIsInRect(getTopCornerLeft([rect1[0], rect1[1], rect1[2], rect1[3]]), rect2)) {
        return true
    }
    if (pointIsInRect(getTopCornerRight([rect1[0], rect1[1], rect1[2], rect1[3]]), rect2)) {
        return true
    }
    if (pointIsInRect(getBottomCornerLeft([rect1[0], rect1[1], rect1[2], rect1[3]]), rect2)) {
        return true
    }
    if (pointIsInRect(getBottomCornerRight([rect1[0], rect1[1], rect1[2], rect1[3]]), rect2)) {
        return true
    }
    return false
}



// Get Corners
// Prends un rect et renvoie un point sous forme -> [x, y]
function getTopCornerLeft(rect) {
    return [rect[0], rect[1]]
}

function getTopCornerRight(rect) {
    return [rect[0] + rect[2], rect[1]]
}

function getBottomCornerLeft(rect) {
    return [rect[0], rect[1] + rect[3]]
}

function getBottomCornerRight(rect) {
    return [rect[0] + rect[2], rect[1] + rect[3]]
}

function getCenterOfRect(rect){
    return [rect[0] + rect[2] / 2, rect[1] + rect[3] / 2]
}
