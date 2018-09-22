-- This is a classic implementation using Haskell

data UnflattenedArray x = El x | List [UnflattenedArray x] -- creating the nested list / UnflattenedArray datatype

-- function for flattening an array
flatten :: UnflattenedArray x -> [x]
flatten (El y) = [y]
flatten (List y) = concatMap flatten y

main = do
    print (flatten (List [El 1, List [El 2, List [El 3, El 4, El 5, El 6], El 7, El 8, El 9], List [El 10]]))
-- Output: [1,2,3,4,5,6,7,8,9,10]
