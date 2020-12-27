class Series (val s: String) {
    val digits = s.map{ it.toString().toInt() }
    init {
        require(s.matches("[0-9]*".toRegex()))
    }

    fun getLargestProduct(span: Int): Long {
        if (span == 0) {
            return 1
        }
        require(digits.count() > 0)
        require(span > 0)
        require(span <= digits.count())
        return digits.windowed(span).map{ nums -> nums.fold(1L){acc, n -> acc * n} }.max() ?: 0
    }
}
