import java.lang.IllegalArgumentException

class Triangle<out T : Number>(val a: T, val b: T, val c: T) {
    val ad = a.toDouble()
    val bd = b.toDouble()
    val cd = c.toDouble()

    init {
        val isValid = ad > 0
                && bd > 0
                && cd > 0
                && ad + bd > cd
                && ad + cd > bd
                && bd + cd > ad
        if (!isValid) {
            throw IllegalArgumentException("not valid")
        }
    }


    val isEquilateral: Boolean = a == b && b == c

    val isIsosceles: Boolean = a == b || a == c || b == c

    val isScalene: Boolean = !isIsosceles
}
