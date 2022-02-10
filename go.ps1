$curr_dir = "content/trading/2022/February/"
echo $curr_dir
test -d $curr_dir
echo ($?)
test -d $curr_dir
if (-Not $?) { mkdir $curr_dir  }
pushd $curr_dir 


