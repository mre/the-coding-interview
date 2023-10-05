object ArraySum {

    // A data type to contain a mixture of single elements X of type A
    // or sequences of this datatype, i.e. again single elements or sequences ...
    // This is independent of whether type A can be summed over or not.
    // The data type is iterable so that we can flatten out the sequence of sequences later.
    trait AOrAs[A] extends Iterable[A]

    case class A[A](a: A) extends AOrAs[A] {
        override def iterator: Iterator[A] = Iterator.single(a)
    }

    // using varargs
    case class As[A](as: AOrAs[A]*) extends AOrAs[A] {
        override def iterator: Iterator[A] = as.foldLeft(Iterator.empty[A]) {
            case (it, a) => it ++ a.iterator
        }
    }

    // The readme requires arraySum to accept a single parameter, being formal list.
    // This implementation also works for an informal list, i.e. varargs.
    // The readme requires the type Int, but summing works on any numeric type, thus we use Numeric
    def arraySum[N: Numeric](as: AOrAs[N]*): N = as.flatten.sum

}

import ArraySum.{A, As, arraySum}
// Test for single list
assert(15 == arraySum(As(A(1), A(2), As(A(3), A(4), As(A(5))))))
// Test for varargs
assert(15 == arraySum(A(1), A(2), As(A(3), A(4), As(A(5)))))
