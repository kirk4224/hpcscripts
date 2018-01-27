## HPL-calculator
### A python instance of HPL(High-Performance Linpack) parameter calculator.
inspired by [Top500 HPL Calculator](http://hpl-calculator.sourceforge.net)
### Input
1/5.Number of Nodes(e.g. 30)<br>
2/5.Cores per Node(e.g. 24)<br>
3/5.Speed Per Core(GHz)(e.g. 2.3)<br>
4/5.Memory per Node(GB)(e.g. 64)<br>
5/5.Operations per Cycle(e.g. 16)<br>
### Output
#### Part I
Total Number of Cores: 720<br>
Total Memory(GB): 1920<br>
#### Part II
Peak Performance(GFlops): <br>
| 70% | ........| 100% |<br>
| 18547 | ... | 26495 |<br>
#### Part III
Possible P & Q combinations:<br>
P=1 x Q=720<br>
P=2 x Q=360<br>
P=4 x Q=180<br>
P=8 x Q=90<br>
P=16 x Q=45<br>
#### Part IV
Range of NB:<br>
[96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256]<br>
Range of Memory Percentage(%):<br>
[80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]<br>
Suggested Parameter for HPL benchmark:<br>
| Memory\NB | 96 |...........| 256 |<br>
| 80% | 406080 | ... | 406016 |<br>
...<br>
| 100% | 507552 | ... | 507392 |<br>
