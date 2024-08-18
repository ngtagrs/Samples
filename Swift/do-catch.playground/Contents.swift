import UIKit

var canConnectServer = false

func connectServer() throws {
    if canConnectServer {
        print("サーバと接続")
    }
    else{
        throw NSError()
    }
}

func getData() {
    do {
        try connectServer()
        print("データを取り出す")
    } catch {
        print("エラーの時の処理")
    }
}

getData()
