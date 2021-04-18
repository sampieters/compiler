@.str.0 = private unnamed_addr constant [9 x i8] c"%f %d %d\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca float, align 4
  store float 5.000000e-01, float* %2, align 4
  %3 = alloca i32, align 4
  %4 = load float, float* %2, align 4
  %5 = fptosi float %4 to i32
  store i32 %5, i32* %3, align 4
  %6 = alloca i32, align 4
  store i32 0, i32* %6, align 4
  %7 = load float, float* %2, align 4
  %8 = load float, float* %2, align 4
  %9 = fpext float %8 to double
  %10 = load i32, i32* %3, align 4
  %11 = load i32, i32* %6, align 4
  %12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.0, i64 0, i64 0), double %9, i32 %10, i32 %11)
  %13 = load i32, i32* %1, align 4
  ret i32 %13
}
declare i32 @printf(i8*, ...)