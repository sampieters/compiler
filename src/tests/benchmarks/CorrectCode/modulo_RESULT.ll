@.str.0 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 1, i32* %2, align 4
  %3 = load i32, i32* %2, align 4
  %4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.0, i64 0, i64 0), i32 %3)
  %5 = load i32, i32* %1, align 4
  ret i32 %5
}
declare i32 @printf(i8*, ...)