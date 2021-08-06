## ENS10 Dataset

A dataset plugin for CliMetLab for the ENS10 dataset from the MAELSTROM project.

The ENS10 dataset is designed to help the development of machine learning tools to improve ensemble predictions via post-processing. It consists of the model output data of ECMWF "hindcast" experiments. These are ensemble forecasts with 10 ensemble members that are spread over 20 years (1998-2017) with two forecasts per week.

Structure
---------

The dataset is grouped by day-of-year (i.e., a single date contains all 20 years of predictions), where 
each date contains three steps: 0, 24, and 48 hour lead time. Thus, files contain three days at a time.
To query the list of dates, run `all_datelist` on the loaded dataset.

In every file, there are 6 dimensions of data (in this order): `number` (ensemble member), 
`time` (year offset from 1998), `step` (forecast lead time, 0=0h, 1=24h, 2=48h), 
`surface`/`isobaricInhPa` (pressure level), `latitude`, and `longitude`.

**A smaller (10 GB) dataset is also available through this plugin as `maelstrom-ens5mini`**. It spans the first 10 years, cropped to Europe, and contains 5 ensemble members. See demo notebook on usage.

Features
--------

## Using CliMetLab to access the data

See the demo notebooks [here](https://github.com/spcl/climetlab-maelstrom-ens10/tree/main/notebooks)

Accessing data is performed on a date basis, where the dataset is organized by day-of-year (i.e., the file of each date contains all 20 forecasts at all of the 20 years). The dataset is also split to surface-level data, and pressure-level data for above-ground forecasts.

The `climetlab` python package allows easy access to the data with a few lines of code:

```python
!pip install climetlab climetlab_maelstrom_ens10
import climetlab as cml

# Toy dataset
ds = cml.load_dataset("maelstrom-ens5mini", date='01')

# Pressure-level data
ds = cml.load_dataset("maelstrom-ens10", date='20170226', dtype='pl')

# Surface-level data
ds = cml.load_dataset("maelstrom-ens10", date='20170226', dtype='sfc')

# Alternatively, the year can be omitted, and pressure levels are given by default:
# ds = cml.load_dataset("maelstrom-ens10", date='0226')

# Convert dataset to xarray data
ds.to_xarray()
```
