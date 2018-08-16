fun atbash(input: String): String {
    if (input.isEmpty()) return ""

    require(input.all { it.isLetter() && it.isLowerCase() }) {
        "input must consist of lowercase Latin alphabet letters only, got: $input"
    }

    return buildString {
        input.forEach {
            append('Z' - (it - 'a'))
        }
    }
}
