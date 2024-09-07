let Hello1 = { (name: String) -> String in
    return "こんにちは、\(name)さん！"
}

let Hello2 = { () -> () in
    print("こんにちは、茂木さん！")
}

let Hello3 = {
    print("こんにちは、茂木さん！")
}

print(Hello1("茂木"))
