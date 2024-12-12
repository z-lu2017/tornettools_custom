#!/bin/bash

tornettools generate relayinfo_staging_2024-05-01--2024-05-31.json userinfo_staging_2024-05-01--2024-05-31.json networkinfo_staging.gml tmodel-ccs2018.github.io --network_scale 0.005 --prefix tornet-0.005-vanilla;

cp -r tornet-0.005-vanilla tornet-0.005-discount;

cp -r tornet-0.005-vanilla tornet-0.005-matching;
