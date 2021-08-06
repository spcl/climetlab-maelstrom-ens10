#!/usr/bin/env python
# (C) Copyright 2021 ETH Zurich.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ETH Zurich does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#


import io
import os

import setuptools


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(file_path, encoding="utf-8").read()


package_name = "climetlab-maelstrom-ens10"

version = None
init_py = os.path.join(package_name.replace("-", "_"), "__init__.py")
for line in read(init_py).split("\n"):
    if line.startswith("__version__"):
        version = line.split("=")[-1].strip()[1:-1]
assert version


extras_require = {}

setuptools.setup(
    name=package_name,
    version=version,
    description="A dataset plugin for climetlab for the ENS10 MAELSTROM dataset.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="SPCL @ ETH Zurich",
    author_email="talbn@inf.ethz.ch",
    url="https://github.com/spcl/climetlab-maelstrom-ens10",
    license="Apache License Version 2.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["climetlab>=0.5.6"],
    extras_require=extras_require,
    zip_safe=True,
    entry_points={
        "climetlab.datasets": [
            "maelstrom-ens10 = climetlab_maelstrom_ens10.ens10:Ens10",
            "maelstrom-ens5mini = climetlab_maelstrom_ens10.toy:Ens5mini",
        ]
    },
    keywords="meteorology",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
    ],
)
