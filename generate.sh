#!/bin/bash

for counter in {1..10};
do 
	tornettools generate relayinfo_staging_2024-05-01--2024-05-31.json userinfo_staging_2024-05-01--2024-05-31.json networkinfo_staging.gml tmodel-ccs2018.github.io --network_scale 0.005 --prefix tornet-0.005-vanilla-$counter &&
		cp -r tornet-0.005-vanilla-$counter tornet-0.005-discount-$counter &&
		cp -r tornet-0.005-vanilla-$counter tornet-0.005-matching-$counter
done

for counter in {1..10};
do
	tornettools simulate tornet-0.005-vanilla-$counter
done
