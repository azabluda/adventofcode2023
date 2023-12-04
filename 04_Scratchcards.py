# https://adventofcode.com/2023/day/4
# Day 04: Scratchcards

def scratchcards(data):
    from collections import defaultdict
    res1 = res2 = 0
    cards = defaultdict(lambda: 1)
    for i, line in enumerate(data.split('\n')):
        L, R = map(str.split, line.split('|'))
        wins = sum(map(L.__contains__, R))
        for j in range(wins):
            cards[i + j + 1] += cards[i]
        res1 += int(2 ** (wins - 1))
        res2 += cards[i]
    return res1, res2


def inputs():

    yield """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

    yield """
Card   1: 99 65 21  4 72 20 77 98 27 70 | 34 84 74 18 41 45 72  2  1 75 52 47 50 93 25 10 79 87 42 69  8 12 54 96 92
Card   2: 51 49 25 92 40 31 18  3 83  4 |  4 40 57 75 16 38 25 92 51  3 36 77 70 94 83 49 18 59 19 31 41 99 43 89 15
Card   3:  5 52 69 84 27 47 17 49 32 98 | 76 82 97  2 17 34 32 31 55 84 87 49 91 81  5 72 23 67 21 35 66 65 44 12 98
Card   4:  2 81 24 58  9 82 21 43 85 83 | 38 21 97 67 82 85 40 24 93 59 53 46  5 15 81 33 22 58  8 89 94  2  3 69 72
Card   5:  6 72 50 45 29 12 55 31 68 62 | 45 16 80 68 29 27 55  7 72 31 66 20 39  9 13 12 62 30 50  6 94 49 42 81  4
Card   6: 26 87 63 54 56 79 90 19 23  7 | 55 13 10 66 17  6 91 93 51 22 65 38 16 68 84 64 43 81 24 85 75 69 11  2  3
Card   7: 63  5 44 82 67 85  1 86 43 47 | 27 69 85 64 34 12  1 36 94 82  4 16 46 63  5 92 14 68 49 86 80 84 67 25 44
Card   8: 51 70 64 30 87 82  2 67 39 56 | 11 49  5 40 58 22 19 53  1 41 66 44  4 65 43 72 98 95 52  8 23 45  3 27 48
Card   9:  9 53 83 37 28 10 74 51 47 59 | 51 65 22  5 87 33 23 17 37 72 60 39 20 88 62 25 40 35  8 11 64 26 55  1 34
Card  10: 84 67 52 95 62 83 39 96  6 14 | 95  5 24 10 96 83 22 21 58 84 26 52 68 32 14  1 67 35 45 37 40  6 76 62 97
Card  11: 62 33 65 83 31 20 45 96  8 63 | 98 96 29 69  7 24 15  4 74 14 65 89 34 37 75 78 46 11 17 40  1 57 94  9 55
Card  12: 29 47 83 13 31 58  3 43  6 46 |  6 81 45 26 31 58  3 21 20 47 75 71 13 74 22 93 35 96 38 44 85 83 29 28 50
Card  13: 33 97 31 48 60 98 94 80 30 29 | 16 33 73 49 37 44 41 47 34 83 11 62 54 86 60 84 29 63 94 28 59 61 71 98 40
Card  14: 47 16 73 33 50 46 39  4 98 14 | 70 62 15 52 98 74 17 69 23  4 94 79 10 19 50  7 37 41  1 39 25  5 86 28 87
Card  15: 27 14 33 76 13 55 87 53 44 74 | 23 17 37 91 66 89 24 86 44 49 52 34 79  6 56  1 46 29  9 71 48 30 31 35 60
Card  16: 95  6  8 69 70 72 60 43 76 30 | 37 83 63 36  9 26  6 20 66 39 52 19 69 12 62 85 32 82 35 45 55 51 18 60 17
Card  17: 74 76 40 52  9 43 59 37 17 92 | 73 62 70 27 55 47 11 18 74  1 71  3 88 65 89  2 58 86 10 42 22 56 29 36 30
Card  18: 79  5 97 48 36 10 67 56  7  6 | 21 54 33 95 43 71 14 46 82 23 70 73 74 51 27 78 91 88 42 92 39 64 18 13 59
Card  19: 62 32  7 51  8 22 26 41 30 16 | 28  9 81  2 53 52 78 25 56 86  3 10 67  1 22 79 24 17 43 99 87 82 93 34 58
Card  20: 41 52 12 40 17 56 72 84 98 63 | 71 69 37 74 47 97  9 34  6 36 96 95  8 49 39 15 85  5 46 64 93 54 20  2 89
Card  21: 85 60 95 97  1 33 27 86 57 54 | 65 97 50 86 45 25 33 70 61 19 54 90 60 57 78  1 29 63 27 76 95 52 46 85 47
Card  22: 43 98 37 17 44 70 52 96 61  8 | 60 17 77 34 74 16 14 22 10 98 52 96 67 62 43 49  8 61 47 90 29 63 70 44 37
Card  23: 68 58 25 26  6 65 38  2 17 80 | 99 26 36 22 52  6 13 82 17 10 65 15 58  3 68 14  2 77 80 84 72 46 29 25 38
Card  24: 47  9 24 20 15 57 29 83 75 11 | 33 47 91 75 20 57 11 27 29 10 14 26 83 15 24 43 82 86  9 18  1 61 98 46 76
Card  25: 92 63  7 80 40 90 46 84 78 12 | 63 40 24 84 75 80 87 56 74 79 92 59  2 66 16 96 78 12 67 46 61 90 86 38  7
Card  26: 33 13 64 23 46 81 73 54 25 95 |  7 75 50 67 44 69 70 22 45 30 12 93 17 26 11 55 10 52 53 36 79 62 27 92  9
Card  27: 58 66 74 59 73 17 92 61 80 99 |  2 83 81 31 34 57  7 22 32 74 39 15 44 23  9 90 88  3 46 20 62 51 42 21 95
Card  28: 35 55 89 36 68 49 79 62  4 31 |  1 26 23 88 28 49 58 54 44 60 33  9  5 99  8  2 95 20 40 12 72 82 43 50 25
Card  29: 73 80  6 42 37 33 68 34 31 79 |  6 63 65 57 77 73 99 56 16 28 80 90 31 51 52 45 79  1 17 42 37 68 46  4 91
Card  30: 99 89  9 45 13  6 91 57 73 90 | 92 54 13  2 40 10 78 71  7  3 49 37 60 53 96 73 61 98  1 45 66 24 48 94 19
Card  31: 21 57  2 83 51 17 96 79 16 60 | 72 35  2 83 51 16 41 96 17 80 25 26 46 57 60 10 50 58 49 79 43 75 21 82  1
Card  32: 25 37 47 88 28 84 49 35 27 71 | 90 73  1 13 93 16 52 74 67 62  7 69 56 87 21 63 86 32 58 59 27 97 61 88 83
Card  33: 68 38 12 31 86 27 41 15 21 66 | 56 64 75 86 19 27 61  7 15 29  3 67 28 11 66 21 22 14 40 24 68 94 13 53 18
Card  34:  9 58  8 48 43 78 67 96 62  6 | 59 56 13 92 77 10 89 71 72 65 98 33 23 40 30 44 97 54 52 84 36 82 26 32 19
Card  35: 74 35 15 51 19  2 98 22  5 20 | 68 60 62 22 84 98 15  7 24 30 18 19 56 52 80 37 74 26 54 41  8 31 34 61 49
Card  36: 82  3 19 48 71 65 47 89 21 36 | 43 75 96  2 32 91 28 37 69 71 18 57 15 35 25 24 88 34 52 31 79 17 49 20 26
Card  37: 72 35 36 87 99 38 91 24  3 20 |  9 62 21 28 64 13  8 35 75 69 87 97 15 46 98 89 24 12 43 34 19 86 72 41 92
Card  38: 96 81 10 64 65 84 38 30 80 68 | 84  3 91 30 26 36 69 95 10 40 87 99 13  7 75 38 82 80  2 31 37 28 90 48 52
Card  39:  6 62 96 34 41 98 81  5 11 57 | 95 59 67 46 36 38 27 74 97 87 72 69 32 37 94 98 79 17 49  5 10 42 48 51 30
Card  40: 96 15 86 31 62 56 22 41 93 33 | 90 21 67 65 50 70 35 89 38 84 55 77 59 57 83 69  2 37 20 36 52 80 27 85 19
Card  41: 40 83 52 58 28 56 68 27 34 87 | 39 38 77 93 69 31 60 54 98 35 15 30 25 73 29 14 66 28 42 82 47 50 17 21 49
Card  42: 11 61 94 85 46 30  7 45 18 93 | 83 93 85 34 22 62 92 60 53 98 41  2 96  1 81 49 72 44 59 26  4 97 65 95 39
Card  43: 11 65 98 28 82 33 80  7  5 36 | 93 83  4 97 60 75 19 23 87 57 52 24 41 32 40 69 30 39 45 88 91 74 37 67 17
Card  44: 61 85  7 94 21 75 84 49 43 92 | 34 66 52 97 82 48 55 12 68 47 99 57  8 30 86 73 28 60 22 63 88 74 78 79 11
Card  45: 68 64 67 10 87  6 29 85 54 86 | 95 85 77 64 35 50 87 97  6 89 86 79 36 43 56  2 10 32 29 68  1 54 67 21 48
Card  46: 13 94 35 87 57 95 50 17 91 20 | 75 91 20 13 76 58 77 19 86 36 87 95  8 80 42 17 57 53 15 94 83 60 35 50 48
Card  47: 75 39 44 23 55 37 76 57 96 34 | 92 40 78 57 75 64 67 66 33 27 23 71 31 37 47 83 16 55 76 96 39 34 44 49  3
Card  48: 29 28 65 97 10 36  1 94 42 23 | 42 65 81 61 56 29 19 28 52 22 66 31  1 43 85 84  5 71 36 23  9 89 27 94 72
Card  49:  8 24 35 89 29 80 42 90 79 41 | 16 60 95 58 53  8 55 22 65 15 97 74 64 93 82 51  1 78 73 61 98 23  5  7 37
Card  50: 58 78  6 97 95 36 26 66 56 99 | 67 52 23 15 73 32 95 29 58 99 36 64 94 98 26 60 47  2 78 56 75 77 97 66  6
Card  51: 23 27 66 17 96  8 90 10 39 91 | 83 65 91 43 90 21 75 99 76 66 57 18 94  8  6 96 54  1 23 28 51 17 27 10 39
Card  52: 54 92 42 65 80 68 45 39 59 24 | 42 86 98 93 39 28 68 65 87 71 37 92 43 76  5 45 54 96 88 59 80 34 24 62 78
Card  53: 55 63 13 70 99 42  1 86 92 23 | 30 17 92 78 32 24 94  1 70  5 13 55 49 88 48 45 99 63 67 79 12 42 86 23 19
Card  54: 94 77 65 92 18 59 44 40 53 79 | 34 65 45  6 99 40 44 59 89 94 55 14 25 47 79 81 53 77 18 23 92 35 33 27 13
Card  55: 92 24 56  3 32 36 50 17  1 74 | 52 78 94  1 74 60 98 55 56 97 89 92 61 85 37 22 17 66 57 50 36 32 48 20 24
Card  56: 72 28 38 64 30 52 84 67 71 89 | 44 58 22 88 70 14 74 26 34 13 85 77  3 52 29 45 84 99 66 73 41 80 81 49 17
Card  57: 21 26 46 29 98 38 80 72 52 47 | 77 79 61 36 98 54  9 87 18 85 42 16 48 51 46 32 47  2 95  8 44 38 58 33 21
Card  58: 78 84 40 65 67  3 37 66 90 74 | 16 46 73 30 26 69 11 49 19 80 97 43 98 18 83  8 60 91  6 24 31 52 74 66 92
Card  59: 29 42 92 24 75 32 72 89 48 81 | 75 78 79 22 19 93 61  1 84 49 15 72 55 40 98 76 36 65 59 24 11 58 32 92 18
Card  60: 64 53 27  3 97 39 40 14 90 81 | 69 35 57 39 46 51 74 71 97 14  1 82 61 68 72 56 93  8 34 75 48  3 78 13 32
Card  61:  7 87 17 45 39 52 18 66 32 48 | 83 42 71 19 65 92 56 27 47 24 70 51 34 23 60 36 49 54 11 80 78 69 38 57 76
Card  62: 77  5 80 47 51 70 64 30 62 63 | 24 21 73  4 80 90 53 70 44 26 39 17 72 89 35 55 36 66 83 25 29 52 98 57 43
Card  63: 67 46 98 44 57  9 15  2 16 58 | 13 61 92 81 10 84 96 82 12 55 99 23  8 29 90 91 95 83 32 63 79 85 51 88 97
Card  64: 35 38 83 64  3 48 87 55 75 34 | 85 41 16  9 80 81 18 86  6 66 33 69 61 37  3 99 32 62 82 30 84  5 40 11 90
Card  65: 59 51 90 42  5 70 88 61 96  2 | 80 12 19 76 40 22 86 34 83 74 26 93 72 71 37 14  3 25 91 30 17 62  4  6 89
Card  66: 85 18  5 57 55 34 32  7 69 80 | 12 31  1 33 28 56 11 17 22 29 47 21 38 20 59 15 50 81 89 63 10 62 79 68 75
Card  67: 69 41 76  8 31 95 13 52 93 23 | 92 41  4 55 93  8  3 89 13 82 31 83 44 78 62  7  2 94 52 95 24 51 23 18 87
Card  68: 80 11 17 71 45 35 91 44 70 52 | 57 91 77  3 14 31 30 53 43 34 27 86 54 79 62 85 83 71 65 18 19 17 10 58 92
Card  69: 59 71 39 44  3 27 69  1 60 58 |  1 65  3 40 71 64 80 51 27 69 83 88 81 59 44 74 75 48 78  9 39 14 60 13 58
Card  70: 83 57 59 27 21 73  3 78 40 64 | 83 59 61 36 57 64 18 70 40 21 97 22 50 28 73 69  1 88  3 43 78 53 31 93 27
Card  71: 58 19 53 76 94 22 67 17 79 25 | 73 54 67 58 61 79 22 76 27 48 88 49 16 94 38 25 52 20 53 63 92 17 19 82  1
Card  72: 67 29  4 47  9 63 72 48 59 11 | 91 89 93  2 69 72 92 80 82 15 86 24 87 75 38 85 16 59 12 28 49 66 50 90 71
Card  73: 82 33 83 63 88 86 18 30 14 28 | 90 14 11 86 13  9 91 34  7 63  4 82 18 30 27 12 92 37 88  2 28 33 51 52 83
Card  74: 27 23 62 83 86 95 66 99 46 92 | 11 83 57 99 91 78 23 27 95 66  3 18 16  7 19 89 28 86 31 47 46  2 79 92 50
Card  75:  5 75 50 22 70 77 82 49 73 46 |  4 50 90 11 32 75 82 71 86 68 64 22 46 70 49 37 79 80 12 45 88 73 58 99  5
Card  76: 10 67 27 35 37 31 41 48 57 50 |  5 68 90 21 51 99 43 79 80  6 23 63 24 76  3 75 19 86 42 67  1 52  4 35 15
Card  77: 53 15 10 16 36 26 31  1 67 73 | 81 25 49  9 46 73 10 99 15 36 86 69 38 30 37 51 53  1 41 27 61 91 16 72 58
Card  78: 41 48  9 35 30 75 82 60 29 45 | 79 81 96 43 45 69 21 42 29 78 41 68 48 27 80 67 37 74  6 51  9 60 30 59 82
Card  79: 27 25 20 58 93  9 50 64 56 79 | 29 91 33  4 36 10 92 54 21 66  7 48 44  8 61 67 12 96 81 22  2 31 62 18 59
Card  80: 20 26 82 39 62  8  3  6 53 14 | 61 67 28 73 87 25 29 60 14 72 56 26 50 66 36 46 31 54 39 84 35 48  6 45 82
Card  81: 12 74 28 96 83 27 91 56 20 31 | 25  8 31 94 38 83 53 57 98 17 24 27 76 39 88 78 21 20  4 15 28 74 81  9 96
Card  82: 34 72 89 67 14 32  4 41 28 22 | 12 45 65 59 43 68 71 34  4 23 10 52 21 27 58  3 48 31 92 98 39 44 86 84 62
Card  83: 58 38 24 92 80 41 36 11 16 56 | 93  2 92 16 64 59 56 11 20 67 88 60 81 65 85 94 39 19 41 83 57 47 97 14  8
Card  84: 64 29 78 39 28 33 88 99 13 32 | 82 84 23 88  3 69 67 35 10 58 93  4 44 41 79 92 30 56 59 60 76 83  6 72 62
Card  85: 79 34 49 17 95 63 60 61 48 15 | 21 16 53 93 74 29 44 52  4 95 64 56 31  1 36 33 92 57 66 67 71 79 34 20  7
Card  86: 93 41 52 71 18 28 19 90 66 36 | 50 33 37 88 61 26 77 92 48 84 78  1 54 58 29 10 63  9 21 31 65  6 24 53 51
Card  87: 13 21 25 32 39 30 86 14 45 49 | 51 42 89 15 12 68 87 27 40 59  9 34 94 46  7 25 62 47 52 75 77 17 81 83 57
Card  88: 91 60 14 46 29 30  1 15 21 51 | 83 40 12 67 41 95  8 31 69 90 63 27 57 36 64 82 54 44 50 93 71 79 17 73 89
Card  89: 33 42 70 89 96 81 83 53 57 23 | 35 33 32 15 57 54  5 74 25 36 81 23 64 22 63 38  4 53 18  7 46 97 26 80 89
Card  90: 80 86 96 81 82 97 60 87 74  6 | 39 74 80 81  6 20 38 96 53 75 97 10 87 59 73  4 60 63 16 31 89 82 68 86 27
Card  91: 64 61 96 73 22 19 32 12 97 95 | 61 88 41  7 57 64 13 90 28 38 95 99 19 22 32 73 12 96 81 43 83 21  1 14 97
Card  92: 87 89 91 57  5 23 75 72 29 47 | 73 39  4  8  1 55 26 83 35 96 45 25 86 62 37 53 68 14 19 76 27 31 50 58 69
Card  93: 95 40 71 56 21 44 23 41 75 82 | 44 23 21 76 40 95 73 97 82 17 50 53 41 74 56 61 75  5 10 71 42 93 78 52 46
Card  94: 19 35 37 46 34 17 13 38 40 87 | 78 34 71  6 29 87 40 45 58 13 79 99 46 35 75 15  9 37 43 17 92 76 38 51 19
Card  95: 37 46 85 19 12 91 66 67 88 23 | 88 37 19 30 56 46 81  6 68  3  9 23 32 71 12  7 91 66 39 67 24 60 85 13 38
Card  96: 30 61 21 49 47 85 45 92 55 33 | 56 33 21  1 30 25 75 55 47 89 34 45 22 12 61 32 85 82 24 79 78 92 49 29 51
Card  97:  3 22 70 51 84 97 60  9 47 20 | 47 26 30 70  3 60 36 57 46 22 51 84 86 79 97 21 59 20 61 98  5 74  9 58 16
Card  98: 85 19 52 60 62 51 50 14 67 96 | 19 22 67 59 16 11 38 60 24 39 29 61  4 42 12  7 46 96 94 69 50 99 25 77 17
Card  99:  4 66 29 36 76 45 32 57 39 81 | 32 45 13 76 38 58 29 72 44  2 50 66 57 23 17  4 85 39 99 20 88  5 36 81 56
Card 100: 65 37 15 55 97 43 72 81 79 98 | 15 23 43 69 95 41 59 92 99 77 24 49 65 80 33 60 79 67  9 48  1 71 57 39  3
Card 101: 95  4 67 42 27 84 75 94 68 49 | 19 24 95  1 56 82 27 94 67 91 34 60 71 14  7 12 78 68  4  2 42 84 75 31 49
Card 102: 50 99 57 21 44 79 45 62 59 41 | 57 37 31 79 99 44 89 64  3 96 34 95 14 63 35 16 26  6 93 45 25 47 41 69  1
Card 103: 91 24 36 35 81 12 96  7 99 32 |  6 63 62 94 42 34 69 28 97 41 60 15 91 35  7  8 92 17 70 10 24 31 16 99 73
Card 104: 33 97 77 80  1 27 98 26 11 34 | 62 91 96 64 70 74 61 28 89 19 71 95 82 17 76 92 56 22 16 26 93 79 78 84  7
Card 105: 93 73 31 75 78 19 85 10 59 37 | 53 26 15 94 74 31 90 19 76 64 42 92 60 27 13 70 99  1  3 83 14 67 36 38 93
Card 106: 71 94 63 90 24 14 58 91 13 88 | 41 91 98 14 88 94 64  4 71 48 22 27 49  3 47 74 63 28 62 12 34 99 84 39 37
Card 107: 86 85 43 91 39  7 15 72 93 18 | 72 59 94  9 66 64 10 31 18 54  3 48 53 41 33  1  7 91 55 78 43 52 37 29 82
Card 108: 34 11 16 22 31 46 64 90 23 25 | 94 92 13 24 70 72 65 18 42  6 60 48  5  4 10 39 20 88 53 33 83 35 68 78 77
Card 109: 72 46 71 52 86 23  9 54 62 81 | 29 35 39 81 34 23 75 92 59 45 89 85 38 65 67 47 61 10 12 98 40 43 46 52 33
Card 110:  5 49 21 64 35 61 31 26 90 45 | 68 48 51 19 58 13  2 67 42 25 55 92 94 81 84 69 15 29 66  6 54 11 59 83  4
Card 111: 16 80 77 99 89 28 21 32 36 24 | 31  8 49 45 43 91  2 39 93  9  4  5 50 82 98 17 25 29 52 36 20 23 38 67 53
Card 112: 23 95 38 52 72 81 69 51 76 82 | 65 93 48 50 96 68 11 39 40 13 19 86 53 47 67 10 49 87 59  5 24 81 31 98 78
Card 113: 33 47 81 24 16  4  8 79 50 45 | 10  5 62 92 43  7 63 57 48 20 72 80 87 59 49 14 13  9 98 53 88 64 56 65 99
Card 114: 75 70 62 72 78 74 93 82 66 57 | 94 38 99  8 80  1 62 30 25 97 78 49 19 45 36 42 82 33 43 10 75 29 72 50 53
Card 115: 21 13 70 11 86 28 49  2 47 75 |  5  2 27 59 31 12 93 50 21 51 56 32 86 47 75  7 20 13 49 28 11 64 70 89 52
Card 116: 21 97 16 68 43 42 63 99 90 19 | 53 70 32 46 90 64 19 97 92 21 42 81  2 30 63 25  6 68  5 69 99 80 95 16 49
Card 117:  5 66 59  7 60 86 55 68 80 96 | 63 61  6 30 33 72 94 64 91  8 28 26 15 49 20  5 56 67 23 90 27  1 85 41 52
Card 118: 83 35 11 17 40 79  7 64 60 32 | 10 76  1 97 81 61 83  9 25 64 78 73 95 41 55 69 11 35 62 60 79 96 52 90 50
Card 119: 69  2 53 20 75 82 42 47 81 15 | 15 97 81 59 47 20 85 69 57 53 25 75 65 39 29 84 42 55 82 94 91  2 11  1 23
Card 120: 31  3 28 24 84 89 77 80 87 82 | 28 22 56 66 10 36 17  6 77 34 49 63 57 41  2 38 97 18 39 24 86 65 20 48 27
Card 121: 41 62 77 63 96 52 30 66 71 90 | 29 83 78 52 26 31 77 96  1 70 32  4 60 41 30 99 57 44 19 51 95 62 50 73 35
Card 122: 71  8 37 35 82 19 67 18 53 16 | 89 67  3 53 19 46 12 83 86 18 37  9 99 71 54  8 27 10 26 15 30 62 16 17 82
Card 123: 82 41 94 61 54 62 88 85 33 91 | 40 96 83 41 78 28  1 88 54 60 85 47 99 36 33 74 77 56 82 61 62 94 91 59 84
Card 124: 94 58 63 64  4 93 27 21 60 10 |  3 81 28  6 58 45 77 70  2 22 83 93 29 78 21 48 75 25 64 27 60 94  4 10 63
Card 125: 61 60 23 16 12 69 45 41 40 24 | 23 14 12 84 69 15 16 83 61 21 60 34 74 92 24 13 45 40 55 85 41 50 25 27 80
Card 126: 32 35 70 58 37 83  6 64 17 78 | 35 48 68 19 41  7 83 71 78  5 75 51 11  9 90 74 26 17 49 37 70 73 64 79 32
Card 127: 80 56 89 61 46 39 71 18 42 76 | 31 43 61 46 76 67 54 74 71 89 66 48 18 37 39 42 83 72 96 11 56 80  1 41 20
Card 128: 23 82 32 51 76 11 20 97  4 68 | 93 10 57 60 34 66 23 84 72 37  4 30 21 90 43  7  5 28 87 55 77 22 86 78 75
Card 129: 91 56  5 89 62 53 52 51 72 32 |  5  4 72 32 94  6 61 17 71 22 93 11 33 81  7  9 14 52 58 27 92 36 40 45 20
Card 130: 86 39 21 68 91 98 41 96 36 53 |  7 55 52 77 93 94 68 96 56 41 45  6 44 76  4 50 32 26 28 29 49  8 37 30 59
Card 131: 52 38 80 69 61 74 82 30 59 51 |  8 76 37 12 22 34 88 50 16 17 85 30 61 27 80 89 52  1 82 32 25 40 51 93 69
Card 132: 53 55 14 45 15 38 94  9 29 80 | 14  3 89 69 94 44 29 16  4 72  1  2 38 84 79 40 22 21 88 64 74 48 24 10 34
Card 133: 81 36 43 29 97 78 35 24 63 17 | 67 98 86 11 51 54 35 71 74 95 50  8 91 27 58 76 49 70 64 30 66 23  3 10 44
Card 134:  4 94 99 23  7 33 79 55 50 70 | 35 23 53 71 38 84 99 52  6 28 42 48 54 58 86 83 66 67 97  7 32 94 75 31 59
Card 135: 81 12 23 92 35 25 30 64 47  9 | 74  8 87  2  3 42 54 79 83 14 76 28 44 32 38 59 70 24 43 95 57  5 63 91 52
Card 136: 87  4 49 94 97 35  6  5 39 29 | 97 20 28 22 63 45 31 41 12 13 92 36  7 27 16 60 47 46 33 61 19 37 78 94 50
Card 137: 83 99  9 76 94 40 20  3 72 67 | 13 44 88 49 85 14  5 55 38  1 46 58 28 93 71 30 66 70 89 17 78 39 92 75 16
Card 138: 37 99 22 13 42 36 20 59 29 10 | 92 95 51 80 24 26 38 86 17  9 90 35 83  4 87 94 12 58  6 64 14 33  8 18 49
Card 139: 26 38 94 41 35 60 99 58 96 36 |  8 27 38 49 99 12 26 87 91 96 76 94 97 14 35 58 29 16 60 36 11 56 73 75 41
Card 140: 10 77 39 49 90 96 25 21 13 41 | 41 45 13  3 77 69 73 85 34 86 16  7 96 30 88 39 70 21 75 10 53 90 49 25 47
Card 141: 22 20 43  3 81 52 92  2 19 18 | 84  2 54 41 19 52  9 92 63 18 48 43 53 20 79 40 75 11 22 81 91 42  3 97 30
Card 142: 38 51 76 11 95 10  6 30 73 93 | 38 61 27 11 59 15 73  5  6 85 93 24  7 30 79 33 35 95 74 10 94 51 76 89 66
Card 143:  6 99 70 44 88 50 79 82 34 49 | 54  8 36 14  1 21 37 34 94  6 99  3 91 88 85 20 81 79 70 50 82 44 29 49 98
Card 144: 53  8 52 47 20 11 85 63 91 30 | 99 37 30 11 53 32 75 80 85  3 27 76 39 67 52 56 40 63 21 47 94  8 83 20 10
Card 145: 53 30 13 68 90 79 87 52 84 85 | 18 52 30 69 67 49 79 74 84  5 11 97 85 90 26 95 23 68 83 64 53 87 13 89 70
Card 146: 70 35 94  6 99 64 91 21 52 48 | 25 50 21 94 10 64 48 90 95 35  6 52 74  3 28 11 65 14 70 99 18 86 88 91 92
Card 147: 39 92 77 71 43 25 64 44 13  6 | 63 48 23 71 35 28 64 43  6 53 14 13 12 59 74 56 39 37 92 77 60 65 44  3 25
Card 148: 11 76 24 45 32 23 66 34 25  6 | 66 71 87 93 32 21 88 45 89 34 14 58 17 25  6  8 91 76 23 33 24 22 52 53 26
Card 149: 25 19 37 10 39 52 33 82 74 71 | 56 27 15 76 53 57  1 54 30 48 88 37 23 36 69 74 45 38 19 61 89 41  8 25 21
Card 150: 81 38 13 61 30 19 56 60 99 52 | 27  4 53 24 39 62  5 78 79 31 89  7 22 20 71 58 14 11 88 30 37 60 19 33 74
Card 151: 41 85 78 42  1 27 28 74 65 12 | 52 53 30 80 22 92 17 94 77 48 70 40 11 89 56 69 86 64 87 37 93 97 29 44 12
Card 152: 77 56 88 41 29  6 72 58 46 39 | 11 61  6 29 24 52 56 86 99 66 88 33 14 47 46 41 77  4 35 39 58 18 89 23 72
Card 153: 13 56 45 64 79 27 33 94 63 82 | 27 83 43 63 82 53 30 14 56  3 64 20 79 13 36 42 90 45 17 10 28 15 94 66 33
Card 154: 96 59 51 76 84 80 12 48 94  4 | 83 59 14 51 84  8 67  4 86 37 97 11 42 23 82 60 12 80  6 49  1 71 69 94 48
Card 155:  6 86 48 72 38 81 11 14 21  2 | 55 90 51 11 67  6 52 57  3 88 43 81 75 47 31 38 54  2  4 92 44 60 14 87 17
Card 156: 83 86 39 84 75 10 97 57 70 92 | 50  8  3 97 89 16 34 79 75 84 41 10 65 57 86 78 24 82  7 36 18 37 27 55 49
Card 157: 32 58 59 75 42 20 81 98 95 96 | 81 60 34 98 31 20 40 19 51  4 32 75 39 68 47 11 96 25 49 56 17 14 44 15 99
Card 158: 24 38 76 95 77 79 58 72 64 34 | 55 16 89 18 31  9 13 46 10  1 72  2 50 47 56 62 79 94 33 90 19 26 24 35 66
Card 159: 97  8 29 31 60 27 50 41  4 15 | 28 45 54 21 11 69 20 25 30 76 18 93 96 92 47  1 59 74 77 95 13 86 79 50 39
Card 160: 38 98 88 70 12  3 11 72 92 95 | 15 17 43  6 90 53 79 58 60 10 67 50 69 35 13 23 74 66 76 89 91 83 87 57 63
Card 161: 41 93 52 17 58 79 74  5 96 38 | 72 49 25 46 35 19 74  2 15 26 94 81 90 51 77 41 18 40  9 48 82  1 11 23 61
Card 162: 56  4 76 44 97 39 40 24 77 28 | 80 20 63 37 25 34 11 99 12 13 50 61 38 95 42 72 35 48 27 75 85  2 17 66 47
Card 163: 78 40 59 68 11  5 16 74 46 15 | 25 42  2 45 47 71 52 84  1  7 10 49 53 60 41 56 51 88  9 26 93  8 92 23 28
Card 164: 31 94 69 47 90 21 11 81 41 61 | 71 93 74 36 58 11 77  2 85 66 26 34 59 97 88 24 15 20 62 61 54 35 27 40 53
Card 165: 13 88 71  4 72 94 42 76 40 50 | 35 59 18 90 11 16 96 61 32 22 29 69 25 89 39 97 28 62 21 17 36 79  8 86 53
Card 166: 50 51 82 70  6 37 81 12  1 32 | 78 22 80 12 64 10 88 55 77 51 23 75 50 19 62 89 99 83 71 44 91 85 24  5 46
Card 167: 12 43 33 53 32 25 77 70  7 75 | 58 18 29 46 24 50 25 75 14 39 43  7  6 53 77 80 16 68 32 21 70 12 62 33 76
Card 168: 46  3 99 72 94 95 69 36  1 91 | 80 81 99 72 56 26  3 17 21 42 39  4 94 70 24 69 18 76 40 34 89 31 20 71 90
Card 169: 68 10 62  1 45 98 60 15 18 79 | 58 15 93 41 59 37 28 39 20 35 26 12 60  7  9 90 88 62 68  1 18 75 45 53 36
Card 170: 42 82 12 31  3  1 92 97 81 45 |  8 28 52 74 21 25 55 41 81  7 40 73 67 63 48  2 90 60 58 54 93 26 18 61 43
Card 171:  3 32 45 54 89 21 80 68 10 67 | 67 79 70 98 65  9 30 34  8 41 53 21 84 89 85 77 50 81 73 52 94  6 62 82 45
Card 172: 90 28  2 40 58 30 92 49 94 57 | 38 16 19 36 63 20 54  2 44 72  5 92 90 33 97 22 46 30 35 24  6 11  4 57 58
Card 173:  4  6 98 85 65 69 25 70 35 33 | 67 12 98 82 54 32 33 66 77 93 49 34 92 29 15 58 91 21 85  5 70 47 37 25 26
Card 174: 35 78 15 91 73  8 64  5 57 87 | 85 29 59 78 88 75 40 17 97 69 68 15 56 44  9 48 12  3 24 27 20  1  2  5 87
Card 175: 13 78 69 93 95 49 36 54 98 41 | 99 45 88 77 94 44 55  5 23 37 64 87 58 89 21 95 76 91  7 30 17 82 53  8 92
Card 176: 79 23 52 33 50 94 37 89  3 29 | 30 69 38 43 90  4  2 45 42 98 96  9 25 63 74 61 13  1 56 17 24 86 10 28 11
Card 177: 43 91 33 34 57 73 90 53 85 94 |  4 92 66 25 16 88 14 21 80 36 41 28 56 49 31 15 38 87 40 59  3 77 45 23 18
Card 178: 92 78 56  1 11 61 88 34 20 95 | 80 90 28 83 29  8 16 21  6 85 40 53 77 65 58 82 72 79 69 64 47 49 59 18 13
Card 179: 67 66  6 26 61 75  3 39 38 92 |  3 17 84 32 99 76 85 41 87 65 10 44 24 48 90 95 30 97 39  7 93 67 77 62 70
Card 180: 55 90 31 49 44 80 23 46 92 52 | 81 93 53 82 46  6  8 55 74 92 31 49 58 52 97 20 90 80 60 30 96 44 35 23 83
Card 181: 91 42 96 69 10 32 61 92 60 21 | 13 50  6 61 58 60 32 59 86 69 85 23 47 42 14 71 92 29 96 91 10 19 75 21 78
Card 182: 18  6 53 76 74 48 92 54 34 52 | 17 16 52 34 54 78 45 49 76 92 48 44 74 18 85 43 21 35 53 57  6 36 29 40 73
Card 183: 46 30 56  7 87 23 15 51 48 12 | 52 51 66 82 86 13 56 33 15 77 36 30 48 12 76 60 99 24  4 39 72 28 11  7 59
Card 184: 86 48 72 24 54 50 76 26 10 61 | 74 55 29 76 42 86 62 48 19 43 50 10 22 24  8 54 53 44 39 61 26 46 23 78 72
Card 185:  3 10 74 35 33  4 26 21 45 36 | 92 60 15 61 76 55 67 16 48 71 72 31 68 94 80 59 28 81 49 91 40 98 47 87 44
Card 186: 73 97 14 59 77 63 64  4 67 76 | 98 97 95 21 73  9 71 50 76  3 59 16 63 14  2 99 18  4 28 67  5 64 31 77 52
Card 187: 28 34 68 97  4 66 93 25 30 86 | 15 42 46 54 76  5 44 17 97 79 81 56 58 99 77 64 67 43 87  3 48 53 92 18 27
Card 188: 90 31 93 23 28 58  4 54 15 38 |  4 31 15 69 93 54 90 44 23 58 51 25 34  2 29 27 40 55 28 41 38 56 72 89  1
Card 189: 29 45 89 18 30 77 99 82 60 36 | 15 82 58 60 99 18 26 64 89  6 30 76 11 68 29 85 45 14 36 77 51 22 83 20 93
Card 190: 44 17 38  7 26 54 18 40 48  8 | 37 31 78 85 39  5 76 91 92 64 35 57 24 38 20 86 63 96 59 11 94 82 60 29 41
Card 191: 56 73 38 58 50 81 19 70  2 99 |  4 52 22 93 20 64 12 27 18 88 89  6 68 31 61 66  1 85 36 23 48 26 86 83 75
Card 192: 82 90 14 47 38 39 32 35 19 80 | 60 17 19 48  9  6 57 93 22 99 21 41 24 70 84 30 64 72  7 47 45 44 53 15 88
Card 193: 68 10 83 67 85 98  3 77 33 35 | 88 27 85 67 17 63 48 59 10 52 23  2 55 75 68 96 57 45 33 16 43 77  3 35 69
Card 194: 70 39 54 44 10 24 28 74 55 21 | 57 23 48 64 43 54 44 36 59  7  5 10  2  4 94 77 69 99 47 42 97 21 18 38 66
Card 195: 25 26 18 81 88 51 54 13 45 46 |  7 46 96 85 81 68 88 26 41 13 56 50 93  3 69 51 90 82 16 64 32 23 70 45 33
Card 196: 52 42  6  9 22 67 34 98 47 64 | 13 98  3 40 63 53 99 61 25 92 88  7 42 41 87  1  6 89 84 51 55 16 43 10 59
Card 197: 67 50 53 82 11 72 14  2 18 88 | 45 35 61 56 47 87 79  2 33 31 32 41 98 51 58 72 59 38 89 80 12 92 14  5 39
Card 198: 75 96 69  8 87 98 66 17 39 86 |  1 50 97 11 54  7 12 99 51 23 14 61 81 77 21 92 20 40 74 18 45 90  4 70 71
Card 199: 41  7 83 11 20 51 85 50 71 33 | 69 84 40 55 35 33 89 34 75  2 19 63 50 14 26 76 13 29 66 47 46 22 62 48 58
Card 200: 37  1 67 65 51 47 28 91 81  8 | 36 69 85 14 72 94 60 25 90 34 88 66 23 30 54 39 31 63 40 38 12  5  7 61 41
Card 201: 72 10 99 46 62 14 87  4 77  6 | 51 37  1 43 28 13 81  9 21 20 18 56 94 79 41 57 76 85 30 65 19 67 92 58 61
Card 202: 35 58 73 33 42 19 64 43 10 57 | 76 38 50 14  4 41 25  2 79 99 85 72 62 17 52 95 15 28 66 82 90  9 65 16  7
Card 203: 28 17 98 38  5 43 88 51  2  8 | 87 53 85 13 37 60 18 52 59 54 32 33 48 58 72 62 81 40 12 56 97 74 35 29 42
Card 204: 20 17 43 90 54 82 50 51 52 65 | 34 26  1 12 52 47 51 29 54 24 31 96 90 39 82 43 20 92 15 65 50 13 14 17 69
Card 205: 88 49 79 76 42 77 40  2 73 54 | 36 44  9 38 24 29 73 76 79 46 93 31 88 98 50 57  6  8 17 49  3 59 64 54 52
Card 206: 20 46 95  1 88 32 38  7 12 29 | 42 56 19 41 37  1 88  7 31 96 33 20 47 72 75  9 77 53 29 38 89 46 32 79 95
Card 207: 90 33 85  4 15 34 89 16 38 46 | 92 54 88 73 24 93 78 82 85  2 38 46 34 45 26 74 79  4 62  8 52 32 33 63 76
Card 208: 77 41 55 18  7 57 59 44 93 91 | 20 56 10 78  8 40 63 85 87  3 67 60 28 73 49 17 22 62 68 86  9 84 70  5 47
Card 209: 66 24  5 41 46 30 67 97 54 59 | 49 90 31 10 45 36 46 22 54  5 78 17 89 59  2 38 77 97 20 35 67  9 26 76 41
Card 210: 75 76 90 44 52 19 82 89  4 56 | 43 44  8 68 74 40 38 96 84 76 77 11 65 89 16 20 14 29 52 56 66 33 90 99 75
Card 211: 88 37  9  2 42 20 79 66 45 90 | 81 13 60 40 19 38 50 11 20  4 37  9 69  7 30 27 47 46 78 64 90 99 17 43 51
Card 212: 87 61 34 76 19  3 62 51 63  1 | 19 67 85 34 89 82 17 91 59 62 21 70 23 96 61 29 74 28 87  5  1 46  6 63 22
Card 213: 11 58 56 99 53 74 70 24 51 29 | 58 44 50 53 94 74 95 93 88 59  2 46 91 77 55 99 21 26 98 30 43 86 11 13 79
Card 214: 32 26 80 46 74 69 12 60 71 36 | 45 58 88 28 70 85 26 96 30  1 74  2 97 15 81 87 86  3 94 19  5  8 62 36 29
Card 215: 90 21 84 54 79 31 35 92  2 19 | 86 18 14 57 99 85 62 23 65 28 39  5  2 69 71 30 16 40 82 83 91 37 26  1 27
Card 216: 30 52 95 64 27 68 90 29 12 50 |  9 60  1 33 57 28 81 38 99 39  8 30 76 37  7 91 36 41 50 27 80 93 75 87 16
Card 217: 82 57 48 80 59 58 86 28 56 88 | 15 10 23 62 14 69 84 66 79 86 68 75 90 78 50 17 40 67  3 63 57 12 42 83 20
Card 218: 40 82 47 31 37 77 90 33  1 41 | 26 38 15 45 94 28 17 75 16 23 30 29 54 80 35 37  4 96 34 27 49 32 58 51 73
Card 219: 58 38 53 49 11 10 14  3 89  2 |  8 16 54 18 44 95 31 15 46 45 73 40 61 28 98  5 70 63 69 26 34 80 12 42 90
"""

for data in inputs():
    print(*scratchcards(data.strip()))
