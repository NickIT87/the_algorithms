{-# OPTIONS -Wall -Werror #-}

main :: IO ()
main 
    | d < 0     = putStrLn "no solutions"
    | otherwise = print (x1, x2)    
    where
        a = 1 :: Double
        b = 2.5
        c = 1
        d = b * b - 4 * a * c
        x1 = (- b - sqrt d) / (2 * a)
        x2 = (- b + sqrt d) / (2 * a)

{- ghcid -a filename -}
-- $> main