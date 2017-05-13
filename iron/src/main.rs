#[macro_use] extern crate cached;
#[macro_use] extern crate lazy_static;

extern crate iron;
extern crate time;

use cached::SizedCache;
use iron::prelude::*;

cached!{ SLOW: SizedCache = SizedCache::with_capacity(50); >>
fn fib_memo(n: i32) -> i32 = {
    match n {
        0 => 1,
        1 => 1,
        n => fib_memo (n-1) + fib_memo (n-2),
    }
}}

fn fib_naive(n: i32) -> i32 {
    match n {
        0 => 1,
        1 => 1,
        n => fib_naive (n-1) + fib_naive (n-2),
    }
}

fn fib_bench(_: &mut Request) -> IronResult<Response> {
    Ok(Response::with((iron::status::Ok, fib_naive(40).to_string())))
}

fn main() {
    let chain = Chain::new(fib_bench);
    Iron::new(chain).http("localhost:3000").unwrap();
}
