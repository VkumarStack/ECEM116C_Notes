import json
import sys

instruction_type = sys.argv[1]

f = open('./latencies.json')
latencies = json.load(f)
f.close()

instruction_fetch = latencies["PC_Read"] + latencies["Mem_Read"]
control = instruction_fetch + latencies["Control"]
register_file = instruction_fetch + latencies["Reg_Read"]
immediate_generator = instruction_fetch + latencies["Imm_Gen"]

input_2 = latencies["MUX"] + max(register_file, control)
if (instruction_type in ["I", "lw", "sw"]):
  input_2 = latencies["MUX"] + max(immediate_generator, control)

alu = latencies["ALU"] + max(register_file, input_2, control)

memory = latencies["Mem_Read"] + max(alu, control)
if (instruction_type in ["sw"]):
  memory = latencies["Mem_Write"] + max(alu, register_file, control)

writeback = latencies["MUX"] + max(alu, control) + latencies["Reg_Write"]
if (instruction_type in ["lw"]):
  writeback = latencies["MUX"] + max(memory, control) + latencies["Reg_Write"]
if (instruction_type in ["sw"]):
  writeback = memory

pc_plus_four = latencies["PC_Read"] + latencies["Adder"]
pc_branch = latencies["Adder"] + max(latencies["PC_Read"], immediate_generator)
branch_signal = latencies["Gate"] + min(control, alu)
if (instruction_type in ["beq"]):
  branch_signal = latencies["Gate"] + max(control, alu)
next_pc = latencies["MUX"] + max(pc_plus_four, branch_signal) + latencies["PC_Write"]
if (instruction_type in ["beq"]):
  next_pc = latencies["MUX"] + max(pc_branch, branch_signal) + latencies["PC_Write"]

total_latency = max(next_pc, writeback) if instruction_type not in ["beq"] else next_pc
print(total_latency)
