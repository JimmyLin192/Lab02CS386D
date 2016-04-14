for i in $(seq 1 15)
do
    echo "Processing queries/$i"
    x=$(cat queries/$i)
    echo "$x"
    mysql LAB02 --execute="$x" #> results/$i.txt
    echo ""
done
