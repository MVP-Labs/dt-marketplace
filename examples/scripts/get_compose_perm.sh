
export PYTHONPATH=$PYTHONPATH:../DataToken:../Compute-to-Data
export dt_client_cmd=../Compute-to-Data/client/dt-cli.py
export org3_private_key=0x858dc470755f747d50053b2e8e3bfca78d5fd9f75ef5a63398d4e8390792e026
export org3_feature_attr_file=./samples/ddo/3rd_algo_attr.json

python $dt_client_cmd asset cdt --attr_file $org3_feature_attr_file --private_key $org3_private_key

python $dt_client_cmd job init --name 'test' --desc 'test_task' --private_key $org3_private_key
