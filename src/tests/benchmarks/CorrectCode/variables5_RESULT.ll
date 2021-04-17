@.str.0 = private unnamed_addr constant [11 x i8] c"%d; %d; %d\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 10, i32* %1, align 4
  %2 = alloca i32, align 4
  %3 = load i32, i32* %1, align 4
  store i32 %3, i32* %2, align 4
  %4 = alloca i32, align 4
  %5 = load i32, i32* %1, align 4
  store i32 %5, i32* %4, align 4
  %6 = load i32, i32* %1, align 4
  %7 = load i32, i32* %2, align 4
  %8 = load i32, i32* %4, align 4
  %9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([11 x i8], [11 x i8]* @.str.0, i64 0, i64 0), i32 %6, i32 %7, i32 %8)
  ret i32 0
}
declare i32 @printf(i8*, ...)