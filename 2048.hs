isZeros :: [Int] -> Bool
isZeros = all (==0)

moveLeftList :: [Int] -> [Int]
moveLeftList [] = []
moveLeftList [x] = [x]
moveLeftList (x:xs)
    |isZeros xs = x:xs
    |x == 0 = moveLeftList xs ++ [0]
    |head xs == 0 = moveLeftList (x:tail xs) ++ [0]
    |x == head xs = (x*2) : moveLeftList(tail xs) ++ [0]
    |otherwise = x : moveLeftList xs

moveRightList :: [Int] -> [Int]
moveRightList xs = reverse (moveLeftList(reverse xs))

moveLeft :: [[Int]] -> [[Int]]
moveLeft = map moveLeftList 

moveRight :: [[Int]] -> [[Int]]
moveRight = map moveRightList 

pushUp' :: [[Int]] -> [[Int]]
pushUp' [w:ws, x:xs, y:ys, z:zs] = moveLeftList[w,x,y,z] : pushUp' [ws,xs,ys,zs]
pushUp' [w,x,y,z] = []
--pushUp' [(w:ws), (x:xs), (y:ys), (z:zs)] = moveLeftList[w,x,y,z] : pushUp' [ws,xs,ys,zs]

moveUp' :: [[Int]] -> [[Int]]
moveUp' [w:ws, x:xs, y:ys, z:zs] = [w,x,y,z] : moveUp' [ws,xs,ys,zs]
moveUp' [w,x,y,z] = []

moveUp :: [[Int]] -> [[Int]]
moveUp xs = moveUp'(pushUp' xs)

pushUp'' :: [[Int]] -> [[Int]]
pushUp'' [w:ws, x:xs, y:ys, z:zs] = moveRightList[w,x,y,z] : pushUp'' [ws,xs,ys,zs]
pushUp'' [w,x,y,z] = []

moveDown :: [[Int]] -> [[Int]]
moveDown xs = moveUp'(pushUp'' xs)

intToString :: [Int] -> String
intToString [x] = show x
intToString (x:xs) = show x ++ " " ++ intToString xs

myNumbers :: String -> [Int]
myNumbers numbers = map (\x -> read x :: Int)(words numbers)

printLine :: [Int] -> IO()
printLine xs = putStrLn (intToString xs)

printLines :: [[Int]] -> IO()
printLines [x] = printLine x
printLines (x:xs) = printLine x >> printLines xs


moveDir :: [[Int]] -> Int -> [[Int]]
moveDir grid n
    |n == 0 = moveLeft grid
    |n == 1 = moveUp grid
    |n == 2 = moveRight grid
    |n == 3 = moveDown grid
    |otherwise = grid

getInput :: IO()
getInput = do
    line1 <- getLine
    line2 <- getLine
    line3 <- getLine
    line4 <- getLine
    direction <- getLine
    let myGraph = moveDir[myNumbers line1, myNumbers line2, myNumbers line3, myNumbers line4] (read direction :: Int)
    printLines myGraph

--myNumbers


main = do
    getInput
