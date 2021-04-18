
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca [0 x i32], align 4
  %3 = load i32, i32* %1, align 4
  ret i32 %3
}