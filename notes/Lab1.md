# gem5运行coremark

## gem5 binary类型
1. debug ，构建时未进行优化且包含调试符号，速度慢
1. opt，使用了大部分优化选项构建（例如，-O3），但同时包含了调试符号
1. fast，使用了所有优化（包括在支持的平台上进行链接时优化）并且没有调试符号。此外，任何断言都被移除，但异常和致命错误仍然包含



## gem5 模拟方式

se : system call emulation , 仅模拟 core + mem ， 更快

fs : full system simulation, 模拟 core + mem + I/O + 外设 ， 更详细	



## 运行方案

fast + se 

```
cd riscv-coremark/coremark
make ITERATIONS=1
```



## 运行命令

1. 设置 要运行的config

2. ```
   ./build/X86/gem5.fast --outdir=coremark_out/normal \
               configs/deprecated/example/se.py --cpu-type DerivO3CPU --cpu-clock 3.1GHz \
               --num-cpu 1 --caches --l2cache --l1i_size 64kB --l1d_size 64kB \
               --l2_size 1MB --l1i_assoc 4 --l1d_assoc 4 --l2_assoc 4 \
               --cacheline_size 128 --mem-type DDR3_2133_8x8 --mem-size 16GB \
               --l2-hwp-type StridePrefetcher \
               -c /home/dzw/Computer-Architecture-Learning/riscv-coremark/coremark/coremark.exe
   ```

获得config.ini + config.json + stats.json , 需要从中dump出来各项perf counter