# coremark simpoint

## 环境

```
git clone  https://github.com/dzwduan/SimPoint.3.2-fix
cd SimPoint.3.2-fix
make
```

## 步骤
+   采用 AtomicSimpleCPU 初始运行一遍程序，并生成 simpoint.bb.gz
+   Simpoint 读取 simpoint.bb.gz，并生成划分结果以及权重文件
+   按照 Simpoint 划分的结果写 checkpoint
+   采用指定的 CPU 以及参数执行 checkpoint （注：这个功能只是为了验证，使用不同参数重跑详见 Reload ）
+   checkpoint reload


## 生成simpoint.bb.gz
```
bash sim_init.sh coremark # 需要修改configs/configs_coremark.sh部分配置
```