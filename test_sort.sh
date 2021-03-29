DIFF=$(cat Sort\ Me.txt | pipenv run python sort_me.py | diff -q sorted.txt -)
if [ "$DIFF" = "" ]; then
	echo "Sort passed"
else
	echo "Sort failed"
	exit 1
fi


DIFF=$(cat Sort\ Me.txt | pipenv run python sort_me.py -r | diff -q sorted_reverse.txt -)
if [ "$DIFF" = "" ]; then
	echo "Reverse sort passed"
else
	echo "Reverse sort failed"
	exit 1
fi


