
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 102, i32* %2, align 4
  store i32 -92, i32* %2, align 4
  store i32 485, i32* %2, align 4
  store i32 0, i32* %2, align 4
  %3 = load i32, i32* %1, align 4
  ret i32 %3
}