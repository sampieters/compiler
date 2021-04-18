@.str.0 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.1 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1
@.str.3 = private unnamed_addr constant [5 x i8] c"%d; \00", align 1

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.0, i64 0, i64 0), i32 10)
  %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.1, i64 0, i64 0), i32 10)
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.2, i64 0, i64 0), i32 10)
  %5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @.str.3, i64 0, i64 0), i32 10)
  %6 = load i32, i32* %1, align 4
  ret i32 %6
}
declare i32 @printf(i8*, ...)