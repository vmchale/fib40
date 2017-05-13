class PagesController < ApplicationController
  def fib( n )
      return  n  if n <= 1 
      fib( n - 1 ) + fib( n - 2 )
  end 
  def fib_memo(n, memo = {})
    if n == 0 || n == 1
      return n
    end
    memo[n] ||= fib_memo(n-1, memo) + fib_memo(n-2, memo)
  end
  def home
    @greeting = fib( 40 )
  end
end
