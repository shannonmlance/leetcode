var str = "abcabc";
var iterations = 0;

function lengthOfLongestSubstring(str) {
    var substr = str[0];
    for (i = 1; i < str.length; i++) {
        if (substr.length > 1) {
            for (j = 0; j < substr.length; j++) {
                if (str[i] != substr[j]) {
                    continue;
                }
                else {
                    break;
                }
            }
        }
        else {
            if (substr[0] != str[1]) {
                substr += str[1];
            }
            else {
                break;
            }
        }
    }
    return substr.length;
}

lengthOfLongestSubstring(str);