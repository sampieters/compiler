  %0 = alloca i32, align 4
  store i32 %None, i32* %0, align 4
  %1 = alloca i32, align 4
  store i32 %None, i32* %1, align 4

define i32 @f(i32) {
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store i32 %2, i32* %5, align 4
  %6 = load i32, i32* %4, align 4
  ret i32 %6
}

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = load i32, i32* %1, align 4
  ret i32 %2
}