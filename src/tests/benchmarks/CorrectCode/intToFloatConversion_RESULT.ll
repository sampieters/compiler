@.str.0 = private unnamed_addr constant [9 x i8] c"%d %f %f\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 5, i32* %1, align 4
  %2 = alloca float, align 4
  %3 = load i32, i32* %1, align 4
  %4 = sitofp i32 %3 to float
  store float %4, float* %2, align 4
  %5 = alloca float, align 4
  store float 1.500000e+00, float* %5, align 4
  %6 = load i32, i32* %1, align 4
  %7 = load float, float* %2, align 4
  %8 = load float, float* %2, align 4
  %9 = fpext float %8 to double
  %10 = load float, float* %5, align 4
  %11 = load float, float* %5, align 4
  %12 = fpext float %11 to double
  %13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.0, i64 0, i64 0), i32 %6, double %9, double %12)
  ret i32 1
}
declare i32 @printf(i8*, ...)