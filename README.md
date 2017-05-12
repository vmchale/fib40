# fib40 benchmarks

This is a replication of the infamous fib40 benchmarks of node.js. Basically, it
shows that many popular libraries & languages don't have memoization (bad!).

## Use

First install `weighttp` from your package manager. Then, the following command
will benchmark whichever server you have running:

```bash
weighttp -n32 -n8 -c8
```

This might take awhile for some of the python ones especially.
