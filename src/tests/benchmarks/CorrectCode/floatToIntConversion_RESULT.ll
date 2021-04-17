@.str.0 = private unnamed_addr constant [9 x i8] c"%f %d %d\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca float, align 4
  store float 5.000000e-01, float* %1, align 4
  %2 = alloca i32, align 4
  %3 = load float, float* %1, align 4
  %4 = fptosi float %3 to i32
  store i32 %4, i32* %2, align 4
  %5 = alloca i32, align 4
  store i32 0, i32* %5, align 4
  %6 = load float, float* %1, align 4
  %7 = load float, float* %1, align 4
  %8 = fpext float %7 to double
  %9 = load i32, i32* %2, align 4
  %10 = load i32, i32* %5, align 4
  %11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.0, i64 0, i64 0), double %8, i32 %9, i32 %10)
  ret i32 1
}
declare i32 @printf(i8*, ...)