
export PYTHONPATH=$PYTHONPATH:../DataToken:../Compute-to-Data
export dt_client_cmd=../Compute-to-Data/client/dt-cli.py

export system_private_key=0xd5b87119980bc80944760f1027d7643dc9bdfff8307cae1e831ff7f74f11ebd3
export org1_public_address=0x515903F47bA0c2911eF90871c98CF333158d556B
export org1_private_key=0xaca737275831497429a47bcd5766950a69a0fa8a1511a8cf656005de1c11546e
export org2_public_address=0xC477723C681aFe9389De20066C34bD90164b8266
export org2_private_key=0xc68daf21bb748605396992aaf95a28eba74b5ec53706ce251e35957baccf7e80
export org3_public_address=0x3689d73690d2c8B350AB955f9cf4376Ec7128068

export op_attr_file=./samples/op/crypten_op_attr.json
export org1_feature_attr_file=./samples/ddo/org1_feature_attr.json
export org1_label_attr_file=./samples/ddo/org1_label_attr.json
export org2_feature_attr_file=./samples/ddo/org2_feature_attr.json
export org1_feature_data_store="./samples/data/org1_feature.pth"
export org1_label_data_store="./samples/data/org1_label.pth"
export org2_feature_data_store="./samples/data/org2_feature.pth"

cd ../dt-contracts
truffle migrate --network development

cd ../dt-examples

python $dt_client_cmd system org --name 'org1' --desc 'test_org1' --address $org1_public_address --private_key $system_private_key
python $dt_client_cmd system org --name 'org2' --desc 'test_org2' --address $org2_public_address --private_key $system_private_key
python $dt_client_cmd system org --name '3rd-party' --desc 'test_3rd' --address  $org3_public_address --private_key $system_private_key

python $dt_client_cmd system op --attr_file $op_attr_file  --private_key $system_private_key

CONFIG_FILE=./samples/config/org1_config.ini python ../Compute-to-Data/dsb/daemon.py &

CONFIG_FILE=./samples/config/org2_config.ini python ../Compute-to-Data/dsb/daemon.py &

python $dt_client_cmd asset dt --attr_file $org1_feature_attr_file --store_path $org1_feature_data_store --private_key $org1_private_key
python $dt_client_cmd asset dt --attr_file $org2_feature_attr_file --store_path $org2_feature_data_store --private_key $org2_private_key
python $dt_client_cmd asset dt --attr_file $org1_label_attr_file --store_path $org1_label_data_store --private_key $org1_private_key
