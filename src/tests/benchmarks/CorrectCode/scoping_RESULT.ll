@.str.0 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.str.2 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.str.3 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@x = global i32 10, align 4

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = load i32, i32* @x, align 4
  %2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.0, i64 0, i64 0), i32 %1)
  %3 = alloca i32, align 4
  store i32 20, i32* %3, align 4
  %4 = load i32, i32* %3, align 4
  %5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.1, i64 0, i64 0), i32 %4)
  store i32 30, i32* %3, align 4
  br i1 1, label %6, label %12

; <label>:6:
  %7 = load i32, i32* %3, align 4
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.2, i64 0, i64 0), i32 %7)
  %9 = alloca i32, align 4
  store i32 40, i32* %9, align 4
  %10 = load i32, i32* %9, align 4
  %11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.3, i64 0, i64 0), i32 %10)
  br label %12

; <label>:12:
  ret i32 1
}
declare i32 @printf(i8*, ...)