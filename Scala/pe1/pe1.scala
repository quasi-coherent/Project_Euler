/** 
Project Euler: Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. */

object ProjectEulerOne {
	def filterSum(xs: Array[Int], f: Int => Boolean): Int = 
	  xs.filter(f(_)).reduce(_ + _)

	def main(args: Array[String]): Unit = {
		println(filterSum((1 until 1000).toArray, x => x%3 == 0 || x%5 == 0))
	}
}