class solution {
    public static void main(String[] args) {
        for (char c : args[0].toCharArray()) {
            System.out.print(c == '\n' ? c : (char) ('z' - (c - 'a')));
        }
    }
}
