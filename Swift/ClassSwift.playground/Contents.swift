class Animal {
    var age: Int
    let kind: String
    
    init(age: Int, kind: String){
        self.age = age
        self.kind = kind
    }
    
    func Bite() {
        print("\(age)歳の\(kind)が噛み付く")
    }
}

var dog = Animal(age: 2, kind: "犬")
print(dog.age)
dog.Bite()
