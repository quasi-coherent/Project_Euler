package pesoln

import utils.Primes.nthPrime

/**
  * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
  * that the 6th prime is 13.
  *
  * What is the 10,001st prime number?
  */

object ProjectEulerSeven {
  def main(args: Array[String]): Unit = {
    println(nthPrime(10001))
  }
}
