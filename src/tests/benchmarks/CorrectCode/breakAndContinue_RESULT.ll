@.str.0 = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  br label %2

; <label>:2:
  %3 = load i32, i32* %1, align 4
  %4 = icmp slt i32 %3, 10
  br i1 %4, label %5, label %15

; <label>:5:
  %6 = load i32, i32* %1, align 4
  %7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.0, i64 0, i64 0), i32 %6)
  %8 = load i32, i32* %1, align 4
  %9 = icmp eq i32 %8, 5
  br i1 %9, label %10, label %11

; <label>:10:
  br label %15

; <label>:11:
  %12 = load i32, i32* %1, align 4
  %13 = add nsw i32 %12, 1
  store i32 %13, i32* %1, align 4
  br label %2

; <label>:14:
  store i32 10, i32* %1, align 4
  br label %2

; <label>:15:
  ret i32 0
}
declare i32 @printf(i8*, ...)