positions=['A', 'B', 'C', 'D', 'E', 'F']
heights=[1, 2, 3, 4, 5, 6]
#np arrays
import numpy as np
np_positions=np.array(positions)
np_heights=np.array(heights)
#storing the A height val in the var AH
AH=np_heights[np_positions=='A']
AHA=np_heights[np_positions!='A']
#printing median of the AH and AHA
print("median of AH: "+str(np.median(AH)) )
print("median of AHA: " +str(np.median(AHA)))