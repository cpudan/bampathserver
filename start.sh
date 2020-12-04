#!/bin/bash

source /broad/software/scripts/useuse
use Anaconda3
conda activate bamserver
gunicorn -b 0.0.0.0:8080 bampathserver:application
