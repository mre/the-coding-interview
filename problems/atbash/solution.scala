object solution {
    def main(args: Array[String]): Unit = {
        args(0).foreach(c => print(if (c == '\n') c else ('z' - (c - 'a')).toChar))
    }
}
