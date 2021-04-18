@.str.0 = private unnamed_addr constant [16 x i8] c"Enter a number:\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.str.2 = private unnamed_addr constant [15 x i8] c"fib(%d)\09= %d;\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @f(i32) {
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  %4 = load i32, i32* %3, align 4
  %5 = icmp slt i32 %4, 2
  br i1 %5, label %6, label %8

; <label>:6:
  %7 = load i32, i32* %3, align 4
  store i32 %7, i32* %2, align 4
  br label %16

; <label>:8:
  %9 = load i32, i32* %3, align 4
  %10 = sub nsw i32 %9, 1
  %11 = call i32 @f(i32 %10)
  %12 = load i32, i32* %3, align 4
  %13 = sub nsw i32 %12, 2
  %14 = call i32 @f(i32 %13)
  %15 = add nsw i32 %11, %14
  store i32 %15, i32* %2, align 4
  br label %16

; <label>:16:
  %17 = load i32, i32* %2, align 4
  ret i32 %17
}

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([16 x i8], [16 x i8]* @.str.0, i64 0, i64 0))
  %4 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i64 0, i64 0), i32* %2)
  %5 = alloca i32, align 4
  store i32 1, i32* %5, align 4
  br label %6

; <label>:6:
  %7 = load i32, i32* %5, align 4
  %8 = load i32, i32* %2, align 4
  %9 = icmp sle i32 %7, %8
  br i1 %9, label %10, label %17

; <label>:10:
  %11 = load i32, i32* %5, align 4
  %12 = add nsw i32 %11, 1
  store i32 %12, i32* %5, align 4
  %13 = load i32, i32* %5, align 4
  %14 = call i32 @f(i32 %13)
  %15 = load i32, i32* %5, align 4
  %16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([15 x i8], [15 x i8]* @.str.2, i64 0, i64 0), i32 %15, i32 %14)
  br label %6

; <label>:17:
  %18 = load i32, i32* %1, align 4
  ret i32 %18
}
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)