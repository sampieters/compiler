  %0 = alloca i32, align 4
  store i32 %None, i32* %0, align 4
  %1 = alloca i32, align 4
  store i32 %None, i32* %1, align 4
  %2 = alloca i32, align 4
  store i32 %None, i32* %2, align 4
  %3 = alloca i32, align 4
  store i32 %None, i32* %3, align 4

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %5 = alloca i32, align 4
  %6 = load i32, i32* %5, align 4
  ret i32 %6
}