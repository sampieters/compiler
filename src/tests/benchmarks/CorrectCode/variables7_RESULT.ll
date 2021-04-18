@.str.0 = private unnamed_addr constant [12 x i8] c"%d; %d; %d;\00", align 1
@a = common global [2 x i32] zeroinitializer, align 4

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 3, i32* %2, align 4
  %3 = getelementptr inbounds [2 x i32], [2 x i32]* @a, i64 0, i64 0
  store i32 1, i32* %3, align 4
  %4 = getelementptr inbounds [2 x i32], [2 x i32]* @a, i64 0, i64 1
  store i32 2, i32* %4, align 4
  %5 = getelementptr inbounds [2 x i32], [2 x i32]* @a, i64 0, i64 0
  %6 = getelementptr inbounds [2 x i32], [2 x i32]* @a, i64 0, i64 1
  %7 = load i32, i32* %5, align 4
  %8 = load i32, i32* %6, align 4
  %9 = load i32, i32* %2, align 4
  %10 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([12 x i8], [12 x i8]* @.str.0, i64 0, i64 0), i32 %7, i32 %8, i32 %9)
  %11 = load i32, i32* %1, align 4
  ret i32 %11
}
declare i32 @printf(i8*, ...)