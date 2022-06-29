
export PYTHONPATH=$PYTHONPATH:../DataToken:../Compute-to-Data
export dt_client_cmd=../Compute-to-Data/client/dt-cli.py
export org3_private_key=0x858dc470755f747d50053b2e8e3bfca78d5fd9f75ef5a63398d4e8390792e026
# export cdt="please set this value if you want to execute"
export cdt="dt:ownership:7204192c4b0a49bcbc32ba42237aa21cb3cbfa03ffca496280325e594c72a5e4"

python $dt_client_cmd job exec --task_id 1 --cdt $cdt --private_key $org3_private_key
python $dt_client_cmd tracer dfs --prefix_path $cdt