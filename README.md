# fib40 benchmarks

This is a replication of the infamous fib40 benchmarks of node.js. Basically, it
showcases the memoization & parallelism that each of the languages have.

## Use

First install `weighttp` from your package manager. Then, the following command
will benchmark a server:

```bash
weighttp -n8 -t8 -c8 # 8 requests with 8 cores
```

## Results

Results on my computer

| Framework | Language | Time |
| --------- | -------- | ---- |
| Flask | python | 1095s |
| Iron | rust | 646 ms |
| node.js | JavaScript | 11.1s | 
| stdlib | python | 560s |
| rails | Ruby | 165s |
| spock | Haskell | 1.37ms | 
| yesod | Haskell | 1.46ms |
