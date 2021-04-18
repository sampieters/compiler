@.str.0 = private unnamed_addr constant [8 x i8] c"%s %s!\0A\00", align 1
@.str.1 = private unnamed_addr constant [6 x i8] c"Hello\00", align 1
@.str.2 = private unnamed_addr constant [6 x i8] c"World\00", align 1

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.str.0, i64 0, i64 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.1, i64 0, i64 0), i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.2, i64 0, i64 0))
  %3 = load i32, i32* %1, align 4
  ret i32 %3
}
declare i32 @printf(i8*, ...)