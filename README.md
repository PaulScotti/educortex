# EduCortex
<img src="logo.png" align="center"/>

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

## Overview

[EduCortex](paulscotti.github.io/educortex) is an educational browser-based visualization tool that allows the user to enter any functional or anatomical term (e.g., "visual", "face", "motion", "precuneus") and visualize the parts of the brain that are most associated with that term. The process can also be reversed, where the user can click anywhere on the brain to see what terms are most associated with the selected brain region. Using principal components analysis, we also display the functional terms that explained the most variance across all activation maps. This tool works through the combination of [Neurosynth](http://neurosynth.org/), a large-scale, automated database of fMRI papers, and [PyCortex](https://gallantlab.github.io/), an interactive 3D brain visualizer.

## Installation

EduCortex can be accessed without installation as an online webviewer, see [EduCortexViewer](https://paulscotti.github.io/educortex/).

If you want to use EduCortex locally, take the following steps:

### 1. Install and setup pycortex (see also instructions [here](https://gallantlab.github.io/install.html))

```
git clone https://github.com/gallantlab/pycortex.git
cd pycortex

python setup.py developpip install
```
You require different dependencies. If using Anaconda use pip install:

```
pip install numpy Cython scipy h5py nibabel matplotlib Pillow numexpr tornado lxml networkx
```

If you are running Ubuntu without Anaconda, use the following commands:

```
sudo apt-get install python-dev python-numpy python-scipy python-matplotlib python-h5py python-nibabel python-lxml python-shapely python-html5lib inkscape
```

### 2. Follow steps in runMappingViz.ipynb

## Contributions
Contributions are welcome, feel free to open an issue or do a pull request. 

## Authors
Paul Scotti, Arman Kulkarni, Matan Mazor, Eduard Klapwijk, Tal Yarkoni, Alex Huth
