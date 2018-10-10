main :: IO ()
main = do
  putStrLn $ show (((sum [1..100]) ^2) - (sum $ map square [1..100]))
    where square x = x * x
