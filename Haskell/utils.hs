module Utils where

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

primeFactors :: Integer -> [Integer]
primeFactors n = 
  case factors of
    [] -> [n]
    _  -> factors ++ primeFactors (n `div` (head factors))
  where factors = take 1 $ filter (\x -> (n `mod` x) == 0) [2 .. n-1]

isPalindrome :: String -> Bool
isPalindrome s = s == reverse s

leastCommonMultiple :: [Integer] -> Integer
leastCommonMultiple ns = foldl lcm 1 ns