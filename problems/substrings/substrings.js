let substrings = (s) => {
    let sb = []
    for (let i = 1; i <= s.length; i++) 
        for (let j = 0; j <= s.length - i; j++)
            sb.push(s.substring(j, j+i));
    return sb;
}

substrings("abcd");
