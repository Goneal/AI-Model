@main
public struct MyApp {
    public private(set) var text = "Hello, World!"

    public static func main() {
        print(MyApp().text)
    }
}
