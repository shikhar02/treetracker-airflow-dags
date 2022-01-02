#!/bin/bash
bash << 'EOF'
SUBDOMAIN=prod-k8s
request(){
    for(( i=$1; i<=$2; i++));
    do
        url="http://treetracker-tile-server.tile-server.svc.cluster.local/${i}/1/1.png"
        if [ ! -z $3 ];
        then
        url="${url}?$3"
        fi
        echo $url
        curl -s -o /dev/null $url && echo "Done at `date`"
    done
}
request 2 15
request 2 15 map_name=freetown
request 2 15 map_name=TheHaitiTreeProject
request 2 15 map_name=addis
request 2 15 map_name=echo
request 2 15 map_name=fairtree
request 2 15 map_name=SustainablyRun
request 2 15 map_name=KijaniForestry
request 2 15 wallet=SustainablyRun
request 2 15 wallet=FreetownCityCouncil
request 2 15 wallet=JonasPhilanthropiesFairtreeSamburu
request 2 15 wallet=TheHaitiTreeProject
request 2 15 wallet=Greenstand
request 2 15 wallet=SGI.OPT
request 2 15 wallet=forestmatic-storage
request 2 15 wallet=usa-river-mali-hai-club
request 2 15 wallet=Greensteps
request 2 15 wallet=forestmatic
request 2 15 wallet=FinorX
request 2 15 userid=5
request 2 15 userid=3703
request 2 15 userid=1073
request 2 15 userid=2367
request 2 15 userid=1301
request 2 15 userid=1060
request 2 15 userid=2415
request 2 15 userid=1108
request 2 15 userid=1155
request 2 15 userid=1483
request 2 15 userid=2368
request 2 15 userid=1953
request 2 15 userid=1670
request 2 15 userid=3747
EOF
exit 0