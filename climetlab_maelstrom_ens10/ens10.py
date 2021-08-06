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

__version__ = "0.1.1"

URL = "https://storage.ecmwf.europeanweather.cloud"

PATTERN = "{url}/MAELSTROM_AP4/output.{dtype}.2018{month}{day}"


class Ens10(Dataset):
    name = "ENS10 Ensemble Prediction System Dataset"
    home_page = "https://confluence.ecmwf.int/display/UDOC/ECMWF+ENS+for+Machine+Learning+%28ENS4ML%29+Dataset"
    licence = "-"
    documentation = """
    The ENS10 dataset is designed to help the development of machine learning tools to improve ensemble predictions
    via post-processing, as described in https://arxiv.org/abs/2005.08748. It consists of the model output data of
    ECMWF "hindcast" experiments. These are ensemble forecasts with 10 ensemble members that are spread over 20
    years (1998-2017) with two forecasts per week.

    The dataset is grouped by day-of-year (i.e., a single date contains all 20 years of predictions), where
    each date contains three steps: 0, 24, and 48 hour lead time. Thus, files contain three days at a time.
    To query the list of dates, run `all_datelist` on the loaded dataset.

    In every file, there are 6 dimensions of data (in this order): `number` (ensemble member),
    `time` (year offset from 1998), `step` (forecast lead time, 0=0h, 1=24h, 2=48h),
    `surface`/`isobaricInhPa` (pressure level), `latitude`, and `longitude`.
    """
    citation = "-"

    terms_of_use = (
        "By downloading data from this dataset, you agree to the terms and conditions defined at "
        "https://github.com/spcl/climetlab-maelstrom-ens10/blob/main/ENS10_LICENCE.txt "
        "If you do not agree with such terms, do not download the data. "
    )

    all_datelist = [
        "0101",
        "0104",
        "0108",
        "0111",
        "0115",
        "0118",
        "0122",
        "0125",
        "0129",
        "0201",
        "0205",
        "0208",
        "0212",
        "0215",
        "0219",
        "0222",
        "0226",
        "0301",
        "0305",
        "0308",
        "0312",
        "0315",
        "0319",
        "0322",
        "0326",
        "0329",
        "0402",
        "0405",
        "0409",
        "0412",
        "0416",
        "0419",
        "0423",
        "0426",
        "0430",
        "0503",
        "0507",
        "0510",
        "0514",
        "0517",
        "0521",
        "0524",
        "0528",
        "0531",
        "0604",
        "0607",
        "0611",
        "0614",
        "0618",
        "0621",
        "0625",
        "0628",
        "0702",
        "0705",
        "0709",
        "0712",
        "0716",
        "0719",
        "0723",
        "0726",
        "0730",
        "0802",
        "0806",
        "0809",
        "0813",
        "0816",
        "0820",
        "0823",
        "0827",
        "0830",
        "0903",
        "0906",
        "0910",
        "0913",
        "0917",
        "0920",
        "0924",
        "0927",
        "1001",
        "1004",
        "1008",
        "1011",
        "1015",
        "1018",
        "1022",
        "1025",
        "1029",
        "1101",
        "1105",
        "1108",
        "1112",
        "1115",
        "1119",
        "1122",
        "1126",
        "1129",
        "1203",
        "1206",
        "1210",
        "1213",
        "1217",
        "1220",
        "1224",
        "1227",
        "1231",
    ]

    @normalize_args(dtype=["pl", "sfc"])
    def __init__(self, date, dtype="pl"):
        self.date = str(date)
        try:
            if len(date) == 8:  # YYYYmmdd
                month = date[4:6]
                day = date[6:]
            elif len(date) == 4:  # mmdd
                month = date[:2]
                day = date[2:]
            else:
                raise ValueError

            # Validate date
            if int(month) > 12 or int(month) < 1 or int(day) > 31 or int(day) < 1:
                raise ValueError
        except ValueError:
            raise ValueError(
                'Invalid date format (either specify "yyyymmdd" or "mmdd")'
            )

        if (str(month) + str(day)) not in Ens10.all_datelist:
            raise ValueError(
                "The specified date cannot be found in the "
                "available files. Query available dates with "
                "``Ens10.all_datelist``"
            )

        self.dtype = dtype
        request = dict(dtype=self.dtype, url=URL, month=month, day=day)
        self.source = cml.load_source("url-pattern", PATTERN, request)
