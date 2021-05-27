
define void @f(i32) {
  %2 = alloca i32, align 4
  store i32 %0, i32* %2, align 4
  ret void
}

define i32 @main() {
  %1 = alloca i32, align 4
  call void @f(i32 99)
  %2 = load i32, i32* %1, align 4
  ret i32 %2
}