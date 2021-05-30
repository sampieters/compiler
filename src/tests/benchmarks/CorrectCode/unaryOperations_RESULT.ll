@.str.0 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.1 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.3 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.4 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.5 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 9, i32* %2, align 4
  %3 = alloca [2 x i32], align 4
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.0, i64 0, i64 0), i32 9)
  %5 = load i32, i32* %2, align 4
  %6 = add nsw i32 %5, 1
  store i32 %6, i32* %2, align 4
  %7 = load i32, i32* %2, align 4
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.1, i64 0, i64 0), i32 %7)
  %9 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 0
  store i32 15, i32* %9, align 4
  %10 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 1
  store i32 12, i32* %10, align 4
  store i32 12, i32* %2, align 4
  %11 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 1
  %12 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 1
  %13 = load i32, i32* %12, align 4
  %14 = sub nsw i32 %13, 1
  store i32 %14, i32* %11, align 4
  %15 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 1
  %16 = load i32, i32* %15, align 4
  %17 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2, i64 0, i64 0), i32 %16)
  %18 = load i32, i32* %2, align 4
  %19 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.3, i64 0, i64 0), i32 %18)
  %20 = load i32, i32* %2, align 4
  %21 = add nsw i32 %20, 1
  store i32 %21, i32* %2, align 4
  %22 = load i32, i32* %2, align 4
  %23 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.4, i64 0, i64 0), i32 %22)
  %24 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 0
  %25 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 0
  %26 = load i32, i32* %25, align 4
  %27 = sub nsw i32 %26, 1
  store i32 %27, i32* %24, align 4
  %28 = getelementptr inbounds [2 x i32], [2 x i32]* %3, i64 0, i64 0
  %29 = load i32, i32* %28, align 4
  %30 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.5, i64 0, i64 0), i32 %29)
  %31 = load i32, i32* %1, align 4
  ret i32 %31
}
declare i32 @printf(i8*, ...)