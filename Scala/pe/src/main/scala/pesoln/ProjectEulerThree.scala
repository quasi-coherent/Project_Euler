package pesoln

import utils.Primes.sieveOfEratosthenes

/**
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143? */

object ProjectEulerThree {
  def largestPrimeFactor(n: Long): Int =
    sieveOfEratosthenes(Math.sqrt(n).toInt + 1).filter(n % _ == 0).max

  def main(args: Array[String]): Unit = {
    println(largestPrimeFactor(600851475143L))
  }
}
