fun isValidShuffle(a: String, b: String, combined: String): Boolean {
    if (a.length + b.length != combined.length)
        return false

    var indexA = 0
    var indexB = 0
    for (c in combined)
        if (indexA < a.length && a[indexA] == c)
            indexA++
        else if(indexB < b.length && b[indexB] == c)
            indexB++
        else return false

    return true
}
