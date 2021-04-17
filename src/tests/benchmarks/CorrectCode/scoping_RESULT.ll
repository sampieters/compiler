@.str.0 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.str.2 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
@.str.3 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1
  %0 = alloca i32, align 4
  store i32 10, i32* %0, align 4

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %2 = load i32, i32* %0, align 4
  %3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.0, i64 0, i64 0), i32 %2)
  %4 = alloca i32, align 4
  store i32 20, i32* %4, align 4
  %5 = load i32, i32* %4, align 4
  %6 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.1, i64 0, i64 0), i32 %5)
  store i32 30, i32* %4, align 4
  br i1 %6, label %7, label %13

; <label>:7:
  %8 = load i32, i32* %4, align 4
  %9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.2, i64 0, i64 0), i32 %8)
  %10 = alloca i32, align 4
  store i32 40, i32* %10, align 4
  %11 = load i32, i32* %10, align 4
  %12 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.3, i64 0, i64 0), i32 %11)
  br label %13

; <label>:13:
  ret i32 1
}
declare i32 @printf(i8*, ...)