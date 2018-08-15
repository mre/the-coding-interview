fun firstNonRepeatedCharacter(input: String): Char? {
    val seen = LinkedHashSet<Char>()
    val seenOnce = LinkedHashSet<Char>()

    input.forEach {                 // O(n)
        if (seen.contains(it)) {    // O(1)
            seenOnce.remove(it)     // O(1)
        } else {
            seen.add(it)            // O(1)
            seenOnce.add(it)        // O(1)
        }
    }

    return seenOnce.firstOrNull()   // O(1)
}
