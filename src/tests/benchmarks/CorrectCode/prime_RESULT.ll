@.str.0 = private unnamed_addr constant [44 x i8] c"Enter the number of prime numbers required\0A\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.str.2 = private unnamed_addr constant [30 x i8] c"First %d prime numbers are :\0A\00", align 1
@.str.3 = private unnamed_addr constant [3 x i8] c"2\0A\00", align 1
@.str.4 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  store i32 3, i32* %3, align 4
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([44 x i8], [44 x i8]* @.str.0, i64 0, i64 0))
  %7 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i64 0, i64 0), i32* %2)
  %8 = load i32, i32* %2, align 4
  %9 = icmp sge i32 %8, 1
  br i1 %9, label %10, label %14

; <label>:10:
  %11 = load i32, i32* %2, align 4
  %12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([30 x i8], [30 x i8]* @.str.2, i64 0, i64 0), i32 %11)
  %13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.3, i64 0, i64 0))
  br label %14

; <label>:14:
  store i32 2, i32* %4, align 4
  br label %15

; <label>:15:
  %16 = load i32, i32* %4, align 4
  %17 = load i32, i32* %2, align 4
  %18 = icmp sle i32 %16, %17
  br i1 %18, label %19, label %46

; <label>:19:
  store i32 2, i32* %5, align 4
  br label %20

; <label>:20:
  %21 = load i32, i32* %3, align 4
  %22 = sub nsw i32 %21, 1
  %23 = load i32, i32* %5, align 4
  %24 = icmp sle i32 %23, %22
  br i1 %24, label %25, label %34

; <label>:25:
  %26 = load i32, i32* %3, align 4
  %27 = load i32, i32* %5, align 4
  %28 = srem i32 %26, %27
  %29 = icmp eq i32 %28, 0
  br i1 %29, label %30, label %31

; <label>:30:
  br label %34

; <label>:31:
  %32 = load i32, i32* %5, align 4
  %33 = add nsw i32 %32, 1
  store i32 %33, i32* %5, align 4
  br label %20

; <label>:34:
  %35 = load i32, i32* %5, align 4
  %36 = load i32, i32* %3, align 4
  %37 = icmp eq i32 %35, %36
  br i1 %37, label %38, label %43

; <label>:38:
  %39 = load i32, i32* %3, align 4
  %40 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.4, i64 0, i64 0), i32 %39)
  %41 = load i32, i32* %4, align 4
  %42 = add nsw i32 %41, 1
  store i32 %42, i32* %4, align 4
  br label %43

; <label>:43:
  %44 = load i32, i32* %3, align 4
  %45 = add nsw i32 %44, 1
  store i32 %45, i32* %3, align 4
  br label %15

; <label>:46:
  %47 = load i32, i32* %1, align 4
  ret i32 %47
}
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)