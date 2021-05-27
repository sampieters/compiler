  %0 = alloca i32, align 4
  store i32 %None, i32* %0, align 4
  %1 = alloca i32, align 4
  store i32 %None, i32* %1, align 4
  %2 = alloca i32, align 4
  store i32 %None, i32* %2, align 4

define i32 @main() {
  %4 = alloca i32, align 4
  %5 = load i32, i32* %4, align 4
  ret i32 %5
}