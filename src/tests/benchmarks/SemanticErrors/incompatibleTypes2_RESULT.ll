
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 5, i32* %2, align 4
  %3 = alloca i8, align 1
  store i8 97, i8* %3, align 1
  %4 = load i32, i32* %2, align 4
  %5 = load i8, i8* %3, align 1
  %7 = load i8, i8* %3, align 1
  %8 = sext i8 %7 to i32
  %6 = add nsw i32 %4, %8
  %9 = load i32, i32* %1, align 4
  ret i32 %9
}