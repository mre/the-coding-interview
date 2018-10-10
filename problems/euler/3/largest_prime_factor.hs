main :: IO ()
main = do
  putStrLn (show (maximum (primeFactors 600851475143)))

primeFactors :: Integer -> [Integer]
primeFactors 1 = []
primeFactors n 
  | factors == [] = [n]
  | otherwise = factors ++ primeFactors (n `div` (head factors))
  where factors = take 1 $ filter (\x -> (n `mod` x == 0)) [2 .. n-1]

