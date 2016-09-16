package pesoln

import utils.NumberTheory.leastCommonMultiple

/**
  * 2520 is the smallest number that can be divided by each of the numbers
  * from 1 to 10 without any remainder.
  *
  * What is the smallest positive number that is evenly divisible by all of
  * the numbers from 1 to 20?
  */

object ProjectEulerFive {
  def main(args: Array[String]): Unit = {
    println((1 until 20).foldLeft(1)(leastCommonMultiple))
  }
}
