## maelstrom-ens10

A dataset plugin for climetlab for the dataset maelstrom-ens10/ens10.


Features
--------

In this README is a description of how to get the maelstrom-ens10.

## Datasets description

There are two datasets: 

### 1 : `ens10`


### 2
TODO


## Using climetlab to access the data (supports grib, netcdf and zarr)

See the demo notebooks here (https://github.com/ecmwf-lab/climetlab_maelstrom_ens10/notebooks

https://github.com/ecmwf-lab/climetlab_maelstrom_ens10/notebooks/demo_ens10.ipynb
[nbviewer] (https://nbviewer.jupyter.org/github/climetlab_maelstrom_ens10/blob/main/notebooks/demo_ens10.ipynb) 
[colab] (https://colab.research.google.com/github/climetlab_maelstrom_ens10/blob/main/notebooks/demo_ens10.ipynb) 

The climetlab python package allows easy access to the data with a few lines of code such as:
```

!pip install climetlab climetlab_maelstrom_ens10
import climetlab as cml
ds = cml.load_dataset(""maelstrom-ens10-ens10", date='20201231',)
ds.to_xarray()
```
