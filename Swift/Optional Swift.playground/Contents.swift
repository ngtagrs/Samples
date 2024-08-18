//var optionalInt: Int? = 30
//print(optionalInt)

// 強制的アンラップ
//var optionalInt: Int? = 30
//print(optionalInt!)

//var optionalInt: Int?
//if let unwrapedInt = optionalInt {
//    print(unwrapedInt)
//}
//else {
//    print("unwrapedIntはnil")
//}

var optionalInt: Int?
func Unwrap() {
    guard let unwrapedInt = optionalInt else {
        print("optionalIntはnil")
        return
    }
    print(unwrapedInt)
}

Unwrap()
