factorial :: Integer -> Integer
factorial 0 = 1;
factorial 1 = 1;
factorial x = x * factorial (x - 1)
