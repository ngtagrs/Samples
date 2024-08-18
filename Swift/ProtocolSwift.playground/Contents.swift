protocol Animal {
    var age: Int { get }
    func Bark()
}

struct Dog: Animal {
    let age: Int
    
    func Bark(){
       print("犬が吠える")
    }
}
