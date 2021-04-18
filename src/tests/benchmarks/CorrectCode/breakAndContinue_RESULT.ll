@.str.0 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

define i32 @main() {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  store i32 0, i32* %2, align 4
  br label %3

; <label>:3:
  %4 = load i32, i32* %2, align 4
  %5 = icmp slt i32 %4, 10
  br i1 %5, label %6, label %16

; <label>:6:
  %7 = load i32, i32* %2, align 4
  %8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.0, i64 0, i64 0), i32 %7)
  %9 = load i32, i32* %2, align 4
  %10 = icmp eq i32 %9, 5
  br i1 %10, label %11, label %12

; <label>:11:
  br label %16

; <label>:12:
  %13 = load i32, i32* %2, align 4
  %14 = add nsw i32 %13, 1
  store i32 %14, i32* %2, align 4
  br label %3

; <label>:15:
  store i32 10, i32* %2, align 4
  br label %3

; <label>:16:
  %17 = load i32, i32* %1, align 4
  ret i32 %17
}
declare i32 @printf(i8*, ...)