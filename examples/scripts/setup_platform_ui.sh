
cd ../dt-marketplace/indexer
export PYTHONPATH=$PYTHONPATH:../../DataToken
python dt_indexer/daemon.py &

cd ../marketplace
npm install
npm run serve &

cd ../tracer
npm install
npm run serve &