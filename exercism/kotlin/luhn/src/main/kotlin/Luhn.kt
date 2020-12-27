object Luhn {

    fun isValid(candidate: String): Boolean {
        val nonNums = candidate.replace("[0-9 ]*".toRegex(), "")
        if (nonNums.count() > 0) {
            return false
        }
        val nums = candidate
                .replace("[^0-9]*".toRegex(), "")
                .map {it.toString().toInt()}
                .reversed()
        if (nums.count() <= 1) {
            return false
        }
        val check = nums
                .mapIndexed{id, n -> if (id % 2 == 1) 2 * n else n}
                .map{ if (it > 9) it - 9 else it}
                .sum() % 10
        println(nums)
        val debug = nums
                .mapIndexed{id, n -> if (id % 2 == 1) 2 * n else n}
                .map{ if (it > 9) it - 9 else it}
        println(debug)
        println(debug.sum())
        println(debug.sum() % 10)
        return check == 0
    }
}
