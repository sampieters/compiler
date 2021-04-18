@.str.0 = private unnamed_addr constant [28 x i8] c"Enter a 5-character string:\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"%5s\00", align 1
@.str.2 = private unnamed_addr constant [3 x i8] c"%s\00", align 1

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca [5 x i8], align 1
  %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([28 x i8], [28 x i8]* @.str.0, i64 0, i64 0))
  %4 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.1, i64 0, i64 0), [5 x i8]* %2)
  %5 = getelementptr inbounds [5 x i8], [5 x i8]* %2, i64 0, i64 0
  %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.2, i64 0, i64 0), i8* %5)
  %7 = load i32, i32* %1, align 4
  ret i32 %7
}
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)