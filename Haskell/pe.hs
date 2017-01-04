import Utils

pe1 :: Integer -> Integer
pe1 n = sum [x | x <- [1..n], x `mod` 3 == 0 || x `mod` 5 == 0]
-- pe1 999 = 233168

pe2 :: Integer -> Integer
pe2 n = 
  let evenFib = filter (\n -> n `mod` 2 == 0) fibs
  in sum (takeWhile (<n) evenFib)
-- pe2 4000000 = 4613732

pe3 :: Integer -> Integer
pe3 n = maximum (primeFactors n)
-- pe3 600851475143 = 6857

pe4 :: Integer -> Integer
pe4 n = maximum [x*y | x <- [10^(n-1)..10^n-1], y <- [10^(n-1)..10^n-1], isPalindrome(show (x*y))]
-- pe4 3 = 906609

pe5 :: [Integer] -> Integer
pe5 ns = leastCommonMultiple ns
  where leastCommonMultiple ns = foldl lcm 1 ns
-- pe5 [1..20] = 232792560

pe6 :: Integer -> Integer
pe6 n = (sum [1..n])^2 - sum [m^2 | m <- [1..n]]
-- pe6 100 = 25164150