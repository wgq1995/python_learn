struct MyMessage {
    string name,
    i32 age
}



service HelloService {
    void sayHello()
    string getData(1:string input)
    string getInfo(1: MyMessage myMessage)
}
