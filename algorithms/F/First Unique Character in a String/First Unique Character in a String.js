/**
 * @param {string} s
 * @return {number}
 */


var firstUniqChar = function(s) {
    let dec = {};

    for(let i=0; i < s.length ; i++){
        if(dec[s[i]]){
            dec[s[i]]['counter']++;
        }else{
            dec[s[i]] = {},
            dec[s[i]]['counter'] =  1;
            dec[s[i]]['index'] = i;
        }
    }
    
    for(let i=0; i < s.length ; i++){
        if(dec[s[i]]['counter'] == 1) {
            return dec[s[i]]['index'];
            break;
        }
    }
    
    return -1;
};


