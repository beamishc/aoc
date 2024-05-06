mkdir -p day_$1
touch day_$1/aoc$1.py
touch day_$1/test_1.txt
touch day_$1/test_2.txt
touch day_$1/input.txt
echo """from icecream import ic\n\ndef day_$1_1(textfile):\n    with open(textfile) as f:\n        lines = f.read().strip().split('/\/n')\n\nic(day_$1_1('day_$1/test_1.txt'))\n\ndef day_$1_2(textfile):\n    with open(textfile) as f:\n        lines = f.read().strip().split('/\/n')\n\nic(day_$1_2('day_$1/test_2.txt'))""" >> day_$1/aoc$1.py
