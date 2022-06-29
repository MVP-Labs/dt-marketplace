cd ../DataToken
pip install -r requirements.txt --no-deps

cd ../Compute-to-Data
pip install -r requirements.txt

cd ../dt-contracts
yarn
truffle compile
./start-local-environment.sh 