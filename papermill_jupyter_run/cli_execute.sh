#!/bin/bash

papermill Clean.ipynb Filled.ipynb -p alpha 0.1 -r txt "abc"
