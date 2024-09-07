func Hello(name: String) -> String {
    return "こんにちは、\(name)さん!"
}
print(Hello(name: "茂木"))


func Hello(name1: String, name2: String, name3: String) -> String {
    return "こんにちは、\(name1)さん、\(name2)、\(name3)さん!"
}
print(Hello(name1: "茂木", name2: "宇都美", name3: "田中"))

func HelloWorld(){
    print("Hello World!")
}
HelloWorld()
