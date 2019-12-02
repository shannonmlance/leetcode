// for solving a palindrome that is centered in the string

// examples:
//     "babab"
//     "babad"
//     "cbbd"

/**
 * @param {string} str
 * @return {string}
 */
var longestPalindrome = function(str) {
    var palindrome = "";
    for (var i = 0; i < str.length/2; i++) {
        if (str[i] == str[str.length - 1 - i]) {
            palindrome += str[i];
        }
    }
    var fullPalindrome = palindrome;
    if (palindrome.length > 1) {
        for (var i = palindrome.length - 2; i >= 0; i--) {
            fullPalindrome += palindrome[i];
        }
    }
    if (palindrome == 0) {
        return "No palindrome exists.";
    }
    else {
        fullPalindrome += palindrome;
    }
    return fullPalindrome;
};

/**
 * @param {string} str
 * @return {string}
 */

var isPalindrome = function(str) {
    console.log("checking if " + str + " is a palindrome");
    if (str.length <= 1) {
        console.log("string has one letter or less");
        console.log(str + " is a palindrome");
        return true;
    }
    else {
        console.log("string has more than one letter");
        if (str[0] == str[str.length - 1]) {
            console.log("the beginning and end letters of the string match");
            console.log("will continue checking");
            return isPalindrome(str.substring(1, str.length - 1))
        }
        else {
            console.log("the beginning and end letters of the string do not match");
            console.log(str + " is not a palindrome");
            return false;
        }
    }
}

var longestPalindrome = function(str) {
    // if there is more than one letter in the string
    if (str.length > 1) {
        console.log("string has more than one letter");
        var palindromeArr = [];
        // loop through the string, to set the first letter for finding a substring palindrome
        for (var i = 0; i < str.length; i++) {
            console.log("starting search with letter " + str[i]);
            palindrome = str[i];
            console.log("adding " + palindrome + " to the array");
            palindromeArr.push(palindrome);
            // loop through the remaining letters, adding them one at a time, and comparing if they are palindromes
            for (var j = i + 1; j < str.length; j++) {
                console.log("adding letter " + str[j]);
                palindrome += str[j];
                var bool = isPalindrome(palindrome);
                // if it is a palindrome, add it to the array
                if (bool == true) {
                    console.log("adding " + palindrome + " to the array");
                    palindromeArr.push(palindrome);
                }
            }
        }
        // sort array and find longest palindrome
        palindromeArr.sort(function(a, b) {
            console.log("sorting array...");
            return b.length - a.length;
        });
        console.log("found the largest palindrome");
        console.log(palindromeArr[0].toUpperCase());
        return palindromeArr[0];
    }
    else {
        console.log("string has one letter or less");
        console.log("found the largest palindrome");
        console.log(str.toUpperCase());
        return str;
    }
}