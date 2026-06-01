echo "****************** TRAIN ******************"
python tracking/train.py --script ostrack --config vit_ce_adapter_modal_256 --save_dir ./output --mode multiple --nproc_per_node 3
echo "****************** TEST ******************"
python tracking/test.py ostrack vit_ce_adapter_modal_256