package utils

object NumberTheory {
  def greatestCommonDivisor(n: Int, m: Int): Int = {
    if (m == 0) n
    else greatestCommonDivisor(m, n % m)
  }

  def leastCommonMultiple(n: Int, m: Int): Int =
    Math.abs(n * m) / greatestCommonDivisor(n, m)
}
