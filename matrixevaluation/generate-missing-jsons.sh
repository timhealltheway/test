

for i in {4..10}
do
  python3 generate_missing_indexes.py  -m $i --data_size 5000 -o 5k_2/missing-5k-$i-pct.json
done
