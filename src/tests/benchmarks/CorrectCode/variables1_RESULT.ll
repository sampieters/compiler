@.str.0 = private unnamed_addr constant [11 x i8] c"%d; %f; %c\00", align 1

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 5, i32* %2, align 4
  %3 = alloca double, align 8
  store double 5.000000e-01, double* %3, align 8
  %4 = alloca i8, align 1
  store i8 99, i8* %4, align 1
  %5 = load i32, i32* %2, align 4
  %6 = load double, double* %3, align 8
  %7 = load i8, i8* %4, align 1
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.str.0, i64 0, i64 0), i32 %5, double %6, i8 %7)
  %9 = load i32, i32* %1, align 4
  ret i32 %9
}
declare i32 @printf(i8*, ...)