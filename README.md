# EduCortex
<img src="logo.png" align="center"/>

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

## Overview

[EduCortex](http://paulscotti.com/educortex/) is an educational browser-based visualization tool that allows the user to enter any functional or anatomical term (e.g., "visual", "face", "motion", "precuneus") and visualize the parts of the brain that are most associated with that term. The process can also be reversed, where the user can click anywhere on the brain to see what terms are most associated with the selected brain region. Using principal components analysis, we also display the functional terms that explained the most variance across all activation maps. This tool works through the combination of [Neurosynth](http://neurosynth.org/), a large-scale, automated database of fMRI papers, and [PyCortex](https://gallantlab.github.io/), an interactive 3D brain visualizer.

## Installation

EduCortex can be accessed without installation as an online webviewer, see [EduCortexViewer](http://paulscotti.com/educortex/).

If you want to use EduCortex locally, take the following steps:

- clone repository
```
git clone https://github.com/PaulScotti/educortex
```

- move into the cloned repository
```
cd educortex
```

- install the list of required dependencies (see https://github.com/gallantlab/pycortex if having trouble with pycortex)
```
pip install -r requirements.txt
```

- follow steps in runMappingViz.ipynb

## Repository layout
This project repository is set up in the following way:
- `runMappingViz.ipynb` is a Jupyter Notebook that details the steps used to load Neurosynth data and project maps onto fsaverage brain using Pycortex
- `my_template.html` is the html template used by runMappingViz.ipynb to add CSS & javascript elements to the Pycortex viewer
- `index.html` is the final webpage that hosts the viewer--note that if you create your own index.html via runMappingViz.ipynb, it will lack some features that is contained in the index.html hosted on this github repository (e.g., no welcome pop-up, no enable/disable wordcloud buttons, etc.)
- `data/` contains .png files, each of which is a meta-analysis map from Neurosynth which gets projected onto the fsaverage 3D brain in EduCortex
- `atlases/` contains annotation files which can be used to create anatomical labels in EduCortex (from Glasser et al. (2016) and Huth et al., (2016))
- `PCA/` contains `PCA_extraction.ipynb` (the code used to create the PCA components across Neurosynth meta-analysis maps) and pngs for the three wordclouds used in EduCortex
- `paper/` contains files used for our manuscript submission to the Journal of Open Source Education (https://jose.theoj.org/)

## Contributions
Contributions are welcome, feel free to open an issue or do a pull request. 

## Authors
Paul Scotti, Arman Kulkarni, Matan Mazor, Eduard Klapwijk, Tal Yarkoni, Alex Huth
