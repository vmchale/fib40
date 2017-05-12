extern crate iron;
extern crate time;

use iron::prelude::*;

fn fib(n: i32) -> i32 {
    match n {
        0 => 1,
        1 => 1,
        n => fib (n-1) + fib (n-2),
    }
}

fn fib_bench(_: &mut Request) -> IronResult<Response> {
    Ok(Response::with((iron::status::Ok, fib(40).to_string())))
}

fn main() {
    let chain = Chain::new(fib_bench);
    Iron::new(chain).http("localhost:3000").unwrap();
}
