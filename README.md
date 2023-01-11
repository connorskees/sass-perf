### Benchmarking different Sass implementations

Methodology can be found in [`install.sh`](install.sh), [`bench.sh`](bench.sh), and [`generate.py`](generate.py). The test cases are largely adapted from [dart-sass's own benchmark suite](https://github.com/sass/dart-sass/blob/main/tool/grind/benchmark.dart). This suite of benchmarks adds a few additional test cases, namely bulma and more benchmarks against bootstrap.

In general, `grass` appears to be ~2x faster on all benchmarks. Full results can be found in [`results`](results). Below are the summaries from all runs:

```sh
Summary
  'grass bootstrap/scss/bootstrap.scss ' ran
    2.12 ± 0.06 times faster than './sassc/bin/sassc bootstrap/scss/bootstrap.scss '
    4.22 ± 5.67 times faster than './dart-sass/sass bootstrap/scss/bootstrap.scss '

Summary
  'grass bulma/bulma.sass ' ran
    1.77 ± 0.08 times faster than './sassc/bin/sassc bulma/bulma.sass '
    2.85 ± 3.03 times faster than './dart-sass/sass bulma/bulma.sass '

Summary
  'grass small-plain.scss ' ran
    1.89 ± 0.24 times faster than './sassc/bin/sassc small-plain.scss '
   17.56 ± 91.83 times faster than './dart-sass/sass small-plain.scss '

Summary
  'grass large-plain.scss ' ran
    2.19 ± 0.02 times faster than './sassc/bin/sassc large-plain.scss '
    2.95 ± 0.75 times faster than './dart-sass/sass large-plain.scss '

Summary
  'grass preceding-sparse-extend.scss ' ran
    2.19 ± 0.02 times faster than './sassc/bin/sassc preceding-sparse-extend.scss '
    2.95 ± 0.72 times faster than './dart-sass/sass preceding-sparse-extend.scss '

Summary
  'grass following-sparse-extend.scss ' ran
    2.29 ± 0.02 times faster than './sassc/bin/sassc following-sparse-extend.scss '
    2.82 ± 0.70 times faster than './dart-sass/sass following-sparse-extend.scss '

Summary
  'grass preceding-dense-extend.scss ' ran
    1.97 ± 0.03 times faster than './dart-sass/sass preceding-dense-extend.scss '
    2.02 ± 0.02 times faster than './sassc/bin/sassc preceding-dense-extend.scss '

Summary
  'grass following-dense-extend.scss ' ran
    1.53 ± 0.21 times faster than './dart-sass/sass following-dense-extend.scss '
    1.55 ± 0.01 times faster than './sassc/bin/sassc following-dense-extend.scss '

Summary
  'grass single-bootstrap.scss ' ran
    2.13 ± 0.03 times faster than './sassc/bin/sassc single-bootstrap.scss '
    3.16 ± 0.04 times faster than './dart-sass/sass single-bootstrap.scss '

Summary
  'grass large-bootstrap.scss ' ran
    1.79 ± 0.02 times faster than './dart-sass/sass large-bootstrap.scss '
    2.01 ± 0.02 times faster than './sassc/bin/sassc large-bootstrap.scss '

Summary
  'grass a11ycolor.scss ' ran
    1.64 ± 0.03 times faster than './sassc/bin/sassc a11ycolor.scss '
    1.82 ± 0.02 times faster than './dart-sass/sass a11ycolor.scss '

# `sassc` (`libsass`) is excluded from this run as it does not support the module
# system
Summary
  './dart-sass/sass duomo.scss ' ran
    3.79 ± 0.03 times faster than 'grass duomo.scss '
```

There isn't one specific optimization that makes `grass` so much faster than other existing implementations. `grass` has a heavily optimized `@extend` implementation that likely plays a large role, and it uses string interning wherever possible, including units. 

`grass` does perform much slower than `dart-sass` on the `duomo` benchmark. `duomo` appears to exercise three pathological cases -- it has a massive number of imports of the same file, it makes heavy use of the module system, and it has a huge number of map operations.

`grass`'s import caching is much less robust than `dart-sass`'s, so it spends more time doing redundant work.

The module system in `grass` is still relatively nascent, especially performance-wise. It has not received any profiling or optimization and it relies on structures of deeply nested `Arc<RefCell<Vec<_>>>`. This makes for a lot of slowness around importing of many modules.

Map insertion and lookup are `O(n)` in `grass`, and map construction is `O(n^2)`. This is because, in `grass`, maps are represented as an array of tuples, while in `dart-sass` maps are represented by proper hash maps. In general this is not enough to be noticeable on performance profiles, but this library manages to come up with a case in which enough maps are used that this matters. 
