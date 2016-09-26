# base
Convenience imports for base packages emulating the core functionality 
of other languages in scientific computing.

## base imports

```
pip install base
```

```
>>> from base.R import *

# Is then equivalent to:

>>> import pandas as pd
>>> import scipy.stats as st
>>> import statsmodels.api as sm
```

While Python, being quite universal language, is good at doing many things,
sometimes doing things that's easy in other languages requires a number of
imports.

For example, to emulate the base-R language functionality, import:

```
import pandas
import scipy.stats
import statsmodels
```

To eulate the Matlab's functionality, we would probably import:

```
import numpy
import scipy.optimize
import scipy.integrate
import scipy.interpolate
...
```

To emulate Maple functionality, we would probably start from:

```
import sympy
...
```

I'd like to start creating a package, which would allow for faster 
one-line imports, so that I could just ``pip install base`` and say, do:

```
from base.MATLAB import *
```

To automatically import these packages. I'm not sure how to accomplish 
this the best, but some of the packages have standard imports in 
scientific community, like, e.g.:

```
import sympy as S
import numpy as np
import pandas as pd
...
```

I think we should try to take a look at what are the conventions already, 
and stick to them when it is reasonable, and suggest new ones.
