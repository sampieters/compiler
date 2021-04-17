
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 10, i32* %1, align 4
  %2 = alloca i32*, align 8
  store i32* %1, i32** %2, align 8
  %3 = alloca i32**, align 8
  store i32** %2, i32*** %3, align 8
  ret i32 1
}