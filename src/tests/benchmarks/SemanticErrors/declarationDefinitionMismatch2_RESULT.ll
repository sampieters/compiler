  %0 = alloca i32, align 4
  store i32 %None, i32* %0, align 4
  %1 = alloca i32, align 4
  store i32 %None, i32* %1, align 4

define i32 @f(float, i32) {
  %5 = alloca i32, align 4
  %6 = alloca float, align 4
  store float %2, float* %6, align 4
  %7 = alloca i32, align 4
  store i32 %3, i32* %7, align 4
  %8 = load i32, i32* %5, align 4
  ret i32 %8
}

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = load i32, i32* %1, align 4
  ret i32 %2
}