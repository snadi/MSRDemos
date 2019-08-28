#build container
docker build --tag=msrdemo:f19 .

#ssh into shell
docker run --name MSRDemo -it -rf msrdemo:f19 /bin/sh

#for rebuilding
docker stop MSRDemo
docker stop MSRDemo
#then run above