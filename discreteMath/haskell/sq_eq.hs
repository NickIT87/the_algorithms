main :: IO ()

main = 
    let
        a = 1
        b = 2
        c = 1
        d = b ^ 2 - 4 * a * c
    in
        if d < 0 then
            putStrLn "no solutions"
        else
            let
                x1 = (- b - sqrt d) / (2 * a)
                x2 = (- b + sqrt d) / (2 * a) :: Double
            in
                print (x1, x2)