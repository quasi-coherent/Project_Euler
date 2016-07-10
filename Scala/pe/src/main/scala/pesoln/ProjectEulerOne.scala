package pesoln

/**
Project Euler: Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. */

object ProjectEulerOne {
  def filterSum(ints: List[Int], acc: Int)(f: Int => Boolean): Int = ints match {
    case h :: Nil if f(h) => acc + h
    case h :: Nil => acc
    case h :: t if f(h) => filterSum(t, acc + h)(f)
    case _ :: t => filterSum(t, acc)(f)
  }

  def main(args: Array[String]): Unit = {
    println(filterSum(List.range(1, 1000), 0)(x => x % 3 == 0 || x % 5 == 0))
  }
}

