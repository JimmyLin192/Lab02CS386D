for i in 16 16a 16b 18 18a 18b 
do
    echo "Processing queries/$i"
    x=$(cat queries/$i)
    echo "$x"
    mysql LAB02 --execute="$x" #> results/$i.txt
    echo ""
done
