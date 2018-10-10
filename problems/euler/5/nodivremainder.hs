main :: IO ()
main = do
  putStrLn $ show $ smallMult 2520 --proven smallMult for [1..10]

smallMult :: Int -> Int
smallMult x = go x 20
  where go x 11 = x
        go x y
          | x `mod` y == 0 = go x (y-1)
          | otherwise      = smallMult (x+2)

