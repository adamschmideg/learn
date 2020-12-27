class Matrix(private val matrixAsString: String) {
    val data = matrixAsString.split("\n").map {
        it.trim().split("\\s+".toRegex()).map {
            s -> s.toIntOrNull() ?: 42} }

    fun column(colNr: Int): List<Int> {
        return data.map{ row -> row[colNr - 1] }
    }

    fun row(rowNr: Int): List<Int> {
        return data[rowNr - 1]
    }
}
