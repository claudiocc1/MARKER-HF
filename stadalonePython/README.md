# MARKER-HF, standalone python3 package

## Usage
```
from pyMarker import *
from mort import *

# pass the 8 variables in a list
marker = pyMarker([BPDIAS, CREATN, BUN, HGB, WBC, PLT, ALB, RDW])

# one year survival
oneYear = mort(marker)

# 90 days survival
ninetyDays = mort(marker, oneYear=False)
```

In case of problems with the inputs pyMarker returns -99 and prints out an error message