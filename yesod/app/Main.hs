{-# LANGUAGE OverloadedStrings     #-}
{-# LANGUAGE QuasiQuotes           #-}
{-# LANGUAGE TemplateHaskell       #-}
{-# LANGUAGE TypeFamilies          #-}

import Yesod
import qualified Data.Text as T

data Fib = Fib

mkYesod "Fib" [parseRoutes|
/ HomeR GET
|]

instance Yesod Fib

fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

getHomeR :: Handler Html
getHomeR = pure . toHtml . T.pack . show . fib $ 40
-- defaultLayout [whamlet|Hello World!|]

main :: IO ()
main = warp 3000 Fib
