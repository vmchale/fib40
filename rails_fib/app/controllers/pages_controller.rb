class PagesController < ApplicationController
  def fibonacci( n )
      return  n  if n <= 1 
      fibonacci( n - 1 ) + fibonacci( n - 2 )
  end 
  def home
    @greeting = fibonacci( 40 )
  end
end
