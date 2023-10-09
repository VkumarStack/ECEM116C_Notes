# Introduction to Computer Architecture
## Computer Abstractions:
- Hardware -> Systems software -> Applications software
  - Computer architecture is mostly concerned with the *interaction* between hardware and systems software, though not necessarily the specifics of hardware
- Application Software:
  - High-level translations of algorithm to code
- Systems Software:
  - **Compiler**: Translates hardware-level-language code to machine code
  - **Operating Systems**: Service code
- Hardware:
  - Processors, memory, etc.
## Running an Application:
- Whenever an application is run, the high-level applications may be written in different languages and the underlying hardware may vary from device-to-device 
- The systems software address these potential compatability issues via the **instruction set architecture (ISA)**
  - It translates the high-level program into a sequence of *known instructions* (translating is done by the compiler)
- Think of the ISA as the *interface* between hardware and software, allowing each to evolve *independently*
- ISA's provide abstraction for high-level software, which effectively sees the *functional description of hardware* (not the specifics)
  - Storage locations (memory, disk)
  - Operations (addition)
- The hardware is able to work with the list of instructions (translated from the high-level architecture) and their order
## Goals in Architecting a Computer
- First and foremost, the most important goal in architecting a computer is to obtain *efficiency*
  - Computers should be *fast*
    - This is generally the most important metric
  - Computers should be *power-efficient*
    - This may incur tradeoffs with the need to be *fast*
  - Computers should have reasonable *cost*
  - Computers should be *reliable and secure*
    - Historically, this has been a secondary goal - it is often seen as an afterthought
## Technology Improvements
- Moore's Law is a prediction that the number of transistors able to fit on a chip roughly doubles every two years
- Moving from one generation of transistors to another results in the voltage being reduced, delays being reduced, frequency being reduced, and capacitance being reduced
  - This implies that power consumption *per transistor* is decreased by 50%
  - Since the number of transistors double (Moore's Law) but the power consumption per transistor is reduced by half, the power of the entire chip roughly stays the same
    - This makes doubling the transistors an actual feasible option for efficiency improvements for computers
- This is an ideal measurement however, as improvements eventually hit a power wall (at around 2005) where manufacturers could not longer double the processor power while keeping consumption constant
  - This is a result of power leakage due to small transistor sizes
- After this power wall, architects began to adopt multi-core designs, which involved utilizing multiple chips
  - This presents new challenges though, especially with synchronization and maximizing parallelism
- Even with multi-core designs, though, **Amdahl's Law** summarizes the limitations of such an architecture since the performance improvement of programs is limited by the part that cannot be improved
  - There is obviously room for performance increase with parts of the program that can be parallelized (by simply adding more cores), but for parts of the program that must be run strictly sequentially act as a significant bottleneck
- Most improvements in computer architecture are not a result of technological advancements, but rather advanced architectural and organizational techniques 
