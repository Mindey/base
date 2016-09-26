# Ostensibly, these 3 packages are sufficient (minimum) 
# to emulate 95% of base R language functionality.
# I avoid imports that are dependencies, such as Numpy.
# So as to make as distilled as possible.
# In fact, maybe we should also add matplotlib here, 
# however, when I use Jupyter Notebooks, I often do:
# %matplotlib inline instead, so, direct import is not needed.
import pandas as pd
import scipy.stats as st
import statsmodels.api as sm

# I did not import things like statsmodels.formula.api as smf,
# even if it is widely used, because it is available here via sm like:
# sm.formula.*method*. The idea is to find minimal number of Python
# packages that are sort of equivalent to each language.
