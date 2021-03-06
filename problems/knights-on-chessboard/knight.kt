import java.io.File
import java.util.stream.Collectors

fun main() {
    KnightProblem().solve()
}

data class BoardField(val char: Char, val index: Pair<Int, Int>)

internal class KnightProblem {

    companion object {
        val board = File("problems/knights-on-chessboard/board.txt").readBoard()
    }

    data class Knight(var currentField: BoardField, var visited: List<BoardField> = mutableListOf()) {
        fun clone(): Knight {
            return Knight(currentField, visited.stream().collect(Collectors.toList()))
        }

        fun move(field: BoardField) {
            visited += field
            currentField = field
        }

        fun possibleMoves(): List<BoardField> {
            return listOf(-1, 1, -1, 1, -2, 2, -2, 2)
                .zip(listOf(-2, -2, 2, 2, -1, -1, 1, 1))
                .map {
                    // calculate new pos relative to current pos
                    it.first + currentField.index.first to it.second + currentField.index.second
                }.mapNotNull {
                    it.asBoardField()
                }.filter(this::isValid)
        }

        fun isValid(field: BoardField): Boolean {
            val vowels = "AEIOU"

            if(field.char == '_') return false
            if(field.index.first < 0 || field.index.second < 0) return false
            if(field.index.first > 4 || field.index.second > 4) return false
            if(visited.contains(field)) return false

            if(vowels.contains(field.char)) {
                val vowelCount = visited.count { vowels.contains(it.char) }
                if((vowelCount + 1) > 2) return false
            }

            return true
        }

        fun Pair<Int, Int>.asBoardField(): BoardField? {
            return board.firstOrNull {
                it.index.first == first && it.index.second == second
            }
        }
    }

    fun solve() {
        board.filter { it.char != '_' }.forEach {
            calculateNextStep(Knight(it))
        }
    }

    fun calculateNextStep(knight: Knight) {
        println(knight.visited.map { it.char })
        knight.possibleMoves().forEach {
            val cloned = knight.clone()
            cloned.move(it)
            calculateNextStep(cloned)
        }
    }
}


fun File.readBoard(): MutableList<BoardField> {
    val result = mutableListOf<BoardField>()
    this.reader().readLines().forEachIndexed { y, line ->
        line.split("|").forEachIndexed { x, char ->
            result.add(BoardField(char[0], x to y))   // (x, y)
        }
    }
    return result
}
