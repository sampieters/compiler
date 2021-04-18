
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = getelementptr inbounds i32, i32* %2, i64 0, i64 1
  %4 = load i32, i32* %1, align 4
  ret i32 %4
}