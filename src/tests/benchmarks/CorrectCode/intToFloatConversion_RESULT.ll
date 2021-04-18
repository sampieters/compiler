@.str.0 = private unnamed_addr constant [9 x i8] c"%d %f %f\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 5, i32* %2, align 4
  %3 = alloca float, align 4
  %4 = load i32, i32* %2, align 4
  %5 = sitofp i32 %4 to float
  store float %5, float* %3, align 4
  %6 = alloca float, align 4
  store float 1.500000e+00, float* %6, align 4
  %7 = load i32, i32* %2, align 4
  %8 = load float, float* %3, align 4
  %9 = load float, float* %3, align 4
  %10 = fpext float %9 to double
  %11 = load float, float* %6, align 4
  %12 = load float, float* %6, align 4
  %13 = fpext float %12 to double
  %14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.0, i64 0, i64 0), i32 %7, double %10, double %13)
  %15 = load i32, i32* %1, align 4
  ret i32 %15
}
declare i32 @printf(i8*, ...)