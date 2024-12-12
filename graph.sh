#!/bin/bash

tornettools parse tornet-0.005-vanilla;

tornettools parse tornet-0.005-discount;

tornettools parse tornet-0.005-matching;

tornettools plot tornet-0.005-vanilla tornet-0.005-matching --tor_metrics_path tor_metrics_2024-05-01--2024-05-31.json --prefix out
