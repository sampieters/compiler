@.str.0 = private unnamed_addr constant [4 x i8] c"%d;\00", align 1

; Function Attrs: noinline nounwind optnone ssp uwtable
define i32 @main() {
  %1 = alloca i32, align 4
  store i32 0, i32* %1, align 4
  br label %2
; <label>:2:
  %3 = load i32, i32* %1, align 4
  %4 = icmp slt i32 %3, 5
  br i1 %4, label %5, label %10
; <label>:5:
  %6 = load i32, i32* %1, align 4
  %7 = add nsw i32 %6, 1
  store i32 %7, i32* %1, align 4
  %8 = load i32, i32* %1, align 4
  %9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.0, i64 0, i64 0), i32 %8)
  br label %2
; <label>:10:
  ret i32 1
}
declare i32 @printf(i8*, ...)