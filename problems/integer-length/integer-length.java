int getsum(int n) {
   return n == 0 ? 0 : n % 10 + getsum(n/10);
}
