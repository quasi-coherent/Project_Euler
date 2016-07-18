package utils

object Primes {
  def isPrime(n: Long): Boolean = {
    def loop(n: Long, lim: Long): Boolean =
      if (lim > Math.sqrt(n)) true
      else if (n % lim == 0) false
      else loop(n, lim + 1)

    n match {
      case 1 => false
      case 2 => true
      case `n` if `n` % 2 == 0 => false
      case _ => loop(n, 3)
    }
  }

  def sieveOfEratosthenes(lim: Int): List[Int] = {
    val odds = Stream.from(3, 2).takeWhile(_ <= Math.sqrt(lim).toInt)
    val composites = odds.flatMap(n => Stream.from(n * n, 2 * n).takeWhile(_ <= lim))
    Stream.from(3, 2).takeWhile(_ <= lim).diff(composites).toList
  }

  def primeFactors(num: Int): List[Int] = sieveOfEratosthenes(num).filter(num % _ == 0)
}
