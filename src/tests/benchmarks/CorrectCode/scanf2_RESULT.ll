@.str.0 = private unnamed_addr constant [28 x i8] c"Enter a 5-character string:\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"%5s\00", align 1
@.str.2 = private unnamed_addr constant [3 x i8] c"%s\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca [5 x i8], align 1
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([28 x i8], [28 x i8]* @.str.0, i64 0, i64 0))
  %3 = call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.1, i64 0, i64 0), i8* %1)
  %4 = load i8, i8* %1, align 1
  %5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.2, i64 0, i64 0), i8 %4)
  ret i32 1
}
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)