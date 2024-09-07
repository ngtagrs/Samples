class Monster {
    var kind = "Monster"
    
    func bodyBrow(){
        print("体当たり")
    }
}

class Dragon: Monster {
    func fireBreath() {
        print("火の息を吐く")
    }
}

class Slime: Monster {
    func recovery() {
        print("回復する")
    }
}

var dragon = Dragon()
print(dragon.kind)
dragon.bodyBrow()
dragon.fireBreath()

var slime = Slime()
print(slime.kind)
slime.bodyBrow()
slime.recovery()
