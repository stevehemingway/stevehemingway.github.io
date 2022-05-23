$curr_dir = "content/trading/2022/May/"
pushd $curr_dir
echo $curr_dir
test -d $curr_dir
if (-Not $?) { mkdir $curr_dir  }
# pushd $curr_dir 
# py $curr_dir/today.py  $curr_dir
# np $curr_dir/$(py todays_date.py)

