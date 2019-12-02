// create a square matrix of any size
function createMatrix(int) {
    // initialize a matrix
    var matrix = [];
    // variable to fill matrix
    var count = 1;
    // first loop to create rows
    for (var i = 0; i < int; i++) {
        // initialize empty rows
        matrix[i] = [];
        // second loop to fill columns
        for (var j = 0; j < int; j++) {
            // fill columns with incremented variable
            matrix[i][j] = count++;
        }
    }
    // return matrix for use in problem
    return matrix;
}

// rotate four points in a matrix that correspond with each other, for example: the four corners
function subrotate(matrix,a,b,c,d) {
    // store one point in a variable
    var i = matrix[a][b];
    // 4-point, in-place swap
    matrix[a][b] = matrix[d][a];
    matrix[d][a] = matrix[c][d];
    matrix[c][d] = matrix[b][c];
    matrix[b][c] = i;
}

// rotate the entire matrix
function rotate(matrix) {
    // if the matrix is empty, or contains only one value, no rotation is necessary
    if (matrix.length <= 1) {
        // simply return the matrix as is
        return matrix;
    }
    // define the end of the matrix
    var e = matrix.length - 1;
    // work from top to bottom, just the top half
    for (var x = 0; x < matrix.length/2; x++) {
        // work from left to right, shortening the ends for each parent loop (moving inward)
        for (var i = 0; i < matrix.length - (x*2) - 1; i++) {
            // rotate four points
            subrotate(matrix,x,x+i,e-x,e-x-i);
        }
    }
    return matrix;
}

// initialize a matrix for rotation
var matrix = createMatrix(10);
// call the main function to rotate the matrix
rotate(matrix);