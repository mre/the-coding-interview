main :: IO ()
main = do
  putStrLn (show $ maximum [ palindrome x x | x <- [999, 998.. 970] ])

palindrome :: Int -> Int -> Int
palindrome x y 
  | y < 500 = 0
  | show (x * y) == (concat $ digs (x * y)) = (x * y)
  | otherwise = palindrome x (y-1)

digs :: Int -> [String]
digs 0 = []
digs x = (show $ x `mod` 10) : digs (x `div` 10)
