object SumOfMultiples {

    fun sum(factors: Set<Int>, limit: Int): Int {
        val posFactors = factors.filter { it > 0 }
        fun multiples(base: Int, limit: Int) = generateSequence(0) { it + base }.takeWhile { it < limit }
        return posFactors.flatMap { multiples(it, limit).asIterable() }.toSet().sum()
    }
}
