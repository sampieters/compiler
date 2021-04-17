
; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 5, i32* %1, align 4
  %2 = alloca float, align 4
  %3 = sitofp i32 %2 to float
  %4 = load float, float* %1, align 4
  store float %4, float* %2, align 4
  %5 = alloca float, align 4
  store float 1.000000e+00, float* %5, align 4
  ret i32 1
}