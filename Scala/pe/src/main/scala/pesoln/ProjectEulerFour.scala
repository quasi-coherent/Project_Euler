package pesoln

/**
  * A palindromic number reads the same both ways.
  * The largest palindrome made from the product of two 2-digit numbers
  * is 9009 = 91 × 99.
  *
  * Find the largest palindrome made from the product of two 3-digit numbers.
  */

object ProjectEulerFour {
  def isPalindrome(n: Int): Boolean = n.toString.reverse == n.toString

  def palindromeProd(n: Int) =
    for (i <- Math.pow(10, n - 1).toInt until Math.pow(10, n).toInt;
         j <- Math.pow(10, n - 1).toInt until i if isPalindrome(i * j)) yield i * j

  def maxPalindromeProd(n: Int): Int = palindromeProd(n).max

  def main(args: Array[String]): Unit =
    println(maxPalindromeProd(3))
}
