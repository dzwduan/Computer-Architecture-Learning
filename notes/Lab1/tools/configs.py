import numpy as np

stats_name='stats.txt'
start_sym='---------- Begin Simulation Statistics ----------'
freq_sym='sim_freq'
inst_sym='system.switch_cpus.committedInsts'
seconds_sym='sim_seconds '
dcache_hit_sym='system.cpu.dcache.overall_hits::.switch_cpus.data'
dcache_miss_sym='system.cpu.dcache.overall_misses::.switch_cpus.data'
branch_pred_sym='system.switch_cpus.branchPred.condPredicted'
branch_miss_pred_sym='system.switch_cpus.branchPred.condIncorrect'
ROB_stall_sym='system.switch_cpus.rename.ROBFullEvents'
rename_inst_sym='system.switch_cpus.rename.renamedInsts'
paras_sym=[freq_sym,inst_sym,seconds_sym,dcache_hit_sym,dcache_miss_sym,branch_pred_sym, \
    branch_miss_pred_sym,ROB_stall_sym,rename_inst_sym]
paras=np.zeros(len(paras_sym))
#freq=inst=ops=dcache_hit=dcache_miss=0

# normal 的一般不用改
freq_sym_nor='simFreq'
inst_sym_nor='system.cpu.thread_0.numInsts'
seconds_sym_nor='simSeconds'
dcache_hit_sym_nor='system.cpu.dcache.overallHits::cpu.data'
dcache_miss_sym_nor='system.cpu.dcache.overallMisses::cpu.data'
branch_pred_sym_nor='system.cpu.branchPred.condPredicted'
branch_miss_pred_sym_nor='system.cpu.branchPred.condIncorrect'
ROB_stall_sym_nor='system.cpu.rename.ROBFullEvents'
rename_inst_sym_nor='system.cpu.rename.renamedInsts'
IPC_nor='system.cpu.ipc'
paras_sym_nor=[freq_sym_nor,inst_sym_nor,seconds_sym_nor,dcache_hit_sym_nor,dcache_miss_sym_nor,branch_pred_sym_nor, \
    branch_miss_pred_sym_nor,ROB_stall_sym_nor,rename_inst_sym_nor]
paras_nor=np.zeros(len(paras_sym_nor))