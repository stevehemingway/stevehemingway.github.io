$curr_dir = "content/trading/2022/June/"
test -d $curr_dir
if (-Not $?) { mkdir $curr_dir  }
pushd $curr_dir
echo $curr_dir

