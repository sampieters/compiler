@.str.0 = private unnamed_addr constant [7 x i8] c"%d%f%c\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([7 x i8], [7 x i8]* @.str.0, i64 0, i64 0), i32 10, double 5.000000e-01, i8 37)
  %3 = load i32, i32* %1, align 4
  ret i32 %3
}
declare i32 @printf(i8*, ...)