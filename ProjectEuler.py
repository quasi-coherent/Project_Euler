import utils
import math
import operator
import datetime
import itertools


def pe1(n=1000):
	'''If we list all the natural numbers below 10 that are multiples of 
	3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000.'''

	return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])


def pe2(n=4000000):
	'''By considering the terms in the Fibonacci sequence whose values 
	do not exceed four million, find the sum of the even-valued terms.'''

	return sum([x for x in utils.fib_list(n) if x % 2 == 0])


def pe3(n=600851475143):
	'''What is the largest prime factor of the number 600851475143?'''

	return max(utils.prime_factors(n))


def pe4(n=3):
	'''Find the largest palindrome made from the product of two 3-digit 
	numbers.'''

	max_ = 0

	for i in range(10 ** (n - 1), 10 ** n):
		for j in range(10 ** (n - 1), 10 ** n):
			if str(i * j) == str(i * j)[::-1] and i * j > max_:
				max_ = i * j
	return max_


def pe5(L=range(1, 20)):
	'''What is the smallest positive number that is evenly divisible 
	by all of the numbers from 1 to 20?'''

	return reduce(utils.lcm, L)


def pe6(n=100):
	'''Find the difference between the sum of the squares of the first one 
	hundred natural numbers and the square of the sum.'''

	return sum([x ** 2 for x in range(1, n)]) - (sum(range(1, n))) ** 2


def pe7(n=10001):
	'''What is the 10001st prime number?'''
	primes = [2]
	p = 3
	while len(primes) < n:
		if utils.is_prime(p):
			primes.append(p)
			p += 2
		else:
			p += 2
	return primes[-1]


def pe8():
	'''Find the thirteen adjacent digits in the 1000-digit number 
	that have the greatest product. What is the value of this product?'''
	num = pe8_num.replace('\n', '')
	max_ = 0

	for i in range(len(num)):
		try:
			if reduce(operator.mul, map(int, num[i:i + 13])) >= max_:
				max_ = reduce(operator.mul, map(int, num[i:i + 13]))
		except IndexError:
			pass

	return max_
	


def pe9(n=1000):
	'''There exists exactly one Pythagorean triplet for which 
	a + b + c = 1000.  Find the product abc.'''
	for a in range(1, n):
		for b in range(a, n):
			c = math.sqrt(a * a + b * b)
			if a + b + c == 1000:
				return int(a * b * c)


def pe10(n=2000000):
	'''Find the sum of all the primes below two million.'''
	return sum(utils.prime_list(n))


def pe11():
	pass


def pe12(n=500):
	'''What is the value of the first triangle number to have 
	over five hundred divisors?'''
	m = 1

	while True:
		if utils.n_div(utils.triangle(m)) > n:
			return utils.triangle(m)
			break
		m += 1


def pe13():
	'''Work out the first ten digits of the sum of the following 
	one-hundred 50-digit numbers.'''
	num = map(int, pe13_num.split('\n'))

	return int(str(sum(num))[:10])


def pe14(n=1000000):
	'''Which starting number, under one million, produces the 
	longest Collatz chain?'''
	max_ = 1

	for m in xrange(n):
		collatz = [m]

		while collatz[-1] != 1:
			if collatz[-1] % 2:
				collatz.append(collatz[-1] / 2)
			else:
				collatz.append(3 * collatz[-1] + 1)
		if len(collatz) >= max_:
			max_ = m

	return m


def pe15(n=20):
	'''How many such routes are there through a 20 by 20 grid?'''
	return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n))


def pe16(n=2 ** 1000):
	'''What is the sum of the digits of the number 2^1000?'''
	return sum(map(int, str(n)))


def pe17():
	pass


def pe18():
	'''Find the maximum total from top to bottom of the triangle below:'''
	triangle = [[int(num) for num in row.split()] for row in pe18_num.split('\n')]

	for row in range(len(triangle) - 1, 0, -1):
		for col in range(row):
			triangle[row - 1][col] += max(triangle[row][col], triangle[row][col + 1])

	return triangle[0][0]


def pe19():
	'''How many Sundays fell on the first of the month during the 
	twentieth century (1 Jan 1901 to 31 Dec 2000)?'''
	tot = 0

	for year in range(1, 101):
		for month in range(1, 13):
			date_ = datetime.date(1900 + year, month, 1)
			if date_.weekday() == 6:
				tot += 1

	return tot


def pe20(n=100):
	'''Find the sum of the digits in the number 100!'''
	return sum(map(int, str(math.factorial(100))))


def pe21():
	pass


def pe22():
	'''What is the total of all the name scores in the file?'''
	letter_score = {letter:i for i, letter in enumerate('\"ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
	names = sorted([name for name in open('files/p022_names.txt').read().split(',')])

	tot = 0
	for i, name in enumerate(names):
		name_score = 0
		for c in name:
			name_score += letter_score[c]
		name_score *= i + 1
		tot += name_score

	return tot


def pe23():
	pass


def pe24(n=1000000):
	'''What is the millionth lexicographic 
	permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''
	n = 1

	for perm in itertools.permutations(range(10), 10):
		if n == 1000000:
			lex_perm = ''
			for c in perm:
				lex_perm += str(c)
		n += 1

	return int(lex_perm)


def pe25(n=1000):
	'''What is the index of the first term in the Fibonacci 
	sequence to contain 1000 digits?'''
	index = 3
	n_1 = 1
	n_2 = 1
	n_3 = 2

	while len(str(n_3)) < 1000:
		n_1, n_2 = n_2, n_3
		n_3 = n_1 + n_2
		index += 1

	return index


def pe26():
	pass


def pe27(lim=1000):
	'''Find the product of the coefficients, a and b,
	 for the quadratic expression that produces the maximum 
	 number of primes for consecutive values of n, starting with n = 0.'''
	primes = [-p for p in utils.prime_list(lim)] + utils.prime_list(lim)
	longest = 0
	a = 0 
	b = 0

	for i in range(-lim, lim):
		for j in primes:
	 		n = 1
	 		while utils.is_prime(abs(n * n + n * i + j)):
	 			n += 1
	 		if n >= longest:
	 			longest = n
	 			a = i
	 			b = j

	return a * b


def pe28(n=1001):
	'''What is the sum of the numbers on the diagonals in a 
	1001 by 1001 spiral formed in the same way?'''
	return sum(4 * n * n - 6 * n + 6 for n in range(3, 1002, 2)) + 1


def pe29(n=100):
	'''How many distinct terms are in the sequence generated 
	by a^b for 2<=a<=100 and 2<=b<=100?'''
	return len(set([a ** b for a in range(2, n + 1) for b in range(2, n + 1)]))


def pe30():
	'''Find the sum of all the numbers that can be written as the sum 
	of fifth powers of their digits.'''
	tot = 0

	for n in range(2, 6 * 9 ** 5):
		if n == sum(int(c) ** 5 for c in str(n)):
			tot += n

	return tot


def pe31():
	pass


def pe32():
	'''Find the sum of all products whose multiplicand/multiplier/product 
	identity can be written as a 1 through 9 pandigital.'''
	pandigital = []

	for n in itertools.permutations(range(1, 10)):
		perm = ''.join(str(i) for i in n)
		for j in range(1, 5):
			for k in range(1, 5):
				if int(perm[:j]) * int(perm[j:j + k]) == int(perm[j + k:]):
					pandigital.append(int(perm[j + k:]))

	return sum(set(pandigital))
























	

	













































































pe8_num = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''


pe13_num = '''37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''


pe18_num = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''