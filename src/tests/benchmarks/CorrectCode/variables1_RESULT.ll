@.str.0 = private unnamed_addr constant [11 x i8] c"%d; %f; %c\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 5, i32* %1, align 4
  %2 = alloca float, align 4
  store float 5.000000e-01, float* %2, align 4
  %3 = alloca i8, align 1
  store i8 99, i8* %3, align 1
  %4 = load i32, i32* %1, align 4
  %5 = load float, float* %2, align 4
  %6 = load float, float* %2, align 4
  %7 = fpext float %6 to double
  %8 = load i8, i8* %3, align 1
  %9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.str.0, i64 0, i64 0), i32 %4, double %7, i8 %8)
  ret i32 0
}
declare i32 @printf(i8*, ...)