
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32*, align 8
  %3 = load i32*, i32** %2, align 8
  %4 = load i32, i32* %3, align 4
  %5 = add nsw i32 97, %4
  %6 = load i32, i32* %1, align 4
  ret i32 %6
}