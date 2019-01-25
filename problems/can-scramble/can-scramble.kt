infix fun String.canScramble(other: String) =
    if (length != other.length)
        false
    else
        toCharArray().sortedArray() contentEquals other.toCharArray().sortedArray()
