struct Animal {
    let age: Int
    var kind: String
    
    init(age: Int, kind: String){
        self.age = age
        self.kind = kind
    }
    
    func Bite(){
        print("\(age)歳の\(kind)が噛み付く")
    }
}

var cat = Animal(age: 3, kind: "猫")
cat.Bite()

var animals: [Animal] = [
    Animal(age: 2, kind: "犬"),
    Animal(age: 5, kind: "猫"),
    Animal(age: 10, kind: "パンダ"),
]

for animal in animals {
    animal.Bite()
}
