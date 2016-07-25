package pesoln

import utils.Primes.primeFactors

/**
  * The prime factors of 13195 are 5, 7, 13 and 29.
  *
  * What is the largest prime factor of the number 600851475143?
  */

object ProjectEulerThree {
  def largestPrimeFactor(n: Long): Int = primeFactors(Math.sqrt(n).toInt).max

  def main(args: Array[String]): Unit = {
    println(largestPrimeFactor(600851475143L))
  }
}
