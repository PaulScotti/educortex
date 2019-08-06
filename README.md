# PyCortexEdu
NeuroHackademy 2019

## SETUP ## 
Create a folder for housing your virtual environment and files

<pre>
mkdir pycortex
cd pycortex
python3 -m venv env  # use `virtualenv env` for python 2
source env/bin/activate
pip install -U setuptools wheel numpy cython
pip install -U git+git://github.com/gallantlab/pycortex.git
pip install ipython
ipython
import cortex
cortex.webshow(cortex.Volume.random("S1", "fullhead"))
</pre>

**If error "no such file" when executing cortex.webshow:**
<pre>
cortex.options.usercfg 
nano "path from above line"
filestore = /Users/scotti.5/Documents/GitHub/pycortex/env/share/pycortex/db
colormaps = /Users/scotti.5/Documents/GitHub/pycortex/env/share/pycortex/colormaps
exit ipython and try again
</pre>

**If you get "started server on port #####" but the browser opens a webpage that errors, try going to localhost:#####**


