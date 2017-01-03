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