# EduCortex
EduCortex is a [Neurohackademy](http://neurohackademy.org) 2019 project. The goal of EduCortex is to visualize different brain atlases, parcellations and associated terms and variance components of the neuroimaging literature from [Neurosynth](http://neurosynth.org) on a 3D brain. This can be used as educational resource to easily visualize anatomical labels and functional activations of Neurosynth keywords on a 3D interactive brain. The [PyCortex](https://github.com/gallantlab/pycortex) software library is used for visualisation. 

## Installation
EduCortex can be accessed without installation as an online webviewer, see [EduCortexViewer](https://paulscotti.github.io/EduCortex/).

If you want to use EduCortex locally, take the following steps:

### 1. Install pycortex (see also instructions [here](https://gallantlab.github.io/install.html))

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

### 2. Download data

### 3. Download Jupyter notebooks


## Contributions
Contributions are welcome, feel free to open an issue or do a pull request.


## Authors
Paul Scotti, Arman Kulkarni, Matan Mazor, Eduard Klapwijk, Alex Huth
