### Benchmarking different Sass implementations

Methodology can be found in [`install.sh`](install.sh), [`bench.sh`](bench.sh), and [`generate.py`](generate.py). The test cases are largely adapted from [dart-sass's own benchmark suite](https://github.com/sass/dart-sass/blob/main/tool/grind/benchmark.dart). This suite of benchmarks adds a few additional test cases, namely bulma and more benchmarks against bootstrap.

In general, `grass` appears to be ~2x faster on all benchmarks. Full results can be found in [`results`](results). 

There isn't one specific optimization that makes `grass` so much faster than other existing implementations. `grass` has a heavily optimized `@extend` implementation that likely plays a large role, and it uses string interning wherever possible, including units. 

`grass` does perform much slower than `dart-sass` on the `duomo` benchmark. `duomo` appears to exercise two pathological cases -- it has a massive number of imports of the same file, and it has a huge number of map operations. `grass`'s import caching is much less robust than `dart-sass`'s, so it spends more time doing redundant work. Map insertion and lookup are `O(n)` in `grass`, and map construction is `O(n^2)`. This is because, in `grass`, maps are represented as an array of tuples, while in `dart-sass` maps are represented by proper hash maps. 
