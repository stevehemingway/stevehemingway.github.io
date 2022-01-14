
q -H -d ',' "select '$'||symbol, round(100*Change/[Current Price],2)||'%' from tiger_global.csv" | csv2md | clip
