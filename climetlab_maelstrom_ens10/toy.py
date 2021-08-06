#!/usr/bin/env python3
# (C) Copyright 2021 ETH Zurich.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ETH Zurich does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#
from __future__ import annotations

import climetlab as cml
from climetlab import Dataset
from climetlab.normalize import normalize_args

__version__ = "0.1.0"

URL = "https://storage.ecmwf.europeanweather.cloud"

PATTERN = "{url}/MAELSTROM_AP4/toy/ens5mini.{month}.nc"


class Ens5mini(Dataset):
    name = "ENS5-mini: Ensemble Prediction System Toy Dataset"
    home_page = "https://confluence.ecmwf.int/display/UDOC/ECMWF+ENS+for+Machine+Learning+%28ENS4ML%29+Dataset"
    licence = "-"
    documentation = """
    The ENS5-mini dataset is a smaller version of ENS10 (see description), which aims to facilitate understanding
    the data and training simple models. It consists of the same data as ENS10 - model output data of
    ECMWF "hindcast" experiments. These are ensemble forecasts with 5 ensemble members that are spread over 10
    years (1998-2007) with two forecasts per week, cropped to the region of Europe (40-60 degrees latitude,
    0-40 degrees longitude). The API of this dataset is designed to be equivalent to that of ENS10.

    The dataset is grouped by month (i.e., a single month contains all 10 years of predictions), where
    each forecast contains two steps: 0 and 24 hour lead time.
    To query the list of months, run `all_datelist` on the loaded dataset.

    In every file, there are 6 dimensions of data (in this order): `number` (ensemble member),
    `time` (year offset from 1998), `step` (forecast lead time, 0=0h, 1=24h),
    `isobaricInhPa` (pressure level), `latitude`, and `longitude`.
    """
    citation = "-"

    terms_of_use = (
        "By downloading data from this dataset, you agree to the terms and conditions defined at "
        "https://github.com/spcl/climetlab-maelstrom-ens10/blob/main/ENS10_LICENCE.txt "
        "If you do not agree with such terms, do not download the data. "
    )

    all_datelist = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
    ]

    @normalize_args(dtype=["pl"])
    def __init__(self, date, dtype="pl"):
        self.date = str(date)
        try:
            if len(date) == 8:  # YYYYmmdd
                month = date[4:6]
            elif len(date) == 4:  # mmdd
                month = date[:2]
            elif len(date) == 2:
                month = date
            else:
                raise ValueError

            # Validate date
            if int(month) > 12 or int(month) < 1:
                raise ValueError
        except ValueError:
            raise ValueError(
                'Invalid date format (either specify "yyyymmdd", "mmdd", or "mm")'
            )

        if str(month) not in Ens5mini.all_datelist:
            raise ValueError(
                "The specified date cannot be found in the "
                "available files. Query available dates with "
                "``Ens5mini.all_datelist``"
            )

        self.dtype = dtype
        request = dict(url=URL, month=month)
        self.source = cml.load_source("url-pattern", PATTERN, request)
